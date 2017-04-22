---
title: Windows Display Driver Model (WDDM) Operation Flow
description: Windows Display Driver Model (WDDM) Operation Flow
ms.assetid: 8d2af92c-392a-457d-af9f-796e1050031d
keywords:
- display driver model WDK Windows Vista , operation flow
- Windows Vista display driver model WDK , operation flow
- rendering devices WDK display
- command buffers WDK display , operation flow
- DMA buffers WDK display , operation flow
- buffers WDK display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows Display Driver Model (WDDM) Operation Flow


The following diagram shows the flow of Windows Display Driver Model (WDDM) operations that occur from when a rendering device is created to when the content is presented to the display. The sequence in the sections that follow describes the operation flow in more detail.

![diagram illustrating the wddm operation flow](images/lddmflow.png)

### <span id="Creating_a_Rendering_Device"></span><span id="creating_a_rendering_device"></span><span id="CREATING_A_RENDERING_DEVICE"></span>Creating a Rendering Device

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>1.</p></td>
<td align="left"><p>After an application requests to create a rendering device, the display miniport driver receives a [<strong>DxgkDdiCreateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559615) call. The display miniport driver initializes direct memory access (DMA) by returning a pointer to a filled [<strong>DXGK_DEVICEINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561047) structure in the <strong>pInfo</strong> member of the [<strong>DXGKARG_CREATEDEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557570) structure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>2.</p></td>
<td align="left"><p>If the call to the display miniport driver's [<strong>DxgkDdiCreateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559615) succeeds, the Microsoft Direct3D runtime calls the user-mode display driver's [<strong>CreateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540634) function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3.</p></td>
<td align="left"><p>In the [<strong>CreateDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540634) call, the user-mode display driver must explicitly call the [<strong>pfnCreateContextCb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568895) function to create one or more contexts—GPU threads of execution on the newly created device. The Direct3D runtime returns information in the <strong>pCommandBuffer</strong> and <strong>CommandBufferSize</strong> members of the [<strong>D3DDDICB_CREATECONTEXT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544143) structure to initialize the command buffer.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Creating_Surfaces_for_a_Device"></span><span id="creating_surfaces_for_a_device"></span><span id="CREATING_SURFACES_FOR_A_DEVICE"></span>Creating Surfaces for a Device

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>4.</p></td>
<td align="left"><p>After an application requests to create surfaces for the rendering device, the Direct3D runtime calls the user-mode display driver's [<strong>CreateResource</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540688) function.</p></td>
</tr>
<tr class="even">
<td align="left"><p>5.</p></td>
<td align="left"><p>The user-mode display driver's [<strong>CreateResource</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540688) calls the [<strong>pfnAllocateCb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568893) runtime-supplied function.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>6.</p></td>
<td align="left"><p>The display miniport driver receives a [<strong>DxgkDdiCreateAllocation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559606) call, which indicates the number and types of allocations to create. <strong>DxgkDdiCreateAllocation</strong> returns information about the allocations in an array of [<strong>DXGK_ALLOCATIONINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560960) structures in the <strong>pAllocationInfo</strong> member of the [<strong>DXGKARG_CREATEALLOCATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff557559) structure.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Submitting_the_Command_Buffer_to_Kernel_Mode"></span><span id="submitting_the_command_buffer_to_kernel_mode"></span><span id="SUBMITTING_THE_COMMAND_BUFFER_TO_KERNEL_MODE"></span>Submitting the Command Buffer to Kernel Mode

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>7.</p></td>
<td align="left"><p>After an application requests to draw to a surface, the Direct3D runtime calls the user-mode display driver function related to the drawing operation, for example, [<strong>DrawPrimitive2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff556151).</p></td>
</tr>
<tr class="even">
<td align="left"><p>8.</p></td>
<td align="left"><p>To submit the command buffer to kernel-mode, the Direct3D runtime calls either the user-mode display driver's [<strong>Present</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569176) or [<strong>Flush</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565957) function. Also, the user-mode display driver submits the command buffer if the command buffer is full.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>9.</p></td>
<td align="left"><p>The user-mode display driver calls the [<strong>pfnPresentCb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568916) runtime-supplied function if [<strong>Present</strong>](https://msdn.microsoft.com/library/windows/hardware/ff569176) was called, or the [<strong>pfnRenderCb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568923) runtime-supplied function if [<strong>Flush</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565957) was called or the command buffer is full.</p></td>
</tr>
<tr class="even">
<td align="left"><p>10.</p></td>
<td align="left"><p>The display miniport driver receives a call to the [<strong>DxgkDdiPresent</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559743) function if [<strong>pfnPresentCb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568916) was called, or the [<strong>DxgkDdiRender</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559793) or [<strong>DxgkDdiRenderKm</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559800) function if [<strong>pfnRenderCb</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568923) was called. The display miniport driver validates the command buffer, writes to the DMA buffer in the hardware's format, and produces an allocation list that describes the surfaces used.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Submitting_the_DMA_Buffer_to_Hardware"></span><span id="submitting_the_dma_buffer_to_hardware"></span><span id="SUBMITTING_THE_DMA_BUFFER_TO_HARDWARE"></span>Submitting the DMA Buffer to Hardware

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>11.</p></td>
<td align="left"><p>The Microsoft DirectX graphics kernel subsystem calls the display miniport driver's [<strong>DxgkDdiBuildPagingBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559587) function to create special purpose DMA buffers, known as paging buffers, that move the allocations specified in the allocation list to and from GPU-accessible memory.</p>
<div class="alert">
<strong>Note</strong>  [<strong>DxgkDdiBuildPagingBuffer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559587) is not called for every frame.
</div>
<div>
 
</div></td>
</tr>
<tr class="even">
<td align="left"><p>12.</p></td>
<td align="left"><p>The DirectX graphics kernel subsystem calls the display miniport driver's [<strong>DxgkDdiSubmitCommand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560790) function to queue the paging buffers to the GPU execution unit.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>13.</p></td>
<td align="left"><p>The DirectX graphics kernel subsystem calls the display miniport driver's [<strong>DxgkDdiPatch</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559737) function to assign physical addresses to the resources in the DMA buffer.</p></td>
</tr>
<tr class="even">
<td align="left"><p>14.</p></td>
<td align="left"><p>The DirectX graphics kernel subsystem calls the display miniport driver's [<strong>DxgkDdiSubmitCommand</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560790) function to queue the DMA buffer to the GPU execution unit. Each DMA buffer submitted to the GPU contains a fence identifier, which is a number. After the GPU finishes processing the DMA buffer, the GPU generates an interrupt.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>15.</p></td>
<td align="left"><p>The display miniport driver is notified of the interrupt in its [<strong>DxgkDdiInterruptRoutine</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559680) function. The display miniport driver should read, from the GPU, the fence identifier of the DMA buffer that just completed.</p></td>
</tr>
<tr class="even">
<td align="left"><p>16.</p></td>
<td align="left"><p>The display miniport driver should call the [<strong>DxgkCbNotifyInterrupt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559545) function to notify the DirectX graphics kernel subsystem that the DMA buffer completed. The display miniport driver should also call the [<strong>DxgkCbQueueDpc</strong>](https://msdn.microsoft.com/library/windows/hardware/ff559559) function to queue a deferred procedure call (DPC).</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%20Display%20Driver%20Model%20%28WDDM%29%20Operation%20Flow%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




