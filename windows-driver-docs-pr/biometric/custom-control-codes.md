---
title: Custom Control Codes
description: vendors can define custom control codes
keywords:
- biometric drivers WDK , control codes
ms.date: 11/13/2017
ms.localizationpriority: medium
---

# Custom Control Codes

Vendors can define custom control codes beginning at 0x800.

To define vendor-specific I/O control codes, use the system-supplied CTL_CODE macro with the following arguments:

```c
#define IOCTL_BIOMETRIC_Device_Function CTL_CODE(FILE_DEVICE_BIOMETRIC, Function, METHOD_BUFFERED, FILE_ANY_ACCESS)
```

All input/output parameters are vendor-defined. The **Status** member is set to one of the values in the following table:

| Status value | Description |
| --- | --- |
| S_OK, STATUS_SUCCESS | The operation completed successfully. If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call. Otherwise, the payload contains the full output buffer. |
| E_INVALIDARG | The parameters were not specified correctly. |

Vendor-defined IOCTLs can be used for any vendor-specific operations. These calls come through the Windows Biometric Service, which has exclusive control of the device. Here are some examples of how vendors can use the vendor specific IOCTLs:

- Set up proprietary secure sessions between an application or component and the device.
- Interface with matching and storage capabilities on the device from a WinBio engine or database plug-in.
- Pend I/O for vendor-specific device events.
- Manage vendor-specific sessions.

This feature is available in Windows 7 and later versions of Windows.


