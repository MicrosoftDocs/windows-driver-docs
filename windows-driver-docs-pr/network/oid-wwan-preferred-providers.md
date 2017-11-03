---
title: OID_WWAN_PREFERRED_PROVIDERS
author: windows-driver-content
description: OID_WWAN_PREFERRED_PROVIDERS returns information about the list of preferred providers for GSM-based devices.
ms.assetid: fa70f1ac-5b14-44f8-a2c4-d2163fe81c5a
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_PREFERRED_PROVIDERS Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_PREFERRED\_PROVIDERS


OID\_WWAN\_PREFERRED\_PROVIDERS returns information about the list of preferred providers for GSM-based devices. Miniport drivers of CDMA-based devices do not need to support this OID.

Miniport drivers must process set and query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an [**NDIS\_STATUS\_WWAN\_PREFERRED\_PROVIDERS**](ndis-status-wwan-preferred-providers.md) status notification containing an [**NDIS\_WWAN\_PREFERRED\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/ff567913) structure to provide information about the Preferred Provider List (PPL) regardless of completing set or query requests.

Remarks
-------

For more information about using this OID, see [WWAN Provider Operations](https://msdn.microsoft.com/library/windows/hardware/ff559101).

Miniport drivers can access the Subscriber Identity Module (SIM card) when processing query requests, but should not access the provider network.

Miniport drivers can access the Subscriber Identity Module (SIM card) or the provider network, when processing set requests.

When processing OID\_WWAN\_PREFERRED\_PROVIDERS, miniport drivers may set only the WWAN\_PROVIDER\_STATE\_PREFERRED or WWAN\_PROVIDER\_STATE\_FORBIDDEN flags to tag the list entries. Be aware that forbidden providers might not appear in the list for GSM-based devices.

Miniport driverrs should set the **PreferredListHeader.ElementType** member to *WwanStructProvider*. The miniport driver should set the **PreferredListHeader.ElementCount** member to 0 when responding to OID\_WWAN\_PREFERRED\_PROVIDERS set requests.

Whether the PPL on the device can be overwritten or not when processing set requests depends on the device capability, the cellular technology, and/or the network provider's policy.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support returning or setting the PPL.

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


[**NDIS\_WWAN\_PREFERRED\_PROVIDERS**](https://msdn.microsoft.com/library/windows/hardware/ff567913)

[**NDIS\_STATUS\_WWAN\_PREFERRED\_PROVIDERS**](ndis-status-wwan-preferred-providers.md)

[WWAN Provider Operations](https://msdn.microsoft.com/library/windows/hardware/ff559101)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_PREFERRED_PROVIDERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


