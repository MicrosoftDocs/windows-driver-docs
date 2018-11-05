---
title: Pausing a Filter Module
description: Pausing a Filter Module
ms.assetid: da75b92d-b662-416a-b350-e5384b870b7f
keywords:
- filter modules WDK networking , pausing
- pausing filter modules
- filter drivers WDK networking , pausing filter modules
- NDIS filter drivers WDK , pausing filter modules
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pausing a Filter Module





To pause a running filter module, NDIS calls the filter driver's [*FilterPause*](https://msdn.microsoft.com/library/windows/hardware/ff549957) function. The filter module enters the *Pausing* state at the start of execution in the *FilterPause* function.

NDIS pauses a filter module as part of a Plug and Play operation to pause a driver stack. For an overview of pausing the driver stack, see [Pausing a Driver Stack](pausing-a-driver-stack.md).

On behalf of a filter module that is in the *Pausing* state, the filter driver:

-   Should not originate any new receive indications.

    For more information about send and receive operations, see [Filter Module Send and Receive Operations](filter-module-send-and-receive-operations.md).

-   If there are receive operations that the filter driver originated and that NDIS has not completed, the filter driver must wait for NDIS to complete such operations. The pause operation is not complete until NDIS calls the [*FilterReturnNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549964) function for all such outstanding receive indications.

-   Should return any outstanding receive indications that underlying drivers originated to NDIS immediately. The pause operation is not complete until the driver calls the [**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613) function for such outstanding receive indications. These outstanding receive indications can exist if the driver queues the buffers that it receives from underlying drivers.

-   Should return new receive indications that underlying drivers originate to NDIS immediately by calling the **NdisFReturnNetBufferLists** function. If necessary, the driver can copy receive indications and queue them before it returns them.

    **Note**  [**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613) should not be called for NBLs indicated with NDIS\_RECEIVE\_FLAGS\_RESOURCES flag set in a corresponding [*FilterReceiveNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549960) call. Such NBLs are returned to NDIS synchronously by returning from the *FilterReceiveNetBufferLists* routine.

     

-   Should not originate any new send requests.

-   If there are send operations that the filter driver originated and that NDIS has not completed, the filter driver must wait for NDIS to complete such operations. The pause operation is not complete until NDIS calls the [*FilterSendNetBufferListsComplete*](https://msdn.microsoft.com/library/windows/hardware/ff549967) function for all such outstanding send requests.

-   Should return all new send requests made to its [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) function immediately by calling the [**NdisFSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562618) function. The filter driver should set the **Status** member in each NET\_BUFFER\_LIST structure to NDIS\_STATUS\_PAUSED.

-   Can provide status indications with the [**NdisFIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff561824) function.

    For more information about status indications, see [Filter Module Status Indications](filter-module-status-indications.md).

-   Should handle status indications in its [*FilterStatus*](https://msdn.microsoft.com/library/windows/hardware/ff549973) function.

-   Should handle OID requests in the [*FilterOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff549954) function.

    For more information about OID requests, see [Filter Module OID Requests](filter-module-oid-requests.md).

-   Can initiate OID requests.

-   Should not free the resources the driver allocated during the attach operation.

-   Should cancel timers, if required to stop send and receive operations.

    For more information about timers, see [NDIS 6.0 Timer Services](https://msdn.microsoft.com/library/windows/hardware/ff567890).

After the filter driver successfully pauses the send and receive operations, it must complete the pause operation. The filter driver can complete the pause operation synchronously or asynchronously by returning NDIS\_STATUS\_SUCCESS or NDIS\_STATUS\_PENDING respectively from [*FilterPause*](https://msdn.microsoft.com/library/windows/hardware/ff549957).

If the driver returns NDIS\_STATUS\_PENDING, it must call the [**NdisFPauseComplete**](https://msdn.microsoft.com/library/windows/hardware/ff561839) function after it completes the pause operation.

On behalf of a filter module that is in the *Paused* state, the filter driver:

-   Should not originate new receive indications.

-   Should return new receive indications that underlying drivers originate to NDIS immediately by calling the [**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613) function. If necessary, the driver can copy receive indications and queue them before it returns them.

-   Should not originate new send requests.

-   Should return all new send requests made to its [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) function immediately by calling the [**NdisFSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562618) function. The filter driver should set the **Status** member in each NET\_BUFFER\_LIST structure to NDIS\_STATUS\_PAUSED.

-   Can provide status indications with the [**NdisFIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff561824) function.

-   Should handle status indications in its [*FilterStatus*](https://msdn.microsoft.com/library/windows/hardware/ff549973) function.

-   Should handle OID requests in the [*FilterOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff549954) function.

-   Can initiate OID requests.

NDIS does not initiate other Plug and Play operations, such as, attach, detach, or a restart requests, while the filter driver is in the *Pausing* state. NDIS can initiate detach or restart requests after a filter driver is in the *Paused* state. For more information about how to detach a filter module, see [Detaching a Filter Module](detaching-a-filter-module.md). For more information about how to restart a filter module, see [Starting a Filter Module](starting-a-filter-module.md).

 

 





