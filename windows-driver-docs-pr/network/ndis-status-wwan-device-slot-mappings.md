---
title: NDIS_STATUS_WWAN_DEVICE_SLOT_MAPPING_INFO
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SLOT_MAPPING_INFO notification to inform the MB service about the completion of a previous OID_WWAN_DEVICE_SLOT_MAPPING_INFO query or set request.
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SLOT_MAPPING_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO


Miniport drivers use the **NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO** notification to inform the MB service about the completion of a previous [OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO](./oid-wwan-device-slot-mappings.md) query or set request.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_slot_mapping_info) structure.

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


[OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO](./oid-wwan-device-slot-mappings.md)

[**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_device_slot_mapping_info)

 

