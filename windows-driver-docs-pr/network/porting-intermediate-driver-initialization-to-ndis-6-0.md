---
title: Porting Intermediate Driver Initialization to NDIS 6.0
description: Porting Intermediate Driver Initialization to NDIS 6.0
ms.assetid: b1029d31-242b-4097-9f2f-e073ac474358
keywords:
- intermediate drivers WDK networking , initializing
- NDIS intermediate drivers WDK , initializing
- porting intermediate drivers WDK networking , initialization
- initializing intermediate drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Intermediate Driver Initialization to NDIS 6.0





Like NDIS 5.*x*, NDIS 6.0 intermediate drivers register with NDIS in the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. In NDIS 6.0, the [**NdisMInitializeWrapper**](https://msdn.microsoft.com/library/windows/hardware/ff553547), [**NdisMRegisterUnloadHandler**](https://msdn.microsoft.com/library/windows/hardware/ff553606), [**NdisMRegisterMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff553602), and [**NdisRegisterProtocol**](https://msdn.microsoft.com/library/windows/hardware/ff554653) functions are eliminated. To register the intermediate driver with NDIS 6.0, the **DriverEntry** routine must, at a minimum:

1.  Call the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function with the NDIS\_INTERMEDIATE\_DRIVER flag set to register the driver's *MiniportXxx* functions.

2.  Call the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function to register the driver's *ProtocolXxx* functions if the driver subsequently binds itself to an underlying NDIS driver.

3.  Call the [**NdisIMAssociateMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff562717) function to inform NDIS about the association between the driver's miniport upper edge and protocol lower edge.

For more information about initializing the miniport upper edge of an intermediate driver, see [Porting Miniport Driver Initialization to NDIS 6.0](porting-miniport-driver-initialization-to-ndis-6-0.md).

For more information about initializing the protocol lower edge of an intermediate driver, see [Porting Protocol Driver Initialization to NDIS 6.0](porting-protocol-driver-initialization-to-ndis-6-0.md).

For more information about NDIS 6.0 intermediate driver initialization, see [Initializing an Intermediate Driver](initializing-an-intermediate-driver.md) and [Initializing a Miniport-Intermediate Driver](initializing-a-miniport-intermediate-driver.md).

 

 





