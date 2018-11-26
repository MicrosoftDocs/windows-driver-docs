---
title: OID_WWAN_DEVICE_SERVICE_COMMAND
description: OID_WWAN_DEVICE_SERVICE_COMMAND allows miniport drivers to implement vendor specific commands.NDIS_STATUS_WWAN_DEVICE_SERVICE_RESPONSE status notification containing a vendor-defined structure (NDIS_WWAN_DEVICE_SERVICE_COMMAND) to provide responses when they have completed the transaction.
ms.assetid: 296E2D23-6EDA-4480-91A3-B6CB39243DAD
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DEVICE_SERVICE_COMMAND Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




