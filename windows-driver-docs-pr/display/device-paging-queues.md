---
title: Device paging queues
description: Various services exposed by the video memory manager can take a non-trivial amount of time to finish.
ms.assetid: AF79ED24-1CE5-4F12-A345-8554AD29057F
---

# Device paging queues


Various services exposed by the video memory manager can take a non-trivial amount of time to finish. For example, making an allocation resident can possibly involve bringing the allocation content, which hasnâ€™t been used in a long time, back from the page file. Reserving graphics processing unit (GPU) virtual address or mapping a virtual address to an already resident allocation arenâ€™t quite as expensive but still involve immediate page table update which needs to be queued onto the paging engine and may take a little while to finish.

Rather than forcing the thread requesting these services to wait until their completion, the video memory manager implements these services using an asynchronous queue. This asynchronous queue is called the device paging queue.

Each graphics device has a dedicated paging queue where various video memory manager requests are queued to the video memory manager thread pool for servicing. A device paging fence object is associated with the queue and every operation gets assigned a unique fence value that gets signaled when the video memory manager completes the operation. An operation that can be done immediately by the video memory manager returns a device paging fence value of zero.

The device paging fence is a regular monitored fence object and the user mode driver can wait on these video memory manager services either on the CPU or on the GPU.

Generally the user mode driver wants to push the synchronization as far as possible and will queue a GPU wait into a context before that context take a dependency on a requested video memory manager operation. For example, after reserving the virtual address for a *tile resource*, the user mode driver must ensure to wait until the reserve operation completes before a GPU engine starts accessing the virtual address range of the tile resource.

To obtain a reference to the device paging fence object a new **GetDevicePagingFenceObjectCb**device driver interface (DDI) is added to the user mode driver. This is illustrated below:

![device paging queues](images/device-paging-queues.1.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Device%20paging%20queues%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




