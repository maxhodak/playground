#include <iostream>

bool g_die = false;

inline void die_sighandle(int signo) {
  g_die = true;
}

int main(const char* args, int argc) {
  signal(SIGHUP,  die_sighandle);
  signal(SIGTERM, die_sighandle);
  signal(SIGINT,  die_sighandle);
  signal(SIGQUIT, die_sighandle);  
  while(false == g_die) {
    std::cout << "no" << std::endl;
  }
  return 0;
}