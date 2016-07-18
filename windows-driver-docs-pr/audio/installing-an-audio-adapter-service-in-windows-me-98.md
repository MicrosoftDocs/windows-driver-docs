---
title: Installing an Audio Adapter Service in Windows Me/98
description: Installing an Audio Adapter Service in Windows Me/98
ms.assetid: d10051c3-bf07-4df5-95d7-c83e75c15250
keywords: ["audio adapters WDK , service installations", "adapter drivers WDK audio , service installations", "Port Class audio adapters WDK , service installations", "adapter services WDK audio"]
---

# Installing an Audio Adapter Service in Windows Me/98


## <span id="installing_an_audio_adapter_service_in_windows_98_me"></span><span id="INSTALLING_AN_AUDIO_ADAPTER_SERVICE_IN_WINDOWS_98_ME"></span>


The INF file sets an **NTMPDriver** entry value in the adapter driver's registry key as follows:

```
  [XYZ-Audio-Device.AddReg]
  HKR,,NTMPDriver,,"xyzaud.sys,sbemul.sys"
```

"NTMP" is an abbreviation for "NT miniport". The **NTMPDriver** keyword indicates that the directive contains the names of one or more auxiliary driver files that are to be loaded at the same time as the driver for the device.

The alternative is to load the auxiliary files at a later time. The **AssociatedFilters** keyword denotes this behavior. For more information, see the example in [Installing Windows Multimedia System Support for an Audio Adapter](installing-windows-multimedia-system-support-for-an-audio-adapter.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Installing%20an%20Audio%20Adapter%20Service%20in%20Windows%20Me/98%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


