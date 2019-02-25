---
title: Submitting a Command Buffer
description: Submitting a Command Buffer
ms.assetid: 3622697a-3989-4756-89d4-c67c81815d49
keywords:
- command buffers WDK display , submitting
- submitting command buffers WDK display
- passing command buffers WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Submitting a Command Buffer


## <span id="ddk_submitting_a_command_buffer_gg"></span><span id="DDK_SUBMITTING_A_COMMAND_BUFFER_GG"></span>


The following sequence of operations must be performed to pass a command buffer through the Windows Vista graphics stack:

1.  The user-mode display driver initiates a command-buffer submission if the Direct3D runtime calls one of the following user-mode display driver functions to perform the specified operation:

    -   The [**Present**](https://msdn.microsoft.com/library/windows/hardware/ff569176) function to display graphics.
    -   The [**Flush**](https://msdn.microsoft.com/library/windows/hardware/ff565957) function to submit hardware commands.
    -   The [**Lock**](https://msdn.microsoft.com/library/windows/hardware/ff568213) function to lock a resource, which is used in the current command batch.

    Note that the user-mode display driver also always initiates a command-buffer submission whenever the command buffer is full.

2.  The user-mode display driver calls the Direct3D runtime's [**pfnRenderCb**](https://msdn.microsoft.com/library/windows/hardware/ff568923) function to submit the command buffer to the runtime.

3.  The DirectX graphics kernel subsystem calls the display miniport driver's [**DxgkDdiRender**](https://msdn.microsoft.com/library/windows/hardware/ff559793) or [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800) function to validate the command buffer, write a DMA buffer in the hardware's format, and produce an allocation list that describes the surfaces used. Note that the DMA buffer has not yet been patched (that is, assigned physical addresses).
    **Note**   If the runtime initiated the command-buffer submission by calling the user-mode display driver's [**Present**](https://msdn.microsoft.com/library/windows/hardware/ff569176) function, the graphics subsystem calls the display miniport driver's [**DxgkDdiPresent**](https://msdn.microsoft.com/library/windows/hardware/ff559743) function, rather than [**DxgkDdiRender**](https://msdn.microsoft.com/library/windows/hardware/ff559793) or [**DxgkDdiRenderKm**](https://msdn.microsoft.com/library/windows/hardware/ff559800).

     

4.  The video memory manager calls the display miniport driver's [**DxgkDdiBuildPagingBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff559587) function to create special purpose DMA buffers, known as paging buffers, that move the allocations specified in the allocation list that accompanies the DMA buffer to and from GPU-accessible memory. For more information, see [Paging Video Memory Resources](paging-video-memory-resources.md).

5.  The GPU scheduler calls the display miniport driver's [**DxgkDdiPatch**](https://msdn.microsoft.com/library/windows/hardware/ff559737) function to assign physical addresses to the resources in the DMA buffer. However, the scheduler is not required to call **DxgkDdiPatch** to assign physical addresses to the paging buffer because physical addresses for the paging buffer were passed in and assigned during the [*DxgkDdiBuildPagingBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff559587) call.

6.  The GPU scheduler calls the display miniport driver's [**DxgkDdiSubmitCommand**](https://msdn.microsoft.com/library/windows/hardware/ff560790) function to request that the driver queue the paging buffer to the GPU execution unit.

7.  The GPU scheduler calls the display miniport driver's [**DxgkDdiSubmitCommand**](https://msdn.microsoft.com/library/windows/hardware/ff560790) function to request that the driver queue the DMA buffer to the GPU execution unit. Each DMA buffer submitted to the GPU contains a fence identifier. After the GPU finishes processing the DMA buffer, the GPU generates an interrupt.

8.  The display miniport driver is notified of the interrupt in its [**DxgkDdiInterruptRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff559680) function. The display miniport driver should read, from the GPU, the fence identifier of the DMA buffer that just completed.

9.  The display miniport driver should call the [**DxgkCbNotifyInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff559545) function to notify the GPU scheduler that the DMA buffer completed.

10. The display miniport driver should call the [**DxgkCbQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff559559) function to queue a deferred procedure call (DPC).

11. The display miniport driver's DPC is notified to handle most of the DMA buffer processing.

 

 





