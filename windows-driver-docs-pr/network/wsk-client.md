---
title: WSK_CLIENT
description: This topic describes the WSK_CLIENT data type for WSK applications.
ms.assetid: 7958dbd6-eaa6-4be8-a3a0-b3433ced924b
keywords:
- WSK_CLIENT, WDK WSK_CLIENT network drivers
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WSK_CLIENT

The WSK_CLIENT data type defines the WSK subsystem's binding context for its attachment to a WSK application.

```c++
typedef PVOID PWSK_CLIENT;
```

**PWSK_CLIENT**  
The contents of the **WSK_CLIENT** structure are opaque to a WSK application.

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

