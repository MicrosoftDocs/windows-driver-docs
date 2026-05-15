---
title: Submitting a Command Buffer
description: Submitting a Command Buffer
keywords:
- command buffers WDK display , submitting
- submitting command buffers WDK display
- passing command buffers WDK display
ms.date: 04/24/2025
ms.topic: how-to
---

# Submitting a Command Buffer

The following sequence of operations must be performed to pass a command buffer through the Windows graphics stack:

1. The user-mode display driver (UMD) initiates a command-buffer submission if the Direct3D runtime calls one of the following UMD functions to perform the specified operation:

    * The [**Present**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_present) function to display graphics.
    * The [**Flush**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_flush) function to submit hardware commands.
    * The [**Lock**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_lock) function to lock a resource, which is used in the current command batch.

    The UMD also always initiates a command-buffer submission whenever the command buffer is full.

1. The UMD calls the Direct3D runtime's [**pfnRenderCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_rendercb) function to submit the command buffer to the runtime.

1. The DirectX graphics kernel subsystem (*Dxgkrnl*) calls the kernel-mode display miniport driver's (KMD) [**DxgkDdiRender**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_render) or [**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm) function to validate the command buffer, write a DMA buffer in the hardware's format, and produce an allocation list that describes the surfaces used. Note that the DMA buffer has not yet been patched (that is, assigned physical addresses).
    **Note**   If the runtime initiated the command-buffer submission by calling the UMD's [**Present**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_present) function, the graphics subsystem calls the KMD's [**DxgkDdiPresent**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_present) function, rather than [**DxgkDdiRender**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_render) or [**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm).

1. The video memory manager calls the KMD's [**DxgkDdiBuildPagingBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) function to create special purpose DMA buffers, known as paging buffers, that move the allocations specified in the allocation list that accompanies the DMA buffer to and from GPU-accessible memory. For more information, see [Paging Video Memory Resources](paging-video-memory-resources.md).

1. The GPU scheduler calls the KMD's [**DxgkDdiPatch**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_patch) function to assign physical addresses to the resources in the DMA buffer. However, the scheduler is not required to call **DxgkDdiPatch** to assign physical addresses to the paging buffer because physical addresses for the paging buffer were passed in and assigned during the [*DxgkDdiBuildPagingBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) call.

1. The GPU scheduler calls the KMD's [**DxgkDdiSubmitCommand**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand) function to request that the driver queue the paging buffer to the GPU execution unit.

1. The GPU scheduler calls the KMD's [**DxgkDdiSubmitCommand**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand) function to request that the driver queue the DMA buffer to the GPU execution unit. Each DMA buffer submitted to the GPU contains a fence identifier. After the GPU finishes processing the DMA buffer, the GPU generates an interrupt.

1. The KMD is notified of the interrupt in its [**DxgkDdiInterruptRoutine**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_interrupt_routine) function. The KMD should read, from the GPU, the fence identifier of the DMA buffer that just completed.

1. The KMD should call the [**DxgkCbNotifyInterrupt**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_notify_interrupt) function to notify the GPU scheduler that the DMA buffer completed.

1. The KMD should call the [**DxgkCbQueueDpc**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_queue_dpc) function to queue a deferred procedure call (DPC).

1. The KMD's DPC is notified to handle most of the DMA buffer processing.
