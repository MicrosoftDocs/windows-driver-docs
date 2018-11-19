---
title: NDIS_STATUS_WWAN_USSD
description: Miniport drivers use the NDIS_STATUS_WWAN_USSD notification to implement the transaction completion response for Unstructured Supplementary Service Data (USSD) operations with the NDIS_WWAN_USSD_REQUEST structure.Miniport drivers can also send unsolicited events with this notification using the NDIS_WWAN_USSD_EVENT structure to describe the nature of the USSD event.
ms.assetid: 6EE1235A-486E-4653-BFAC-6151C795676B
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_USSD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_USSD


Miniport drivers use the NDIS\_STATUS\_WWAN\_USSD notification to implement the transaction completion response for Unstructured Supplementary Service Data (USSD) operations with the [NDIS\_WWAN\_USSD\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh439846) structure.

Miniport drivers can also send unsolicited events with this notification using the [NDIS\_WWAN\_USSD\_EVENT](https://msdn.microsoft.com/library/windows/hardware/hh439844) structure to describe the nature of the USSD event.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[NDIS\_WWAN\_USSD\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh439846)

[NDIS\_WWAN\_USSD\_EVENT](https://msdn.microsoft.com/library/windows/hardware/hh439844)

 

 




