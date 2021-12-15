---
title: GPU preemption
description: A new GPU preemption model is available starting with Windows 8.
ms.date: 04/20/2017
---

# GPU preemption

A newer GPU preemption model was available starting with Windows 8. In this model the operating system no longer allows the preemption of GPU direct memory access (DMA) packets to be disabled, and it guarantees that preemption requests will be sent to the GPU before a [Timeout Detection and Recovery (TDR)](timeout-detection-and-recovery.md) process is initiated.

| Requirement | Description |
| ----------- | ----------- |
| Minimum Windows Display Driver Model (WDDM) version | 1.2
| Minimum Windows version | 8 |
| Driver implementation—Full graphics and Render only |  Mandatory |
| [WHLK](/windows-hardware/test/hlk) requirements and tests | **Device.Graphics…Preemption Test**, **Device.Graphics…FlipOnVSyncMmIo** |

If long-running packets cannot be successfully preempted, high-priority GPU work, such as work required by the Desktop Window Manager (DWM), can be delayed, resulting in glitches during window transitions and animations. Also, long-running GPU packets that cannot be preempted can cause a TDR process to repeatedly reset the GPU, and eventually a system bugcheck can occur.

**Note**  
All WDDM 1.2 display miniport drivers must support the Windows 8 preemption model. However, when in operation, WDDM 1.2 drivers can also reject the Windows 8 preemption model and retain Windows 7 behavior by the Microsoft DirectX graphics kernel subsystem scheduler.

## GPU preemption device driver interfaces (DDIs)

The following device driver interfaces (DDIs) are available for the display miniport driver to implement the Windows 8 GPU preemption model.

- [*DxgkCbCreateContextAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_createcontextallocation)
- [*DxgkCbDestroyContextAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_destroycontextallocation)
- [*pfnSetPriorityCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_setprioritycb)
- [Dxgkrnl Interface](/windows-hardware/drivers/ddi/dispmprt)
- [**DXGKRNL_INTERFACE**](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgkrnl_interface)
- [**D3DKMDT_COMPUTE_PREEMPTION_GRANULARITY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_compute_preemption_granularity)
- [**D3DKMDT_GRAPHICS_PREEMPTION_GRANULARITY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_graphics_preemption_granularity)
- [**D3DKMDT_PREEMPTION_CAPS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_preemption_caps)
- [**D3DKMT_QUERYADAPTERINFO**](/windows-hardware/drivers/ddi/d3dkmthk/ns-d3dkmthk-_d3dkmt_queryadapterinfo)
- [**DXGK_DRIVERCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_drivercaps)
- [**DXGK_SUBMITCOMMANDFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_submitcommandflags)
- [**DXGK_VIDSCHCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps)
- [**DXGKARGCB_CREATECONTEXTALLOCATION**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkargcb_createcontextallocation)

## Display miniport driver implementation

Follow these general steps to implement the Windows 8 GPU preemption model in your display miniport driver:

