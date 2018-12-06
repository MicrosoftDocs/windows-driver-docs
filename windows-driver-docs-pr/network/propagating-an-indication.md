---
title: Propagating an Indication
description: Propagating an Indication
ms.assetid: df26503f-e717-41b8-b208-41e0193cd222
keywords:
- intermediate drivers WDK TCP chimney offload , propagating indication
- indication propagation WDK TCP chimney offload
- propagating offloaded TCP connection indication
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Propagating an Indication


\[The TCP chimney offload feature is deprecated and should not be used.\]

An offload target makes an indication on an offloaded TCP connection by calling one of the following NDIS functions:

-   [**NdisMOffloadEventIndicate**](https://msdn.microsoft.com/library/windows/hardware/ff563619)

-   [**NdisTcpOffloadEventHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564595)

-   [**NdisTcpOffloadReceiveHandler**](https://msdn.microsoft.com/library/windows/hardware/ff564606)

When calling one of the preceding indication functions, an offload target passes in an *NdisOffloadHandle* parameter in addition to other parameters. The *NdisMiniportHandle* parameter is the **NdisOffloadHandle** member that the offload target stored in its miniport offload context when the TCP connection was offloaded. (For more information about this stored **NdisOffloadHandle**, see [Storing and Referencing Offloaded State](storing-and-referencing-offloaded-state.md).)

In response to the offload target's indication, NDIS calls the corresponding intermediate driver function:

-   [*ProtocolIndicateOffloadEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570260)

-   [**ProtocolTcpOffloadEvent**](https://msdn.microsoft.com/library/windows/hardware/ff570272)

-   [*ProtocolTcpOffloadReceiveIndicate*](https://msdn.microsoft.com/library/windows/hardware/ff570275)

To each of the above *Protocol* Xxx functions, NDIS passes, among other parameters, an *OffloadContext* parameter. The *OffloadContext* parameter points to the [**NDIS\_OFFLOAD\_HANDLE**](https://msdn.microsoft.com/library/windows/hardware/ff566705) structure in the intermediate driver's context (called the *IM offload entry*) for the offloaded TCP connection.

To propagate the indication to the host stack, the intermediate driver calls the same NDIS indication function that the offload target called. To this NDIS indication function, the intermediate driver passes the following:

-   The **NdisOffloadHandle** member that the offload target stored in its context (IM offload entry) for the offloaded TCP connection. (For more information about this stored **NdisOffloadHandle**, see [Referencing Offloaded State Through an Intermediate Driver](referencing-offloaded-state-through-an-intermediate-driver.md).)

-   The same additional parameters that NDIS passed to the intermediate driver's *ProtocolXxx* function.

For example, to propagate a call to the **NdisTcpOffloadReceiveHandler** function, the intermediate driver passes:

-   The **NdisOffloadHandle** member that the offload target stored in its context (IM offload entry) for the offloaded TCP connection.

-   The *EventType* and *EventSpecificInformation* parameters that NDIS passed to the intermediate driver's *ProtocolTcpOffloadReceiveIndicate* function.

 

 





