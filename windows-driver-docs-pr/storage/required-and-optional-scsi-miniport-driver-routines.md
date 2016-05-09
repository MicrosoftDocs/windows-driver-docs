---
title: Required and Optional SCSI Miniport Driver Routines
author: windows-driver-content
description: Required and Optional SCSI Miniport Driver Routines
ms.assetid: 6fd1f7af-e8ba-4679-bd8c-f757b57821b0
keywords: ["SCSI miniport drivers WDK storage , required routines", "SCSI miniport drivers WDK storage , optional routines"]
---

# Required and Optional SCSI Miniport Driver Routines


## <span id="ddk_required_and_optional_scsi_miniport_driver_routines_kg"></span><span id="DDK_REQUIRED_AND_OPTIONAL_SCSI_MINIPORT_DRIVER_ROUTINES_KG"></span>


Every SCSI miniport driver must have at least the following system-defined routines:

-   [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654) to initialize the miniport driver

-   [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) to determine how (or whether) driver-supported HBA(s) are configured in the machine

-   [*HwScsiInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff557302) to initialize supported HBA(s)

-   [**HwScsiStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557323) to start operations on its HBA(s) for incoming requests

-   [*HwScsiResetBus*](https://msdn.microsoft.com/library/windows/hardware/ff557318) to handle bus reset requests

Depending on each HBA and the driver designer, SCSI miniport drivers also have some or all of the following system-defined routines:

-   [**HwScsiInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff557312)to handle HBA-generated interrupts, which is optional if and only if the HBA does not generate interrupts so the miniport driver manages all I/O operations on its HBA by polling. However, using polling exclusively has an adverse effect on a miniport driver's performance and on its HBA's I/O throughput. Such a miniport driver should also have an [*HwScsiTimer*](https://msdn.microsoft.com/library/windows/hardware/ff557327) routine.

-   [**HwScsiDisableInterruptsCallback**](https://msdn.microsoft.com/library/windows/hardware/ff557288) and [**HwScsiEnableInterruptsCallback**](https://msdn.microsoft.com/library/windows/hardware/ff557295) to handle deferred I/O processing if interrupt-driven I/O operations take a long time

-   *HwScsiTimer* to time operations that require long delays on the HBA, or for any other purpose determined by the driver designer. A miniport driver should have a *HwScsiTimer* routine if it has no *HwScsiInterrupt* routine so it can use the *HwScsiTimer* routine for efficient polling of its HBA.

-   [**HwScsiDmaStarted**](https://msdn.microsoft.com/library/windows/hardware/ff557291), which is required if the HBA uses a system DMA controller, to set up an HBA transfer after the system DMA controller has been programmed by the port driver

-   [**HwScsiAdapterState**](https://msdn.microsoft.com/library/windows/hardware/ff557278), which is optional if and only if the HBA has no BIOS or x86-real-mode driver and/or will never run in x86-only Microsoft Windows systems

-   [**HwScsiAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557274), which is required if the miniport driver supports Plug and Play

Each of the preceding miniport driver routines, except [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff552654), has a name chosen to describe its functionality. Except for **DriverEntry**, which is a required name for every miniport driver's initial entry point, names for miniport driver routines can be anything the driver writer chooses.

The following sections describe the requirements for and functionality of each of these miniport driver routines. See [SCSI Miniport Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff565312) for their formal definitions and for descriptions of their parameters.

[Error Handling in SCSI Miniport Drivers](error-handling-in-scsi-miniport-drivers.md) describes error-handling requirements for SCSI miniport drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Required%20and%20Optional%20SCSI%20Miniport%20Driver%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


