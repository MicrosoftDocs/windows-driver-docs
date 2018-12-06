---
title: System Worker Threads
description: System Worker Threads
ms.assetid: 01ae1c1b-0cb0-4b9b-bd74-341b7c289fd4
keywords: ["executive worker threads WDK kernel", "work items WDK kernel", "thread objects WDK kernel", "WorkItem", "WorkItemEx", "worker threads WDK kernel", "worker-thread callback routines WDK kernel", "callback routines WDK worker threads"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# System Worker Threads





A driver that requires delayed processing can use a [*work item*](https://msdn.microsoft.com/library/windows/hardware/ff556347#wdkgloss-work-item), which contains a pointer to a driver callback routine that performs the actual processing. The driver queues the work item, and a *system worker thread* removes the work item from the queue and runs the driver's callback routine. The system maintains a pool of these system worker threads, which are system threads that each process one work item at a time.

The driver associates a [*WorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff566380) callback routine with the work item. When the system worker thread processes the work item, it calls the associated *WorkItem* routine. In Windows Vista and later versions of Windows, a driver can instead associate a [*WorkItemEx*](https://msdn.microsoft.com/library/windows/hardware/ff566381) routine with a work item. *WorkItemEx* takes parameters that are different from the parameters that *WorkItem* takes.

*WorkItem* and *WorkItemEx* routines run in a system thread context. If a driver dispatch routine can run in a user-mode thread context, that routine can call a *WorkItem* or *WorkItemEx* routine to perform any operations that require a system thread context.

To use a work item, a driver performs the following steps:

1.  Allocate and initialize a new work item.

    The system uses an [**IO\_WORKITEM**](https://msdn.microsoft.com/library/windows/hardware/ff550679) structure to hold a work item. To allocate a new **IO\_WORKITEM** structure and initialize it as a work item, the driver can call [**IoAllocateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff548276). In Windows Vista and later versions of Windows, the driver can alternatively allocate its own **IO\_WORKITEM** structure, and call [**IoInitializeWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549349) to initialize the structure as a work item. (The driver should call [**IoSizeofWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff550352) to determine the number of bytes that are necessary to hold a work item.)

2.  Associate a callback routine with the work item, and queue the work item so that it will be processed by a system worker thread.

    To associate a *WorkItem* routine with the work item and queue the work item, the driver should call [**IoQueueWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549466). To instead associate a *WorkItemEx* routine with the work item and queue the work item, the driver should call [**IoQueueWorkItemEx**](https://msdn.microsoft.com/library/windows/hardware/ff549474).

3.  After the work item is no longer required, free it.

    A work item that was allocated by **IoAllocateWorkItem** should be freed by [**IoFreeWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549133). A work item that was initialized by **IoInitializeWorkItem** must be uninitialized by [**IoUninitializeWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff550392) before it can be freed.

    The work item can only be uninitialized or freed when the work item is not currently queued. The system dequeues the work item before it calls the work item's callback routine, so **IoFreeWorkItem** and **IoUninitializeWorkItem** can be called from within the callback.

A DPC that needs to initiate a processing task that requires lengthy processing or that makes a blocking call should delegate the processing of that task to one or more work items. While a DPC runs, all threads are prevented from running. Additionally, a DPC, which runs at IRQL = DISPATCH\_LEVEL, must not make blocking calls. However, the system worker thread that processes a work item runs at IRQL = PASSIVE\_LEVEL. Thus, the work item can contain blocking calls. For example, a system worker thread can wait on a dispatcher object.

Because the pool of system worker threads is a limited resource, *WorkItem* and *WorkItemEx* routines can be used only for operations that take a short period of time. If one of these routines runs for too long (if it contains an indefinite loop, for example) or waits for too long, the system can deadlock. Therefore, if a driver requires long periods of delayed processing, it should instead call [**PsCreateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559932) to create its own system thread.

Do not call **IoQueueWorkItem** or **IoQueueWorkItemEx** to queue a work item that is already in the queue. In checked builds, this error causes a bug check. In retail builds, the error is not detected but can cause corruption of system data structures. If your driver queues the same work item each time a particular driver routine runs, you can use the following technique to avoid queuing the work item a second time if it is already in the queue:

-   The driver maintains a list of tasks for the worker routine.
-   This task list is available in the context that is supplied to the worker routine. The worker routine and any driver routines that modify the task list synchronize their access to the list.
-   Each time the worker routine runs, it performs all the tasks in the list, and removes each task from the list as the task is completed.
-   When a new task arrives, the driver adds this task to the list. The driver queues the work item only if the task list was previously empty.

The system worker thread removes the work item from the queue before it calls the worker thread. Thus, a driver thread can safely queue the work item again as soon as the worker thread starts to run.

 

 




