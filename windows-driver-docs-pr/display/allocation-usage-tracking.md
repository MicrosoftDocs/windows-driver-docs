---
title: Allocation usage tracking
description: With the allocation list going away, the video memory manager no longer has visibility into the allocations being referenced in a particular command buffer.
ms.assetid: F913C9A3-535F-4DA0-8895-7A05CBF4D4AC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocation usage tracking


With the allocation list going away, the video memory manager no longer has visibility into the allocations being referenced in a particular command buffer. As a result of this, the video memory manager is no longer in a position to track allocation usage and to handle related synchronization. This responsibility will now fall to the user mode driver. In particular, the user mode driver will have to handle the synchronization with respect to direct CPU access to allocation as well as renaming.

For allocation destruction, the video memory manager will asynchronously defer these in a safe manner that will be both non-blocking for the calling thread and very performant. As such a user mode driver doesn't have to worry about having to defer allocation destruction. When an allocation destruction request is received, the video memory manager assumes, by default, that commands queued prior to the destruction request may potentially access the allocation being destroyed and defers the destruction operation until the queued commands finish. If the user mode driver knows that pending commands don't access the allocation being destroyed, it can instruct the video memory manager process the request without waiting by setting the **AssumeNotInUse** flag when calling [*Deallocate2*](https://msdn.microsoft.com/library/windows/hardware/dn906353) or [**DestroyAllocation2**](https://msdn.microsoft.com/library/windows/hardware/dn906772).

## <span id="Lock2"></span><span id="lock2"></span><span id="LOCK2"></span>Lock2


The user mode driver will be responsible for handling proper synchronization with respect to direct CPU access. In particular, a user mode driver will be required to support the following:

1.  Support no-overwrite and discard lock semantics. This implies that the user mode driver will have to implement its own renaming scheme.
2.  For map operations requiring synchronization (i.e. not the above no-overwrite or discard), the user mode driver will be required to:

    -   Return **WasStillDrawing** if an attempt is made to access an allocation which is currently busy and the caller has requested that the **Lock** operation not block the calling thread (**D3D11\_MAP\_FLAG\_DO\_NOT\_WAIT**).
    -   Or, if the **D3D11\_MAP\_FLAG\_DO\_NOT\_WAIT** flags is not set, wait until an allocation becomes available for CPU access. The user mode driver will be required to implement a non-polling wait. The user mode driver will make use of the new context monitoring mechanism.

For now, the user mode driver will continue to need to call [*LockCb*](https://msdn.microsoft.com/library/windows/hardware/ff568914)/[*UnlockCb*](https://msdn.microsoft.com/library/windows/hardware/ff569011) to ask the video memory manager to setup an allocation for CPU access. In most cases, the user mode driver will be able to keep the allocation mapped for its entire lifetime. However, in the future, *LockCb* and *UnlockCb* will be deprecated in favor of new [*Lock2Cb*](https://msdn.microsoft.com/library/windows/hardware/dn914483) and [*Unlock2Cb*](https://msdn.microsoft.com/library/windows/hardware/dn914484) calls. The goal of these new callbacks is to provide a fresh clean implementation with a fresh set of arguments and flags.

Swizzling ranges are removed from the Windows Display Driver Model (WDDM) v2 and it is the responsibility of the driver developer to remove the dependency on swizzling ranges from calls to [*LockCb*](https://msdn.microsoft.com/library/windows/hardware/ff568914) as they move towards an implementation that is based on [*Lock2Cb*](https://msdn.microsoft.com/library/windows/hardware/dn914483).

[*Lock2Cb*](https://msdn.microsoft.com/library/windows/hardware/dn914483) is exposed as a simple method for obtaining a virtual address to an allocation. There are a few restrictions based on the type of allocation as well as the current segment that it is currently resident in.

The following apply for *CPUVisible* allocations:

-   Cached *CPUVisible* allocations must reside within an aperture segment or not be resident in order to be locked. We cannot guarantee cache coherency between the CPU and a memory segment on the graphics processing unit (GPU).
-   *CPUVisible* allocations located in a fully *CPUVisible* memory segment (resized using the resizable BAR) are guaranteed to be lockable and able to return a virtual address. No special constraints are required in this scenario.
-   *CPUVisible* allocations located within a !*CPUVisible* memory segment (with or without access to a *CPUHostAperture*) can fail to be mapped into a CPU virtual address for various reasons. If the *CPUHostAperture* is out of available space or the allocation does not specify an aperture segment, a virtual address is impossible to obtain. For this reason we require that all *CPUVisible* allocations in !*CPUVisible* memory segments must contain an aperture segment in their supported segment set to guarantee that we will be able to place the allocation within system memory and provide a virtual address.
-   *CPUVisible* allocations already located within system memory (and/or mapped into an aperture segment) are guaranteed to work.

The following applies for !*CPUVisible* allocations:

-   *CPUVisible* allocations are backed by section objects which cannot point directly to the GPUs frame buffer. In order to lock a !*CPUVisible* allocation, we require that the allocation support an aperture segment in the supported segment set, or already be in system memory (must not be resident on the device).

If an allocation is successfully locked while the allocation is not resident on the device, but does not support an aperture segment, the allocation must be guaranteed to not be committed into a memory segment during the duration of the lock.

**Lock2** currently contains no flags, and **Reserved** flag bits must all be 0.

## <span id="CPUHostAperture"></span><span id="cpuhostaperture"></span><span id="CPUHOSTAPERTURE"></span>CPUHostAperture


To better support locking with !*CPUVisible* memory segments when resizing the BAR fails, a *CPUHostAperture* is provided in the PCI aperture. The *CPUHostAperture* behaves as a page-based manager which can then be mapped directly to regions of video memory via the [*DxgkDdiMapCpuHostAperture*](https://msdn.microsoft.com/library/windows/hardware/dn906340)device driver interface (DDI) function. This allows us to then map a range of virtual address space directly to a non-contiguous range of the *CPUHostAperture*, and have the *CPUHostAperture* then map to video memory without the need for swizzling ranges.

The maximum amount of lockable memory that can be referenced by the CPU within !*CPUVisible* memory segments is limited to the size of the *CPUHostAperture*. The details for exposing the *CPUHostAperture* to the Microsoft DirectX graphics kernel can be found in the [CPU host aperture](cpu-host-aperature.md) topic.

## <span id="I_O_coherency"></span><span id="i_o_coherency"></span><span id="I_O_COHERENCY"></span>I/O coherency


On x86/x64 today, we require that all GPUs support I/O coherency over PCIe in order to allow a GPU to read or write to a cacheable system memory surface and maintain coherency with the CPU. When a surface is mapped as cache coherent from the point of view of the GPU, the GPU needs to snoop the CPU caches when accessing the surface. This form of coherency is typically used for resources that the CPU is expected to read from, such as some staging surfaces.

On some ARM platforms, I/O coherency is not supported directly in hardware. On these platforms, I/O coherency needs to be emulated by manually invalidating the CPU cache hierarchy. The video memory manager achieves this today by tracking operations to an allocation coming from the GPU (allocation list read/write operation) as well as the CPU (Map operation, read/write) and emitting a cache invalidation when we determine the cache may either contain data that needs to be written back (CPU write, GPU read) or contain stale data that needs to be invalidated (GPU write, CPU reads).

On platform with no I/O coherency, the responsibility to track CPU and GPU access to allocations falls to the user mode driver. The graphics kernel exposes a new *Invalidate Cache*DDI that the user mode driver may use to write back and invalidate the virtual address range associated with a cacheable allocation. On platforms which do not have support for I/O coherency, the user mode driver will be required to call this function after CPU write and before GPU read as well as after write and before CPU read. The latter may seem unintuitive at first, but since the CPU could have speculatively read data prior to the GPU write making it to memory, it is necessary to invalidate all CPU caches to ensure the CPU re-reads data from RAM.

 

 





