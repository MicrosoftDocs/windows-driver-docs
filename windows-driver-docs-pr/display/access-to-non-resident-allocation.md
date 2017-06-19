---
title: Access to non-resident allocation
description: GPU access to allocations which are not resident is illegal and will result in a device removed for the application that generated the error.
ms.assetid: 698ECD53-861A-4750-B33C-DF0611B87829
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# <span id="display.access_to_non-resident_allocation"></span>Access to non-resident allocation


Graphics processing unit (GPU) access to allocations which are not resident is illegal and will result in a device removed for the application that generated the error.

There are two distinct models of handling such invalid access dependent on whether the faulting engine supports GPU virtual addressing or not:

-   For engines which don’t support GPU virtual addressing and use the allocation and patch location list to patch memory references, an invalid access occurs when the user mode driver submits an allocation list which references an allocation which is not resident on the device (i.e. the user mode driver hasn’t called [*MakeResidentCb*](https://msdn.microsoft.com/library/windows/hardware/dn906357) on that allocation). When this occurs, the graphics kernel will put the faulty context/device in error.
-   For engines which do support GPU virtual addressing but access a GPU virtual address that is invalid, either because there is no allocation behind the virtual address or there is a valid allocation but it hasn’t been made resident, the GPU is expected to raise an unrecoverable page fault in the form of an interrupt. When the page fault interrupt occurs, the kernel mode driver will need to forward the error to the graphics kernel through a new page fault notification. Upon receiving this notification, the graphics kernel will initiate an engine reset on the faulting engine and put the faulty context/device in error. If the engine reset is unsuccessful, the graphics kernel will promote the error to a full adapter wide timeout detection and recovery (TDR).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Access%20to%20non-resident%20allocation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




