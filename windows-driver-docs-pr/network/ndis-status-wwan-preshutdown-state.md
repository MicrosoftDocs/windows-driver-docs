---
title: NDIS_STATUS_WWAN_PRESHUTDOWN_STATE
description: The NDIS_STATUS_WWAN_PRESHUTDOWN_STATE notification is a one-way notification from the MBB driver to the host.
ms.assetid: 191629A1-2BBF-42D8-A053-827222CE35B0
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_WWAN_PRESHUTDOWN_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_PRESHUTDOWN\_STATE


The NDIS\_STATUS\_WWAN\_PRESHUTDOWN\_STATE notification is a one-way notification from the MBB driver to the host. The MBB driver sends up this notification when the modem has finished all operations required before shutdown.

This notification uses the [**NDIS\_WWAN\_PRESHUTDOWN\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt593234) structure.

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
<td><p>Supported starting with Windows 10, version 1511.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

 

 




