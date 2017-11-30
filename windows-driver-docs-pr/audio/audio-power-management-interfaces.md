---
title: Audio Power Management Interfaces
description: Audio Power Management Interfaces
ms.assetid: 7b123d3f-4f11-448e-8b20-92578fda7e69
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Audio Power Management Interfaces


## <span id="ddk_audio_power_management_interfaces_ks"></span><span id="DDK_AUDIO_POWER_MANAGEMENT_INTERFACES_KS"></span>


This section describes the interfaces that the Port Class Library (portcls.sys) uses to manage power in a WDM audio adapter. These interfaces are implemented by the adapter driver and exposed to the PortCls system driver.

The following two interfaces are discussed:

Implemented by an adapter driver and exposed to PortCls for power management of an audio adapter card.

Implemented by an adapter driver and exposed to PortCls. This interface provides power managent messages about the audio adapter and the system.

An optional interface that a miniport driver can expose if it requires advance notification of impending power-state changes.

[IAdapterPowerManagement](https://msdn.microsoft.com/library/windows/hardware/ff536485)

[IAdapterPowermanagement2](https://msdn.microsoft.com/library/windows/hardware/ff536486)

[IAdapterPowerManagement3](https://msdn.microsoft.com/library/windows/hardware/jj200330)

[IPowerNotify](https://msdn.microsoft.com/library/windows/hardware/ff536947)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Audio%20Power%20Management%20Interfaces%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




