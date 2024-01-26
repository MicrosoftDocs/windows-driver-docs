---
title: Allocation Usage Tracking
description: With the allocation list going away, the video memory manager no longer has visibility into the allocations being referenced in a particular command buffer.
ms.date: 01/18/2024
---

# Allocation usage tracking

With the allocation list going away, the video memory manager (VidMm) no longer has visibility into the allocations being referenced in a particular command buffer. As a result, the VidMm is no longer in a position to track allocation usage and to handle related synchronization. This responsibility now falls to the user-mode driver (UMD). In particular, the UMD needs to handle the synchronization with respect to direct CPU access to allocation and renaming.

The VidMm asynchronously defers allocation destruction in a safe manner that is both nonblocking for the calling thread and performant. As such a UMD doesn't have to worry about having to defer allocation destruction. When VidMm receives an allocation destruction request, it assumes by default that commands queued prior to the destruction request might potentially access the allocation being destroyed. VidMm thus defers the destruction operation until the queued commands finish. If the UMD knows that pending commands don't access the allocation being destroyed, it can instruct the VidMm to process the request without waiting by setting the **AssumeNotInUse** flag when calling [*Deallocate2*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_deallocate2cb) or [**DestroyAllocation2**](/windows-hardware/drivers/ddi/d3dkmthk/nf-d3dkmthk-d3dkmtdestroyallocation2).

## Lock2

The UMD is responsible for handling proper synchronization with respect to direct CPU access. In particular, a UMD is required to:

1. Support no-overwrite and discard lock semantics, which implies that the UMD needs to implement its own renaming scheme.
2. For map operations requiring synchronization (that is, not the above no-overwrite or discard):

   - Return **WasStillDrawing** if an attempt is made to access an allocation that is currently busy and the caller has requested that the **Lock** operation not block the calling thread (**D3D11_MAP_FLAG_DO_NOT_WAIT**).
   - Or, if the **D3D11_MAP_FLAG_DO_NOT_WAIT** flag isn't set, wait until an allocation becomes available for CPU access. The UMD needs to implement a nonpolling wait. The UMD will make use of the new context monitoring mechanism.

For now, the UMD continues to need to call [*LockCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lockcb)/[*UnlockCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlockcb) to ask the VidMm to set up an allocation for CPU access. In most cases, the UMD is able to keep the allocation mapped for its entire lifetime. However, in the future, *LockCb* and *UnlockCb* will be deprecated in favor of new [*Lock2Cb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lock2cb) and [*Unlock2Cb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_unlock2cb) calls. The goal of these newer callbacks is to provide a fresh clean implementation with a fresh set of arguments and flags.

Swizzling ranges are removed from WDDM version 2. It's the responsibility of the driver developer to remove the dependency on swizzling ranges from calls to [*LockCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lockcb) as they move towards an implementation that is based on [*Lock2Cb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lock2cb).

[*Lock2Cb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lock2cb) is exposed as a simple method for obtaining a virtual address to an allocation. There are a few restrictions based on the type of allocation and the current segment that it's currently resident in.

The driver indicates whether a segment is CPU-accessible through the [**CpuVisible**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) flag, which is in the **Flags** member of the [**DXGK_SEGMENTDESCRIPTOR**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_segmentflags) structure.

For CPU-accessible allocations:

- Cached CPU-accessible allocations must reside within an aperture segment or not be resident in order to be locked. We can't guarantee cache coherency between the CPU and a memory segment on the graphics processing unit (GPU).
- CPU-accessible allocations located in a fully CPU-accessible memory segment (resized using the resizable BAR) are guaranteed to be lockable and able to return a virtual address. No special constraints are required in this scenario.
- CPU-accessible allocations located within a non-CPU-accessible memory segment (with or without access to a *CpuHostAperture*) can fail to be mapped into a CPU virtual address for various reasons. If the *CpuHostAperture* is out of available space or the allocation doesn't specify an aperture segment, a virtual address is impossible to obtain. For this reason, all CPU-accessible allocations in non-CPU-accessible memory segments must contain an aperture segment in their supported segment set. This requirement guarantees that VidMm is able to place the allocation within system memory and provide a virtual address.
- CPU-accessible allocations already located within system memory (and/or mapped into an aperture segment) are guaranteed to work.

For non-CPU-accessible allocations:

- CPU-accessible allocations are backed by section objects that can't point directly to the GPUs frame buffer. In order to lock a non-CPU-accessible allocation, the allocation must support an aperture segment in the supported segment set, or already be in system memory (must not be resident on the device).

If an allocation is successfully locked while the allocation isn't resident on the device, but doesn't support an aperture segment, the allocation must not be committed into a memory segment for the duration of the lock.

**Lock2** currently contains no flags, and **Reserved** flag bits must all be 0.

## CpuHostAperture

To better support locking with non-CPU-accessible memory segments when resizing the BAR fails, a *CpuHostAperture* is provided in the PCI aperture. The *CpuHostAperture* behaves as a page-based manager, which can then be mapped directly to regions of video memory via the [*DxgkDdiMapCpuHostAperture*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_mapcpuhostaperture)device driver interface (DDI) function. The VidMm can then map a range of virtual address space directly to a noncontiguous range of the *CpuHostAperture*, and have the *CpuHostAperture* then map to video memory without the need for swizzling ranges.

The maximum amount of lockable memory that the CPU can reference within non-CPU-accessible memory segments is limited to the size of the *CpuHostAperture*. The details for exposing the *CpuHostAperture* to the DirectX graphics kernel can be found in [CPU host aperture](cpu-host-aperature.md).

## I/O coherency

On x86/x64 today, all GPUs must support I/O coherency over PCIe in order to allow a GPU to read or write to a cacheable system memory surface and maintain coherency with the CPU. When a surface is mapped as cache coherent from the point of view of the GPU, the GPU needs to snoop the CPU caches when accessing the surface. This form of coherency is typically used for resources that the CPU is expected to read from, such as some staging surfaces.

On some Arm platforms, I/O coherency isn't supported directly in hardware. On these platforms, I/O coherency needs to be emulated by manually invalidating the CPU cache hierarchy. The VidMm does so by tracking operations to an allocation coming from the GPU (allocation list read/write operation) and the CPU (Map operation, read/write). VidMm emits a cache invalidation when it determines the cache might either contain:

- Data that needs to be written back (CPU write, GPU read)
- Stale data that needs to be invalidated (GPU write, CPU reads).

On platform with no I/O coherency, the responsibility to track CPU and GPU access to allocations falls to the UMD. The graphics kernel exposes a new *Invalidate Cache*DDI that the UMD can use to write back and invalidate the virtual address range associated with a cacheable allocation. On platforms that don't have support for I/O coherency, the UMD is required to call this function after CPU write and before GPU read as well as after write and before CPU read. The latter might seem unintuitive at first. But, since the CPU could have speculatively read data prior to the GPU write making it to memory, it's necessary to invalidate all CPU caches to ensure the CPU re-reads data from RAM.
