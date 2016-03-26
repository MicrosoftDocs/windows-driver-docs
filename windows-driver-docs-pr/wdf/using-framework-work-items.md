---
title: Using Framework Work Items
description: Using Framework Work Items
ms.assetid: d7e6d187-bed4-4071-a50b-90f32c4f0d5a
keywords: ["work items WDK KMDF", "queues WDK KMDF , framework work items"]
---

# Using Framework Work Items


## <a href="" id="ddk-using-framework-work-items-df"></a>


A *work item* is a task that a driver performs in an [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) event callback function. These functions run asynchronously, at IRQL = PASSIVE\_LEVEL, in the context of a system worker thread.

Framework-based drivers commonly use work items if an [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) function, which runs at IRQL = DISPATCH\_LEVEL, must perform additional processing at IRQL = PASSIVE\_LEVEL.

In other words, a driver can use work items if a function that runs at IRQL = DISPATCH\_LEVEL must call a function that can be called only at IRQL = PASSIVE\_LEVEL.

Typically, a driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDpcFunc*](https://msdn.microsoft.com/library/windows/hardware/ff541683) callback function creates a work-item object and adds it to the system's work-item queue. Subsequently, a system worker thread dequeues the object and calls the work item's [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function.

### Sample Drivers That Use Work Items

[Sample framework-based drivers](sample-kmdf-drivers.md) that use work items include 1394, AMCC5933, PCIDRV, and Toaster.

### <a href="" id="ddk-setting-up-a-work-item-df"></a>Setting Up a Work Item

To set up a work item, your driver must:

1.  Create the work item.

    Your driver calls [**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201) to create a work-item object and to identify an [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function that will process the work item.

2.  Store information about the work item.

    Typically, drivers use the context memory of the work-item object to store information about the task that the [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function should perform. When the *EvtWorkItem* callback function is called, it can retrieve the information by accessing this context memory. For information about how to allocate and access context memory, see [Framework Object Context Space](framework-object-context-space.md).

3.  Add the work item to the system's work-item queue.

    Your driver calls [**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203), which adds the driver's work item to the work-item queue.

When your driver calls [**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201), it must supply a handle to either a framework device object or a framework queue object. When the system deletes that object, it also deletes any existing work items that are associated with the object.

### <a href="" id="ddk-using-the-work-item-callback-function-df"></a>Using the Work-Item Callback Function

After the work item has been added to the work-item queue, it remains in the queue until a system worker thread becomes available. The system worker thread removes the work item from the queue and then calls the driver's [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function, passing the work-item object as input.

Typically, the [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function performs the following steps:

1.  Obtains driver-supplied information about the work item by accessing the context memory of the work-item object.

2.  Performs the task that you specified. If necessary, the callback function can call [**WdfWorkItemGetParentObject**](https://msdn.microsoft.com/library/windows/hardware/ff551207) to determine the work item's parent object.

3.  Calls [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the work-item object or, if the driver will requeue the work item, indicates that the handle to the work item is now available for reuse.

The task that each work item's callback function performs must be relatively short. The operating system provides a limited number of system worker threads, so your driver can impede system performance if it uses work-item callback functions to perform time-consuming tasks.

### <a href="" id="ddk-creating-and-deleting-work-items-df"></a>Creating and Deleting Work Items

Drivers can use one of the following two techniques to create and delete work items:

-   Use each work item once: create the work item when you need it and delete it immediately after it is used.

    This technique is useful for drivers that require infrequent use (less often than once per minute) of a small number of work items.

    For example, a driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function can call [**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201) and then [**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203), and the work item's [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function can call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734).

    If your driver follows this scenario, and if its [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function receives a STATUS\_INSUFFICIENT\_RESOURCES return value from [**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201), the driver must be able to postpone the required work until system resources (typically memory) become available.

-   Create one or more work items that your driver requeues as necessary.

    This technique is useful for drivers that use work items frequently (more often than once per minute), or if your driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function cannot easily handle a STATUS\_INSUFFICIENT\_RESOURCES return value from [**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201).

    The system does not allocate a worker thread to a work item until the driver calls [**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203). Therefore, even though system worker threads are a limited resource, creating work items while initializing a device consumes a small amount of memory but does not otherwise affect system performance.

    The following steps describe a possible scenario:

    1.  A driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function calls [**WdfWorkItemCreate**](https://msdn.microsoft.com/library/windows/hardware/ff551201) to obtain a work item handle.
    2.  The driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function creates a list of actions that the [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function must perform and then calls [**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203), using the handle from step 1.
    3.  The driver's [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function performs the list of actions and sets a flag to indicate that the callback function has run.

    Subsequently, each time that the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function is called it must determine if the [*EvtWorkItem*](https://msdn.microsoft.com/library/windows/hardware/ff541859) callback function has run. If the *EvtWorkItem* callback function has not run, the *EvtInterruptDpc* callback function does not call [**WdfWorkItemEnqueue**](https://msdn.microsoft.com/library/windows/hardware/ff551203), because the work item is still queued. In this case, the *EvtInterruptDpc* callback function only updates the list of actions for the *EvtWorkItem* callback function.

    Each work item is associated with a device or a queue. When the associated device or queue is removed, the framework deletes all of the associated work items, so if you are using this technique, the driver does not have to call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734).

A few drivers might need to call [**WdfWorkItemFlush**](https://msdn.microsoft.com/library/windows/hardware/ff551204) to flush their work items from the work-item queue. For an example use of **WdfWorkItemFlush**, see the method's reference page.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Framework%20Work%20Items%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




