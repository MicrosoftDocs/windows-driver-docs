---
title: Canceling a Send Operation
description: Canceling a Send Operation
ms.assetid: 5bd7a815-4e4d-4259-b322-f4f8d07f2e1a
keywords:
- network data WDK , sending
- data WDK networking , sending
- packets WDK networking , sending
- sending data WDK networking
- NDIS_SET_NET_BUFFER_LIST_CANCEL_ID
- canceling send operations WDK networking
- cancellation IDs WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling a Send Operation





The following figure illustrates canceling a send operation.

![diagram illustrating canceling a send operation](images/netbuffercancelsend.png)

A driver calls the [**NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff567299) macro for each [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure that it passes to lower-level drivers for transmission. The NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID function marks the specified packet with a cancellation identifier.

Before assigning cancellation IDs to packets, a driver should call [**NdisGeneratePartialCancelId**](https://msdn.microsoft.com/library/windows/hardware/ff562623) to obtain the high-order byte of each cancellation ID that it assigns. This ensures that the driver does not duplicate cancellation IDs assigned by other drivers in the system. Drivers typically call **NdisGeneratePartialCancelId** once from the **DriverEntry** routine; however, drivers can obtain more than one partial cancellation identifier by calling **NdisGeneratePartialCancelId** more than once.

To cancel the pending transmission of data in a marked NET\_BUFFER\_LIST structure, a driver passes the cancellation ID to the [**NdisCancelSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff561623) function. Drivers can obtain a NET\_BUFFER\_LIST structure's cancellation ID by calling the [**NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff565683) macro.

If a driver marks all [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures with the same cancellation identifier, it can cancel all pending transmissions with a single call to **NdisCancelSendNetBufferLists**. If a driver marks all NET\_BUFFER\_LIST structures within a subgroup of NET\_BUFFER\_LIST structures with a unique identifier, it can cancel all pending transmissions within that subgroup with a single call to **NdisCancelSendNetBufferLists**.

NDIS calls the [*MiniportCancelSend*](https://msdn.microsoft.com/library/windows/hardware/ff559342) function of the appropriate lower-level driver on the binding. After aborting the pending transmission, the underlying miniport driver calls the [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) function, to return the NET\_BUFFER\_LIST structures and a completion status of NDIS\_STATUS\_SEND\_ABORTED. NDIS, in turn, calls the appropriate driver's [**ProtocolSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff570268) function.

In its *ProtocolSendNetBufferListsComplete* function, a protocol driver can call NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID with *CancelId* set to **NULL**. This prevents the NET\_BUFFER\_LIST from inadvertently being used again with a stale cancellation ID.

 

 





