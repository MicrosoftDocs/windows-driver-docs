---
title: Canceling a Send Request in a Filter Driver
description: Canceling a Send Request in a Filter Driver
ms.assetid: afa9c8d3-b30b-4009-8428-d31719885154
keywords:
- canceling send operations WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Canceling a Send Request in a Filter Driver





Filter drivers can cancel send requests that were originated by the filter driver or that were originated by overlying drivers.

### Canceling Filter Driver Send Requests

The following figure illustrates canceling a send request that was originated by a filter driver.

![diagram illustrating canceling a send request that was originated by a filter driver](images/filtercancelsend.png)

A filter driver calls the [**NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-set-net-buffer-list-cancel-id) macro for each [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structure that it creates for send operations. The NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID function marks the specified data with a cancellation identifier.

Before assigning cancellation IDs to network data, a filter driver must call [**NdisGeneratePartialCancelId**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisgeneratepartialcancelid) to obtain the high-order byte of each cancellation ID that it assigns. This ensures that the driver does not duplicate cancellation IDs assigned by other drivers in the system. Drivers typically call **NdisGeneratePartialCancelId** one time from the [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-driver_initialize) routine. However, drivers can obtain more than one partial cancellation identifier by calling **NdisGeneratePartialCancelId** multiple times.

To cancel the pending transmission of data in a marked NET\_BUFFER\_LIST structure, a filter driver passes the cancellation ID to the [**NdisFCancelSendNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfcancelsendnetbufferlists) function. Drivers can obtain a NET\_BUFFER\_LIST structure's cancellation ID by calling the [**NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-get-net-buffer-list-cancel-id) macro.

If a filter driver marks all NET\_BUFFER\_LIST structures with the same cancellation identifier, it can cancel all pending transmissions with a single call to **NdisFCancelSendNetBufferLists**. If a filter driver marks all NET\_BUFFER\_LIST structures within a subgroup of NET\_BUFFER\_LIST structures with a unique identifier, it can cancel all pending transmissions within that subgroup with a single call to **NdisFCancelSendNetBufferLists**.

NDIS calls the cancel send function of the underlying drivers. After aborting the pending transmission, the underlying drivers call a send complete function (for example [**NdisMSendNetBufferListsComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndismsendnetbufferlistscomplete)) to return the NET\_BUFFER\_LIST structures with a completion status of NDIS\_STATUS\_SEND\_ABORTED. NDIS, in turn, calls the filter driver's [*FilterSendNetBufferListsComplete*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-filter_send_net_buffer_lists_complete) function.

In *FilterSendNetBufferListsComplete*, a filter driver can call NDIS\_SET\_NET\_BUFFER\_LIST\_CANCEL\_ID with *CancelId* set to **NULL**. This prevents the NET\_BUFFER\_LIST from accidentally being used again with a stale cancellation ID.

### Canceling Send Requests Originated by Overlying Drivers

The following figure illustrates canceling a send request that was originated by an overlying driver.

![diagram illustrating canceling a send request that was originated by an overlying driver](images/cancelfiltersend.png)

Overlying drivers call a cancel send function ( [**NdisFCancelSendNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfcancelsendnetbufferlists) or [**NdisCancelSendNetBufferLists**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndiscancelsendnetbufferlists)) to cancel outstanding send requests. These overlying drivers must mark the send data with a cancellation ID before making a send request.

NDIS calls a filter driver's [*FilterCancelSendNetBufferLists*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nc-ndis-filter_cancel_send_net_buffer_lists) function to cancel the transmission of all [**NET\_BUFFER\_LIST**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/ns-ndis-_net_buffer_list) structures that are marked with a specified cancellation identifier.

*FilterCancelSendNetBufferLists* performs the following operations:

1.  Traverses the filter driver's list of queued NET\_BUFFER\_LIST structures for the specified filter module and calls the [**NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID**](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-get-net-buffer-list-cancel-id) macro to obtain the cancellation identifier for each structure. The filter driver compares the cancellation ID that NDIS\_GET\_NET\_BUFFER\_LIST\_CANCEL\_ID returns with the cancellation ID that NDIS passed to *FilterCancelSendNetBufferLists*.

2.  Removes from the send queue (unlinks) all NET\_BUFFER\_LIST structures whose cancellation identifiers match the specified cancellation identifier.

3.  Calls the [**NdisFSendNetBufferListsComplete**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ndis/nf-ndis-ndisfsendnetbufferlistscomplete) function for all unlinked NET\_BUFFER\_LIST structures to return the structures. The filter driver sets the status field of the NET\_BUFFER\_LIST structures to NDIS\_STATUS\_SEND\_ABORTED.

4.  Calls the **NdisFCancelSendNetBufferLists** function to pass the cancel send request to underlying drivers. The filter driver passes on the cancellation identifier that it received from the overlying driver. The cancel operation proceeds as with a filter-driver-originated cancel send operation.

 

 





