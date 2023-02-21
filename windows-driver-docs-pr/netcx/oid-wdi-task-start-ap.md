---
title: OID_WDI_TASK_START_AP (dot11wificxintf.h)
ms.topic: reference
description: The OID_WDI_TASK_START_AP command requests that the IHV component configures a port to start a Wi-Fi Direct Group Owner on the specified port.
ms.date: 07/31/2021
keywords:
 - OID_WDI_TASK_START_AP Network Drivers Starting with Windows Vista
---

# OID\_WDI\_TASK\_START\_AP (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_TASK\_START\_AP requests that the IHV component configures a port to start a Wi-Fi Direct Group Owner on the specified port.

| Object | Abort capable                                     | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------------------------------------------|---------------------------------------|---------------------------------|
| Port   | Yes. The abort must be followed by a dot11 reset. | 4                                     | 1                               |

 

During initialization, the driver sets the GO on 5GHz band capability in [**WIFI_WIFIDIRECT_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_wifidirect_capabilities) to indicate whether it can start the access point on the 5 GHz band.

If GO on 5 GHz band support is set, the adapter should start the AP on the Advertised Operating channel, and if that fails, it should try the list specified in the AP band channel list parameter. The operating system will provide a hint to the driver about whether this AP would provide internet connectivity by setting the **DOT11\_WFD\_GROUP\_CAPABILITY\_CROSS\_CONNECTION\_SUPPORTED** flag in [**WDI\_TLV\_P2P\_GROUP\_OWNER\_CAPABILITY**](./wdi-tlv-p2p-group-owner-capability.md).

If **MustUseSpecifiedChannel** in [**WDI\_TLV\_START\_AP\_PARAMETERS**](./wdi-tlv-start-ap-parameters.md) is specified, the AP may return one of the following errors if it is unable to start the AP on the specified band/channel(s):

* ****NDIS\_STATUS\_DOT11\_AP\_CHANNEL\_CURRENTLY\_NOT\_AVAILABLE****: Unable to start the AP on the specified channel(s) right now . Retry on the specified channel(s) later.

* ****NDIS\_STATUS\_DOT11\_AP\_BAND\_CURRENTLY\_NOT\_AVAILABLE****: Unable to start the AP on the specified band(s) right now. Retry on the specified band(s) later.

* ****NDIS\_STATUS\_DOT11\_AP\_CHANNEL\_NOT\_ALLOWED****: Unable to start the AP on the specified channel(s) due to regulatory reasons.

* ****NDIS\_STATUS\_DOT11\_AP\_BAND\_NOT\_ALLOWED****: Unable to start the AP on the specified band(s) due to regulatory reasons.


 

## Task parameters


|TLV|Multiple TLV instances allowed|Optional|Description|
|--- |--- |--- |--- |
|[**WDI_TLV_SSID**](wdi-tlv-ssid.md)|||The SSID to be used by the AP.|
|[**WDI_TLV_START_AP_PARAMETERS**](wdi-tlv-start-ap-parameters.md)|||Additional parameters for this task.|
|[**WDI_TLV_AUTH_ALGO_LIST**](wdi-tlv-auth-algo-list.md)|||The list of authentication algorithms that the connection can use.|
|[**WDI_TLV_MULTICAST_CIPHER_ALGO_LIST**](wdi-tlv-multicast-cipher-algo-list.md)|||The list of multicast cipher algorithms that the connection can use.|
|[**WDI_TLV_UNICAST_CIPHER_ALGO_LIST**](wdi-tlv-unicast-cipher-algo-list.md)|||The list of multicast cipher algorithms that the connection can use.|
|[**WDI_TLV_P2P_CHANNEL_NUMBER**](wdi-tlv-p2p-channel-number.md)||X|If specified, this defines the operating channel determined in group formation. This may only be specified when the operating mode is Wi-Fi Direct GO.|
|[**WDI_TLV_AP_BAND_CHANNEL**](wdi-tlv-ap-band-channel.md)|X|X|Optional list of bands and channels to start the access point on. If MustUseSpecifiedChannels is set to 1, the AP can only be started from this list. If it is not set, this list is meant to be a recommendation of channels that the firmware can pick from, and it may pick another channel if it is not possible to start the AP on any of the specified channels.|

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_START\_AP\_COMPLETE](ndis-status-wdi-indication-start-ap-complete.md)

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

