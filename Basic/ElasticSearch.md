# ElasticSearch
- 基于Lucene引擎的分布式全文检索工具。
- 特点
  1. 分布式
  2. 近实时
  3. 丰富API
## 理论篇
### ES的重点
- 倒排索引
- 集群状态
- 分片
- 副本
- 检索流程
- 写入流程
- 并发控制
- 排序算法
- 路由
- 段合并
### ES和MySQL对比
| MySQL    | ES       |
|----------|----------|
| database | index    |
| row      | document |
| column   | field    |
| schema   | mapping  |
| SQL      | DSL      |
| select   | get      |
| update   | put      |

### ES服务发现机制
- Zen算法

### 检索原理
> ES中最先接收到客户端请求的数据节点data_node，自动变为协调节点 coordinating_node。

- 主要分为两大步：
    1. query
    2. fetch
- query阶段：
  1. 协调节点广播请求。协调节点将搜索请求转发到具有该数据的任意分片，该分片取得from+size的数据，经过优先队列排序后返回给coordinating node节点
- fetch阶段：
  2. 协调节点将所有分片的数据再放入自己的优先队列，然后找到需要的doc_id，再将这些具体的文档内容从分片获取到，最后返回给客户端。

### 写入流程
1. coordinating node 进行计算对应主分片位置转发到data node
2. data node中的主分片同步
3. data node 副分片同步
4. 返回到coordinating node节点

### 持久性
- ES的WAL预写日志技术称为translog，默认5秒刷新一次disk。
- 数据写入，首先写入index buffer（不可被检索），默认1秒后刷新（refresh）到os cache中（可以被检索），默认每30分钟刷新（flush）一次到disk
### 副本
- 同步机制
    1. quorum 超过半数
    2. ALL 全部
    3. One 主节点
- 超时机制
### 删除
- 逻辑删除，记录在.del文件中，查询时过滤掉已经删除的数据。

### 更新

- 不更新，直接新建，然后旧的文档标记为删除。

### Lucene写流程

- 主分片-----内存buffer-----OS Cache( refresh 1s) ----segment file(fsync  5s) / translog(5s)-----segment file(30min)



### ES和Solr的区别

1. Solr对稳定数据的查询效率较高，对实时数据的查询效率较低； Solr依赖于ZooKeeper；Solr的社区逐渐没落。
2. ES对云计算和大数据支持得很好。


### 倒排索引

- 正排索引是记录了文档doc_id中有哪些词word。
- 倒排索引记录的是词word对应了哪些文档doc_id。

### 路由规则

- 根据主分片数进行轮询。

- 文档到分片的路由算法：round-robin
- shard = hash(_routing) % number_of_primary_shards

- hash算法确保文档均匀的分散到分片中

- 默认的_routing值是文档id

- 设置index settings后，主分片数不能随意修改的根本原因。


默认情况下，每个索引由5个主分片，每个主分片又有1个副本分片，一共10份分片。

### 并发

- ES采用的是乐观锁进行并发控制。
- ES中的文档是不可变更的。如果你更新一个文档，会将旧文档标记为删除，同时增加一个全新的文档，同时文档的version字段加1。
- 以前版本通过version来控制并发冲突。最新版本内部版本控制采用序列号来判断：if_seq_no + if_primary_term
- 最新版本使用外部版本（使用其他数据库作为主要存储）：version+version_type=external



## 脑裂问题

brain split脑裂：集群的2个部分不能彼此交流，都认为对方宕机了。
lucene先生成索引，再进行搜索。**每个document相当于数据库中表的一行，field相当于每个字段。
ES所处理的最小单位：分片。一份分片是lucene的索引：一个包含倒排索引的文件目录。
ES的索引由多个分片组成，也就是说ES的索引对应多个Lucene的索引。
一个节点是一个ES的实例，再服务器上启动ES之后，你就拥有了一个节点。甚至可以通过启动多个ES进程，再同一台服务器上拥有多个节点。多个节点可以加入同一集群。
- 指在分布式集群中节点之间由于网络分区而不能正常通信，是的原本为一个而整体的集群分裂为两个或多个集群，从而导致系统混乱，服务异常，数据不一致的现象。为防止脑裂的发生，ES通过discovery.zen.minimum_master_nodes来控制选主的条件。
### 集群
- master_slave方式


