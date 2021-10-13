---
title: SCSI Miniport Driver's HwScsiResetBus Routine
description: SCSI Miniport Driver's HwScsiResetBus Routine
keywords:
- SCSI miniport drivers WDK storage , HwScsiResetBus
- HwScsiResetBus
- bus-reset operations WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiResetBus Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiresetbus_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIRESETBUS_ROUTINE_KG"></span>


Every miniport driver must have an [*HwScsiResetBus*](/previous-versions/windows/hardware/drivers/ff557318(v=vs.85)) routine, which is called with a pointer to the miniport driver's device extension for HBA state and the **PathId** of the bus to be reset. If an attempted bus-reset operation fails or times out, the miniport driver should call [**ScsiPortLogError**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportlogerror) and then program the HBA for a hard reset.

A bus-reset operation might require the miniport driver to clean up the state it maintains in the device extension and/or logical unit extensions for devices on the bus. *HwScsiResetBus* must complete any outstanding requests by calling [**ScsiPortCompleteRequest**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportcompleterequest) with the **SrbStatus** value SRB\_STATUS\_BUS\_RESET or, for individual SRBs, [**ScsiPortNotification**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportnotification) with this status value.

After completing the bus-reset request and any outstanding requests, the miniport driver must call **ScsiPortNotification** (if it has not already done so) with the *NotificationType***NextRequest**, or **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

Note that the operating system - specific port driver manages SCSI bus-reset delays on behalf of miniport drivers.

 

