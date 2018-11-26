---
title: Wait/Wake Callback Routines
description: Wait/Wake Callback Routines
ms.assetid: 55749f14-37eb-45d9-8a2c-9ebf7fb3bc75
keywords: ["sending wait/wake IRPs", "wait/wake IRPs WDK power management , sending", "callback routines WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Wait/Wake Callback Routines





When a driver requests a wait/wake IRP, it must specify a callback routine so that it can return the device to the working state (D0) when the wake-up event occurs. After the wake-up event occurs and all drivers have completed the IRP, the system calls the callback routine passed to [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734).

Because this callback routine is set on behalf of the driver that originated the IRP—and not for a driver that is handling the IRP—it must not call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776); only the [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines set as drivers pass the IRP down the stack should start the next power IRP. Keep in mind that the policy owner not only sends the IRP but handles it, and it therefore might set an *IoCompletion* routine as it passes the IRP down the stack in addition to setting a callback routine when it requests the wait/wake IRP.

The callback routine has the following responsibilities:

1.  If the driver controls more than one device, determine which of its devices signaled the wake-up.

2.  Service the event that caused the wake-up signal.

3.  Set the device that signaled the wake-up in the D0 state by calling [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to send a **PowerDeviceD0** request. The driver must also call [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to inform the power manager of the new device power state. For more information, see [Sending IRP\_MN\_QUERY\_POWER or IRP\_MN\_SET\_POWER for Device Power States](sending-irp-mn-query-power-or-irp-mn-set-power-for-device-power-states.md).

4.  If the driver set a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine for the IRP, call [**IoSetCancelRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549674) to reset the *Cancel* routine to **NULL**.

5.  If the driver owns power policy for more than one device, decrement its wait/wake reference count. If the count is nonzero, indicating that another device had previously sent a wait/wake IRP, request another wait/wake IRP (**PoRequestPowerIrp**) for its PDO.

    For example, a PCI device might have wait/wake enabled for both a modem and a Network Interface Card (NIC). If the NIC wakes the system (thus completing the IRP), the PCI FDO must send another wait/wake IRP to itself so that the modem will still be able to wake up.

Because the driver that requested the wait/wake IRP controls power policy for its device stack, it is responsible for returning its device to the working state when the IRP completes. Although lower drivers might already have physically applied power to the device, the policy owner must call **PoRequestPowerIrp** to send an **IRP\_MN\_SET\_POWER** request for device power state D0. Only after all drivers in the device stack have handled this power-up IRP will the device be returned to the working state.

 

 




