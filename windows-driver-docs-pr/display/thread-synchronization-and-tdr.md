---
title: Thread Synchronization and TDR
description: Thread Synchronization and TDR
keywords:
- threading WDK display , TDR
- synchronization WDK display , TDR
- TDR (timeout detection and recovery) WDK display , and thread synchronization
- Windows Display Driver Model , WDDM , thread synchronization and TDR
ms.date: 12/18/2024
ms.topic: concept-article
---

# Thread Synchronization and TDR

The following figure shows how thread synchronization works for the kernel-mode display miniport driver (KMD) in the WDDM.

:::image type="content" source="images/lddmsync.png" alt-text="Diagram that shows thread synchronization in WDDM.":::

If a hardware timeout occurs, the system initiates the [Timeout Detection and Recovery (TDR)](timeout-detection-and-recovery.md) process. The GPU scheduler calls the driver's [*DxgkDdiResetFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout) function, which resets the GPU:

* *DxgkDdiResetFromTimeout* is called synchronously with any other KMD function, except for the runtime power management functions [*DxgkDdiSetPowerComponentFState*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddisetpowercomponentfstate) and [*DxgkDdiPowerRuntimeControlRequest*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddipowerruntimecontrolrequest). That is, the OS guarantees that no other thread runs in the driver while the *DxgkDdiResetFromTimeout* thread runs.
* The OS also guarantees that applications can't access the frame buffer during the call to *DxgkDdiResetFromTimeout*. Therefore, the driver can reset a memory controller phase locked loop (PLL) and so on.

While the recovery thread executes [*DxgkDdiResetFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout), interrupts and deferred procedure calls (DPCs) can continue to be called. The [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) function can be used to synchronize portions of the reset procedure with device interrupts.

After the driver returns from [*DxgkDdiResetFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout), most driver functions can again be called, and the OS starts to clean up resources that are no longer required. During the cleanup period, the following driver functions are called for the indicated reasons:

* The driver is called to notify about an allocation being evicted.

  For example, if the allocation was paged in a memory segment, the driver's [*DxgkDdiBuildPagingBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) function is called with the **Operation** member of the [**DXGKARG_BUILDPAGINGBUFFER**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_buildpagingbuffer) structure set to DXGK_OPERATION_TRANSFER and with the **Transfer.Size** member set to zero to inform the driver about the eviction. No content transfer is involved because the content was lost during the reset.

  If the allocation was paged in an aperture segment, the driver's [*DxgkDdiBuildPagingBuffer*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer) function is called with the **Operation** member of DXGKARG_BUILDPAGINGBUFFER set to DXGK_OPERATION_UNMAP_APERTURE_SEGMENT to inform the driver to unmap the allocation from the aperture.

* The driver's [*DxgkDdiReleaseSwizzlingRange*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_releaseswizzlingrange) function is called to release an unswizzling aperture and segment aperture ranges.

The driver shouldn't access the GPU during the preceding calls unless absolutely necessary.

After the cleanup period is over, the OS calls the driver's [*DxgkDdiRestartFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_restartfromtimeout) function to inform the driver that cleanup is complete and that the OS will resume using the adapter for rendering.
