#include <iostream>
#ifdef _WIN32
    #include <windows.h>
#endif
#ifdef __APPLE__
// PLACEHOLDER
#else
    #include <EGL/egl.h>
#endif

int main()
{
    std::cout << "Bincrafters\n";
    return 0;
}
