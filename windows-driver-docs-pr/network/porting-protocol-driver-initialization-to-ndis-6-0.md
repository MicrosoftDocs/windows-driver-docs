---
title: Porting Protocol Driver Initialization to NDIS 6.0
description: Porting Protocol Driver Initialization to NDIS 6.0
ms.assetid: 3dfa1698-47bd-4203-8e16-8e4cc31ab72e
keywords:
- protocol drivers WDK networking , initialization
- NDIS protocol drivers WDK , initialization
- initializing protocol drivers
- porting protocol drivers WDK networking , initialization
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Porting Protocol Driver Initialization to NDIS 6.0


## <a href="" id="ddk-porting-protocol-driver-initialization-to-ndis-6-0-nd"></a>


To support NDIS 6.0 initialization, update the protocol driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine and the driver's entry points in the [**NDIS\_PROTOCOL\_DRIVER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566825) structure.

The following topics provide more information about porting protocol driver initialization:

[Updating the DriverEntry Routine for an NDIS 6.0 Protocol Driver](updating-the-driverentry-routine-for-an-ndis-6-0-protocol-driver.md)

[Updating the NDIS 6.0 Protocol Driver Characteristics Structure](updating-the-ndis-6-0-protocol-driver-characteristics-structure.md)

[Registering Optional NDIS 6.0 Protocol Driver Entry Points](registering-optional-ndis-6-0-protocol-driver-entry-points.md)

 

 





