---
title: WSK_CLIENT
author: windows-driver-content
description: This topic describes the WSK_CLIENT data type for WSK applications.
ms.assetid: 7958dbd6-eaa6-4be8-a3a0-b3433ced924b
keywords:
- WSK_CLIENT, WDK WSK_CLIENT network drivers
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WSK_CLIENT

The WSK_CLIENT data type defines the WSK subsystem's binding context for its attachment to a WSK application.

```c++
typedef PVOID PWSK_CLIENT;
```

**PWSK_CLIENT**  
THe contents of the **WSK_CLIENT** structure are opaque to a WSK application.

## Remarks

When a WSK application calls the [WskCaptureProviderNPI](https://msdn.microsoft.com/library/windows/hardware/ff571122) function, the WSK subsystem returns a pointer to a WSK_CLIENT structure to the WSK application by means of the *WskProviderNpi* parameter. The WSK subsystem uses this structure to track the state of the binding between the WSK application and the WSK subsystem. A WSK application passes this pointer as a parameter to all the functions in [WSK_PROVIDER_DISPATCH](https://msdn.microsoft.com/library/windows/hardware/ff571175) ([WskControlClient](https://msdn.microsoft.com/library/windows/hardware/ff571126), [WskSocket](https://msdn.microsoft.com/library/windows/hardware/ff571149), and [WskSocketConnect](https://msdn.microsoft.com/library/windows/hardware/ff571150)).

For more information, see [Registering a Winsock Kernel Application](registering-a-winsock-kernel-application.md).

## Requirements

|   |   |
| --- | --- |
| Version | Available in Windows Vista and later versions of the Windows operating systems. |
| Header | Wsk.h (include Wsk.h) |

## See also

[WskCaptureProviderNPI](https://msdn.microsoft.com/library/windows/hardware/ff571122)  
[WskControlClient](https://msdn.microsoft.com/library/windows/hardware/ff571126)  
[WskSocket](https://msdn.microsoft.com/library/windows/hardware/ff571149)  
[WskSocketConnect](https://msdn.microsoft.com/library/windows/hardware/ff571150)  
[WSK_PROVIDER_DISPATCH](https://msdn.microsoft.com/library/windows/hardware/ff571175)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")