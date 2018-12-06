---
title: Power IRPs for the System
description: Power IRPs for the System
ms.assetid: a37e8dda-af7a-4f28-bf04-908a74bb5b2f
keywords: ["power IRPs WDK kernel , system", "system power IRPs WDK kernel", "IRP_MJ_POWER", "IRP_MN_SET_POWER", "IRP_MN_QUERY_POWER", "inrush power WDK kernel", "system inrush power WDK kernel", "change power states WDK kernel", "reaffirming power states", "idle time-outs WDK power management", "expired batteries WDK power management", "battery expirations WDK power management", "user-requested power changes WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Power IRPs for the System





A *system power IRP* specifies major IRP code [**IRP\_MJ\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff550784), one of the minor power IRP codes listed below, and the value **SystemPowerState** in the **Power.Type** member of the IRP stack. Only the power manager can send such an IRP; a driver cannot send a system power IRP.

The power manager sends a system power IRP for one of the following reasons:

-   To change the system power state in response to an idle time-out, a change in system activity, a user request, or an expiring battery ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744))

-   To query devices to determine whether the system can go to sleep ([**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699))

-   To reaffirm the current system power state after a query (**IRP\_MN\_SET\_POWER**)

The power manager sends **IRP\_MN\_QUERY\_POWER** and **IRP\_MN\_SET\_POWER** requests on behalf of the system. A driver can fail an **IRP\_MN\_QUERY\_POWER** request but cannot fail **IRP\_MN\_SET\_POWER**.

For example, to change the system power state, the power manager sends a system power IRP to the top driver in the stack at each device node of the device tree. The following figure shows how drivers within a single device stack handle a system power IRP.

![diagram illustrating the path of a system power irp](images/s2dirp.png)

As the previous figure shows:

1.  The power manager calls the I/O manager to send a system power IRP to each leaf node in the device tree.

2.  Drivers handle the IRP if possible, set [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines if necessary, and call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (Windows 7 and Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (Windows Server 2003, Windows XP, and Windows 2000) to forward the IRP down the stack. If a driver must fail the IRP, the driver does so immediately and completes the IRP. Drivers can fail **IRP\_MN\_QUERY\_POWER** IRPs, but must not fail **IRP\_MN\_SET\_POWER** IRPs that set the system power state.

3.  When the driver that owns power policy for the device receives the IRP, that driver sets an *IoCompletion* routine for the system IRP and then forwards the IRP.

4.  Any other drivers in the stack handle the IRP if possible, set *IoCompletion* routines if necessary, and forward the IRP to the next-lower driver, as in step 2.

5.  Eventually, the bus driver receives and completes the system IRP.

6.  The I/O manager calls any *IoCompletion* routines that were set as drivers passed the system IRP down the device stack.

7.  In its *IoCompletion* routine, the device power policy owner calls [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to send a device power IRP, specifying a device power state that is valid for the system power state in the system IRP. The driver sets a callback routine to be invoked when the device power IRP completes.

    If necessary, the driver consults the **DeviceState** member in its cached copy of the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure (see [Reporting Device Power Capabilities](reporting-device-power-capabilities.md)) to determine which device power states correspond to the system power state in the IRP.

8.  After the device IRP is complete and any device IRP completion routines have run, the power policy owner's callback routine is invoked. In the callback routine, the driver copies its returned status into the system IRP. In Windows Server 2003, Windows XP, and Windows 2000, the callback calls [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to start the next power IRP. However, in Windows 7 and Windows Vista, calling **PoStartNextPowerIrp** is not required and such a call performs no power management operation. Finally, the callback calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the system IRP.

For further information, see [Handling System Power State Requests](handling-system-power-state-requests.md).

Because some devices require an inrush of current when they power on, system inrush power IRPs are handled synchronously and serially throughout the system. Only one such IRP can be active at a time. For further information, see [Calling IoCallDriver vs. Calling PoCallDriver](calling-iocalldriver-versus-calling-pocalldriver.md).

 

 




