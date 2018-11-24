---
title: Porting Miniport Driver Initialization to NDIS 6.0
description: Porting Miniport Driver Initialization to NDIS 6.0
ms.assetid: b4363a35-9a16-47bb-bae0-5ad41e5d334d
keywords:
- porting miniport drivers WDK networking , initialization
- miniport drivers WDK networking , initializing
- NDIS miniport drivers WDK , initializing
- initializing miniport drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver Initialization to NDIS 6.0





To support NDIS 6.0, update the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine and the driver entry points in the [**NDIS\_MINIPORT\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565958) structure. There is also a mechanism specific to NDIS 6.0 for registering optional entry points. The following topics provide more information about porting miniport driver initialization:

[Updating the DriverEntry Routine for an NDIS 6.0 Miniport Drivers](updating-the-driverentry-routine-for-an-ndis-6-0-miniport-driver.md)

[Updating the NDIS 6.0 Miniport Driver Characteristics Structure](updating-the-ndis-6-0-miniport-driver-characteristics-structure.md)

[Registering Optional NDIS 6.0 Entry Points for Miniport Drivers](registering-optional-ndis-6-0-entry-points-for-miniport-drivers.md)

 

 





