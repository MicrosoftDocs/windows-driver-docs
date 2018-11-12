---
title: Retreat and Advance Operations
description: Retreat and Advance Operations
ms.assetid: 90d4acae-e66c-486b-8b38-59f7fe159047
keywords:
- network data WDK , advance operations
- network data WDK , retreat operations
- data WDK networking , advance operations
- data WDK networking , retreat operations
- packets WDK networking , advance operations
- packets WDK networking , retreat operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Retreat and Advance Operations





NDIS provides retreat and advance functions to manipulate [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures. [Retreat operations](retreat-operations.md) make more *used data space* available to the current driver. [Advance operations](advance-operations.md) release *used data space*.

Retreat operations are required during send operations or when a driver returns received data to an underlying driver. For example, during a send operation, a driver can call the [**NdisRetreatNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff564527) function to make room for header data.

Advance operations are required when a send operation is complete or when a driver receives data from an underlying driver. For example, during a receive operation, a driver can call the [**NdisAdvanceNetBufferDataStart**](https://msdn.microsoft.com/library/windows/hardware/ff560703) function to skip over the header data that was used by a lower level driver. In this case, the header data remains in the buffer in the *unused data space*.

The following figure shows the relationship between the network data and these operations.

![diagram illustrating data space allocation](images/netbufferdata-basic.png)

The following topics provide more information about advance and retreat operations:

[Retreat Operations](retreat-operations.md)

[Advance Operations](advance-operations.md)

 

 





