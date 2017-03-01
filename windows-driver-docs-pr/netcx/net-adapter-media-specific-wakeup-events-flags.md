---
title: NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS enumeration
topic_type:
- apiref
api_name:
- NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS
api_location:
- netadapter.h
api_type:
- HeaderDef
---

# NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies the media-specific wake-up events that a network adapter supports.

Syntax
------

```cpp
typedef enum _NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS { 
  NET_ADAPTER_WLAN_WAKE_ON_NLO_DISCOVERY           = NDIS_WLAN_WAKE_ON_NLO_DISCOVERY_SUPPORTED,
  NET_ADAPTER_WLAN_WAKE_ON_AP_ASSOCIATION_LOST     = NDIS_WLAN_WAKE_ON_AP_ASSOCIATION_LOST_SUPPORTED,
  NET_ADAPTER_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR     = NDIS_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR_SUPPORTED,
  NET_ADAPTER_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST  = NDIS_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_REGISTER_STATE          = NDIS_WWAN_WAKE_ON_REGISTER_STATE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_SMS_RECEIVE             = NDIS_WWAN_WAKE_ON_SMS_RECEIVE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_USSD_RECEIVE            = NDIS_WWAN_WAKE_ON_USSD_RECEIVE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_PACKET_STATE            = NDIS_WWAN_WAKE_ON_PACKET_STATE_SUPPORTED,
  NET_ADAPTER_WWAN_WAKE_ON_UICC_CHANGE             = NDIS_WWAN_WAKE_ON_UICC_CHANGE_SUPPORTED
} NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS;
```

Constants
---------

**NET_ADAPTER_WLAN_WAKE_ON_NLO_DISCOVERY**  
If this flag is set, the 802.11 network adapter can generate a wake-up event if it detects a service set identifier (SSID) that was specified through a network list offload (NLO). 

For more information about NLO, see [Wi-Fi Network List Offload](../network/wi-fi-network-list-offload.md).

**NET_ADAPTER_WLAN_WAKE_ON_AP_ASSOCIATION_LOST**  
If this flag is set, the 802.11 network adapter can generate a wake-up event if it disassociates with the access point (AP).

**NET_ADAPTER_WLAN_WAKE_ON_GTK_HANDSHAKE_ERROR**  
If this flag is set, the 802.11 network adapter can generate a wake-up event if it encounters an error during the IEEE 802.11i RSN group transient key (GTK) handshake with the AP.


**NET_ADAPTER_WLAN_WAKE_ON_4WAY_HANDSHAKE_REQUEST**  
If this flag is set, the 802.11 network adapter can generate a wake-up event if it receives the first frame of the IEEE 802.11i RSN 4-way handshake with the AP. This handshake is performed when the adapter authenticates with the AP.

**NET_ADAPTER_WWAN_WAKE_ON_REGISTER_STATE**  
If this flag is set, the mobile broadband (MB) network adapter can generate a wake-up event if its registration state to the MB Service has changed.

**NET_ADAPTER_WWAN_WAKE_ON_SMS_RECEIVE**  
If this flag is set, the MB network adapter can generate a wake-up event if the MB Service has to be notified about the receipt of a Short Message Service (SMS) message. The adapter generates this wake-up event either after the completion of a previously issued OID_WWAN_SMS_READ query request, or the arrival of a new class-0 (flash/alert) message from the network provider as an event notification.


**NET_ADAPTER_WWAN_WAKE_ON_USSD_RECEIVE**  
If this flag is set, the MB network adapter can generate a wake-up event if it receives an Unstructured Supplementary Service Data (USSD) message.


**NET_ADAPTER_WWAN_WAKE_ON_PACKET_STATE**  
If this flag is set, the MB network adapter can generate a wake-up event when the Packet Service state of the Modem changes.

**NET_ADAPTER_WWAN_WAKE_ON_UICC_CHANGE**  
If this flag is set, the MB network adapter can generate a wake-up event when the UICC (SIM) is inserted or removed. 

Remarks
-----
The **NET_ADAPTER_MEDIA_SPECIFIC_WAKEUP_EVENTS_FLAGS** enumeration is used to specify protocol offloads in the [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure.

The [**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md) structure is used as input to [**NetAdapterSetPowerCapabilities**](netadaptersetpowercapabilities.md).

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

See Also
-----
[**NET_ADAPTER_POWER_CAPABILITIES**](net-adapter-power-capabilities.md)
