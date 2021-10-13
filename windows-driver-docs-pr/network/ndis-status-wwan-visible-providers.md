---
title: NDIS_STATUS_WWAN_VISIBLE_PROVIDERS
description: Miniport drivers use the NDIS_STATUS_WWAN_VISIBLE_PROVIDERS notification to inform the MB Service about the completion of OID_WWAN_VISIBLE_PROVIDERS \ 160;query requests.
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_VISIBLE_PROVIDERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_VISIBLE\_PROVIDERS


Miniport drivers use the NDIS\_STATUS\_WWAN\_VISIBLE\_PROVIDERS notification to inform the MB Service about the completion of [OID\_WWAN\_VISIBLE\_PROVIDERS](oid-wwan-visible-providers.md) query requests.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_VISIBLE\_PROVIDERS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_visible_providers) structure.

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


[OID\_WWAN\_VISIBLE\_PROVIDERS](oid-wwan-visible-providers.md)

[**NDIS\_WWAN\_VISIBLE\_PROVIDERS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_visible_providers)

 

