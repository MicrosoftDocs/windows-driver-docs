---
title: SCSI Miniport Driver's HwScsiInitialize Routine
description: SCSI Miniport Driver's HwScsiInitialize Routine
keywords:
- SCSI miniport drivers WDK storage , HwScsiInitialize
- HwScsiInitialize
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiInitialize Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiinitialize_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIINITIALIZE_ROUTINE_KG"></span>


For each supported HBA found by the miniport driver, its [*HwScsiInitialize*](/previous-versions/windows/hardware/drivers/ff557302(v=vs.85)) routine is called to set up the HBA's registers and initial state, if any.

If the *HwScsiInitialize* routine enables interrupts on the HBA, the miniport driver's [**HwScsiInterrupt**](/previous-versions/windows/hardware/drivers/ff557312(v=vs.85)) routine will be called to handle any interrupts the device generates during the initialization.

If initializing the HBA causes a bus reset, the *HwScsiInitialize* routine must call [**ScsiPortNotification**](/windows-hardware/drivers/ddi/srb/nf-srb-scsiportnotification) with the *NotificationType* value **ResetDetected**.

 

