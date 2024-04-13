---
title: SD Card I/O Requests (Windows Drivers)
description: Learn more about SD Card I/O Requests.
ms.date: 03/03/2023
---

# SD Card I/O Requests

The IOCTLs in this section allow user-mode applications to operate devices in the Secure Digial (SD) card stack. To use the IOCTLs, the caller must first use [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) to get a handle to a device in the SD stack, as shown here, where szDevice points to a NULL-terminated string that references the device.

```cpp
    hVol = CreateFile (szDevice,
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

After opening a handle to a volume in the SD stack, the application sends IOCTLs to a device in the SD stack by calling [**DeviceIoControl**](/windows/win32/devio/device-input-and-output-control-ioctl-). For more information about the Windows SD architecture, see [SD Card Driver Stack](sd-card-driver-stack.md).

This section describes the following IOCTLs:

[**IOCTL\_SFFDISK\_DEVICE\_COMMAND**](/windows-hardware/drivers/ddi/sffdisk/ni-sffdisk-ioctl_sffdisk_device_command)

[**IOCTL\_SFFDISK\_DEVICE\_PASSWORD**](/windows-hardware/drivers/ddi/sffdisk/ni-sffdisk-ioctl_sffdisk_device_password)

[**IOCTL\_SFFDISK\_QUERY\_DEVICE\_PROTOCOL**](/windows-hardware/drivers/ddi/sffdisk/ni-sffdisk-ioctl_sffdisk_query_device_protocol)
