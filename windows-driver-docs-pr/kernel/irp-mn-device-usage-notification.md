---
title: IRP_MN_DEVICE_USAGE_NOTIFICATION
description: System components send this IRP to ask the drivers for a device whether the device can support a special file.
ms.date: 08/12/2017
ms.assetid: d8287ba2-ac0a-4407-b587-a5aa5b3617a2
keywords:
 - IRP_MN_DEVICE_USAGE_NOTIFICATION Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION


System components send this IRP to ask the drivers for a device whether the device can support a *special file*. Special files include paging files, dump files, and hibernation files. If all the drivers for the device succeed the IRP, the system creates the special file. The system also sends this IRP to inform drivers that a special file has been removed from the device.

Function drivers must handle this IRP if their device can contain a paging file, dump file, or hibernation file. Filter drivers must handle this IRP if the function driver they are filtering handles the IRP. Bus drivers must handle this IRP for their adapter or controller (bus FDO) and for their child devices (child PDOs).

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The system sends this IRP when it is creating or deleting a paging file, dump file, or hibernation file. If a device has a power management relationship that falls outside of the conventional parent-child relationship, the driver can send this IRP to propagate device usage information to another device stack. For more information, see the description of the **PowerRelations** request in [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](irp-mn-query-device-relations.md).

System components and drivers send this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


The **Parameters.UsageNotification.InPath** member of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure is a BOOLEAN. When this parameter is **TRUE**, the system is creating a paging, crash dump, or hibernation file on the device. When **InPath** is **FALSE**, such a file has been removed from the device.

**Parameters.UsageNotification.Type** is an enum indicating the kind of file. This parameter has one of the following values: **DeviceUsageTypePaging**, **DeviceUsageTypeDumpFile**, or **DeviceUsageTypeHibernation**.

## Output Parameters


None

## I/O Status Block


Drivers set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

Drivers do not modify the **Irp-&gt;IoStatus.Information** field; it remains at zero, as set by the component sending the IRP.

Operation
---------

A driver handles this IRP on the IRP's way down the device stack and on the IRP's way back up the stack.

A driver responds to this IRP with a procedure like the following:

-   If **Parameters.UsageNotification.InPath** is **TRUE**, determine whether the device supports the special file.

    A driver should test for the specific **Parameters.UsageNotification.Type**(s) that the driver can support. Additional notification types might be added in the future.

    See further information below describing the actions required to support each notification type.

    If **Parameters.UsageNotification.InPath** is **TRUE** and the driver cannot support the special file on the device, the driver must complete the IRP with a failure status.

-   If the device supports the special file:

    1.  Take appropriate actions to reflect that the device now contains, or no longer contains, a special file.

        A driver typically increments or decrements a counter. For example, if **Parameters.UsageNotification.Type** is **DeviceUsageTypePaging** and **Parameters.UsageNotification.InPath** is **TRUE**, increment a count of the number of paging files on the device. Certain driver dispatch routines must check the counter(s).

        A device that contains a special file should not be disabled. A driver can call [**IoInvalidateDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff549361), requesting the PnP manager to re-query for the device's PnP device state information. In response to the resulting [**IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE**](irp-mn-query-pnp-device-state.md) IRP, the driver should set the PNP\_DEVICE\_NOT\_DISABLEABLE flag.

        If **InPath** is **FALSE**, a driver sets the DO\_POWER\_PAGABLE bit in its device object for the device.

    2.  Propagate the device usage information to any related devices that require the information.

        As part of its handling of an **IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION** IRP, a driver might be required to pass the information to one or more other device stacks. Such a driver creates a new **IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION** IRP (or IRPs) and sends them to the appropriate device stack (or stacks). The driver must wait for completion of any device-usage-notification IRP(s) that it sends before the driver finishes processing the device-usage IRP that it received.

        How to identify the related devices is device- and driver-specific. Typically, a driver sends the IRP to other drivers to which it would send I/O requests for the file. When a bus driver handles this request for a child device, it must send a usage notification IRP to the device stack for the device's parent.

        For example, when ftdisk is running a five-disk stripe set, it propagates paging notifications to each of these five disks, since each of these devices can be required to handle paging file operations.

    3.  In a function or filter driver, set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine.

    4.  In a function or filter driver, set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS, set up the next stack location, and pass the IRP to the next lower driver with [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336). Do not complete the IRP.

        In a bus driver that is handling the IRP for a child PDO: set **Irp-&gt;IoStatus.Status** and complete the IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)).

    5.  During IRP completion processing:

        If an *IoCompletion* routine detects that a lower driver has failed the IRP, the function or filter driver must undo any operations it performed in response to the IRP and propagate the error. If the function or filter driver propagated the usage information to any other device stacks, the driver must send another usage IRP to those stacks to notify them of the failure.

        If status is STATUS\_SUCCESS and **InPath** is **TRUE**, clear the DO\_POWER\_PAGABLE bit.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Supporting Paging, Crash Dump, and Hibernation Files on a Device**

