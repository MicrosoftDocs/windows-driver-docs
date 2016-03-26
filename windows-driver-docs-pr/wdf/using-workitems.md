---
title: Using Work Items
description: Using Work Items
ms.assetid: 4617A33F-9026-45FF-9CC2-7215423E6D35
---

# Using Work Items


\[This topic applies to UMDF 1.*x*.\]

A work item is a task that a driver performs in an [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) event callback function. These functions run asynchronously.

UMDF drivers commonly use work items if an [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902) must perform additional processing without delaying the execution of the interrupt service request (ISR) because the interrupt line may be shared by multiple devices.

Typically, a driver's [*OnInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/hh463902) callback function creates a work-item object and adds it to the system's work-item queue. Subsequently, a threadpool thread dequeues the object and calls the work item's [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) callback function.

## Setting Up a Work Item


To set up a work item, your driver must:

1.  Create the work item.

    Your driver calls [**IWDFDevice3::CreateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/hh451213) to create a work-item object and to identify an [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) callback function that will process the work item.

2.  Store information about the work item.

    Typically, drivers use the context memory of the work-item object to store information about the task that the [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) callback function should perform. When the *OnWorkItem* callback function is called, it can retrieve the information by accessing this context memory. For information about how to allocate and access context memory, see[**IWDFObject::AssignContext**](https://msdn.microsoft.com/library/windows/hardware/ff560208).

3.  Add the work item to the system's work-item queue.

    Your driver calls [**IWDFWorkItem::Enqueue**](https://msdn.microsoft.com/library/windows/hardware/hh463883), which adds the driver's work item to the work-item queue.

When your driver calls [**IWDFDevice3::CreateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/hh451213), it may optionally supply a parent object (for example a device object or a queue object). When the system deletes that object, it also deletes any existing work items that are associated with the object.

## Using the WorkItem Callback Function


After the work item has been added to the work-item queue, it remains in the queue until a system worker thread becomes available. The system worker thread removes the work item from the queue and then calls the driver's OnWorkItem callback function, passing the work-item object as input.

Typically, the OnWorkItem callback function performs the following steps:

1.  Obtains driver-supplied information about the work item by accessing the context memory of the work-item object.
2.  Performs the task that you specified. If necessary, the callback function can call [**IWDFWorkItem::GetParentObject**](https://msdn.microsoft.com/library/windows/hardware/hh463891) to determine the work item's parent object.
3.  If the driver will requeue the work item, indicates that the handle to the work item is now available for reuse.

A few drivers might need to call [**IWDFWorkItem::Flush**](https://msdn.microsoft.com/library/windows/hardware/hh463886) to flush their work items from the work-item queue. If a driver calls the **Flush** method, the method does not return until a worker thread has removed the specified work item from the work-item queue and called the driver's [*OnWorkItem*](https://msdn.microsoft.com/library/windows/hardware/hh463909) callback function, and the *OnWorkItem* callback function has subsequently returned after processing the work item.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Work%20Items%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




