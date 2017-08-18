---
title: IRP\_MN\_QUERY\_RESOURCES
author: windows-driver-content
description: The PnP manager uses this IRP to get a device's boot configuration resources.Bus drivers must handle this request for their child devices that require hardware resources. Function and filter drivers do not handle this IRP.
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: b9a6f06b-07d9-4539-bd41-21cdccdc4b25
keywords:
 - IRP_MN_QUERY_RESOURCES Kernel-Mode Driver Architecture
---

# IRP\_MN\_QUERY\_RESOURCES


The PnP manager uses this IRP to get a device's boot configuration resources.

Bus drivers must handle this request for their child devices that require hardware resources. Function and filter drivers do not handle this IRP.

Major Code
----------

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)
When Sent
---------

The PnP manager sends this IRP when a device is enumerated.

The PnP manager sends this IRP at IRQL PASSIVE\_LEVEL in an arbitrary thread context.

## Input Parameters


None

## Output Parameters


Returned in the I/O status block.

## I/O Status Block


A bus driver that handles this IRP sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS or to an appropriate error status.

On success, a bus driver sets **Irp-&gt;IoStatus.Information** to a pointer to a [**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994) that contains the requested information. On an error, the bus driver sets **Irp-&gt;IoStatus.Information** to zero.

Operation
---------

If a bus driver returns a resource list in response to this IRP, it allocates a [**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994) from paged memory. The PnP manager frees the buffer when it is no longer needed.

If a device requires no hardware resources, the device's parent bus driver completes the IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)) without modifying **Irp-&gt;IoStatus.Status** or **Irp-&gt;IoStatus.Information**.

Function and filter drivers do not receive this IRP.

See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for the general rules for handling [Plug and Play minor IRPs](plug-and-play-minor-irps.md).

**Sending This IRP**

Reserved for system use. Drivers must not send this IRP.

Drivers can call [**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203) to get the boot configuration for a device, in both raw and translated forms.

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


[**CM\_RESOURCE\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff541994)

[**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP_MN_QUERY_RESOURCES%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


