---
title: Work Queue Dispatching Mechanisms
description: Work Queue Dispatching Mechanisms
ms.assetid: d4ce929f-2d84-4194-9afa-e00629594c36
keywords:
- RDBSS WDK file systems , work queue dispatching
- Redirected Drive Buffering Subsystem WDK file systems , work queue dispatching
- work queue dispatching WDK RDBSS
- dispatching work queue WDK RDBSS
- memory allocations WDK RDBSS
- Critical work queue WDK RDBSS
- Delayed work queue WDK RDBSS
- HyperCritical work queue WDK RDBSS
- bookkeeping WDK RDBSS
- statistics WDK RDBSS
- queues WDK RDBSS
- states WDK RDBSS
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Work Queue Dispatching Mechanisms


## <span id="ddk_work_queue_dispatching_mechanisms_if"></span><span id="DDK_WORK_QUEUE_DISPATCHING_MECHANISMS_IF"></span>


RDBSS uses Windows kernel work queues to dispatch operations on multiple threads for later execution. Network mini-redirector drivers can use the work queues maintained by RDBSS for dispatching operations for later execution.

RDBSS provides several routines that implement the dispatching mechanism used in RDBSS. These routines can also be used by network mini-redirector drivers.

RDBSS keeps track of the work items on a per-device-object basis. This allows RDBSS to handle the race conditions associated with loading and unloading network mini-redirectors. This also provides a mechanism in RDBSS for preventing a single network mini-redirector from unfairly using all of the resources.

There are certain scenarios in which dispatching of work items is inevitable. To avoid frequent memory allocation and to free operations in these scenarios, the WORK\_QUEUE\_ITEM is allocated as part of another data. In other scenarios where dispatching is rare, it pays to avoid memory allocation until it is required. The RDBSS work queue implementation provides for both of these scenarios in the form of dispatching and posting work queue requests. In the case of dispatching using the [**RxDispatchToWorkerThread**](https://msdn.microsoft.com/library/windows/hardware/ff554398) routine, no memory for the WORK\_QUEUE\_ITEM needs to be allocated by the caller. For posting using the [**RxPostToWorkerThread**](https://msdn.microsoft.com/library/windows/hardware/ff554620) routine, the memory for the WORK\_QUEUE\_ITEM needs to be allocated by the caller.

There are two common cases of dispatching operations to worker threads:

-   For a very infrequent operation, use the **RxDispatchToWorkerThread** routine to conserve memory use by dynamically allocating and freeing memory for the work queue item when it is needed.

-   When an operation is going to be repeatedly dispatched, use the **RxPostToWorkerThread** routine to conserve time by allocating in advance the WORK\_QUEUE\_ITEM as part of the data structure to be dispatched.

The trade off between the two dispatching operations is time versus space (memory use).

The dispatching mechanism in RDBSS provides for multiple levels of work queues on a per-processor basis. The following levels of work queues currently supported:

-   Critical

-   Delayed

-   HyperCritical

The distinction between Critical and Delayed is one of priority. The HyperCritical level is different from the other two in that the routines should not block (wait for any resource). This requirement cannot be enforced, so the effectiveness of the dispatching mechanism relies on the implicit cooperation of the clients.

The work queue implementation in RDBSS is built around a KQUEUE implementation. The additional support involves the regulation of a number of threads that are actively waiting for the work items. Each work queue data structure is allocated from nonpaged pool memory and has its own synchronization mechanism (a spinlock).

In addition to bookkeeping information (queue state and type, for example), RDBSS also maintains statistics that are gathered over the lifetime of the work queue. This can provide valuable information in tuning a work queue. The number of items that have been processed , the number of items that have to be processed, and the cumulative queue length is structureed. The cumulative queue length is an important metric and represents the sum of the number of items waiting to be processed each time an additional work item was queued. The cumulative queue length divided by the sum of the total number of items processed and the number of items to be processed gives an indication of the average queue length. A value much greater than one signifies that the minimum number of worker threads associated with the work queue can be increased. A value much less than one signifies that the maximum number of work threads associated with the queue can be decreased.

The work queue typically start in an active state and continue until either a non-recoverable situation is encountered (lack of system resources, for example) or when it transitions to the inactive state. When a rundown is initiated, it transitions to the rundown-in-progress state.

The rundown of work queues is not complete when the threads have been spun down. The termination of the threads needs to be ensured before the data structures can be torn down. The work queue implementation in RDBSS follows a protocol in which each of the threads being spun down saves a reference to the thread object in the rundown context. The rundown issuing thread (which does not belong to the work queue) waits for the completion of all of the threads spun down before tearing down the data structures.

The current implementation of **RxDispatchToWorkerThread** and **RxPostToWorkerThread** queues work onto the same processor from which the call originated.

The following RDBSS routines for work queue dispatching include.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554398" data-raw-source="[&lt;strong&gt;RxDispatchToWorkerThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554398)"><strong>RxDispatchToWorkerThread</strong></a></p></td>
<td align="left"><p>This routine invokes a routine in the context of a worker thread. The memory for the WORK_QUEUE_ITEM is allocated by this routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554620" data-raw-source="[&lt;strong&gt;RxPostToWorkerThread&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554620)"><strong>RxPostToWorkerThread</strong></a></p></td>
<td align="left"><p>This routine invokes the routine in the context of a worker thread. Memory for the WORK_QUEUE_ITEM must be allocated by the caller.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554734" data-raw-source="[&lt;strong&gt;RxSpinDownMRxDispatcher&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554734)"><strong>RxSpinDownMRxDispatcher</strong></a></p></td>
<td align="left"><p>This routine tears down the dispatcher context for a network mini-redirector.</p>
<p>Note that this routine is only available on Windows Server 2003 and Windows XP.</p></td>
</tr>
</tbody>
</table>

 

 

 




