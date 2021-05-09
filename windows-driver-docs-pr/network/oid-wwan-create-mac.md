---
title: OID_WWAN_CREATE_MAC
description: OID_WWAN_CREATE_MAC requests the miniport driver to create a new NDIS port.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_CREATE_MAC Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_CREATE\_MAC


OID\_WWAN\_CREATE\_MAC requests the miniport driver to create a new NDIS port. Context activation requests for the additional PDP context will be sent on this new NDIS port.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later completing the request with the [**NDIS\_WWAN\_MAC\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_mac_info) structure that indicates the NDIS port number and MAC address associated with the port.

Query requests are not supported.

## Remarks

Miniport drivers must process requests to create (activate) new NDIS ports asynchronously in order to prevent deadlocks.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 8.1 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_MAC\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_mac_info)

[OID\_WWAN\_DELETE\_MAC](oid-wwan-delete-mac.md)

 

