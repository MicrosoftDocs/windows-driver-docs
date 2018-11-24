---
title: Audio Power Management Interfaces
description: Audio Power Management Interfaces
ms.assetid: 7b123d3f-4f11-448e-8b20-92578fda7e69
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





