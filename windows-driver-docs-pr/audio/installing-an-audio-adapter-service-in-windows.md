---
title: Installing an Audio Adapter Service
description: Installing an Audio Adapter Service
ms.assetid: 465005da-bf06-497b-801c-fe5aa19a3974
keywords:
- audio adapters WDK , service installations
- adapter drivers WDK audio , service installations
- Port Class audio adapters WDK , service installations
- adapter services WDK audio
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing an Audio Adapter Service in Windows

The following [**INF AddService directive**](https://msdn.microsoft.com/library/windows/hardware/ff546326) installs the adapter driver Xyzaud.sys for the XYZ Audio Device:

```
  [XYZ-Audio-Device.Services.NTX86]
  AddService = XYZ-Audio-Device, 0x00000002, XYZ-Audio-Device.Service.Install

  [XYZ-Audio-Device.Service.Install]
  DisplayName   = %XYZ-Audio-Device.ServiceDescription%
  ServiceType   = 1                  ; SERVICE_KERNEL_DRIVER
  StartType     = 3                  ; SERVICE_DEMAND_START
  ErrorControl  = 1                  ; SERVICE_ERROR_NORMAL
  ServiceBinary = %12%\system32\drivers\xyzaud.sys
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Installing%20an%20Audio%20Adapter%20Service%20in%20Windows%202000%20and%20Later%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


