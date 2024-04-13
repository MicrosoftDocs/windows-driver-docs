---
title: Installing an Audio Adapter Service
description: Installing an Audio Adapter Service
keywords:
- audio adapters WDK , service installations
- adapter drivers WDK audio , service installations
- Port Class audio adapters WDK , service installations
- adapter services WDK audio
ms.date: 10/26/2017
---

# Installing an Audio Adapter Service in Windows

The following [**INF AddService directive**](../install/inf-addservice-directive.md) installs the adapter driver Xyzaud.sys for the XYZ Audio Device:

```cpp
  [XYZ-Audio-Device.Services.NTX86]
  AddService = XYZ-Audio-Device, 0x00000002, XYZ-Audio-Device.Service.Install

  [XYZ-Audio-Device.Service.Install]
  DisplayName   = %XYZ-Audio-Device.ServiceDescription%
  ServiceType   = 1                  ; SERVICE_KERNEL_DRIVER
  StartType     = 3                  ; SERVICE_DEMAND_START
  ErrorControl  = 1                  ; SERVICE_ERROR_NORMAL
  ServiceBinary = %12%\system32\drivers\xyzaud.sys
```

 

