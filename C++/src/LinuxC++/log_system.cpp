#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <assert.h>
#include <fcntl.h>
#include <mutex>
#include <atomic>
using namespace std;
class Logger{
public:
    static Logger* get_instance();
    static Logger* log;
    static mutex log_mutex;
    static void write_log(int level, char* s);
    static void create_file();
    static int fd;
private:
    Logger();
    Logger(const Logger& other);
    ~Logger();
};
Logger* Logger::log = NULL;
mutex Logger::log_mutex;
int Logger::fd = 0;
Logger::Logger(){};
Logger::~Logger(){
    if(log != NULL){
        delete log;
        log = NULL;
    }
    close(fd);
}
Logger* Logger::get_instance(){
    if(log == NULL){
        log_mutex.lock();
        if(log == NULL){
            log = new Logger();
        }
        log_mutex.unlock();
    }
    return log;
}
void Logger::create_file(){
    fd = open("logger.txt", O_RDWR|O_CREAT|O_TRUNC, 777);
    assert(fd > 0);
}
void Logger::write_log(int level, char* s){
    int n = strlen(s);
    log_mutex.lock();
    write(fd, s, n);
    log_mutex.unlock();
}
