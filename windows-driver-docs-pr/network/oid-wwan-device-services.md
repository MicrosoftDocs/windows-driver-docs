---
title: OID_WWAN_DEVICE_SERVICES
description: OID_WWAN_DEVICE_SERVICES returns the list of device services supported by the miniport driver.NDIS_WWAN_DEVICE_SERVICES structure that indicates the supported device service GUIDs.
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DEVICE_SERVICES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_DEVICE\_SERVICES


OID\_WWAN\_DEVICE\_SERVICES returns the list of device services supported by the miniport driver.

Miniport drivers must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending a NDIS\_STATUS\_WWAN\_DEVICE\_SERVICES status notification containing a [**NDIS\_WWAN\_DEVICE\_SERVICES**](/windows-hardware/drivers/ddi/_netvista/) structure that indicates the supported device service GUIDs.

Set requests are not supported.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Versions: Supported in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

