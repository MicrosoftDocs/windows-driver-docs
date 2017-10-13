---
title: NDIS_STATUS_WWAN_PIN_LIST
author: windows-driver-content
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_PIN\_LIST notification to respond to OID query requests of OID\_WWAN\_PIN\_LIST. Miniport drivers cannot use this notification to send unsolicited events.This notification uses the NDIS\_WWAN\_PIN\_LIST structure.
ms.assetid: fd8e6734-d032-445a-819a-0d5a773e9ea3
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_WWAN_PIN_LIST Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_PIN\_LIST


Miniport drivers use the NDIS\_STATUS\_WWAN\_PIN\_LIST notification to respond to OID query requests of [OID\_WWAN\_PIN\_LIST](oid-wwan-pin-list.md).

Miniport drivers cannot use this notification to send unsolicited events.

This notification uses the [**NDIS\_WWAN\_PIN\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff567912) structure.

Remarks
-------

This INDICATION is a response only notification to OID query requests of OID\_WWAN\_PIN\_LIST. Unsolicited indications are not expected for this INDICATION.

Any change in the PIN-entry mode caused as a result of an OID\_WWAN\_PIN enable or disable operation will not result in an NDIS\_STATUS\_WWAN\_PIN\_LIST INDICATION.

Note that the current PinMode for all of the PINs that the device supports must be updated to reflect the current state by the miniport driver on each query request.

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

## See also


[OID\_WWAN\_PIN\_LIST](oid-wwan-pin-list.md)

[**NDIS\_WWAN\_PIN\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff567912)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_PIN_LIST%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


