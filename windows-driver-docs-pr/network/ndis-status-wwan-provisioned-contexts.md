---
title: NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS
description: Miniport drivers use the NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS notification to inform the MB Service about updates to the list of provisioned contexts as a result of a network update.
ms.assetid: 3ec3d991-98c0-4be3-a157-a04e8565a54b
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_PROVISIONED_CONTEXTS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS


Miniport drivers use the NDIS\_STATUS\_WWAN\_PROVISIONED\_CONTEXTS notification to inform the MB Service about updates to the list of provisioned contexts as a result of a network update.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_PROVISIONED\_CONTEXTS**](https://msdn.microsoft.com/library/windows/hardware/ff567914) structure.

Remarks
-------

Miniport drivers must set the **ElementType** member of the NDIS\_WWAN\_PROVISIONED\_CONTEXTS structure's **ContextListHeader** to **WwanStructContext**.

In some cases, the list of provisioned contexts is updated by the network either Over-The-Air (OTA) or by Short Message Service (SMS). The miniport driver must update the list of provisioned contexts accordingly. Thereafter, miniport drivers must notify the MB Service about the updates using this INDICATION with the updated list.

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
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_PROVISIONED\_CONTEXTS**](https://msdn.microsoft.com/library/windows/hardware/ff567914)

[OID\_WWAN\_PROVISIONED\_CONTEXTS](oid-wwan-provisioned-contexts.md)

 

 




