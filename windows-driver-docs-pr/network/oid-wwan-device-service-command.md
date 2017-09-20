---
title: OID\_WWAN\_DEVICE\_SERVICE\_COMMAND
author: windows-driver-content
description: OID\_WWAN\_DEVICE\_SERVICE\_COMMAND allows miniport drivers to implement vendor specific commands.NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_RESPONSE status notification containing a vendor-defined structure (NDIS\_WWAN\_DEVICE\_SERVICE\_COMMAND) to provide responses when they have completed the transaction.
ms.assetid: 296E2D23-6EDA-4480-91A3-B6CB39243DAD
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_DEVICE_SERVICE_COMMAND Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_DEVICE\_SERVICE\_COMMAND


OID\_WWAN\_DEVICE\_SERVICE\_COMMAND allows miniport drivers to implement vendor specific commands.

Both query and set requests are supported.

Miniport drivers must process query and set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh846205) status notification containing a vendor-defined structure ([**NDIS\_WWAN\_DEVICE\_SERVICE\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/hh439836)) to provide responses when they have completed the transaction.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support the specified device service or operation.

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
<td><p>Versions: Supported in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_WWAN\_DEVICE\_SERVICE\_RESPONSE**](https://msdn.microsoft.com/library/windows/hardware/hh846205)

[**NDIS\_WWAN\_DEVICE\_SERVICE\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/hh439836)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_SERVICE_COMMAND%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


