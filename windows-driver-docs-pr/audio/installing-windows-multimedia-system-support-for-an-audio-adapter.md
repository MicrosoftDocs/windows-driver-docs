---
title: Installing Windows Multimedia System Support for an Audio Adapter
description: Installing Windows Multimedia System Support for an Audio Adapter
ms.assetid: 5846404f-3a6a-4e55-ba83-18404ea7cace
keywords:
- audio adapters WDK , multimedia support
- adapter drivers WDK audio , multimedia support
- Port Class audio adapters WDK , multimedia support
- multimedia WDK audio
- Windows multimedia support WDK audio
ms.date: 10/27/2017
ms.localizationpriority: medium
---

# Installing Windows Multimedia System Support for an Audio Adapter


## <span id="ddk_installing_windows_multimedia_system_support_for_an_audio_adapter_"></span><span id="DDK_INSTALLING_WINDOWS_MULTIMEDIA_SYSTEM_SUPPORT_FOR_AN_AUDIO_ADAPTER_"></span>


An INF add-registry section creates or modifies driver-specific information in the system registry. The add-registry section for a PortCls audio adapter contains information that makes the adapter accessible to the Windows multimedia system components.

The following example presents the add-registry section, XYZ-Audio-Device.AddReg, that was named in an [**INF AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) in a previous example (see [Installing a Port Class Audio Adapter](installing-a-port-class-audio-adapter.md)):

```cpp
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

The **AssociatedFilters** keyword in the example add-registry section indicates that the directive contains the names of one or more auxiliary driver files whose loading is to be deferred until they are needed by the adapter driver. The alternative is to load the auxiliary files at the same time that the device driver is loaded.

 

 




