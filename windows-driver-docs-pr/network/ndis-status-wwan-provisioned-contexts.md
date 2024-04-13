---
title: NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS notification to inform the MB Service about updates to the list of provisioned contexts as a result of a network update.
ms.date: 03/02/2023
keywords: 
 -NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS


Miniport drivers use the NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS notification to inform the MB Service about updates to the list of provisioned contexts as a result of a network update.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_PROVISIONED\_CONTEXTS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_provisioned_contexts) structure.

## Remarks

Miniport drivers must set the **ElementType** member of the NDIS\_WWAN\_PROVISIONED\_CONTEXTS structure's **ContextListHeader** to **WwanStructContext**.

In some cases, the list of provisioned contexts is updated by the network either Over-The-Air (OTA) or by Short Message Service (SMS). The miniport driver must update the list of provisioned contexts accordingly. Thereafter, miniport drivers must notify the MB Service about the updates using this INDICATION with the updated list.

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


[**NDIS\_WWAN\_PROVISIONED\_CONTEXTS**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_provisioned_contexts)

[OID\_WWAN\_PROVISIONED\_CONTEXTS](oid-wwan-provisioned-contexts.md)

 

