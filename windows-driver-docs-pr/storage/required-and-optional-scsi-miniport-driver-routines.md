---
title: Required and Optional SCSI Miniport Driver Routines
description: Required and Optional SCSI Miniport Driver Routines
ms.assetid: 6fd1f7af-e8ba-4679-bd8c-f757b57821b0
keywords:
- SCSI miniport drivers WDK storage , required routines
- SCSI miniport drivers WDK storage , optional routines
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




