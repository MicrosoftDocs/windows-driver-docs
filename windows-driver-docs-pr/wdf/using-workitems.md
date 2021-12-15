---
title: Using Work Items
description: Using Work Items
ms.date: 04/20/2017
---

# Using Work Items


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

A work item is a task that a driver performs in an [*OnWorkItem*](/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) event callback function. These functions run asynchronously.

UMDF drivers commonly use work items if an [*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr) must perform additional processing without delaying the execution of the interrupt service request (ISR) because the interrupt line may be shared by multiple devices.

Typically, a driver's [*OnInterruptIsr*](/windows-hardware/drivers/ddi/wudfinterrupt/nc-wudfinterrupt-wudf_interrupt_isr) callback function creates a work-item object and adds it to the system's work-item queue. Subsequently, a threadpool thread dequeues the object and calls the work item's [*OnWorkItem*](/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) callback function.

## Setting Up a Work Item


To set up a work item, your driver must:

1.  Create the work item.

    Your driver calls [**IWDFDevice3::CreateWorkItem**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createworkitem) to create a work-item object and to identify an [*OnWorkItem*](/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) callback function that will process the work item.

2.  Store information about the work item.

    Typically, drivers use the context memory of the work-item object to store information about the task that the [*OnWorkItem*](/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) callback function should perform. When the *OnWorkItem* callback function is called, it can retrieve the information by accessing this context memory. For information about how to allocate and access context memory, see[**IWDFObject::AssignContext**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfobject-assigncontext).

3.  Add the work item to the system's work-item queue.

    Your driver calls [**IWDFWorkItem::Enqueue**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfworkitem-enqueue), which adds the driver's work item to the work-item queue.

When your driver calls [**IWDFDevice3::CreateWorkItem**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice3-createworkitem), it may optionally supply a parent object (for example a device object or a queue object). When the system deletes that object, it also deletes any existing work items that are associated with the object.

## Using the WorkItem Callback Function


After the work item has been added to the work-item queue, it remains in the queue until a system worker thread becomes available. The system worker thread removes the work item from the queue and then calls the driver's OnWorkItem callback function, passing the work-item object as input.

Typically, the OnWorkItem callback function performs the following steps:

1.  Obtains driver-supplied information about the work item by accessing the context memory of the work-item object.
2.  Performs the task that you specified. If necessary, the callback function can call [**IWDFWorkItem::GetParentObject**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfworkitem-getparentobject) to determine the work item's parent object.
3.  If the driver will requeue the work item, indicates that the handle to the work item is now available for reuse.

A few drivers might need to call [**IWDFWorkItem::Flush**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfworkitem-flush) to flush their work items from the work-item queue. If a driver calls the **Flush** method, the method does not return until a worker thread has removed the specified work item from the work-item queue and called the driver's [*OnWorkItem*](/windows-hardware/drivers/ddi/wudfworkitem/nc-wudfworkitem-wudf_workitem_function) callback function, and the *OnWorkItem* callback function has subsequently returned after processing the work item.

 

