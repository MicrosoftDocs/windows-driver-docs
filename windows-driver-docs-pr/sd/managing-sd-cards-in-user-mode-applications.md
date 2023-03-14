---
title: Managing SD Cards in User-Mode Applications (Windows Drivers)
description: Learn more about Managing SD Cards in User-Mode Applications.
ms.date: 03/03/2023
---

# Managing SD Cards in User-Mode Applications

The MultiMedia Card Association (MMCA) has defined a set of IOCTLs that allow user-mode applications to control operations on an SD storage stack. The IOCTLs are defined in the *sffdisk.h* header file provided with the Microsoft Windows SDK.

To use the IOCTLs, application software must get a handle to the volume of the target storage stack, as shown here:

```cpp
    hVol = CreateFile(szVol,
        GENERIC_READ | GENERIC_WRITE,
        FILE_SHARE_WRITE | FILE_SHARE_DELETE,
        NULL,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        NULL
    );
    if (hVol == INVALID_HANDLE_VALUE) {
        return GetLastError();
    }
```

Parameter *szVol* points to a NULL-terminated string that references the volume. After opening a handle, application software can send IOCTLs to the SD storage stack by calling [**DeviceIoControl**](/windows/win32/devio/device-input-and-output-control-ioctl-).
