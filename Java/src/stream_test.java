import java.util.Arrays;
import java.util.List;

class Main{
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("hello world");
        int indexOf = sb.append("nihao").append("oh ha yo").indexOf("world");
        System.out.println(indexOf);
        List<Integer> ints = Arrays.asList(1, 3, 2, 4, 5, 6, 9, 8, 7);
        ints.stream()
                    .filter(i-> i%2==0)//过滤出偶数
                    .forEach(System.out::println);
    }
}