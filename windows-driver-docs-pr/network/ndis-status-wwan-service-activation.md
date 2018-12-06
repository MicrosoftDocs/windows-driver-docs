---
title: NDIS_STATUS_WWAN_SERVICE_ACTIVATION
description: Miniport drivers use the NDIS_STATUS_WWAN_SERVICE_ACTIVATION notification to respond to OID set requests of OID_WWAN_SERVICE_ACTIVATION.
ms.assetid: c5700759-b903-4564-a8b8-c49140d2acd3
ms.date: 08/08/2017
keywords: 
 -NDIS_STATUS_WWAN_SERVICE_ACTIVATION Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION


Miniport drivers use the NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION notification to respond to OID set requests of [OID\_WWAN\_SERVICE\_ACTIVATION](oid-wwan-service-activation.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the NDIS\_WWAN\_SERVICE\_ACTIVATION\_STATUS structure.

Remarks
-------

Miniport drivers must return the service activation status in response to an OID set request of [OID\_WWAN\_SERVICE\_ACTIVATION](oid-wwan-service-activation.md).

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

 

 




