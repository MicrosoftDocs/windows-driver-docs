---
title: GPU preemption
description: A new GPU preemption model is available starting with Windows 8.
ms.assetid: 9382786E-2E1E-408F-A9E9-04EEEA1CC34A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPU preemption


A new GPU preemption model is available starting with Windows 8. In this model the operating system no longer allows the preemption of GPU direct memory access (DMA) packets to be disabled, and it guarantees that preemption requests will be sent to the GPU before a [Timeout Detection and Recovery (TDR)](timeout-detection-and-recovery.md) process is initiated.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left">Minimum Windows Display Driver Model (WDDM) version</td>
<td align="left">1.2</td>
</tr>
<tr class="even">
<td align="left">Minimum Windows version</td>
<td align="left">8</td>
</tr>
<tr class="odd">
<td align="left">Driver implementation—Full graphics and Render only</td>
<td align="left">Mandatory</td>
</tr>
<tr class="even">
<td align="left"><a href="https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit" data-raw-source="[WHCK](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit)">WHCK</a> requirements and tests</td>
<td align="left"><p><strong>Device.Graphics…Preemption Test</strong></p>
<p><strong>Device.Graphics…FlipOnVSyncMmIo</strong></p></td>
</tr>
</tbody>
</table>

 

If long-running packets cannot be successfully preempted, high-priority GPU work, such as work required by the Desktop Window Manager (DWM), can be delayed, resulting in glitches during window transitions and animations. Also, long-running GPU packets that cannot be preempted can cause a TDR process to repeatedly reset the GPU, and eventually a system bugcheck can occur.

**Note**  
All WDDM 1.2 display miniport drivers must support the Windows 8 preemption model. However, when in operation, WDDM 1.2 drivers can also reject the Windows 8 preemption model and retain Windows 7 behavior by the Microsoft DirectX graphics kernel subsystem scheduler.

 

## <span id="GPU_preemption_device_driver_interfaces__DDIs_"></span><span id="gpu_preemption_device_driver_interfaces__ddis_"></span><span id="GPU_PREEMPTION_DEVICE_DRIVER_INTERFACES__DDIS_"></span>GPU preemption device driver interfaces (DDIs)


The following device driver interfaces (DDIs) are available for the display miniport driver to implement the Windows 8 GPU preemption model.

