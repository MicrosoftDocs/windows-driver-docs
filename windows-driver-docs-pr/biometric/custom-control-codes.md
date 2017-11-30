---
title: Custom Control Codes
description: vendors can define custom control codes
ms.assetid: 66eebb4b-ee1e-42d2-9a4b-98a79a0f7b75
keywords:
- biometric drivers WDK , control codes
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Custom%20Control%20Codes%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
