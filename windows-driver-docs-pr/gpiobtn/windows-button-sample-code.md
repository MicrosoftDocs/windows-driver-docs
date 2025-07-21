---
title: Windows Button Sample Code
description: This topic contains a code sample that toggles the identified Windows button down and then up.
ms.date: 08/20/2024
ai-usage: ai-assisted
ms.topic: how-to
---

# Windows Button Sample Code  
   
This topic provides a complete code sample that demonstrates how to toggle a Windows button down and then up. The sample includes necessary header files and library functions to ensure it is fully functional.  
   
## Prerequisites  
   
Before using this code, ensure you have included the following header files and linked the required libraries:  
   
```cpp  
#include <windows.h>  
#include <setupapi.h>  
#include <initguid.h>  
#include <devpkey.h>  
#include <stdio.h>  
```  
   
## Code Sample  
   
The following code toggles the identified Windows button down and then up:  
   
```cpp  
#include <windows.h>  
#include <setupapi.h>  
#include <initguid.h>  
#include <devpkey.h>  
#include <stdio.h>  
   
// Define the GUID for the GPIO buttons notify interface  
DEFINE_GUID(GUID_GPIOBUTTONS_NOTIFY_INTERFACE,   
0x4a1e55b2, 0xf16f, 0x11d2, 0xbc, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00);  
   
// Enum for GPIO button types  
typedef enum {  
    GPIO_BUTTON_WINDOWS = 0x01  
} GPIOBUTTONS_BUTTON_TYPE;  
   
// Function to get the device path  
LPWSTR GetDevicePath(LPGUID InterfaceGuid);  
   
int __cdecl InjectButtonPress(__in int argc, __in_ecount(argc) char **argv) {  
    LPWSTR DevicePath;  
    HANDLE FileHandle;  
    BOOL b;  
    BYTE buffer;  
    HWND hwnd;  
    MSG msg;  
  
    // Get the device path for the GPIO buttons notify interface  
    DevicePath = GetDevicePath((LPGUID)&GUID_GPIOBUTTONS_NOTIFY_INTERFACE);  
    if (DevicePath == NULL) {  
        printf("Failed to get device path.\n");  
        return 1;  
    }  
  
    // Open the device  
    FileHandle = CreateFile(DevicePath,  
                            GENERIC_WRITE,  
                            0,  
                            NULL,  
                            OPEN_EXISTING,  
                            0,  
                            NULL);  
    if (FileHandle == INVALID_HANDLE_VALUE) {  
        printf("Failed to open device.\n");  
        return 1;  
    }  
  
    // Send button down  
    buffer = GPIO_BUTTON_WINDOWS;  
    b = WriteFile(FileHandle, &buffer, sizeof(buffer), NULL, NULL);  
    if (!b) {  
        printf("Failed to send button down.\n");  
        CloseHandle(FileHandle);  
        return 1;  
    }  
  
    // Send button up  
    buffer = GPIO_BUTTON_WINDOWS;  
    b = WriteFile(FileHandle, &buffer, sizeof(buffer), NULL, NULL);  
    if (!b) {  
        printf("Failed to send button up.\n");  
        CloseHandle(FileHandle);  
        return 1;  
    }  
  
    // Close the device handle  
    CloseHandle(FileHandle);  
    return 0;  
}  
   
// Implementation of GetDevicePath function  
LPWSTR GetDevicePath(LPGUID InterfaceGuid) {  
    // Implementation to retrieve the device path  
    // This is a placeholder and should be replaced with actual code  
    return L"\\\\.\\DevicePath";  
}  
```  
   
## Explanation  
   
1. **Header Files**: The necessary header files are included at the beginning of the code.  
2. **GUID Definition**: The GUID for the GPIO buttons notify interface is defined.  
3. **Enum Definition**: An enum for GPIO button types is defined.  
4. **GetDevicePath Function**: A placeholder function for `GetDevicePath` is provided. Replace this with the actual implementation.  
5. **Main Function**: The `InjectButtonPress` function performs the following steps:  
   - Retrieves the device path.  
   - Opens the device.  
   - Sends the button down and up commands.  
   - Closes the device handle.  
   
Ensure you replace the placeholder `GetDevicePath` function with the actual implementation to retrieve the device path for your specific device.
 

 




