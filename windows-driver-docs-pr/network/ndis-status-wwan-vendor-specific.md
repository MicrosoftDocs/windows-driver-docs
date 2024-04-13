---
title: NDIS_STATUS_WWAN_VENDOR_SPECIFIC
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_VENDOR_SPECIFIC notification to implement the transaction completion response for vendor specific operation or vendor specific change notifications.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_VENDOR_SPECIFIC Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_VENDOR\_SPECIFIC


Miniport drivers use the NDIS\_STATUS\_WWAN\_VENDOR\_SPECIFIC notification to implement the transaction completion response for vendor specific operation or vendor specific change notifications.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_VENDOR\_SPECIFIC**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_vendor_specific) structure.

## Remarks

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
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_VENDOR\_SPECIFIC**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_vendor_specific)

[OID\_WWAN\_VENDOR\_SPECIFIC](oid-wwan-vendor-specific.md)

 

