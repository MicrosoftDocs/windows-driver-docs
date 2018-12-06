---
title: IRP_MN_QUERY_POWER
description: This IRP queries a device to determine whether the system power state or the device power state can be changed.
ms.date: 08/12/2017
ms.assetid: fc4c5364-2160-4525-889a-96785a3c7a07
keywords:
 - IRP_MN_QUERY_POWER Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_POWER


This IRP queries a device to determine whether the system power state or the device power state can be changed.

Major Code
----------

[**IRP\_MJ\_POWER**](irp-mj-power.md)
When Sent
---------

The power manager or a device power policy owner sends this IRP to determine whether it can change the system or device power state, typically to go to sleep. A driver must call [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to allocate and send this IRP.

The power manager sends this IRP at IRQL = PASSIVE\_LEVEL to device stacks that set the DO\_POWER\_PAGABLE flag in the PDO.

The power manager can send the IRP at IRQL = DISPATCH\_LEVEL if the DO\_POWER\_INRUSH flag is set. Such drivers cannot directly or indirectly access any paged code or data.

## Input Parameters


**Parameters.Power.Type** specifies the type of power state being set, either **SystemPowerState** or **DevicePowerState**.

**Parameters.Power.State** specifies the power state itself, as follows:

-   If **Parameters.Power.Type** is **SystemPowerState**, the value is an enumerator of the [**SYSTEM\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff564565) type.

-   If **Parameters.Power.Type** is **DevicePowerState**, the value is an enumerator of the [**DEVICE\_POWER\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff543160) type.

**Parameters.Power.ShutdownType** specifies additional information about the requested transition. Possible values are enumerators of the **POWER\_ACTION** type.

## Output Parameters


None.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS to indicate that the device can enter the requested state. A driver sets any appropriate failure status to indicate that it cannot enter the requested state.

Operation
---------

The parameters for **IRP\_MN\_QUERY\_POWER** are identical to those for [**IRP\_MN\_SET\_POWER**](irp-mn-set-power.md). Rather than notifying drivers of an irrevocable change to the power state, however, **IRP\_MN\_QUERY\_POWER** queries whether the system or a device can enter a particular power state.

A driver must not change the power state of its device in response to an **IRP\_MN\_QUERY\_POWER** request.

After a driver receives an **IRP\_MN\_QUERY\_POWER** request on Windows Server 2003, Windows XP, and Windows 2000, a driver must call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), as described in [Calling **PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff540724). Beginning with Windows Vista, calling **PoStartNextPowerIrp** is not required and such a call performs no power management operation.

**IRP\_MN\_QUERY\_POWER for a System Power State**

The power manager sends this IRP to ensure that it can change the system power state without disrupting work, such as dropping network connections.

Whenever possible, the power manager queries before sending **IRP\_MN\_SET\_POWER** to request a system sleep state or a normal system shutdown. However, under some critical conditions (such as the user pressing the **Power Off** button or a battery expiring), the power manager might send an **IRP\_MN\_SET\_POWER** request without first sending a query power request. The power manager queries only for sleep states; it never queries before returning to the working state.

When a driver receives a system power query IRP, it should fail the IRP if it cannot support any of the device states that are valid for the queried system state. For more information, see [**DeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff543087). Otherwise, the driver should pass the IRP to the next lower driver. The bus driver completes the IRP.

Beginning with Windows Vista, transition to a system sleep state is considered a critical operation. Although a driver might fail a system query-power IRP, the power manager might still change the system power state to a sleep state. After a driver receives a system query-power IRP, the driver should always be prepared for a subsequent change in the system power state.

When a device power policy owner receives a system power query IRP, it should set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine in the IRP before passing it down. In the *IoCompletion* routine, it should send an **IRP\_MN\_QUERY\_POWER** for a device state that is valid for the queried system state. For more information, see [Handling a System Query-Power IRP in a Device Power Policy Owner](https://msdn.microsoft.com/library/windows/hardware/ff546725).

When the IRP specifies **PowerSystemShutdown** (S5), the value at **Parameters.Power.ShutdownType** provides a reason for the shutdown. The **ShutdownType** tells the driver whether the system is resetting (**PowerActionShutdownReset**) or powering off indefinitely to reboot later (**PowerActionShutdownOff**). For drivers of most devices, the difference is inconsequential. However, for certain devices, such as a video streaming device that performs DMA, a driver might opt to power down its device when the system is resetting, thus stopping any ongoing I/O.

On Microsoft Windows 2000 and later systems, the value at **ShutdownType** can also be **PowerActionShutdown**. In this case, the driver cannot tell what type of shutdown is requested and should therefore proceed as for a reset.

If a driver fails an **IRP\_MN\_QUERY\_POWER** request for a system power state, the power manager typically responds by issuing an **IRP\_MN\_SET\_POWER** IRP. Usually, this IRP will reaffirm the current system state. However, it is possible that drivers might receive an **IRP\_MN\_SET\_POWER** to the queried state or to some other intermediate state. Drivers should be prepared to handle these situations.

**IRP\_MN\_QUERY\_POWER for a Device Power State**

A device power policy owner sends this IRP to its stack in response to a system **IRP\_MN\_QUERY\_POWER** request.

If a driver can put its device in the requested device state, it sets **IoStatus.Status** to STATUS\_SUCCESS and passes the IRP down to the next lower driver, and so forth until the IRP reaches the bus driver. If any driver in the stack must fail the IRP, that driver should complete the IRP immediately by calling **IoCompleteRequest** and returning a failure status. Drivers that fail the IRP do not pass it further down the stack.

By returning STATUS\_SUCCESS, the driver guarantees that it will not start any operation that would change its ability to set the requested power state. The driver should queue any IRPs that require such operations until it completes a set-power IRP that returns the device to an acceptable power state.

On Windows 2000 and later systems, when the IRP specifies **PowerDeviceD1**, **PowerDeviceD2**, or **PowerDeviceD3**, the value at **Parameters.Power.ShutdownType** provides information about the current system power IRP, if a system power IRP is active. In this case, the value at **ShutdownType** indicates the currently requested system power state, or **PowerActionNone** if a system request is not outstanding. On Windows 98/Me, this field always contains **PowerActionNone** when the IRP requests a device power state.

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


[**IRP\_MN\_QUERY\_POWER**](irp-mn-query-power.md)

[**IRP\_MN\_SET\_POWER**](irp-mn-set-power.md)

[**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734)

[**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776)

 

 




