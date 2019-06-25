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

Every SCSI miniport driver must have at least the following system-defined routines:

- [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index) to initialize the miniport driver

- [*HwScsiFindAdapter*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557300(v=vs.85)) to determine how (or whether) driver-supported HBA(s) are configured in the machine

- [*HwScsiInitialize*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557302(v=vs.85)) to initialize supported HBA(s)

- [**HwScsiStartIo**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557323(v=vs.85)) to start operations on its HBA(s) for incoming requests

- [*HwScsiResetBus*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557318(v=vs.85)) to handle bus reset requests

Depending on each HBA and the driver designer, SCSI miniport drivers also have some or all of the following system-defined routines:

- [**HwScsiInterrupt**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557312(v=vs.85))to handle HBA-generated interrupts, which is optional if and only if the HBA does not generate interrupts so the miniport driver manages all I/O operations on its HBA by polling. However, using polling exclusively has an adverse effect on a miniport driver's performance and on its HBA's I/O throughput. Such a miniport driver should also have an [*HwScsiTimer*](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557327(v=vs.85)) routine.

- [**HwScsiDisableInterruptsCallback**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557288(v=vs.85)) and [**HwScsiEnableInterruptsCallback**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557295(v=vs.85)) to handle deferred I/O processing if interrupt-driven I/O operations take a long time

- *HwScsiTimer* to time operations that require long delays on the HBA, or for any other purpose determined by the driver designer. A miniport driver should have a *HwScsiTimer* routine if it has no *HwScsiInterrupt* routine so it can use the *HwScsiTimer* routine for efficient polling of its HBA.

- [**HwScsiDmaStarted**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557291(v=vs.85)), which is required if the HBA uses a system DMA controller, to set up an HBA transfer after the system DMA controller has been programmed by the port driver

- [**HwScsiAdapterState**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557278(v=vs.85)), which is optional if and only if the HBA has no BIOS or x86-real-mode driver and/or will never run in x86-only Microsoft Windows systems

- [**HwScsiAdapterControl**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff557274(v=vs.85)), which is required if the miniport driver supports Plug and Play

Each of the preceding miniport driver routines, except [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index), has a name chosen to describe its functionality. Except for **DriverEntry**, which is a required name for every miniport driver's initial entry point, names for miniport driver routines can be anything the driver writer chooses.

The following sections describe the requirements for and functionality of each of these miniport driver routines.

[Error Handling in SCSI Miniport Drivers](error-handling-in-scsi-miniport-drivers.md) describes error-handling requirements for SCSI miniport drivers.

## See also

[HwScsiWmiExecuteMethod](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/scsiwmi/nc-scsiwmi-pscsiwmi_execute_method)

[HwScsiWmiFunctionControl](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/scsiwmi/nc-scsiwmi-pscsiwmi_function_control)

[HwScsiWmiQueryDataBlock](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock)

[HwScsiWmiQueryReginfo](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/scsiwmi/nc-scsiwmi-pscsiwmi_query_reginfo)

[HwScsiWmiSetDataBlock](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/scsiwmi/nc-scsiwmi-pscsiwmi_set_datablock)

[HwScsiWmiSetDataItem](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/scsiwmi/nc-scsiwmi-pscsiwmi_set_dataitem)