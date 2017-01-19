---
title: NET\_ADAPTER\_MEDIA\_SPECIFIC\_WAKEUP\_EVENTS\_FLAGS enumeration
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


\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS%20enumeration%20%20RELEASE:%20%281/19/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




