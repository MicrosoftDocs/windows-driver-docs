---
title: OID_WWAN_VENDOR_SPECIFIC
ms.topic: reference
description: OID_WWAN_VENDOR_SPECIFIC allows miniport drivers to implement vendor specific objects.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_VENDOR_SPECIFIC Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_VENDOR\_SPECIFIC


OID\_WWAN\_VENDOR\_SPECIFIC allows miniport drivers to implement vendor specific objects.

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a [**NDIS\_STATUS\_WWAN\_VENDOR\_SPECIFIC**](ndis-status-wwan-vendor-specific.md) status notification containing a vendor-defined structure to implement private objects when they have completed the transaction.

## Remarks

For more information about using this OID, see [WWAN Vendor Specific Operations](./mb-vendor-specific-operations.md).

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support vendor-specific operations.

## Requirements

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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[WWAN Vendor Specific Operations](./mb-vendor-specific-operations.md)

[**NDIS\_STATUS\_WWAN\_VENDOR\_SPECIFIC**](ndis-status-wwan-vendor-specific.md)

 