1. 水平扩展：在节点中加入更多节点被称为水平扩展。使用分片使得你可以进行水平扩展。
2. 垂直扩展：增加更多的硬件资源，可能是为虚拟机分配更多处理器，或是为物理机增加更多的内存。
### 索引
分布式索引：通过散列确定主分片，然后同步到副本分片。
- 轮询算法的缺点：轮询调度算法假设所有服务器的处理性能都相同，不关心每台服务器的当前连接数和响应速度。当请求服务间隔时间变化比较大时，轮询调度算法容易导致服务器间的负载不平衡。
- 分布式搜索流程：**在搜索的时候，接受请求的节点将请求转发到一组包含所有数据的分片。**ES使用轮询机制选择可用的主/副分片，并将搜索请求转发过去。ES从这些每个分片返回的部分结果，聚集成完整的结果，返回给调用方。

## 排序算法

打分：确定文档和查询有多么相关的过程被称为打分。
排序算法TF/IDF，计算结果的相关性得分。
一个词条出现在某个文档中的次数越多，它就越相关，但是如果该词条出现在不同的文档的次数越多，他就越不相关。
TF-词频：关键词在一篇文档中出现的次数。
IDF-逆文档频率：不同文档中出现的次数。检查是否出现，而不是出现多少次。
BM25：替代TF-IDF算法，一种基于概率的打分框架。k1=1.2，b = 0.75。
lucene4.0采用FST。
优点：内存占用率低，压缩率一般在3~20倍之间、模糊查询支持好，查询块。缺点：结构复杂，输入要求有序，更新不易。
跳表优点：结构简单，跳跃间隔和级数可控。缺点：模糊查询支持不好。


### ES集群底层

健康状态：
- Green：所有主分片和副分片都运行正常。

- Yellow：所有主分片都运行正常，但至少有一个副本分片运行异常。

- Red：至少有一个主分片运行异常。


### 节点类型：

- Master Node：主节点主要负责集群节点状态的维护，索引的创建删除，数据的rebalance，分片的分配等工作。

- Data Node：数据节点主要负责集群中数据的索引创建和检索，具体操作包括数据的索引，检索，聚合等。

- Coordinating Node：协调节点用于接收客户端请求，并将请求转发到各个DataNode。

- Ingest Node：提取节点是执行数据预处理的管道，它在索引之前预处理文档。

- Tribe Node：部落节点允许在多个集群之间充当联合客户端，用于实现跨集群访问。


### 实例
- 一个集群由一个或多个节点组织在一起，它们共同持有整个集群的数据，并一起提供索引和搜索功能。
- 一个节点是集群中的一个服务器。

### 分片
- ES默认分片为5片，全加起来才是一个整体，每片数据都不一样。
- 一个物理的存储单元是一个Lucene创建的索引库，一个Shard分片就是一个Lucene Index。

### 集群选举

ES集群选主操作采用bully算法。


