---
title: NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS enumeration
description: .
ms.assetid: ddff8578-b521-4c86-a157-ab55b467379e
keywords: ["NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET\_ADAPTER\_MEDIA\_SPECIFIC\_WAKEUP\_EVENTS\_FLAGS enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS { 
  NET_ADAPTER_WLAN_WAKE_ON_NLO_DISCOVERY           = = NDIS_WLAN_WAKE_ON_NLO_DISCOVERY_SUPPORTED,
  NET_ADAPTER_WLAN_WAKE_ON_AP_ASSOCIATION_LOST     = = NDIS_WLAN_WAKE_ON_AP_ASSOCIATION_LOST_SUPPORTED,
  NET_ADAPTER_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR     = = NDIS_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR_SUPPORTED,
  NET_ADAPTER_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST  = = NDIS_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_REGISTER_STATE          = = NDIS_WWAN_WAKE_ON_REGISTER_STATE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_SMS_RECEIVE             = = NDIS_WWAN_WAKE_ON_SMS_RECEIVE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_USSD_RECEIVE            = = NDIS_WWAN_WAKE_ON_USSD_RECEIVE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_PACKET_STATE            = = NDIS_WWAN_WAKE_ON_PACKET_STATE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_UICC_CHANGE             = = NDIS_WWAN_WAKE_ON_UICC_CHANGE_SUPPORTED
} NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS;
```

Constants
---------

<a href="" id="net-adapter-wlan-wake-on-nlo-discovery"></a>**NET\_ADAPTER\_WLAN\_WAKE\_ON\_NLO\_DISCOVERY**  

<a href="" id="net-adapter-wlan-wake-on-ap-association-lost"></a>**NET\_ADAPTER\_WLAN\_WAKE\_ON\_AP\_ASSOCIATION\_LOST**  

<a href="" id="net-adapter-wlan-wake-on-gtk-handshake-error"></a>**NET\_ADAPTER\_WLAN\_WAKE\_ON\_GTK\_HANDSHAKE\_ERROR**  

<a href="" id="net-adapter-wlan-wake-on-4way-handshake-request"></a>**NET\_ADAPTER\_WLAN\_WAKE\_ON\_4WAY\_HANDSHAKE\_REQUEST**  

<a href="" id="net-adapter-wwan-wake-on-register-state"></a>**NET\_ADAPTER\_WWAN\_WAKE\_ON\_REGISTER\_STATE**  

<a href="" id="net-adapter-wwan-wake-on-sms-receive"></a>**NET\_ADAPTER\_WWAN\_WAKE\_ON\_SMS\_RECEIVE**  

<a href="" id="net-adapter-wwan-wake-on-ussd-receive"></a>**NET\_ADAPTER\_WWAN\_WAKE\_ON\_USSD\_RECEIVE**  

<a href="" id="net-adapter-wwan-wake-on-packet-state"></a>**NET\_ADAPTER\_WWAN\_WAKE\_ON\_PACKET\_STATE**  

<a href="" id="net-adapter-wwan-wake-on-uicc-change"></a>**NET\_ADAPTER\_WWAN\_WAKE\_ON\_UICC\_CHANGE**  

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netadapter.h</td>
</tr>
</tbody>
</table>

 

 





