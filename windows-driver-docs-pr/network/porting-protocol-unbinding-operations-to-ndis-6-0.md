---
title: Porting Protocol Unbinding Operations to NDIS 6.0
description: Porting Protocol Unbinding Operations to NDIS 6.0
ms.assetid: 5dee57da-9c45-4e12-bc5e-ae60d4219480
keywords:
- protocol drivers WDK networking , binding operations
- NDIS protocol drivers WDK , binding operations
- protocol bindings WDK networking
- binding operations WDK networking
- porting protocol drivers WDK networking , unbinding operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Protocol Unbinding Operations to NDIS 6.0





In NDIS 6.0, the [*ProtocolUnbindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570278) function replaces the NDIS 5.x [**ProtocolUnbindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff563260) function. A protocol driver calls the [**NdisCloseAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff561640) function (formerly [**NdisCloseAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff550904)) from *ProtocolUnbindAdapterEx* to close a binding to a miniport adapter.

The driver must wait for all outstanding send operations to complete and must complete all outstanding receive operations before calling **NdisCloseAdapterEx**.

If NDIS returns NDIS\_STATUS\_PENDING from **NdisCloseAdapterEx**, NDIS later calls the protocol driver's [*ProtocolCloseAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570236) function (formerly [**ProtocolCloseAdapterComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562502)) with the final status after the close request has been completed.

Unlike NDIS 5.x, the final status of an NDIS 6.0 close operation, whether synchronous or asynchronous, is always NDIS\_STATUS\_SUCCESS. Similarly, *ProtocolUnbindAdapterEx* always succeeds.

For more information about NDIS 6.0 unbinding operations, see [Unbinding from an Adapter](unbinding-from-an-adapter.md).

 

 