## 实战篇
### 参考博客
- [docker启动ES和Kibana](https://blog.csdn.net/qq_33339182/article/details/119772941)
### 安装方式
```shell
# 安全校验
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.3.3
# 无安全校验
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.5
# 启动容器
docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.5
```
### ES服务端
- 端口 9200
### Kibana可视化
- 端口 5601
### Java客户端调用
- 依赖包
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-elasticsearch</artifactId>
</dependency>
```
- 保持ES与本地版本一致
```xml
<properties>
      <java.version>1.8</java.version>
       <!--自定义ES版本保证本地和SpringBoot一致-->
       <elasticsearch.version>7.3.1</elasticsearch.version>
</properties>
```
- ES配置
```shell
@Configuration
public class EsConfig {
    @Bean
    public RestHighLevelClient restHighLevelClient(){
        RestHighLevelClient client = new RestHighLevelClient(
                RestClient.builder(
                        new HttpHost("127.0.0.1", 9200, "http")));
        return client;
    }
}

```
- 单元测试
```
@SpringBootTest
class DemoApplicationTests {
    @Autowired
    @Qualifier("restHighLevelClient")   //配置类中的方法名
    private RestHighLevelClient client;

    //测试索引的创建
    @Test
    void testCreateIndex() throws IOException {
        //1.创建索引
        CreateIndexRequest request = new CreateIndexRequest("yaojun_index");
        //2.客户端执行请求 获得响应
        CreateIndexResponse response = client.indices().create(request, RequestOptions.DEFAULT);

        System.out.println(response);
    }
    //获取索引
    @Test
    void testGetIndex() throws IOException {
        //1.获取索引
        GetIndexRequest request = new GetIndexRequest("yaojun_index");
        //2.客户端执行请求 获得响应
        boolean response = client.indices().exists(request, RequestOptions.DEFAULT);
        System.out.println(response);
    }
    //删除索引，注意只能删除一次
    @Test
    void testDeleteIndex() throws IOException {
        DeleteIndexRequest request = new DeleteIndexRequest("yaojun_index");
        AcknowledgedResponse response = client.indices().delete(request, RequestOptions.DEFAULT);
        System.out.println(response.isAcknowledged());
    }

    //测试添加文档
    @Test
    void testAddDocument() throws Exception{
        //1.创建对象
        User user = new User("yaojun", 3);
        // 2.创建请求
        IndexRequest request = new IndexRequest("yaojun");
        //3.规则 put /yaojun_index/doc/1
        request.id("1");
        request.timeout(TimeValue.timeValueSeconds(1));
        //4.将我们的数据放入请求 json
        IndexRequest source = request.source(JSON.toJSONString(user), XContentType.JSON);

        //5.客户端发送请求 获取响应结果
        IndexResponse response = client.index(request, RequestOptions.DEFAULT);

        System.out.println(response.toString());
        System.out.println(response.status());
    }

    //获取文档 判断是否存在get /yaojun/doc/1
    @Test
    void testIsExist() throws Exception{
        GetRequest getRequest = new GetRequest("yaojun", "1");
        //不获取返回的_source的上下文了
        getRequest.fetchSourceContext(new FetchSourceContext(false));

        boolean exists = client.exists(getRequest, RequestOptions.DEFAULT);
        System.out.println(exists);
    }

    //获取文档
    @Test
    void testGetDocument()throws  Exception{
        GetRequest getRequest = new GetRequest("yaojun", "1");


        GetResponse response = client.get(getRequest, RequestOptions.DEFAULT);
        System.out.println(response.getSourceAsString()); //打印文档的内容
        System.out.println(response);
    }
    //更新文档
    @Test
    void testUpdateDocument()throws  Exception{
        UpdateRequest updateRequest = new UpdateRequest("yaojun", "1");
        updateRequest.timeout("1s");
        User user = new User("姚军",18);
        updateRequest.doc(JSON.toJSONString(user), XContentType.JSON);

        UpdateResponse response = client.update(updateRequest, RequestOptions.DEFAULT);
        System.out.println(response.status());
    }
    //删除文档
    @Test
    void testDeleteDocument()throws  Exception{
        DeleteRequest request = new DeleteRequest("yaojun", "1");
        request.timeout("1s");


        DeleteResponse response = client.delete(request, RequestOptions.DEFAULT);
        System.out.println(response.status());
    }

    //删除文档
    @Test
    void testBulkDocument()throws  Exception{
        BulkRequest bulkRequest = new BulkRequest();
        bulkRequest.timeout("10s");

        ArrayList<User> userList = new ArrayList<>();
        userList.add(new User("姚军1", 18));
        userList.add(new User("姚军2", 19));
        userList.add(new User("姚军3", 8));
        userList.add(new User("姚军4", 8));
        userList.add(new User("姚军5", 8));

        //批处理请求
        for(int i = 0; i < userList.size(); i++){
            bulkRequest.add(
                    new IndexRequest("yaojun").id(""+(i+1)).source(JSON.toJSONString(userList.get(i)), XContentType.JSON)
            );
        }
        BulkResponse bulkResponse = client.bulk(bulkRequest, RequestOptions.DEFAULT);

        System.out.println(bulkResponse.hasFailures()); //判断是否失败
    }

    //查询
    @Test
    void testSearchDocument()throws Exception{
        SearchRequest request = new SearchRequest("yaojun");
        //构建搜索条件
        SearchSourceBuilder searchSource = new SearchSourceBuilder();
        //查询语句
        //QueryBuilders.termQuery() 精确匹配
        //  QueryBuilders.matchAllQuery() 匹配全部

        TermQueryBuilder termQuery = QueryBuilders.termQuery("name", "yaojun");
        searchSource.query(termQuery);
        //searchSource.from(); 构建分页
        //searchSource.size();

        searchSource.timeout(new TimeValue(60, TimeUnit.SECONDS));

        request.source(searchSource);
        SearchResponse response = client.search(request, RequestOptions.DEFAULT);
        System.out.println(JSON.toJSONString(response.getHits()));
        System.out.println("====================");
        for (SearchHit hit : response.getHits().getHits()) {
            System.out.println(hit.getSourceAsMap());
        }
    }
}

```
## FAQ
### 深度分页如何处理？
1. search after
2. scroll
### 查询效率高的原因？
1. 倒排索引
2. 前缀树
3. FST
4. doc_values 列式存储
### 分片大小如何设定？
1. 日志类：单个分片不要大于50G
2. 搜索类：单个分片不要大于20G
