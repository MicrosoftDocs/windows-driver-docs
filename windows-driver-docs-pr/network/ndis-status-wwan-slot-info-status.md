---
title: NDIS_STATUS_WWAN_SLOT_INFO
description: Miniport drivers use the NDIS_STATUS_WWAN_SLOT_INFO notification to inform the MB service about the completion of a previous OID_WWAN_SLOT_INFO query request.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_SLOT_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_SLOT\_INFO


Miniport drivers use the **NDIS\_STATUS\_WWAN\_SLOT\_INFO** notification to inform the MB service about the completion of a previous [OID\_WWAN\_SLOT\_INFO](./oid-wwan-slot-info-status.md) query request.

Miniport drivers can send a **NDIS\_STATUS\_WWAN\_SLOT\_INFO** notification as an unsolicited event when the slot/card state changes.

This notification uses the [**NDIS\_WWAN\_SLOT\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_slot_info) structure.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Windows 10, version 1703</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_SLOT\_INFO](./oid-wwan-slot-info-status.md)

[**NDIS\_WWAN\_SLOT\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_slot_info)

 

