---
title: Installing Windows Multimedia System Support for an Audio Adapter
description: Installing Windows Multimedia System Support for an Audio Adapter
ms.assetid: 5846404f-3a6a-4e55-ba83-18404ea7cace
keywords: ["audio adapters WDK , multimedia support", "adapter drivers WDK audio , multimedia support", "Port Class audio adapters WDK , multimedia support", "multimedia WDK audio", "Windows multimedia support WDK audio"]
---

# Installing Windows Multimedia System Support for an Audio Adapter


## <span id="ddk_installing_windows_multimedia_system_support_for_an_audio_adapter_"></span><span id="DDK_INSTALLING_WINDOWS_MULTIMEDIA_SYSTEM_SUPPORT_FOR_AN_AUDIO_ADAPTER_"></span>


An INF add-registry section creates or modifies driver-specific information in the system registry. The add-registry section for a PortCls audio adapter contains information that makes the adapter accessible to the Windows multimedia system components.

The following example presents the add-registry section, XYZ-Audio-Device.AddReg, that was named in an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) in a previous example (see [Installing a Port Class Audio Adapter](installing-a-port-class-audio-adapter.md)):

```
  [XYZ-Audio-Device.AddReg]
  HKR,,AssociatedFilters,,"wdmaud,swmidi,redbook"
  HKR,,Driver,,xyzaud.sys 
  HKR,Drivers,SubClasses,,"wave,midi,mixer,aux"

  HKR,Drivers\wave\Wdmaud.drv,Driver,,Wdmaud.drv
  HKR,Drivers\midi\Wdmaud.drv,Driver,,Wdmaud.drv
  HKR,Drivers\mixer\Wdmaud.drv,Driver,,Wdmaud.drv
  HKR,Drivers\aux\Wdmaud.drv,Driver,,Wdmaud.drv

  HKR,Drivers\wave\Wdmaud.drv,Description,,%XYZ-Audio-Device-Description%
  HKR,Drivers\midi\Wdmaud.drv,Description,,%XYZ-Audio-Device-Description%
  HKR,Drivers\mixer\Wdmaud.drv,Description,,%XYZ-Audio-Device-Description%
  HKR,Drivers\aux\Wdmaud.drv,Description,,%XYZ-Audio-Device-Description%
```

The add-registry section adds the registry entries that specify the components that the system needs to load so that the Windows multimedia system can use the audio adapter. These components include both the adapter driver, Xyzaud.sys, and the system drivers WDMAud, SWMidi, and Redbook (see [Kernel-Mode WDM Audio Components](kernel-mode-wdm-audio-components.md)).

The **AssociatedFilters** keyword in the example add-registry section indicates that the directive contains the names of one or more auxiliary driver files whose loading is to be deferred until they are needed by the adapter driver. The alternative is to load the auxiliary files at the same time that the device driver is loaded. For more information, see the description of the **NTMPDriver** keyword in [Installing an Audio Adapter Service in Windows Me/98](installing-an-audio-adapter-service-in-windows-me-98.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Installing%20Windows%20Multimedia%20System%20Support%20for%20an%20Audio%20Adapter%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




