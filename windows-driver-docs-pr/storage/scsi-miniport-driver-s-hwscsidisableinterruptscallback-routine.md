---
title: SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine
description: SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine
keywords:
- SCSI miniport drivers WDK storage , HwScsiDisableInterruptsCallback
- HwScsiDisableInterruptsCallback
- interrupts WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine


## <span id="ddk_scsi_miniport_drivers_hwscsidisableinterruptscallback_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIDISABLEINTERRUPTSCALLBACK_ROUTINE_KG"></span>


An [**HwScsiDisableInterruptsCallback**](/previous-versions/windows/hardware/drivers/ff557288(v=vs.85)) routine should do the following:

-   Reenable interrupts from the HBA

-   Return control

Note that this routine must execute as quickly as possible to avoid using I/O operations for other devices in the machine. Consequently, an *HwScsiDisableInterruptsCallback* must do no more than reenable interrupts on the HBA before it returns control.

 

