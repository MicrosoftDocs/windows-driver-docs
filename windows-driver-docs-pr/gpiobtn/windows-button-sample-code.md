---
title: Windows button sample code
description: This topic contains a code sample that toggles the identified Windows button down and then up.
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows button sample code


This topic contains a code sample that toggles the identified Windows button down and then up.

```cpp
int __cdecl InjectButtonPress(
    __in int argc,
    __in_ecount(argc) char **argv)
{
    LPWSTR DevicePath;
    HANDLE FileHandle;
    BOOL b;
    BYTE buffer;
    HWND hwnd;
    MSG msg;

    DevicePath = GetDevicePath((LPGUID)&GUID_GPIOBUTTONS_NOTIFY_INTERFACE);

    FileHandle = CreateFile(DevicePath,
                            GENERIC_WRITE,
                            0,
                            NULL,
                            OPEN_EXISTING,
                            0,
                            NULL);
   
    buffer = GPIO_BUTTON_WINDOWS; //using GPIOBUTTONS_BUTTON_TYPE enum defined above
    WriteFile(FileHandle, &buffer, sizeof(buffer), NULL, NULL); // send button down
    buffer = GPIO_BUTTON_WINDOWS;
    WriteFile(FileHandle, &buffer, sizeof(buffer), NULL, NULL); // send button up

    return 0;
}
```

 

 




