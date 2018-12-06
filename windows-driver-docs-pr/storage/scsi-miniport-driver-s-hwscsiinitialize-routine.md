---
title: SCSI Miniport Driver's HwScsiInitialize Routine
description: SCSI Miniport Driver's HwScsiInitialize Routine
ms.assetid: 2a776c0a-1bac-4f8c-beab-fd53300f68c8
keywords:
- SCSI miniport drivers WDK storage , HwScsiInitialize
- HwScsiInitialize
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiInitialize Routine


## <span id="ddk_scsi_miniport_drivers_hwscsiinitialize_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIINITIALIZE_ROUTINE_KG"></span>


For each supported HBA found by the miniport driver, its [*HwScsiInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff557302) routine is called to set up the HBA's registers and initial state, if any.

If the *HwScsiInitialize* routine enables interrupts on the HBA, the miniport driver's [**HwScsiInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff557312) routine will be called to handle any interrupts the device generates during the initialization.

If initializing the HBA causes a bus reset, the *HwScsiInitialize* routine must call [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657) with the *NotificationType* value **ResetDetected**.

 

 




