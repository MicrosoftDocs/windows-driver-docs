---
title: NDIS_STATUS_MEDIA_DISCONNECT
description: The NDIS_STATUS_MEDIA_DISCONNECT status indicates that the status of a network connection has changed from connected to disconnected.
ms.assetid: 490853ca-c849-4b2b-9639-4be670616101
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_MEDIA_DISCONNECT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_MEDIA\_DISCONNECT


The NDIS\_STATUS\_MEDIA\_DISCONNECT status indicates that the status of a network connection has changed from connected to disconnected. For example, the network device loses the connection because it is out of range (for a wireless device), or the user unplugs the device's network cable.

Remarks
-------

NDIS translates NDIS\_STATUS\_MEDIA\_DISCONNECT status indications to [**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md) status indications for overlying NDIS 6.0 drivers.

NDIS 5.*x* and earlier miniport drivers indicate an [**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md) status when the connection is restored.

For more information about NDIS\_STATUS\_MEDIA\_DISCONNECT, see [Indicating Connection Status (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff546856) and [Media Status Indications for 802.11 Networks](https://msdn.microsoft.com/library/windows/hardware/ff549301).

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
<td><p>Not supported in NDIS 6.0 and later (use <a href="ndis-status-link-state.md" data-raw-source="[&lt;strong&gt;NDIS_STATUS_LINK_STATE&lt;/strong&gt;](ndis-status-link-state.md)"><strong>NDIS_STATUS_LINK_STATE</strong></a> instead). Supported only for NDIS 5.1 drivers in Windows Vista and Windows XP.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md)

[**NDIS\_STATUS\_MEDIA\_CONNECT**](ndis-status-media-connect.md)

 

 




