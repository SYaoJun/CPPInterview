//C++11 atomic
std::atomic<Logger*> Logger::log;
std::mutex Logger::log_mutex;
Logger* Logger::get_instance(){
    Logger* tmp = log.load(std::memory_order_relaxed);
    std::atomic_thread_fence(std::memory_order_acquire); //获取内存fence
    if(tmp == NULL){
        std::lock_guard<std::mutex> lock(log_mutex);
        tmp = log.load(std::memory_order_relaxed);
        if(tmp == NUll){
            tmp = new Logger;
            std::atomic_thread_fence(std::memory_order_release); //释放内存fence
            log.store(tmp, std::memory_order_relaxed);
        }
    }
    return tmp;
}