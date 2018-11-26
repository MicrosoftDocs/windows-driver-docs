---
title: OID_WWAN_DELETE_MAC
description: OID_WWAN_DELETE_MAC requests the miniport driver to delete the NDIS port specified in the NDIS_WWAN_MAC_INFO parameter.
ms.assetid: 3C992E0D-132E-4687-B38E-31409E1A9F54
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DELETE_MAC Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_DELETE\_MAC


OID\_WWAN\_DELETE\_MAC requests the miniport driver to delete the NDIS port specified in the NDIS\_WWAN\_MAC\_INFO parameter. The NDIS port should have been created earlier using [OID\_WWAN\_CREATE\_MAC](oid-wwan-create-mac.md).

Miniport drivers must process the set request asynchronously, initially returning NDIS\_STATUS\_PENDING to the original request, and later completing the request with NDIS\_STATUS\_SUCCESS.

Query requests are not supported.

Remarks
-------

Miniport drivers must process requests to delete (deactivate) NDIS ports asynchronously in order to prevent deadlocks.

OID\_WWAN\_DELETE\_MAC requests sent to delete the default port will fail with the NDIS status error code NDIS\_STATUS\_INVALID\_PORT.

Upon receiving an OID\_WWAN\_DELETE\_MAC request, miniport drivers should deactivate the PDP context associated with the port, if it has not already been deactivated. This is because a surprise removal event could occur. Deactivating the PDP context at such time will ensure that the modem and the miniport driver remain in a good state.

When the driver receives a surprise removal, the driver blocks and cancels all further OIDs. This means that the driver filters out OID\_WWAN\_DELETE\_MAC even though Windows sends a call with OID\_WWAN\_DELETE\_MAC as part of the [*FILTER\_DETACH*](https://msdn.microsoft.com/library/windows/hardware/ff549918) call.

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
<td><p>Available in Windows 8.1 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_WWAN\_CREATE\_MAC](oid-wwan-create-mac.md)

 

 




