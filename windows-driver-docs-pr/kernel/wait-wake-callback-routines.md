---
title: Wait/Wake Callback Routines
author: windows-driver-content
description: Wait/Wake Callback Routines
MS-HAID:
- 'PwrMgmt\_9b60b7e9-5ca1-4ba0-b44d-fc98ff2f2b76.xml'
- 'kernel.wait\_wake\_callback\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 55749f14-37eb-45d9-8a2c-9ebf7fb3bc75
keywords: ["sending wait/wake IRPs", "wait/wake IRPs WDK power management , sending", "callback routines WDK power management"]
---

# Wait/Wake Callback Routines


## <a href="" id="ddk-wait-wake-callback-routines-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Wait/Wake%20Callback%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