When any of a driver's special file counts is nonzero, the driver must support the presence of the special file(s) on its device (or a descendant device).

For a **DeviceUsageTypePaging** file created on its device, a driver must do the following:

-   Lock code in memory for its [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376), [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034), [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287), and [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routines.

-   Clear the DO\_POWER\_PAGABLE bit in its device object for the device (on the IRP's way up the device stack).

-   Fail **IRP\_MN\_QUERY\_STOP\_DEVICE** and **IRP\_MN\_QUERY\_REMOVE\_DEVICE** requests for the device.

For a **DeviceUsageTypeDumpFile** file on its device, a driver must do the following:

-   Lock code in memory for its *DispatchRead*, *DispatchWrite*, *DispatchDeviceControl*, and *DispatchPower* routines.

-   Do not take the device out of the D0 state.

    Do not register the device for idle detection ([**PoRegisterDeviceForIdleDetection**](https://msdn.microsoft.com/library/windows/hardware/ff559721)). If the device is already registered, cancel the registration. If the driver performs its own idle detection for the device, suspend such detection.

-   Clear the DO\_POWER\_PAGABLE bit in its device object for the device (on the IRP's way up the device stack).

-   Fail [**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md) and [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md) requests for the device.

For a **DeviceUsageTypeHibernation** file on its device, a driver must do the following:

-   Lock code in memory for its *DispatchRead*, *DispatchWrite*, *DispatchDeviceControl*, and *DispatchPower* routines.

-   Ensure the device is in the D0 state when the driver receives an S4 system power IRP indicating that the system is about to hibernate.

-   Do not power down the device in response to a D3 set-power IRP that is part of an S4 hibernate action. See [System Power Actions](https://msdn.microsoft.com/library/windows/hardware/ff564553) for more information.

    Upon receipt of such a D3 set-power IRP, perform all tasks required to put the device in the D3 state except for powering off the device and notifying the power manager ([**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765)). The device must retain power until the hibernation file has been written.

-   Clear the DO\_POWER\_PAGABLE bit in its device object for the device (on the IRP's way up the device stack).

-   Fail [**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md) and [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md) requests for the device.

See [Power Management](https://msdn.microsoft.com/library/windows/hardware/ff547131) for more information about device power states, power IRPs, and supporting power management in drivers.

**Sending This IRP**

A driver can send an **IRP\_MN\_DEVICE\_USAGE\_INFORMATION** IRP, but only to propagate device usage information to another device stack. A driver is never the initial source of device usage information.

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


[*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287)

[*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354)

[*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376)

[*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034)

[**IoAdjustPagingPathCount**](https://msdn.microsoft.com/library/windows/hardware/ff548209)

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)

[**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)

[**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

[**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](irp-mn-query-device-relations.md)

[**IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE**](irp-mn-query-pnp-device-state.md)

[**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md)

[**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md)

[**PoRegisterDeviceForIdleDetection**](https://msdn.microsoft.com/library/windows/hardware/ff559721)

[**PoSetPowerState**](https://msdn.microsoft.com/library/windows/hardware/ff559765)

 

 




