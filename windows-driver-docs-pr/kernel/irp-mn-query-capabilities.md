---
title: IRP_MN_QUERY_CAPABILITIES
description: The PnP manager sends this IRP to get the capabilities of a device, such as whether the device can be locked or ejected.Function and filter drivers can handle this request if they alter the capabilities supported by the bus driver.
ms.date: 08/12/2017
ms.assetid: 3c968a46-5bfb-4579-b09a-ad6bce4d9e3b
keywords:
 - IRP_MN_QUERY_CAPABILITIES Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_CAPABILITIES


The PnP manager sends this IRP to get the capabilities of a device, such as whether the device can be locked or ejected.

Function and filter drivers can handle this request if they alter the capabilities supported by the bus driver. Bus drivers must handle this request for their child devices.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP to the bus driver for a device immediately after the device is enumerated. The PnP manager sends this IRP again after all the drivers for a device have started the device. A driver can send this IRP to get the capabilities for a device.

The PnP manager and drivers send this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


The **Parameters.DeviceCapabilities.Capabilities** member of the [**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659) structure points to a [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure containing information about the capabilities of the device.

## Output Parameters


**Parameters.DeviceCapabilities.Capabilities** points to the **DEVICE\_CAPABILITIES** structure that reflects any modifications made by the drivers that handle the IRP.

## I/O Status Block


A driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status such as STATUS\_UNSUCCESSFUL.

If a function or filter driver does not handle this IRP, it calls [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) and passes the IRP down to the next driver. Such a driver must not modify **Irp-&gt;IoStatus.Status** and must not complete the IRP.

A bus driver sets **Irp-&gt;IoStatus.Status** and completes the IRP.

Operation
---------

When a device is enumerated, but before the function and filter drivers are loaded for the device, the PnP manager sends an **IRP\_MN\_QUERY\_CAPABILITIES** request to the parent bus driver for the device. The bus driver must set any relevant values in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure and return it to the PnP manager.

After the device stack is built and drivers have started the device, the PnP manager sends this IRP again to be handled first by the driver at the top of the device stack and then by each lower driver in the stack. Function and filter drivers can set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine and handle this IRP on its way back up the device stack.

Drivers should add capabilities before they pass the IRP to the next lower driver.

Drivers should remove capabilities after all lower drivers have finished with the IRP. A driver does not typically remove capabilities that have been set by other drivers, but it might do so if it has special information about the capabilities of the device in a certain configuration. See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for information about postponing IRP processing until lower drivers have finished.

After a device is enumerated and its drivers are loaded, its capabilities should not change. A device's capabilities might change if the device is removed and re-enumerated.

When handling an **IRP\_MN\_QUERY\_CAPABILITIES** IRP, the driver that is the power policy manager for the device should set an *IoCompletion* routine and copy the device power capabilities, such as the S-to-D power state mappings, on the IRP's way back up the device stack. To determine the power capabilities of a child device, the parent bus driver creates another query-capabilities IRP and sends the IRP to its parent driver. See [Reporting Device Power Capabilities](https://msdn.microsoft.com/library/windows/hardware/ff561058) for more information.

If a driver handles this IRP, it should check the **DEVICE\_CAPABILITIES** **Version** value. If that value is not a version that the driver supports, the driver should fail the IRP. If the version is supported, the driver should check the **Size** field. A driver should set only those fields that are within the bounds of the capabilities structure that it received as input.

Drivers that handle this IRP can set some **DEVICE\_CAPABILITIES** fields but must not set the **Size** and **Version** fields. These fields are only set by the component that sent the IRP.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

A bus driver sends this IRP to the parent device stack when it handles an **IRP\_MN\_QUERY\_CAPABILITIES** request for one of its child devices. Also, a driver might send this IRP to get the device capabilities for one of its devices. A single driver in the stack has only part of the capabilities information for the device; sending an IRP to the device stack enables it to gather the full picture, including modifications by any filter drivers, and so forth.

See [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847) for information about sending IRPs. The following steps apply specifically to this IRP:

-   Allocate a [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure from paged pool, and initialize it to zeros by calling [**RtlZeroMemory**](https://msdn.microsoft.com/library/windows/hardware/ff563610). Initialize the **Size** to **sizeof**(**DEVICE\_CAPABILITIES**), the **Version** to 1, and **Address** and **UINumber** to -1.

-   Set the values in the next I/O stack location of the IRP: set **MajorFunction** to [**IRP\_MJ\_PNP**](irp-mj-pnp.md), set **MinorFunction** to **IRP\_MN\_QUERY\_CAPABILITIES**, and set **Parameters.DeviceCapabilities** to a pointer to the allocated **DEVICE\_CAPABILITIES** structure.

-   Initialize **IoStatus.Status** to STATUS\_NOT\_SUPPORTED.

-   Deallocate the IRP and the **DEVICE\_CAPABILITIES** structure when they are no longer needed.

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


[**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095)

 

 




