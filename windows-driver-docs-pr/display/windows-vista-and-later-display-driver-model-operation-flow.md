---
title: Windows Display Driver Model (WDDM) Operation Flow
description: Windows Display Driver Model (WDDM) Operation Flow
keywords:
- display driver model WDK Windows Vista , operation flow
- Windows Vista display driver model WDK , operation flow
- rendering devices WDK display
- command buffers WDK display , operation flow
- DMA buffers WDK display , operation flow
- buffers WDK display
ms.date: 01/06/2023
---

# Windows Display Driver Model (WDDM) operation flow

The following diagram shows the flow of WDDM operations that occur from when a rendering device is created to when the content is presented to the display. The information that follows the diagram describes the ordered sequence of the operation flow in more detail.

![diagram illustrating the wddm operation flow.](images/lddmflow.png)

* **Creating a Rendering Device**

  After an application requests to create a rendering device:

  * **1**: The DirectX Graphics Kernel Subsystem (DXGK) calls the display miniport driver's (KMD) [**DxgkDdiCreateDevice**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice) function.

    KMD initializes direct memory access (DMA) by returning a pointer to a filled [**DXGK_DEVICEINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_deviceinfo) structure in the **pInfo** member of the [**DXGKARG_CREATEDEVICE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_createdevice) structure.

  * **2**: If the call to [**DxgkDdiCreateDevice**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createdevice) succeeds, the Direct3D runtime calls the user-mode display driver's (UMD) [**CreateDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) function.

  * **3**: In the [**CreateDevice**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createdevice) call, UMD must explicitly call the runtime's [**pfnCreateContextCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createcontextcb) function to create one or more GPU contexts, which are GPU threads of execution on the newly created device. The runtime returns information to UMD in the **pCommandBuffer** and **CommandBufferSize** members of the [**D3DDDICB_CREATECONTEXT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddicb_createcontext) structure to initialize the command buffer.

* **Creating Surfaces for a Device**

  After an application requests to create surfaces for the rendering device:

  * **4**:  The Direct3D runtime calls UMD's [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) function.

  * **5**: [**CreateResource**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_createresource) calls the runtime-supplied [**pfnAllocateCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_allocatecb) function.

  * **6**: The runtime calls KMD's [**DxgkDdiCreateAllocation**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_createallocation) function, specifying the number and types of allocations to create. **DxgkDdiCreateAllocation** returns information about the allocations in an array of [**DXGK_ALLOCATIONINFO**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_allocationinfo) structures in the **pAllocationInfo** member of the [**DXGKARG_CREATEALLOCATION**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_createallocation) structure.

* **Submitting the Command Buffer to Kernel Mode**

  After an application requests to draw to a surface:

  * **7**: The Direct3D runtime calls the UMD function related to the drawing operation, for example, [**DrawPrimitive2**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_drawprimitive2).

  * **8**: The Direct3D runtime calls either the UMD's [**Present**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_present) or [**Flush**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_flush) function to cause the command buffer to be submitted to kernel-mode. Note: UMD will also submit the command buffer if the command buffer is full.

  * **9**: In response to Step 8, UMD calls one of the following runtime-supplied functions:

    * The runtime's [**pfnPresentCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_presentcb) function if [**Present**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_present) was called.
    * The runtime's' [**pfnRenderCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_rendercb) function if [**Flush**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_flush) was called or the command buffer is full.

  * **10**: KMD's [**DxgkDdiPresent**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_present) function is called if [**pfnPresentCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_presentcb) was called, or the [**DxgkDdiRender**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_render) or [**DxgkDdiRenderKm**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_renderkm) function if [**pfnRenderCb**](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_rendercb) was called. KMD validates the command buffer, writes to the DMA buffer in the hardware's format, and produces an allocation list that describes the surfaces used.

* **Submitting the DMA Buffer to Hardware**

  * **11**: DXGK calls KMD's [**DxgkDdiBuildPagingBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) function to create special purpose DMA buffers that move the allocations specified in the allocation list to and from GPU-accessible memory. These special DMA buffers are known as paging buffers. [**DxgkDdiBuildPagingBuffer**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) is not called for every frame.

  * **12**: DXGK calls KMD's [**DxgkDdiSubmitCommand**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand) function to queue the paging buffers to the GPU execution unit.

  * **13**: DXGK calls KMD's [**DxgkDdiPatch**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_patch) function to assign physical addresses to the resources in the DMA buffer.

  * **14**: DXGK calls KMD's [**DxgkDdiSubmitCommand**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand) function to queue the DMA buffer to the GPU execution unit. Each DMA buffer submitted to the GPU contains a fence identifier, which is a number. After the GPU finishes processing the DMA buffer, the GPU generates an interrupt.

  * **15**: KMD is notified of the interrupt in its [**DxgkDdiInterruptRoutine**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_interrupt_routine) function. KMD should read, from the GPU, the fence identifier of the DMA buffer that just completed.

  * **16**: KMD should call the [**DxgkCbNotifyInterrupt**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_notify_interrupt) function to notify the DXGK that the DMA buffer completed. KMD should also call the [**DxgkCbQueueDpc**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_queue_dpc) function to queue a deferred procedure call (DPC).
