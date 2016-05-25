---
title: SCSI Miniport Driver's HwScsiEnableInterruptsCallback Routine
author: windows-driver-content
description: SCSI Miniport Driver's HwScsiEnableInterruptsCallback Routine
ms.assetid: 8519924f-ad69-46e7-8b24-bf36523f30c9
keywords: ["SCSI miniport drivers WDK storage , HwScsiEnableInterruptsCallback", "HwScsiEnableInterruptsCallback", "interrupts WDK SCSI"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Miniport%20Driver's%20HwScsiEnableInterruptsCallback%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


