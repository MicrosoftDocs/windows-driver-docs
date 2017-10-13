---
title: OID_WWAN_AUTH_CHALLENGE
author: windows-driver-content
description: OID\_WWAN\_AUTH\_CHALLENGE sends an authentication challenge to the MB device, or Subscriber Identity Module (SIM) card, to obtain the response from the SIM.n NDIS\_STATUS\_WWAN\_AUTHENTICATION\_RESPONSE status notification containing an NDIS\_WWAN\_AUTHENTICATION\_RESPONSE structure to provide the authentication keys requested based on challenges by the caller when completing query requests.
ms.assetid: C39300F2-DF14-4DA8-9BD2-83593CC29837
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_WWAN_AUTH_CHALLENGE Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_AUTH\_CHALLENGE


OID\_WWAN\_AUTH\_CHALLENGE sends an authentication challenge to the MB device, or Subscriber Identity Module (SIM) card, to obtain the response from the SIM.

Set requests are not supported.

This is an optional OID. When miniport drivers implement it, they must process query requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later sending an NDIS\_STATUS\_WWAN\_AUTHENTICATION\_RESPONSE status notification containing an NDIS\_WWAN\_AUTHENTICATION\_RESPONSE structure to provide the authentication keys requested based on challenges by the caller when completing query requests.

Remarks
-------

When processing this OID, miniport drivers can access the SIM card, but should not access the provider network. This OID must work even in Radio OFF or Airplane Mode.

OID\_WWAN\_AUTH\_CHALLENGE supports both second-generation and third-generation mobile networks. SIM specifies an authentication mechanism that is based on the GSM authentication and key agreement primitives, which is a second-generation mobile network standard. AKA and AKA' uses the third-generation Authentication and Key Agreement mechanism, specified for Universal Mobile Telecommunications System (UMTS) in \[TS33.102\] and for CDMA2000 in \[S.S0055-A\] depending on the capabilities of the device.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED if they do not support returning one or all authentication methods.

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
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_AUTH_CHALLENGE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


