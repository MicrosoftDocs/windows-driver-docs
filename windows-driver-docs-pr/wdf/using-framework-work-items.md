---
title: Using Framework Work Items
description: Using Framework Work Items
keywords:
- work items WDK KMDF
- queues WDK KMDF , framework work items
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Framework Work Items





A *work item* is a task that a driver performs in an [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) event callback function. These functions run asynchronously, at IRQL = PASSIVE\_LEVEL, in the context of a system worker thread.

Framework-based drivers commonly use work items if an [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) function, which runs at IRQL = DISPATCH\_LEVEL, must perform additional processing at IRQL = PASSIVE\_LEVEL.

In other words, a driver can use work items if a function that runs at IRQL = DISPATCH\_LEVEL must call a function that can be called only at IRQL = PASSIVE\_LEVEL.

Typically, a driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) or [*EvtDpcFunc*](/windows-hardware/drivers/ddi/wdfdpc/nc-wdfdpc-evt_wdf_dpc) callback function creates a work-item object and adds it to the system's work-item queue. Subsequently, a system worker thread dequeues the object and calls the work item's [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function.

### Sample Drivers That Use Work Items

[Sample framework-based drivers](sample-kmdf-drivers.md) that use work items include 1394, AMCC5933, PCIDRV, and Toaster.

### <a href="" id="ddk-setting-up-a-work-item-df"></a>Setting Up a Work Item

To set up a work item, your driver must:

1.  Create the work item.

    Your driver calls [**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate) to create a work-item object and to identify an [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function that will process the work item.

2.  Store information about the work item.

    Typically, drivers use the context memory of the work-item object to store information about the task that the [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function should perform. When the *EvtWorkItem* callback function is called, it can retrieve the information by accessing this context memory. For information about how to allocate and access context memory, see [Framework Object Context Space](framework-object-context-space.md).

3.  Add the work item to the system's work-item queue.

    Your driver calls [**WdfWorkItemEnqueue**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue), which adds the driver's work item to the work-item queue.

When your driver calls [**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate), it must supply a handle to either a framework device object or a framework queue object. When the system deletes that object, it also deletes any existing work items that are associated with the object. The work item object will be disposed and its associated work-item callback will be cleaned up before the parent object's [*EvtCleanupCallback*](/windows-hardware/drivers/ddi/wdfobject/nc-wdfobject-evt_wdf_object_context_cleanup) callback is invoked.

For more info about the cleanup rules for a framework object hierarchy, see [Framework Object Life Cycle](./framework-object-life-cycle.md).

### <a href="" id="ddk-using-the-work-item-callback-function-df"></a>Using the Work-Item Callback Function

After the work item has been added to the work-item queue, it remains in the queue until a system worker thread becomes available. The system worker thread removes the work item from the queue and then calls the driver's [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function, passing the work-item object as input.

Typically, the [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function performs the following steps:

1.  Obtains driver-supplied information about the work item by accessing the context memory of the work-item object.

2.  Performs the task that you specified. If necessary, the callback function can call [**WdfWorkItemGetParentObject**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemgetparentobject) to determine the work item's parent object.

3.  Calls [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) to delete the work-item object or, if the driver will requeue the work item, indicates that the handle to the work item is now available for reuse.

The task that each work item's callback function performs must be relatively short. The operating system provides a limited number of system worker threads, so your driver can impede system performance if it uses work-item callback functions to perform time-consuming tasks.

### <a href="" id="ddk-creating-and-deleting-work-items-df"></a>Creating and Deleting Work Items

Drivers can use one of the following two techniques to create and delete work items:

-   Use each work item once: create the work item when you need it and delete it immediately after it is used.

    This technique is useful for drivers that require infrequent use (less often than once per minute) of a small number of work items.

    For example, a driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function can call [**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate) and then [**WdfWorkItemEnqueue**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue), and the work item's [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function can call [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

    If your driver follows this scenario, and if its [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function receives a STATUS\_INSUFFICIENT\_RESOURCES return value from [**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate), the driver must be able to postpone the required work until system resources (typically memory) become available.

-   Create one or more work items that your driver requeues as necessary.

    This technique is useful for drivers that use work items frequently (more often than once per minute), or if your driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function cannot easily handle a STATUS\_INSUFFICIENT\_RESOURCES return value from [**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate).

    The system does not allocate a worker thread to a work item until the driver calls [**WdfWorkItemEnqueue**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue). Therefore, even though system worker threads are a limited resource, creating work items while initializing a device consumes a small amount of memory but does not otherwise affect system performance.

    The following steps describe a possible scenario:

    1.  A driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function calls [**WdfWorkItemCreate**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemcreate) to obtain a work item handle.
    2.  The driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function creates a list of actions that the [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function must perform and then calls [**WdfWorkItemEnqueue**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue), using the handle from step 1.
    3.  The driver's [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function performs the list of actions and sets a flag to indicate that the callback function has run.

    Subsequently, each time that the driver's [*EvtInterruptDpc*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_dpc) callback function is called it must determine if the [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) callback function has run. If the *EvtWorkItem* callback function has not run, the *EvtInterruptDpc* callback function does not call [**WdfWorkItemEnqueue**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemenqueue), because the work item is still queued. In this case, the *EvtInterruptDpc* callback function only updates the list of actions for the *EvtWorkItem* callback function.

    Each work item is associated with a device or a queue. When the associated device or queue is removed, the framework deletes all of the associated work items, so if you are using this technique, the driver does not have to call [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete).

A few drivers might need to call [**WdfWorkItemFlush**](/windows-hardware/drivers/ddi/wdfworkitem/nf-wdfworkitem-wdfworkitemflush) to flush their work items from the work-item queue. For an example use of **WdfWorkItemFlush**, see the method's reference page.

If the driver calls [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) on an outstanding work item, the result depends on the state of the work item:

|Work item state|Result|
|-|-|
|Created but not enqueued|Work item is cleaned up immediately.|
|Enqueued|Call to [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) waits until work item finishes execution, then work item is cleaned up|
|Executing|If the driver calls [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) from within [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) (on same thread), [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) returns immediately. Once [*EvtWorkItem*](/windows-hardware/drivers/ddi/wdfworkitem/nc-wdfworkitem-evt_wdf_workitem) finishes, the work item will be cleaned up.  Otherwise, [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete) waits for EvtWorkItem to finish.|

