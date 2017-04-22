---
title: Installing in Windows 2000 and Later
description: Installing in Windows 2000 and Later
ms.assetid: 790caffd-ebb0-4ba1-b31c-b03d3c83bc59
keywords:
- audio adapters WDK , system components
- adapter drivers WDK audio , system components
- Port Class audio adapters WDK , system components
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing in Windows 2000 and Later


## <span id="installing_in_windows_2000_and_later"></span><span id="INSTALLING_IN_WINDOWS_2000_AND_LATER"></span>


In the following example of an INF device-driver-installation section, the two directives add the system-driver information that installs the core system components for an audio adapter in Windows 2000 and later:

```
  [XYZ-Audio-Device.Registration.NTX86]
  Include=ks.inf, wdmaudio.inf
  Needs=KS.Registration, WDMAUDIO.Registration
```

For information about the **Include** and **Needs** directives, see [**INF DDInstall Section**](https://msdn.microsoft.com/library/windows/hardware/ff547344).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Installing%20in%20Windows%202000%20and%20Later%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


