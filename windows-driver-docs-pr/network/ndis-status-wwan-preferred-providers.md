---
title: NDIS_STATUS_WWAN_PREFERRED_PROVIDERS
author: windows-driver-content
description: Miniport drivers use the NDIS\_STATUS\_WWAN\_PREFERRED\_PROVIDERS notification to inform the MB Service that the Preferred Provider List (PPL) has changed.
ms.assetid: b0c06db9-82ca-4f94-80e6-3cf13197abf5
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -NDIS_STATUS_WWAN_PREFERRED_PROVIDERS Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WWAN\_PREFERRED\_PROVIDERS


Miniport drivers use the NDIS\_STATUS\_WWAN\_PREFERRED\_PROVIDERS notification to inform the MB Service that the Preferred Provider List (PPL) has changed.

Miniport drivers can also send unsolicited events with this notification.

This notification uses the [**NDIS\_WWAN\_PREFERRED\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/ff567913) structure.

Remarks
-------

In some cases, the PPL (for GSM-based devices) is updated by the network either Over-The-Air (OTA) or by Short Message Service (SMS). The miniport driver must update the PPL accordingly. Afterwards, miniport drivers must notify the MB Service about the updates using this INDICATION with the updated PPL. For GSM-based networks, the **PreferredListHeader** member of the NDIS\_WWAN\_PREFERRED\_PROVIDERS structure must point to the updated PPL.

Miniport drivers use this INDICATION to inform the MB Service about the update as a result of a [OID\_WWAN\_PREFERRED\_PROVIDERS](oid-wwan-preferred-providers.md) set request from the MB Service. A response to an OID\_WWAN\_PREFERRED\_PROVIDERS set request must contain zero elements in the **PreferredListHeader** member.

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


[**NDIS\_WWAN\_PREFERRED\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/ff567913)

[OID\_WWAN\_PREFERRED\_PROVIDERS](oid-wwan-preferred-providers.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_PREFERRED_PROVIDERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


