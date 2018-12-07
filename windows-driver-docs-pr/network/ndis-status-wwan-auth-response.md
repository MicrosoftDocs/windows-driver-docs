---
title: NDIS_STATUS_WWAN_AUTH_RESPONSE
description: Miniport drivers use the NDIS_STATUS_WWAN_AUTH_RESPONSE notification to inform the MB Service of a challenge response received from a previous challenge request issued using an OID_WWAN_AUTH_CHALLENGE query request.NDIS_WWAN_AUTH_RESPONSE structure.
ms.assetid: 24831764-4F6D-481B-A440-4F9CAE1F7501
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_AUTH_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_AUTH\_RESPONSE


Miniport drivers use the NDIS\_STATUS\_WWAN\_AUTH\_RESPONSE notification to inform the MB Service of a challenge response received from a previous challenge request issued using an [OID\_WWAN\_AUTH\_CHALLENGE](https://msdn.microsoft.com/library/windows/hardware/hh440092) query request.

Miniport drivers can also send unsolicited events with this notification.

This NDIS status notification uses the [NDIS\_WWAN\_AUTH\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh439834) structure.

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


[OID\_WWAN\_AUTH\_CHALLENGE](https://msdn.microsoft.com/library/windows/hardware/hh440092)

[NDIS\_WWAN\_AUTH\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh439834)

 

 




