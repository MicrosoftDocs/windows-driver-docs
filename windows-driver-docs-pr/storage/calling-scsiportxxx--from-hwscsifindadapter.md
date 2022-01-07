---
title: Calling ScsiPortXxx from HwScsiFindAdapter
description: Calling ScsiPortXxx from HwScsiFindAdapter
keywords:
- HwScsiFindAdapter
- SCSI miniport drivers WDK storage , HwScsiFindAdapter
- calling ScsiPortXxx routines WDK storage
- ScsiPortXxx calls
ms.date: 10/08/2019
---

# Calling ScsiPortXxx from HwScsiFindAdapter

Certain **ScsiPort**_Xxx_ routines can be called *only* from the miniport driver's *HwScsiFindAdapter* routine(s), in particular, the following:

- [**ScsiPortValidateRange**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportvalidaterange) to verify that a miniport driver-supplied, bus-relative access range has not already been claimed in the registry by another driver for its device.

- [**ScsiPortGetDeviceBase**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetdevicebase) to map the (bus-relative) "physical" address range for an HBA to a system-assigned logical address range that the driver can use to communicate with the HBA by calling the **ScsiPortRead**_Xxx_ and **ScsiPortWrite**_Xxx_ routines with the mapped logical range addresses.

- [**ScsiPortFreeDeviceBase**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportfreedevicebase) to release such a mapped range if *HwScsiFindAdapter* does not find an HBA it can support on a given I/O bus, as indicated by the PORT\_CONFIGURATION\_INFORMATION **SystemIoBusNumber** value.

- [**ScsiPortGetUncachedExtension**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetuncachedextension) to allocate a DMA buffer shared between the system and a bus-master HBA.

In addition to these four routines, there is one routine that can only be called from the miniport driver's *HwScsiFindAdapter* routine, *or* from *HwScsiAdapterControl* when the control type is **ScsiSetRunningConfig**:

- [**ScsiPortGetBusData**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportgetbusdata) to get BUS_DATA_TYPE-specific configuration information, such as bus-relative device memory (access) ranges, interrupt vector or IRQL, and DMA channel or port.

For more information about these **ScsiPort**_Xxx_ routines, see [SCSI Port Driver Support Routines](scsi-port-driver-support-routines.md).
