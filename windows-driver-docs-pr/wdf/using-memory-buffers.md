---
title: Using Memory Buffers
author: windows-driver-content
description: Using Memory Buffers
ms.assetid: f5699837-f1ba-4088-82b3-d7e27341fb46
keywords: ["memory buffers WDK KMDF", "buffers WDK KMDF", "memory objects WDK KMDF", "framework objects WDK KMDF , memory objects", "lookaside lists WDK KMDF", "memory descriptor lists WDK KMDF", "MDLs WDK KMDF", "local buffers WDK KMDF"]
---

# Using Memory Buffers


## <a href="" id="ddk-referencing-memory-df"></a>


Drivers typically use memory buffers to pass data to and from the framework and other drivers or to store information locally. This topic describes [framework memory objects](#using-framework-memory-objects), [lookaside lists](#using-lookaside-lists), [MDLs](#using-mdls), and [local buffers](#allocating-local-buffers).

### <a href="" id="using-framework-memory-objects"></a> Using Framework Memory Objects

The framework uses *memory objects* to describe the memory buffers that a driver receives from and passes to the framework. Each framework memory object represents one buffer.

To create a memory object, your driver calls one of the following object methods:

-   [**WdfMemoryCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548706), which creates a memory object and allocates a memory buffer of a specified size.

-   [**WdfMemoryCreatePreallocated**](https://msdn.microsoft.com/library/windows/hardware/ff548712), which creates a memory object for a preallocated buffer.

-   [**WdfMemoryCreateFromLookaside**](https://msdn.microsoft.com/library/windows/hardware/ff548709), which creates a memory buffer from a [lookaside list](#using-lookaside-lists).

To obtain a memory object that represents a received I/O request's buffers, your driver calls [**WdfRequestRetrieveInputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550015) and [**WdfRequestRetrieveOutputMemory**](https://msdn.microsoft.com/library/windows/hardware/ff550019). For more information about retrieving an I/O request's buffers, see [Accessing Data Buffers in Framework-Based Drivers](https://msdn.microsoft.com/library/windows/hardware/ff540701).

To obtain the address and size of a memory object's buffer, your driver calls [**WdfMemoryGetBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548715).

To move data into or out of a memory object's buffer, your driver calls either [**WdfMemoryCopyFromBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548701) or [**WdfMemoryCopyToBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548703). These object methods check the source and destination sizes and prevent buffer overrun errors.

If your driver creates a memory object by calling [**WdfMemoryCreatePreallocated**](https://msdn.microsoft.com/library/windows/hardware/ff548712), it can subsequently assign a different buffer to the memory object by calling [**WdfMemoryAssignBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff548697).

When a driver sends an I/O request to an [I/O target](using-i-o-targets.md), it typically passes an input or output buffer to a [framework I/O target object method](https://msdn.microsoft.com/library/windows/hardware/dn265644). The driver specifies the buffer by either passing a [**WDF\_MEMORY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff552392) structure that describes the buffer or by passing a memory object handle. (I/O target object methods that send I/O requests synchronously require a **WDF\_MEMORY\_DESCRIPTOR** structure, and methods that send I/O requests asynchronously require a memory object handle.)

For information about when a memory buffer is valid, see [Memory Buffer Life Cycle](memory-buffer-life-cycle.md).

### <a href="" id="using-lookaside-lists"></a> Using Lookaside Lists

If your driver will require many buffers of approximately the same size, it should allocate them from a *lookaside list*. The driver creates a lookaside list by calling [**WdfLookasideListCreate**](https://msdn.microsoft.com/library/windows/hardware/ff548694). Subsequently, the driver can obtain buffers from the lookaside list by calling [**WdfMemoryCreateFromLookaside**](https://msdn.microsoft.com/library/windows/hardware/ff548709).

Each time the driver calls [**WdfMemoryCreateFromLookaside**](https://msdn.microsoft.com/library/windows/hardware/ff548709), the framework creates a memory object, obtains a buffer from the lookaside list, and assigns the buffer to the object. When the driver has finished using one of these memory objects it calls [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734), which deletes the memory object and returns the buffer space to the lookaside list.

The operating system manages the memory resources that are assigned to the lookaside list. If the driver requests a buffer from the lookaside list when none are available, such as the first time that the driver calls [**WdfMemoryCreateFromLookaside**](https://msdn.microsoft.com/library/windows/hardware/ff548709), the system allocates a buffer and assigns it to the list. When the driver calls [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) (and the buffer space is returned to the lookaside list), the system keeps the now unassigned buffer in the list until the driver needs it again. The system increases the list's size as necessary; for example, drivers that more frequently request buffers receive larger lookaside lists. On the other hand, the system might reduce the number of buffers in the list if the driver is not using them all.

### <a href="" id="using-mdls"></a> Using MDLs

Some drivers use memory descriptor lists (MDLs) to describe buffers. For example, a driver for a direct memory access (DMA) device must pass a MDL to the [**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099) method, if it calls that method.

A driver that uses MDLs can obtain an MDL that represents a received I/O request's buffers by calling [**WdfRequestRetrieveInputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550016) and [**WdfRequestRetrieveOutputWdmMdl**](https://msdn.microsoft.com/library/windows/hardware/ff550021).

Most framework-based drivers do not use MDLs.

### <a href="" id="allocating-local-buffers"></a> Allocating Local Buffers

A driver that requires local, internal buffer space that it will not pass to the framework does not have to create memory objects to represent the buffers. The driver can call [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) to allocate internal buffers. When the driver has finished using the buffer, it must call [**ExFreePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544593).

However, drivers can also use memory objects for local buffers. An advantage to using memory buffers, instead of calling [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520), is that the framework automatically deletes memory objects and their buffers when each object's parent object is deleted.

### Aligning Buffers

Your driver can use the [**WDF\_ALIGN\_SIZE\_UP**](https://msdn.microsoft.com/library/windows/hardware/ff551217) or [**WDF\_ALIGN\_SIZE\_DOWN**](https://msdn.microsoft.com/library/windows/hardware/ff551214) function to calculate a buffer size that is aligned to a specified alignment offset. This calculation is useful if your driver must allocate multiple contiguous buffers, if each buffer must begin at an address alignment boundary.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Memory%20Buffers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




