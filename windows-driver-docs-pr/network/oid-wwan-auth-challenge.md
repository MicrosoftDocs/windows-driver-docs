---
title: OID_WWAN_AUTH_CHALLENGE
description: OID_WWAN_AUTH_CHALLENGE sends an authentication challenge to the MB device, or Subscriber Identity Module (SIM) card, to obtain the response from the SIM.n NDIS_STATUS_WWAN_AUTHENTICATION_RESPONSE status notification containing an NDIS_WWAN_AUTHENTICATION_RESPONSE structure to provide the authentication keys requested based on challenges by the caller when completing query requests.
ms.assetid: C39300F2-DF14-4DA8-9BD2-83593CC29837
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_AUTH_CHALLENGE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




