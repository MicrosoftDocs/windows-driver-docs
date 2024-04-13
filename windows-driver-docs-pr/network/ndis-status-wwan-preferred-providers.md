---
title: NDIS_STATUS_WWAN_PREFERRED_PROVIDERS
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_PREFERRED_PROVIDERS notification to inform the MB Service that the Preferred Provider List (PPL) has changed.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_PREFERRED_PROVIDERS Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_PREFERRED\_PROVIDERS


Miniport drivers use the NDIS\_STATUS\_WWAN\_PREFERRED\_PROVIDERS notification to inform the MB Service that the Preferred Provider List (PPL) has changed.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_PREFERRED\_PROVIDERS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_preferred_providers) structure.

## Remarks

In some cases, the PPL (for GSM-based devices) is updated by the network either Over-The-Air (OTA) or by Short Message Service (SMS). The miniport driver must update the PPL accordingly. Afterwards, miniport drivers must notify the MB Service about the updates using this INDICATION with the updated PPL. For GSM-based networks, the **PreferredListHeader** member of the NDIS\_WWAN\_PREFERRED\_PROVIDERS structure must point to the updated PPL.

Miniport drivers use this INDICATION to inform the MB Service about the update as a result of a [OID\_WWAN\_PREFERRED\_PROVIDERS](oid-wwan-preferred-providers.md) set request from the MB Service. A response to an OID\_WWAN\_PREFERRED\_PROVIDERS set request must contain zero elements in the **PreferredListHeader** member.

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


[**NDIS\_WWAN\_PREFERRED\_PROVIDERS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_preferred_providers)

[OID\_WWAN\_PREFERRED\_PROVIDERS](oid-wwan-preferred-providers.md)

 

