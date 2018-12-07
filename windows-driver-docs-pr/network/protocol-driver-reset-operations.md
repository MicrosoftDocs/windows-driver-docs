---
title: Protocol Driver Reset Operations
description: Protocol Driver Reset Operations
ms.assetid: 862029e5-8c46-4889-80f5-15c463f228a3
keywords:
- protocol drivers WDK networking , reset operations
- NDIS protocol drivers WDK , reset operations
- reset operations WDK NDIS protocol
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Protocol Driver Reset Operations





Protocol drivers cannot initiate a reset operation in NDIS 6.0 and later versions.

Typically, an underlying miniport driver resets a NIC because the NIC is timing out during send or request operations. This condition causes NDIS to call the miniport driver's [*MiniportCheckForHangEx*](https://msdn.microsoft.com/library/windows/hardware/ff559346) and subsequently [*MiniportResetEx*](https://msdn.microsoft.com/library/windows/hardware/ff559432) functions. Alternatively, the miniport driver determines a NIC's receive capability is dysfunctional.

If a reset is initiated by NDIS and *MiniportResetEx* returns NDIS\_STATUS\_PENDING, NDIS calls the [**ProtocolStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570270)(or [**ProtocolCoStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff570258)) function of each bound protocol driver with a status of NDIS\_STATUS\_RESET\_START. When the miniport driver calls [**NdisMResetComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563663), NDIS again calls *ProtocolStatusEx*(or *ProtocolCoStatusEx*) with a status of NDIS\_STATUS\_RESET\_END.

A protocol driver must handle the possibility that outstanding sends on a binding to an underlying NIC can be canceled because the NIC is reset. If a bound protocol driver has any transmit requests pending, NDIS will indicate a send complete to the protocol driver with an appropriate status. The protocol driver must resubmit the send requests when the reset operation is completed, assuming the NIC becomes operational again.

When a protocol driver receives a status of NDIS\_STATUS\_RESET\_START, it should:

-   Hold any network data that is ready to be transmitted until *Protocol(Co)Status* receives an NDIS\_STATUS\_RESET\_END notification.

-   Not make any NDIS calls that are directed to the underlying miniport driver, except calls to return resources such as returning network data with [**NdisReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564534).

After *ProtocolStatusEx*(or *ProtocolCoStatusEx*) receives an NDIS\_STATUS\_RESET\_END message, the protocol driver can resume sending network data and OID requests.

 

 





