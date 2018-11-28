---
title: IRP_MN_SET_POWER
description: This IRP notifies a driver of a change to the system power state or sets the device power state for a device.
ms.date: 08/12/2017
ms.assetid: 1294183a-bd0b-4ead-bd64-669d5b3725ce
keywords:
 - IRP_MN_SET_POWER Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_SET\_POWER


This IRP notifies a driver of a change to the system power state or sets the device power state for a device.

Major Code
----------

[**IRP\_MJ\_POWER**](irp-mj-power.md)
When Sent
---------

Either the system power manager or a device power policy owner can send this IRP.

The power manager sends this IRP to notify drivers of a change to the system power state. If a driver has registered its device for idle detection, the power manager sends this IRP to change the power state of an idle device.

A driver that owns power policy sends this IRP to set the device power state for its device. A driver must call [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to send this IRP.

The power manager sends this IRP at IRQL = PASSIVE\_LEVEL to device stacks that set the DO\_POWER\_PAGABLE flag in the PDO. Drivers in such stacks can touch paged code or data to complete the request.

The power manager can send the IRP at IRQL = DISPATCH\_LEVEL if the DO\_POWER\_INRUSH flag is set. Such drivers cannot directly or indirectly access any paged code or data.

## Input Parameters


The **Parameters.Power.Type** member specifies the type of power state being set, either **SystemPowerState** or **DevicePowerState**.

The **Parameters.Power.State** member specifies the power state itself, as follows:

-   If **Parameters.Power.Type** is **SystemPowerState**, the value is an enumerator of the [**SYSTEM\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff564565) type.

-   If **Parameters.Power.Type** is **DevicePowerState**, the value is an enumerator of the [**DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff543160) type.

The **Parameters.Power.ShutdownType** member specifies additional information about the requested transition. The possible values for this member are **POWER\_ACTION** enumeration values. For more information, see [System Power Actions](https://msdn.microsoft.com/library/windows/hardware/ff564553).

Starting with Windows Vista, the **Parameters.Power.SystemPowerStateContext** member is a read-only, partially opaque [**SYSTEM\_POWER\_STATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/jj835780) structure that contains information about the previous system power states of a computer. If **Parameters.Power.Type** is **SystemPowerState** and **Parameters.Power.State** is **PowerSystemWorking**, two flag bits in this structure indicate whether a fast startup or a wake-from-hibernation caused the computer to enter the S0 (working) system state. For more information, see [Distinguishing Fast Startup from Wake-from-Hibernation](https://msdn.microsoft.com/library/windows/hardware/jj835779).

## Output Parameters


**Parameters.Power.SystemContext** is reserved for system use.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS to indicate that the device has entered the requested state.

A driver must not fail a request to set the system power state.

Function and filter drivers that are located above a bus driver must not fail a request to set a device power state. The bus driver can fail a device power-up request if the device is removed or in the process of being removed.

Operation
---------

The power manager or a driver can request an **IRP\_MN\_SET\_POWER** IRP. The power manager sends this IRP for one of the following reasons:

-   To notify drivers of a change to the system power state

-   To change the power state of a device for which the power manager is performing idle detection

A driver that owns device power policy sends **IRP\_MN\_SET\_POWER** to change the power state of its device.

At any given time, the system allows only one such IRP to be active for each device object.

Each driver must pass each power IRP down to the next-lower driver by calling [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (starting with Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (Windows Server 2003, Windows XP, and Windows 2000). The **PoCallDriver** interface is similar to that of **IoCallDriver**, except that the power management subsystem might delay the IRP before passing it on to the next driver. For example, delays can occur on a **PowerDeviceD0** request if the device requires inrush current and therefore must be powered up serially with another such device.

After a driver receives an **IRP\_MN\_SET\_POWER** request on Windows Server 2003, Windows XP, or Windows 2000, a driver must call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), as described in [Calling PoStartNextPowerIrp](https://msdn.microsoft.com/library/windows/hardware/ff540724). Beginning with Windows Vista, calling **PoStartNextPowerIrp** is not required, and such a call performs no power management operation.

**IRP\_MN\_SET\_POWER for System Power States**

Only the system power manager can send a system set-power IRP.

A driver must not fail a request to set the system power state.

Whenever possible, the power manager sends [**IRP\_MN\_QUERY\_POWER**](irp-mn-query-power.md) before sending **IRP\_MN\_SET\_POWER** to request a system sleep state. However, under some conditions (such as the user pressing the **Power Off** button or a battery expiring), the power manager might issue **IRP\_MN\_SET\_POWER** without first querying. The power manager queries only for sleep states; it never queries before powering up.

The **IRP\_MN\_SET\_POWER** request is sent to the top driver in the device stack for a device. The top driver passes the IRP down to the next lower driver and so forth until the IRP reaches the bus driver, which must complete the IRP.

A filter driver typically does not need to act on a system set-power IRP, other than to pass it on.

The device power policy owner, however, sets an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine before passing down the IRP. In the *IoCompletion* routine, it sends an **IRP\_MN\_SET\_POWER** request for a device power IRP. For more information, see [Handling a System Set-Power IRP in a Device Power Policy Owner](https://msdn.microsoft.com/library/windows/hardware/ff546749).

A system set-power IRP informs drivers that a change to the system power state is imminent and the drivers must prepare for it. However, a driver should not change the power state of its device until it receives an **IRP\_MN\_SET\_POWER** for a *device* power state.

The value at **Parameters.Power.ShutdownType** provides additional information about the pending actions. When the IRP specifies **PowerSystemShutdown** (S5), a driver can determine whether the system is resetting (**PowerActionShutdownReset**) or powering off indefinitely to reboot later (**PowerActionShutdownOff**). For drivers of most devices, the difference is inconsequential. However, for certain devices, such as video streaming devices, a driver might power off the device in order to stop I/O when the system is resetting.

On Windows 2000 and later versions of the operating system, the value at **ShutdownType** can also be **PowerActionShutdown**. In this case, the driver cannot tell what type of shutdown is requested and should therefore proceed as for a reset.

**Device Power States**

Function and filter drivers that are located above a bus driver must not fail a request to set a device power state. The bus driver can fail a device power-up request if the device is removed or in the process of being removed.

A driver must set the device into the requested state before completing the IRP.

When the IRP requests a transition to a lower power state, drivers must handle the IRP as it travels down the device stack, saving any context the driver will need to restore the device to the working state. After a bus driver receives an IRP, the driver:

-   Saves any context the driver will need to restore the device to the working state.

-   Sets the device to the requested power state.

-   Calls [**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765) to notify the power manager.

-   Calls **PoStartNextPowerIrp** to start the next power IRP (Windows Server 2003, Windows XP, and Windows 2000 only).

-   Completes the device power IRP.

The driver must complete this IRP in a timely manner. In general, drivers should avoid any delay that a typical user would find noticeably slow. For example, a driver could delay a system state change to flush cached disk or network data, but should not keep a network connection alive or format a tape. For more information, see [Passing Power IRPs](https://msdn.microsoft.com/library/windows/hardware/ff558785).

On Windows 2000 and later versions of the operating system, if the IRP specifies **PowerDeviceD1**, **PowerDeviceD2**, or **PowerDeviceD3**, and a system set-power IRP is active, the value at **Parameters.Power.ShutdownType** provides information about the system IRP.

Drivers of devices on the hibernate path should inspect this value. If the IRP requests **PowerDeviceD3** and **ShutdownType** is **PowerActionHibernate**, such a driver should save any context required to restore the device, but should not power down the device; the device will enter the D3 state when the machine loses power.

On Windows 2000 and later versions of the operating system, drivers should not rely on the value at **ShutdownType** if the requested power state is **PowerDeviceD0**.

On Windows 98/Me, if the IRP requests a device power state, the **ShutdownType** is always **PowerActionNone**.

The driver that determines when to power down a device varies depending on the device class.

The driver that determines when to power up a device is almost always a driver that accesses the device registers. The driver must verify that the device is in the D0 state before accessing the device's hardware registers. If the device is not in the D0 state, the driver must call **PoRequestPowerIrp** to send an IRP to power up the device. A driver cannot access its device unless the device is in the D0 state.

When a driver receives a set-power IRP for device state D0, it sets an *IoCompletion* routine and passes the IRP to the next lower driver.

When the IRP reaches the bus driver, that driver applies (or resets) power to the device, calls **PoStartNextPowerIrp** (Windows Server 2003, Windows XP, and Windows 2000 only), and calls **PoSetPowerState** to inform the power manager of the new power state for the device.

After the bus driver completes the power-up IRP, function and filter drivers handle the IRP in their *IoCompletion* routines as it travels back up the device stack. In the *IoCompletion* routine, each driver restores or reinitializes its device context and performs any other required start-up tasks.

For more information, see [Handling IRP\_MN\_SET\_POWER for Device Power States](https://msdn.microsoft.com/library/windows/hardware/ff546885).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</td>
</tr>
</tbody>
</table>

## See also


[**DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff543160)

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)

[**IRP\_MN\_QUERY\_POWER**](irp-mn-query-power.md)

[**IRP\_MN\_SET\_POWER**](irp-mn-set-power.md)

[**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654)

[**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776)

[**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765)

[**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)

[**SYSTEM\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff564565)

[**SYSTEM\_POWER\_STATE\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/jj835780)

 

 