-   [*DxgkCbCreateContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/hh451312)
-   [*DxgkCbDestroyContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/hh451317)
-   [*pfnSetPriorityCb*](https://msdn.microsoft.com/library/windows/hardware/ff568931)
-   [Dxgkrnl Interface](https://msdn.microsoft.com/library/windows/hardware/ff560940)
-   [**DXGKRNL\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff560942)
-   [**D3DKMDT\_COMPUTE\_PREEMPTION\_GRANULARITY**](https://msdn.microsoft.com/library/windows/hardware/hh439326)
-   [**D3DKMDT\_GRAPHICS\_PREEMPTION\_GRANULARITY**](https://msdn.microsoft.com/library/windows/hardware/hh439329)
-   [**D3DKMDT\_PREEMPTION\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh439334)
-   [**D3DKMT\_QUERYADAPTERINFO**](https://msdn.microsoft.com/library/windows/hardware/ff548203)
-   [**DXGK\_DRIVERCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561062)
-   [**DXGK\_SUBMITCOMMANDFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562058)
-   [**DXGK\_VIDSCHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562863)
-   [**DXGKARGCB\_CREATECONTEXTALLOCATION**](https://msdn.microsoft.com/library/windows/hardware/hh451242)

## <span id="Display_miniport_driver_implementation"></span><span id="display_miniport_driver_implementation"></span><span id="DISPLAY_MINIPORT_DRIVER_IMPLEMENTATION"></span>Display miniport driver implementation


Follow these general steps to implement the Windows 8 GPU preemption model in your display miniport driver:

1.  Compile your driver against headers that have **DXGKDDI\_INTERFACE\_VERSION** &gt;= **DXGKDDI\_INTERFACE\_VERSION\_WIN8**.
2.  Declare support for the Windows 8 GPU preemption model by setting the **PreemptionAware** and **MultiEngineAware** members of the [**DXGK\_VIDSCHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562863) structure to 1. To support the Windows 7 preemption model, set **PreemptionAware** to zero.
3.  Specify the supported level of preemption granularity in the [**D3DKMDT\_PREEMPTION\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh439334) structure, which takes constant values from the [**D3DKMDT\_GRAPHICS\_PREEMPTION\_GRANULARITY**](https://msdn.microsoft.com/library/windows/hardware/hh439329) and [**D3DKMDT\_COMPUTE\_PREEMPTION\_GRANULARITY**](https://msdn.microsoft.com/library/windows/hardware/hh439326) enumerations.
4.  If the hardware supports lazy context switching, submit a zero-length buffer to the [*DxgkDdiSubmitCommand*](https://msdn.microsoft.com/library/windows/hardware/ff560790) function and set the *pSubmitCommand*-&gt;**Flags**-&gt;**ContextSwitch** member to 1. Note the discussion under the **ContextSwitch** member of the [**DXGK\_SUBMITCOMMANDFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562058) structure.
5.  Set GPU context allocations and device context allocations by calling the [*DxgkCbCreateContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/hh451312) function. Note the specific instructions and restrictions given in Remarks for the function.
6.  Call the [*DxgkCbDestroyContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/hh451317) function to destroy GPU context allocations and device context allocations that were created with [*DxgkCbCreateContextAllocation*](https://msdn.microsoft.com/library/windows/hardware/hh451312).
7.  When preparing the DMA buffer in response to a call to the [*DxgkDdiBuildPagingBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff559587) function, initialize the context resource by filling in the **InitContextResource** internal structure within the [**DXGKARG\_BUILDPAGINGBUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff557540) structure. If context resources are evicted or relocated, the video memory manager will preserve the content of the context resources.
8.  The driver must support memory-mapped I/O flip on the next vertical sync. In Windows 8, the GPU scheduler attempts to preempt hardware even if flips are pending. Therefore, to prevent tearing and rendering artifacts, the driver must support the memory-mapped I/O flip model and must set the **FlipOnVSyncMmIo** member of the [**DXGK\_FLIPCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff561069) structure to 1 and support the operations described under **FlipOnVSyncMmIo**.

### <span id="Memory_mapping_considerations_in_your_implementation"></span><span id="memory_mapping_considerations_in_your_implementation"></span><span id="MEMORY_MAPPING_CONSIDERATIONS_IN_YOUR_IMPLEMENTATION"></span>Memory mapping considerations in your implementation

Create a robust driver that supports the Windows 8 GPU preemption model and provides a quality user experience by following this guidance:

-   Request mid-DMA buffer preemption from the GPU when the DirectX graphics kernel (Dxgkrnl) scheduler sends a preemption command. Hardware devices that have a finer granularity of mid-DMA buffer preemption should produce a better customer experience.
-   Allow paging command fence IDs to be reused: if a preemption request resulted in preempting paging commands in the hardware queue, the Dxgkrnl scheduler will resubmit preempted paging commands with the same fence IDs that were originally used for them, and the paging commands will be scheduled prior to any other commands on that engine. Non-paging commands will be resubmitted with newly assigned fence IDs.
-   Provide a patch location list for split DMA buffers—see [Splitting a DMA Buffer](splitting-a-dma-buffer.md).
-   A verification mode, called binding leak detection, is available that walks through the patch location list and rejects packets that do not unbind, or that do not reprogram allocations for each split packet. Some hardware support virtual addresses, allowing an extra level of indirection that can make this verification unnecessary. In such a case, to indicate that the driver opts out of the verification mode, set the **NoDmaPatching** member of the [**DXGK\_VIDSCHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562863) structure to 1.
-   In Windows 7, the Dxgkrnl scheduler guarantees that all split DMA packets that correspond to the same render command are executed sequentially without switching to another render context. In the Windows 8 preemption model, the scheduler can execute render packets from a different context between two split packets that correspond to the same render command. As a consequence, drivers that are aware of preemption should handle a split/partial DMA packet submission in the same way as a regular full packet submission. In particular, GPU state must be saved or restored at the boundary for such submissions.
-   A preemption-aware driver must not change the content of a split DMA buffer when it is broadcast to multiple adapters in linked display adapter (LDA) mode, where multiple physical GPUs are linked to form a single, faster, virtual GPU. This is because, in the Windows 8 preemption model, the Dxgkrnl scheduler no longer guarantees synchronous execution of a split packet sequence without switching to another context. A driver that changed the content of a split DMA packet would compromise the integrity of the packet's data because if the packet were executed on another engine, it would operate on the same copy of DMA buffer data.
-   In the Windows 8 GPU preemption model, the Dxgkrnl scheduler enables preemption for packets that have associated "signal on submit" synchronization primitives. If a device uses "signal on submit" synchronization primitives in conjunction with hardware-based wait states, it must support the ability to preempt a wait instruction before the wait condition is satisfied.

## <span id="Hardware_certification_requirements"></span><span id="hardware_certification_requirements"></span><span id="HARDWARE_CERTIFICATION_REQUIREMENTS"></span>Hardware certification requirements


For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](https://docs.microsoft.com/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…Preemption Test** and **Device.Graphics…FlipOnVSyncMmIo**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.

 

 





