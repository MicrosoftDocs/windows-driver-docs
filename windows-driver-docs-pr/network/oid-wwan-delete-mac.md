---
title: OID\_WWAN\_DELETE\_MAC
author: windows-driver-content
description: OID\_WWAN\_DELETE\_MAC requests the miniport driver to delete the NDIS port specified in the NDIS\_WWAN\_MAC\_INFO parameter.
ms.assetid: 3C992E0D-132E-4687-B38E-31409E1A9F54
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_DELETE_MAC Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DELETE_MAC%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


