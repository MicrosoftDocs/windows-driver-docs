---
title: Starting a Filter Module
description: Starting a Filter Module
ms.assetid: 493cb922-22bc-4845-b5a2-6f610559534d
keywords:
- filter modules WDK networking , starting
- starting filter modules
- filter drivers WDK networking , starting filter modules
- NDIS filter drivers WDK , starting filter modules
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting a Filter Module





To start a paused filter module, NDIS calls the filter driver's [*FilterSetModuleOptions*](https://msdn.microsoft.com/library/windows/hardware/ff549970) function, if any, followed by a call to the [*FilterRestart*](https://msdn.microsoft.com/library/windows/hardware/ff549962) function. The filter module enters the *Restarting* state at the start of execution in the *FilterRestart* function.

If the driver provided an entry point for [*FilterSetModuleOptions*](https://msdn.microsoft.com/library/windows/hardware/ff549970), the driver can change the partial characteristic for a filter module. For more information, see [Data Bypass Mode](data-bypass-mode.md).

When it calls a filter driver's [*FilterRestart*](https://msdn.microsoft.com/library/windows/hardware/ff549962) function, NDIS passes a pointer to an [**NDIS\_RESTART\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff567255) structure to filter driver in the **RestartAttributes** member of the [**NDIS\_FILTER\_RESTART\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565572) structure. Filter drivers can modify the restart attributes that are specified by underlying drivers. For more information about how to modify restart attributes, see *FilterRestart*.

**Note**  NDIS calls [*FilterSetModuleOptions*](https://msdn.microsoft.com/library/windows/hardware/ff549970) for all filter modules in a stack before NDIS calls the [*FilterRestart*](https://msdn.microsoft.com/library/windows/hardware/ff549962) function for any filter module in the stack.

 

NDIS starts a filter module as part of a Plug and Play operation to restart a driver stack. For an overview of restarting the driver stack, see [Restarting a Driver Stack](restarting-a-driver-stack.md).

On behalf of a filter module that is in the *Restarting* state, the filter driver:

-   Completes any operations that are required to restart normal send and receive operations.

    For more information about send and receive operations, see [Filter Module Send and Receive Operations](filter-module-send-and-receive-operations.md).

-   Can read or write configurable parameters for the filter module.

-   Can receive network data indications. The driver can copy and queue such data and indicate it to overlying drivers later, or it can discard the data.

-   Should not initiate any new receive indications.

-   Should reject all new send requests made to its [*FilterSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff549966) function immediately by calling the [**NdisFSendNetBufferListsComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562618) function. It should set the complete status in each [NET\_BUFFER\_LIST](net-buffer-list-structure.md) to NDIS\_STATUS\_PAUSED.

-   Can provide status indications with the [**NdisFIndicateStatus**](https://msdn.microsoft.com/library/windows/hardware/ff561824) function.

    For more information about status indications, see [Filter Module Status Indications](filter-module-status-indications.md).

-   Should handle OID requests in the [*FilterOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff549954) function.

    For more information about OID requests, see [Filter Module OID Requests](filter-module-oid-requests.md).

-   Should not initiate any new send requests.

-   Should return new receive indications to NDIS immediately by calling the [**NdisFReturnNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff562613) function. If necessary, the driver can copy such receive indications before it returns them.

-   Can make OID requests to the underlying drivers to set or query updated configuration information.

-   Should handle status indications in its [*FilterStatus*](https://msdn.microsoft.com/library/windows/hardware/ff549973) function.

-   Should Indicate NDIS\_STATUS\_SUCCESS or a failure status. If a filter module does not restart, NDIS will detach it and if it is a mandatory filter, NDIS terminates the entire driver stack.

After the filter driver successfully restarts the send and receive operations, it must complete the restart operation. The filter driver can complete the restart operation synchronously or asynchronously by returning NDIS\_STATUS\_SUCCESS or NDIS\_STATUS\_PENDING respectively from [*FilterRestart*](https://msdn.microsoft.com/library/windows/hardware/ff549962).

If the driver returns NDIS\_STATUS\_PENDING, it must call the [**NdisFRestartComplete**](https://msdn.microsoft.com/library/windows/hardware/ff562610) function after it completes the restart operation. In this case, he driver passes the final status of the restart operation to **NdisFRestartComplete**.

After the restart operation is complete, the filter module is in the *Running* state. The driver resumes normal send and receive processing.

NDIS does not initiate other Plug and Play operations, such as, attach, detach, or pause requests, while the filter driver is in the *Restarting* state. NDIS can initiate pause requests after a filter driver is in the *Running* state. For more information about pausing a filter module, see [Pausing a Filter Module](pausing-a-filter-module.md).

 

 





