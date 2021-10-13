---
title: NDIS_STATUS_WWAN_AUTH_RESPONSE
description: Miniport drivers use the NDIS_STATUS_WWAN_AUTH_RESPONSE notification to inform the MB Service of a challenge response received from a previous challenge request issued using an OID_WWAN_AUTH_CHALLENGE query request.NDIS_WWAN_AUTH_RESPONSE structure.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_AUTH_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_AUTH\_RESPONSE


Miniport drivers use the NDIS\_STATUS\_WWAN\_AUTH\_RESPONSE notification to inform the MB Service of a challenge response received from a previous challenge request issued using an [OID\_WWAN\_AUTH\_CHALLENGE](./oid-wwan-auth-challenge.md) query request.

Miniport drivers can also send unsolicited events with this notification.

This NDIS status notification uses the [NDIS\_WWAN\_AUTH\_RESPONSE](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_auth_response) structure.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_AUTH\_CHALLENGE](./oid-wwan-auth-challenge.md)

[NDIS\_WWAN\_AUTH\_RESPONSE](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_auth_response)

 

