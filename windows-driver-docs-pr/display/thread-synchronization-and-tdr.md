---
title: Thread Synchronization and TDR
description: Thread Synchronization and TDR
ms.assetid: 3690ad06-002a-4939-9b04-b87245678464
keywords: ["threading WDK display , TDR", "synchronization WDK display , TDR", "TDR (timeout detection and recovery) WDK display , and thread synchronization"]
---

# Thread Synchronization and TDR


The following figure shows how thread synchronization works for the display miniport driver in the Windows Display Driver Model (WDDM).

![diagram illustrating windows vista thread synchronization](images/lddmsync.png)

If a hardware timeout occurs, the [Timeout Detection and Recovery (TDR)](timeout-detection-and-recovery.md) process initiates. The GPU scheduler calls the driver's [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815) function, which resets the GPU. *DxgkDdiResetFromTimeout* is called synchronously with any other display miniport driver function, except for the runtime power management functions [*DxgkDdiSetPowerComponentFState*](https://msdn.microsoft.com/library/windows/hardware/hh451422) and [*DxgkDdiPowerRuntimeControlRequest*](https://msdn.microsoft.com/library/windows/hardware/hh451396). That is, no other thread runs in the driver while the *DxgkDdiResetFromTimeout* thread runs. The operating system also guarantees that no access to the frame buffer can occur from any application during the call to *DxgkDdiResetFromTimeout*; therefore, the driver can reset a memory controller phase locked loop (PLL) and so on.

While the recovery thread executes [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815), interrupts and deferred procedure calls (DPCs) can continue to be called. The [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) function can be used to synchronize portions of the reset procedure with device interrupts.

After the driver returns from [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815), most driver functions can again be called, and the operating system starts to clean up resources that are no longer required. During the cleanup period, the following driver functions are called for the indicated reasons:

-   The driver is called to notify about an allocation being evicted.

    For example, if the allocation was paged in a memory segment, the driver's [*DxgkDdiBuildPagingBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff559587) function is called with the **Operation** member of the [**DXGKARG\_BUILDPAGINGBUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff557540) structure set to DXGK\_OPERATION\_TRANSFER and with the **Transfer.Size** member set to zero to inform the driver about the eviction. Note that no content transfer is involved because the content was lost during the reset.

    If the allocation was paged in an aperture segment, the driver's [*DxgkDdiBuildPagingBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff559587) function is called with the **Operation** member of DXGKARG\_BUILDPAGINGBUFFER set to DXGK\_OPERATION\_UNMAP\_APERTURE\_SEGMENT to inform the driver to unmap the allocation from the aperture.

-   The driver's [*DxgkDdiReleaseSwizzlingRange*](https://msdn.microsoft.com/library/windows/hardware/ff559786) function is called to release an unswizzling aperture and segment aperture ranges.

The driver should not access the GPU during the preceding calls unless absolutely necessary.

After the cleanup period is over, the operating system calls the driver's [*DxgkDdiRestartFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559820) function to inform the driver that cleanup is complete and that the operating system will resume using the adapter for rendering.

**Note**  TDR functionality has been updated for Windows 8. See [TDR changes in Windows 8](tdr-changes-in-windows-8.md).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Thread%20Synchronization%20and%20TDR%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




