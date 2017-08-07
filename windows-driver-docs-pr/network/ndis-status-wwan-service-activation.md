---
title: NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION
author: windows-driver-content
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_SERVICE\_ACTIVATION notification to respond to OID set requests of OID\_WWAN\_SERVICE\_ACTIVATION.
ms.assetid: c5700759-b903-4564-a8b8-c49140d2acd3
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - NDIS_STATUS_WWAN_SERVICE_ACTIVATION Network Drivers Starting with Windows Vista
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
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_SERVICE_ACTIVATION%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


