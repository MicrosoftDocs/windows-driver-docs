---
title: SCSI Miniport Driver's HwScsiEnableInterruptsCallback Routine
description: SCSI Miniport Driver's HwScsiEnableInterruptsCallback Routine
ms.assetid: 8519924f-ad69-46e7-8b24-bf36523f30c9
keywords:
- SCSI miniport drivers WDK storage , HwScsiEnableInterruptsCallback
- HwScsiEnableInterruptsCallback
- interrupts WDK SCSI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Miniport Driver's HwScsiEnableInterruptsCallback Routine


## <span id="ddk_scsi_miniport_drivers_hwscsienableinterruptscallback_routine_kg"></span><span id="DDK_SCSI_MINIPORT_DRIVERS_HWSCSIENABLEINTERRUPTSCALLBACK_ROUTINE_KG"></span>


An [**HwScsiEnableInterruptsCallback**](https://msdn.microsoft.com/library/windows/hardware/ff557295) routine finishes processing an interrupt-driven I/O operation without inhibiting I/O operations for other devices in the machine.

When the *HwScsiEnableInterruptsCallback* routine gets control, all system device interrupts are enabled except from the HBA because the *HwScsiInterrupt* routine disabled interrupts on the HBA before it called [**ScsiPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff564657). Thus, the miniport driver's *HwScsiInterrupt* routine cannot be called and cannot disturb the context data it set up about the current operation while the *HwScsiEnableInterruptsCallback* routine is running.

A *HwScsiEnableInterruptsCallback* routine should do the following:

1.  Use the context that was set up for the operation in the input device extension to complete processing of the request that caused the interrupt.

2.  Call **ScsiPortNotification** with the *NotificationType***RequestComplete** and the just-satisfied SRB.

3.  Call **ScsiPortNotification** with the *NotificationType***NextRequest**, or with **NextLuRequest** if the HBA supports tagged queuing or multiple requests per logical unit.

4.  Call **ScsiPortNotification** with a pointer to the device extension, the *NotificationType***CallDisableInterrupts**, and the miniport driver's *HwScsiDisableInterruptsCallback* routine, described in [SCSI Miniport Driver's HwScsiDisableInterruptsCallback Routine](scsi-miniport-driver-s-hwscsidisableinterruptscallback-routine.md).

5.  Return control.

The NT-based operating system **ScsiPortNotification** routine calls the *HwScsiDisableInterruptsCallback* routine with a subset of the system device interrupts disabled. No device interrupt with a system-assigned hardware priority (IRQL) less than or equal to the HBA's can occur.

See [IRQL](https://msdn.microsoft.com/library/windows/hardware/ff551779) for more information.

 

 




