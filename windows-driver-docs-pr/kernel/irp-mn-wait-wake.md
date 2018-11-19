---
title: IRP_MN_WAIT_WAKE
description: This IRP enables a driver to awaken a sleeping system or to awaken a sleeping device.
ms.date: 08/12/2017
ms.assetid: b79fd057-bf95-457e-882a-42221789e6e6
keywords:
 - IRP_MN_WAIT_WAKE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_WAIT\_WAKE


This IRP enables a driver to awaken a sleeping system or to awaken a sleeping device.

Major Code
----------

[**IRP\_MJ\_POWER**](irp-mj-power.md)
When Sent
---------

A driver that owns power policy targets this IRP to its PDO to enable its device to awaken in response to an external event, such as an incoming phone call. A driver must call [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to send this IRP.

As a general rule, a driver should send this IRP as soon as it determines that its device should be enabled for wake-up. Consequently, drivers for most such devices send this IRP after powering on their devices and before completing the [**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md) request.

However, a driver can send the IRP any time the device is in the working state (**PowerDeviceD0**). The device stack must not be in transition; that is, a driver should not send an **IRP\_MN\_WAIT\_WAKE** while any other power IRP is active in its device stack.

A wait/wake IRP does not change the power state of the device or of the system. It simply enables a wake-up signal from the device. When the wake-up signal arrives, the policy owner must call **PoRequestPowerIrp** to send a set-power IRP to return its device to D0.

The driver must be running at IRQL = PASSIVE\_LEVEL to send this IRP. However, the IRP can be completed at IRQL = DISPATCH\_LEVEL.

## Input Parameters


<a href="" id="parameters-waitwake-powerstate-contains-the-lowest--least-powered--system-power-state-from-which-the-device-should-be-allowed-to-awaken-the-system-"></a>**Parameters.WaitWake.PowerState** contains the lowest (least-powered) system power state from which the device should be allowed to awaken the system.  

## Output Parameters


None.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to one of the following:

<a href="" id="status-pending-"></a>STATUS\_PENDING   
The driver received the IRP and is waiting for the device to signal wake-up.

<a href="" id="status-invalid-device-state-"></a>STATUS\_INVALID\_DEVICE\_STATE   
The device is in a less-powered state than the **DeviceWake** state specified in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure for the device, or the device cannot awaken the system from the **SystemWake** state passed in the IRP.

<a href="" id="status-not-supported-"></a>STATUS\_NOT\_SUPPORTED   
The device does not support wake-up.

<a href="" id="status-device-busy-"></a>STATUS\_DEVICE\_BUSY   
An **IRP\_MN\_WAIT\_WAKE** request is already pending and must be completed or canceled before another IRP\_MN\_WAIT\_WAKE request can be issued.

<a href="" id="status-success"></a>STATUS\_SUCCESS  
The device has signaled a wake event.

<a href="" id="status-cancelled"></a>STATUS\_CANCELLED  
The IRP has been canceled.

If a driver must fail this IRP, it completes the IRP immediately and does not pass the IRP to the next-lower driver.

Operation
---------

A driver sends **IRP\_MN\_WAIT\_WAKE** for either of two reasons:

1.  To enable its device to awaken a sleeping system in response to an external wake-up signal.

2.  To enable its device to awaken from a device sleep state in response to an external wake-up signal.

The IRP must be passed down the device stack to the bus driver for the device, which calls [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) and returns STATUS\_PENDING from its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine. The IRP remains pending until a wake-up signal occurs or until the driver that sent the IRP cancels it.

Only one wait/wake IRP can be held pending for a PDO at any given time. If a driver already holds a wait/wake IRP for a PDO, it must fail any additional such IRPs with STATUS\_DEVICE\_BUSY. A driver that enumerates more than one child PDO can have a wait/wake IRP pending for each such PDO.

Each driver sets an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine as the IRP travels down the device stack. When the device signals a wake-up event, the bus driver services the wake-up signal and completes the IRP, returning STATUS\_SUCCESS. The I/O manager then calls the *IoCompletion* routine of the next higher driver, and so on up the device stack.

When a driver sends a wait/wake IRP, it should specify a callback routine in the **PoRequestPowerIrp** call. In the callback routine, the driver typically services the device. For example, the power policy owner for the device must call **PoRequestPowerIrp** to send an [**IRP\_MN\_SET\_POWER**](irp-mn-set-power.md) for device state D0.

A driver that acts as the bus driver for one device and the policy owner for a parent device requests an **IRP\_MN\_WAIT\_WAKE** IRP for the parent's device stack when it receives a **IRP\_MN\_WAIT\_WAKE** request from a child PDO. If the driver enumerates more than one child PDO, it should request only one wait/wake IRP for the parent's device stack no matter how many child PDOs send wait/wake requests. Instead, such a driver should keep an internal count of wait/wake IRPs, incrementing the count each time it receives a request and decrementing the count each time it completes a request. If the count is nonzero after it has completed a wait/wake IRP, the driver should send another wait/wake IRP to its device stack to "rearm" itself for wake-up. For more information, see [Understanding the Path of Wait/Wake IRPs through a Device Tree](https://msdn.microsoft.com/library/windows/hardware/ff564867).

To cancel an **IRP\_MN\_WAIT\_WAKE**, a driver calls [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338). Only the driver that originated the IRP can cancel it. A driver cancels a pending **IRP\_MN\_WAIT\_WAKE** when any of the following occurs:

-   The driver receives a PnP IRP that stops or removes the device.

-   The system is going to sleep and the device wake signal must not awaken it.

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


[**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)

 

 




