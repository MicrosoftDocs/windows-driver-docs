---
title: IRP_MN_QUERY_RESOURCES
description: The PnP manager uses this IRP to get a device's boot configuration resources.Bus drivers must handle this request for their child devices that require hardware resources. Function and filter drivers do not handle this IRP.
ms.date: 08/12/2017
keywords:
 - IRP_MN_QUERY_RESOURCES Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_QUERY\_RESOURCES


The PnP manager uses this IRP to get a device's boot configuration resources.

Bus drivers must handle this request for their child devices that require hardware resources. Function and filter drivers do not handle this IRP.

## Value

0x0A

## Major Code

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

## When Sent

The PnP manager sends this IRP when a device is enumerated.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


None

## Output Parameters


Returned in the I/O status block.

## I/O Status Block


A bus driver that handles this IRP sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

On success, a bus driver sets **Irp-&gt;IoStatus.Information** to a pointer to a [**CM\_RESOURCE\_LIST**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cm_resource_list) that contains the requested information. On an error, the bus driver sets **Irp-&gt;IoStatus.Information** to zero.

## Operation

If a bus driver returns a resource list in response to this IRP, it allocates a [**CM\_RESOURCE\_LIST**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cm_resource_list) from paged memory. The PnP manager frees the buffer when it is no longer needed.

If a device requires no hardware resources, the device's parent bus driver completes the IRP ([**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest)) without modifying **Irp-&gt;IoStatus.Status** or **Irp-&gt;IoStatus.Information**.

Function and filter drivers do not receive this IRP.

See [Plug and Play](./introduction-to-plug-and-play.md) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

Drivers can call [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty) to get the boot configuration for a device, in both raw and translated forms.

## Requirements

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


[**CM\_RESOURCE\_LIST**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_cm_resource_list)

[**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty)

 

