---
title: Handling Device Power-Up IRPs
description: Handling Device Power-Up IRPs
ms.assetid: 8fcfd324-97f9-4fd0-8fa1-87685c6b5ec3
keywords: ["set-power IRPs WDK kernel", "device set power IRPs WDK kernel", "power IRPs WDK kernel , device changes", "power-up IRPs WDK kernel", "startup power management WDK kernel", "restoring power WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling Device Power-Up IRPs





Device power-up IRPs specify [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) and a device power state that requires more power than the current device power state. Typically, a power-up IRP specifies the device working state **PowerDeviceD0**.

Requests to power up a device must be handled first by the underlying bus driver for the device, and then by each successive driver going back up the stack.

The following figure shows the steps involved in handling a power-up IRP.

![diagram illustrating handling a device power-up request](images/devd0.png)

When handling an **IRP\_MN\_SET\_POWER** request for power-up, a function or filter driver must:

-   Call [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204) to ensure that the driver does not receive an [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request while handling the power-up IRP.

    If **IoAcquireRemoveLock** returns a failure status, the driver should not continue processing the IRP. Instead, beginning with Windows Vista, the driver should call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP and then return the failure status. In Windows Server 2003, Windows XP, and Windows 2000, the driver should call **IoCompleteRequest** to complete the IRP, then call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to start the next power IRP, and then return the failure status.

-   Call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) to mark the IRP pending.

-   Call [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387) to set the IRP stack location. A driver must not call **IoSkipCurrentIrpStackLocation** if it sets an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine.

-   Call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) to set a power-up *IoCompletion* routine.

    When handling a device power-up IRP, the driver should set an *IoCompletion* routine to restore context, release the remove lock, and perform other required tasks after the IRP is complete and the device powers on. The driver should not restore context before the IRP has completed. For more information, see [IoCompletion Routines for Device Power IRPs](iocompletion-routines-for-device-power-irps.md).

-   Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (in Windows 7 and Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (Windows Server 2003, Windows XP, and Windows 2000) to pass the IRP to the next-lower driver. The IRP must travel all the way down the device stack to the bus driver. Only the bus driver is allowed to complete the IRP.

-   Return STATUS\_PENDING.

When the bus driver receives the IRP, it should first check to ensure the device is still present and has not been removed or replaced while asleep. If the device is no longer present, the bus driver should call [**IoInvalidateDeviceRelations**](https://msdn.microsoft.com/library/windows/hardware/ff549353) on the parent device to notify the Plug and Play manager that the device has disappeared. In this situation, the bus driver can fail the device power-up IRP.

If the device is still present, the bus driver then performs the tasks required to return the device to an operating condition, calls [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to inform the power manager of the new device power state, and completes the IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)). If drivers have queued I/O while the device was sleeping, or if the device requires inrush power, the bus driver applies power to the device. Otherwise, the bus driver applies power as soon as it has to communicate with the device.

For a list of best practices to achieve fast startup times from power-off, standby, and hibernation states, see [Improving System Startup Performance](improving-system-startup-performance.md).

 

 




