---
title: IRP_MN_DEVICE_ENUMERATED
description: The PnP manager uses this I/O request packet (IRP) to notify bus drivers that a device object exists and that it has been fully enumerated by the plug and play manager.
ms.date: 08/12/2017
ms.assetid: 50ECF6E1-4FC6-4EEA-BACF-EBAD0329DA2E
keywords:
 - IRP_MN_DEVICE_ENUMERATED Kernel-Mode Driver Architecture
ms.localizationpriority: medium
---

# IRP\_MN\_DEVICE\_ENUMERATED


The PnP manager uses this I/O request packet (IRP) to notify bus drivers that a device object exists and that it has been fully enumerated by the plug and play manager.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP just before user mode is notified with GUID\_DEVICE\_ENUMERATED. This IRP allows drivers to provide a preprocess routine for IRP\_MN\_DEVICE\_ENUMERATED, such as filling in additional device properties. This IRP primarily allows drivers to set device properties for the physical device object (PDO) by using [**IoSetDevicePropertyData**](https://msdn.microsoft.com/library/windows/hardware/ff549704).

## Input Parameters


None

## Output Parameters


None

## I/O Status Block


A driver that handles this IRP sets [Irp-&gt;IoStatus.Status](https://msdn.microsoft.com/library/windows/hardware/ff551825) to STATUS\_SUCCESS or an appropriate error status.

Operation
---------

The **IRP\_MN\_DEVICE\_ENUMERATED** IRP is sent to the bus driver's PDO to indicate that the bus driver PDO exists.

## Sending the IRP


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
<td><p>Version</p></td>
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wdm.h</td>
</tr>
</tbody>
</table>

## See also


[Plug and Play Minor IRPs](plug-and-play-minor-irps.md)

 

 




