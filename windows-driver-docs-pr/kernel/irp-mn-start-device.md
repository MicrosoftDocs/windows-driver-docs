---
title: IRP_MN_START_DEVICE
description: All PnP drivers must handle this IRP.
ms.date: 08/12/2017
ms.assetid: 0aac1346-b5c7-4dcc-ab86-03e8fd151505
keywords:
 - IRP_MN_START_DEVICE Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_START\_DEVICE


All PnP drivers must handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP after it has assigned hardware resources, if any, to the device. The device may have been recently enumerated and is being started for the first time, or the device may be restarting after being stopped for resource rebalancing.

Sometimes the PnP manager sends an **IRP\_MN\_START\_DEVICE** to a device that is already started, supplying a different set of resources than the device is currently using. A driver initiates this action by calling [**IoInvalidateDeviceState**](https://msdn.microsoft.com/library/windows/hardware/ff549361) and responding to the subsequent [**IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE**](irp-mn-query-pnp-device-state.md) request with the PNP\_RESOURCE\_REQUIREMENTS\_CHANGED flag set. A bus driver might use this mechanism, for example, to open a new aperture on a PCI-to-PCI bridge.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in the context of a system thread.

## Input Parameters


The **Parameters.StartDevice.AllocatedResources** member of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure points to a [**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994) describing the hardware resources that the PnP manager assigned to the device. This list contains the resources in raw form. Use the raw resources to program the device.

**Parameters.StartDevice.AllocatedResourcesTranslated** points to a [**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994) describing the hardware resources that the PnP manager assigned to the device. This list contains the resources in translated form. Use the translated resources to connect the interrupt vector, map I/O space, and map memory.

## Output Parameters


None

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as STATUS\_UNSUCCESSFUL or STATUS\_INSUFFICIENT\_RESOURCES.

If a driver requires some time to run its start operations for a device, it can mark the IRP pending and return STATUS\_PENDING.

Operation
---------

This IRP must be handled first by the parent bus driver for a device and then by each higher driver in the device stack.

In response to this IRP, drivers start a device for the first time or restart a device that was stopped. The exact operations required to start a device vary from device to device, but can include powering on the device, performing device-specific initialization, and connecting the interrupt.

A driver can typically handle this IRP in the same way whether it is starting a device for the first time or restarting a device after an [**IRP\_MN\_STOP\_DEVICE**](irp-mn-stop-device.md), except if a driver needs to restore device state on a restart after a stop.

On Windows Vista and later operating systems, we recommend that drivers always pend the **IRP\_MN\_START\_DEVICE** IRP and complete its processing later. This order enables the system to process device restarts asynchronously. (On operating systems before Windows Vista, drivers can return STATUS\_PENDING from their dispatch routines, but the PnP manager does not overlap the device restart with any other operation.)

For more information about handling a start IRP, see [Starting a Device](https://msdn.microsoft.com/library/windows/hardware/ff563849).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

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


[**IRP\_MN\_STOP\_DEVICE**](irp-mn-stop-device.md)

 

 




