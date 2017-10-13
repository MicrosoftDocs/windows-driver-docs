---
title: IRP_MN_DEVICE_ENUMERATED
author: windows-driver-content
description: The PnP manager uses this I/O request packet (IRP) to notify bus drivers that a device object exists and that it has been fully enumerated by the plug and play manager.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 50ECF6E1-4FC6-4EEA-BACF-EBAD0329DA2E
keywords:
 - IRP_MN_DEVICE_ENUMERATED Kernel-Mode Driver Architecture
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_DEVICE_ENUMERATED%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


