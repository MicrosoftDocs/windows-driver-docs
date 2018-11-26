---
title: NDIS_STATUS_WWAN_DEVICE_SLOT_MAPPING_INFO
description: Miniport drivers use the NDIS_STATUS_WWAN_DEVICE_SLOT_MAPPING_INFO notification to inform the MB service about the completion of a previous OID_WWAN_DEVICE_SLOT_MAPPING_INFO query or set request.
ms.assetid: 7825C20E-FB56-420D-B516-1ADA0C7C382E
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_DEVICE_SLOT_MAPPING_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO


Miniport drivers use the **NDIS\_STATUS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO** notification to inform the MB service about the completion of a previous [OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO](https://msdn.microsoft.com/library/windows/hardware/mt799831) query or set request.

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782403) structure.

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
<td><p>Windows 10, version 1703</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO](https://msdn.microsoft.com/library/windows/hardware/mt799831)

[**NDIS\_WWAN\_DEVICE\_SLOT\_MAPPING\_INFO**](https://msdn.microsoft.com/library/windows/hardware/mt782403)

 

 




