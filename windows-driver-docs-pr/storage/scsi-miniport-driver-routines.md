---
title: Required and Optional SCSI Miniport Driver Routines
description: Required and Optional SCSI Miniport Driver Routines
keywords:
- SCSI miniport drivers WDK storage , required routines
- SCSI miniport drivers WDK storage , optional routines
ms.date: 10/08/2019
---

# Required and Optional SCSI Miniport Driver Routines

A miniport driver's *HwScsiXxx* routines can have any name chosen by the driver writer. **DriverEntry** is a required name.

Every SCSI miniport driver must have at least the following system-defined routines:

| Required Routine | Description |
| ---------------- | ----------- |
| [**DriverEntry**](driverentry-of-scsi-miniport-driver.md) | Initializes the miniport driver |
| [*HwScsiFindAdapter*](scsi-miniport-driver-s-hwscsifindadapter-routine.md) | Determines how (or whether) driver-supported host bus adapter(s) (HBAs) are configured in the machine |
| [*HwScsiInitialize*](scsi-miniport-driver-s-hwscsiinitialize-routine.md) | Initializes supported HBA(s) |
| [*HwScsiStartIo*](scsi-miniport-driver-s-hwscsistartio-routine.md) | Starts operations on the miniport's HBA(s) for incoming requests |
| [*HwScsiResetBus*](scsi-miniport-driver-s-hwscsiresetbus-routine.md) | Handles bus reset requests |

Depending on each HBA and the driver designer, SCSI miniport drivers also have some or all of the following system-defined routines:

|  Routine | Description |
| -------- | ----------- |
| [*HwScsiInterrupt*](scsi-miniport-driver-s-hwscsiinterrupt-routine.md) | Handles HBA-generated interrupts, which is optional if and only if the HBA does not generate interrupts so the miniport driver manages all I/O operations on its HBA by polling. However, using polling exclusively has an adverse effect on a miniport driver's performance and on its HBA's I/O throughput. Such a miniport driver should also have an [*HwScsiTimer*](scsi-miniport-driver-s-hwscsitimer-routine.md) routine. |
| [*HwScsiDisableInterruptsCallback*](scsi-miniport-driver-s-hwscsidisableinterruptscallback-routine.md) and [*HwScsiEnableInterruptsCallback*](scsi-miniport-driver-s-hwscsienableinterruptscallback-routine.md) | Handle deferred I/O processing if interrupt-driven I/O operations take a long time. |
| [*HwScsiTimer*](scsi-miniport-driver-s-hwscsitimer-routine.md) | Times operations that require long delays on the HBA, or for any other purpose determined by the driver designer. A miniport driver should have a *HwScsiTimer* routine if it has no *HwScsiInterrupt* routine so it can use the *HwScsiTimer* routine for efficient polling of its HBA. |
| [*HwScsiDmaStarted*](scsi-miniport-driver-s-hwscsidmastarted-routine.md) | Required if the HBA uses a system DMA controller, to set up an HBA transfer after the system DMA controller has been programmed by the port driver. |
| [*HwScsiAdapterState*](scsi-miniport-driver-s-hwscsiadapterstate-routine.md) | Optional if and only if the HBA has no BIOS or x86-real-mode driver and/or will never run in x86-only Microsoft Windows systems. |
| [*HwScsiAdapterControl*](scsi-miniport-driver-s-hwscsiadaptercontrol-routine.md) | Required if the miniport driver supports Plug and Play. |
| [HwScsiWmiExecuteMethod](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_execute_method) | Executes a method associated with a data block. This routine is optional. |
| [HwScsiWmiFunctionControl](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_function_control) | Enables or disables notification of events, and also enables or disables data collection for data blocks that the miniport driver designated as expensive to collect. Optional. |
| [HwScsiWmiQueryDataBlock](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_datablock) | Obtains either a single instance or all instances of a data block. Required. |
| [HwScsiWmiQueryReginfo](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_query_reginfo) | Obtains information about the data and event blocks to be registered on behalf of the miniport driver by the SCSI port driver. Required. |
| [HwScsiWmiSetDataBlock](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_set_datablock) | Changes all data items in a single instance of a data block. Optional. |
| [HwScsiWmiSetDataItem](/windows-hardware/drivers/ddi/scsiwmi/nc-scsiwmi-pscsiwmi_set_dataitem) | Changes a single data item in an instance of a data block. Optional. |

Each of the preceding miniport driver routines, except [**DriverEntry**](driverentry-of-scsi-miniport-driver.md), has a name chosen to describe its functionality. Except for **DriverEntry**, which is a required name for every miniport driver's initial entry point, names for miniport driver routines can be anything the driver writer chooses.

[Error Handling in SCSI Miniport Drivers](error-handling-in-scsi-miniport-drivers.md) describes error-handling requirements for SCSI miniport drivers.
