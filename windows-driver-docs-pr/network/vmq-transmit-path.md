---
title: VMQ Transmit Path
description: VMQ Transmit Path
ms.assetid: a34f0708-e477-4acc-b854-f00f752be423
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# VMQ Transmit Path





For transmit requests, the overlying driver uses the [**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407) macro to set the queue identifier of the outgoing queue in the outgoing data with the **NetBufferListFilteringInfo** OOB information. The **NetBufferListFilteringInfo** information is specified in an [**NDIS\_NET\_BUFFER\_LIST\_FILTERING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566567) structure.

NDIS drivers can use the [**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407) macro to set or get the queue identifier of a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. If a queue group contains more than one VM queue, the queue identifier of the transmit packet might be set to the queue identifier of any of the VM queues in the group.

Protocol drivers set the NDIS\_SEND\_FLAGS\_SINGLE\_QUEUE bit on the *SendFlags* parameter of the [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) function to indicate that all of the transmit NET\_BUFFER\_LIST structures in the call are for the same transmit queue.

Miniport drivers set the NDIS\_SEND\_COMPLETE\_FLAGS\_SINGLE\_QUEUE bit on the *SendCompleteFlags* parameter of the [**NdisMSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff563668) function to indicate that all NET\_BUFFER\_LISTs in the call were sent on the same transmit queue.

For more information about filter tests, see [VMQ Filter Operations](vmq-filter-operations.md).

**Note**  When a VMQ is deleted (for example, during VM live migration), it is possible for the miniport driver to receive an NBL that contains an invalid **QueueId** value. If this happens, the miniport should ignore the invalid queue ID and use 0 (the default queue) instead. The **QueueId** is found in the **NetBufferListFilteringInfo** portion of the NBL's OOB data, and is retrieved by using the [**NET\_BUFFER\_LIST\_RECEIVE\_QUEUE\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff568407) macro.

 

 

 





