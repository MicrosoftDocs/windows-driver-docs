---
title: NDIS_STATUS_MEDIA_CONNECT
description: The NDIS_STATUS_MEDIA_CONNECT status indicates that the status of a device's network connection has changed from disconnected to connected.
ms.assetid: de03d265-c8bf-4b7d-bfff-f583fcf08904
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_MEDIA_CONNECT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_MEDIA\_CONNECT


The NDIS\_STATUS\_MEDIA\_CONNECT status indicates that the status of a device's network connection has changed from disconnected to connected. For example, a device connects when it comes within range of an access point (for a wireless device) or when the user connects the device's network cable.

Remarks
-------

NDIS translates NDIS\_STATUS\_MEDIA\_CONNECT status indications to [**NDIS\_STATUS\_LINK\_STATE**](ndis-status-link-state.md) status indications for overlying NDIS 6.0 drivers.

NDIS 5.*x* and earlier miniport drivers indicate an [**NDIS\_STATUS\_MEDIA\_DISCONNECT**](ndis-status-media-disconnect.md) status when a miniport driver determines that the network connection has been lost. When the connection is restored, the driver indicates an NDIS\_STATUS\_MEDIA\_CONNECT status.

For more information about NDIS\_STATUS\_MEDIA\_CONNECT, see [Indicating Connection Status (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff546856) and [Media Status Indications for 802.11 Networks](https://msdn.microsoft.com/library/windows/hardware/ff549301).

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

[**NDIS\_STATUS\_MEDIA\_DISCONNECT**](ndis-status-media-disconnect.md)

 

 




