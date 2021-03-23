---
title: Laptop/slate mode toggling between states
description: This topic contains sample code that toggles the laptop/slate mode indicator state.
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Laptop/slate mode toggling between states


This topic contains sample code that toggles the laptop/slate mode indicator state.

```cpp
int __cdecl ToggleConversionIndicator(
    __in int argc,
    __in_ecount(argc) char **argv)
{
    LPWSTR DevicePath;
    HANDLE FileHandle;
    BOOL b;
    BYTE buffer;
    HWND hwnd;
    MSG msg;

//assuming our GetDevicePath method is creating a device path using use SetupDi API
    DevicePath = GetDevicePath((LPGUID)&GUID_GPIOBUTTONS_LAPTOPSLATE_INTERFACE);
   
    FileHandle = CreateFile(DevicePath,
                            GENERIC_WRITE,
                            0,
                            NULL,
                            OPEN_EXISTING,
                            0,
                            NULL);
   
    buffer = 0;
    WriteFile(FileHandle, &buffer, sizeof(buffer), NULL, NULL);

    return 0;
}
```

<b>Note:</b> The laptop/slate mode indicator device can be opened by only one process at a time. CreateFile will fail and GetLastError will return ERROR_ACCESS_DENIED when the device is already opened by another process. 

 