1. Compile your driver against headers that have **DXGKDDI_INTERFACE_VERSION** &gt;= **DXGKDDI_INTERFACE_VERSION_WIN8**.
2. Declare support for the Windows 8 GPU preemption model by setting the **PreemptionAware** and **MultiEngineAware** members of the [**DXGK_VIDSCHCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps) structure to 1. To support the Windows 7 preemption model, set **PreemptionAware** to zero.
3. Specify the supported level of preemption granularity in the [**D3DKMDT_PREEMPTION_CAPS**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_preemption_caps) structure, which takes constant values from the [**D3DKMDT_GRAPHICS_PREEMPTION_GRANULARITY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_graphics_preemption_granularity) and [**D3DKMDT_COMPUTE_PREEMPTION_GRANULARITY**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_compute_preemption_granularity) enumerations.
4. If the hardware supports lazy context switching, submit a zero-length buffer to the [*DxgkDdiSubmitCommand*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand) function and set the *pSubmitCommand*-&gt;**Flags**-&gt;**ContextSwitch** member to 1. Note the discussion under the **ContextSwitch** member of the [**DXGK_SUBMITCOMMANDFLAGS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_submitcommandflags) structure.
5. Set GPU context allocations and device context allocations by calling the [*DxgkCbCreateContextAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_createcontextallocation) function. Note the specific instructions and restrictions given in Remarks for the function.
6. Call the [*DxgkCbDestroyContextAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_destroycontextallocation) function to destroy GPU context allocations and device context allocations that were created with [*DxgkCbCreateContextAllocation*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_createcontextallocation).
7. When preparing the DMA buffer in response to a call to the [*DxgkDdiBuildPagingBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) function, initialize the context resource by filling in the **InitContextResource** internal structure within the [**DXGKARG_BUILDPAGINGBUFFER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_buildpagingbuffer) structure. If context resources are evicted or relocated, the video memory manager will preserve the content of the context resources.
8. The driver must support memory-mapped I/O flip on the next vertical sync. In Windows 8, the GPU scheduler attempts to preempt hardware even if flips are pending. Therefore, to prevent tearing and rendering artifacts, the driver must support the memory-mapped I/O flip model and must set the **FlipOnVSyncMmIo** member of the [**DXGK_FLIPCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_flipcaps) structure to 1 and support the operations described under **FlipOnVSyncMmIo**.

### Memory mapping considerations in your implementation

Create a robust driver that supports the Windows 8 GPU preemption model and provides a quality user experience by following this guidance:

- Request mid-DMA buffer preemption from the GPU when the DirectX graphics kernel (Dxgkrnl) scheduler sends a preemption command. Hardware devices that have a finer granularity of mid-DMA buffer preemption should produce a better customer experience.
- Allow paging command fence IDs to be reused: if a preemption request resulted in preempting paging commands in the hardware queue, the Dxgkrnl scheduler will resubmit preempted paging commands with the same fence IDs that were originally used for them, and the paging commands will be scheduled prior to any other commands on that engine. Non-paging commands will be resubmitted with newly assigned fence IDs.
- Provide a patch location list for split DMA buffers—see [Splitting a DMA Buffer](splitting-a-dma-buffer.md).
- A verification mode, called binding leak detection, is available that walks through the patch location list and rejects packets that do not unbind, or that do not reprogram allocations for each split packet. Some hardware support virtual addresses, allowing an extra level of indirection that can make this verification unnecessary. In such a case, to indicate that the driver opts out of the verification mode, set the **NoDmaPatching** member of the [**DXGK_VIDSCHCAPS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps) structure to 1.
- In Windows 7, the Dxgkrnl scheduler guarantees that all split DMA packets that correspond to the same render command are executed sequentially without switching to another render context. In the Windows 8 preemption model, the scheduler can execute render packets from a different context between two split packets that correspond to the same render command. As a consequence, drivers that are aware of preemption should handle a split/partial DMA packet submission in the same way as a regular full packet submission. In particular, GPU state must be saved or restored at the boundary for such submissions.
- A preemption-aware driver must not change the content of a split DMA buffer when it is broadcast to multiple adapters in linked display adapter (LDA) mode, where multiple physical GPUs are linked to form a single, faster, virtual GPU. This is because, in the Windows 8 preemption model, the Dxgkrnl scheduler no longer guarantees synchronous execution of a split packet sequence without switching to another context. A driver that changed the content of a split DMA packet would compromise the integrity of the packet's data because if the packet were executed on another engine, it would operate on the same copy of DMA buffer data.
- In the Windows 8 GPU preemption model, the Dxgkrnl scheduler enables preemption for packets that have associated "signal on submit" synchronization primitives. If a device uses "signal on submit" synchronization primitives in conjunction with hardware-based wait states, it must support the ability to preempt a wait instruction before the wait condition is satisfied.

## Hardware certification requirements

For info on requirements that hardware devices must meet when they implement this feature, refer to the relevant [WHCK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) on **Device.Graphics…Preemption Test** and **Device.Graphics…FlipOnVSyncMmIo**.

See [WDDM 1.2 features](wddm-v1-2-features.md) for a review of features added with Windows 8.
