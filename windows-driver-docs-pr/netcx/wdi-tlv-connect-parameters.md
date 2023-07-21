---
title: WDI_TLV_CONNECT_PARAMETERS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_CONNECT_PARAMETERS is a WiFiCx TLV that contains parameters for OID_WDI_TASK_CONNECT and OID_WDI_TASK_ROAM.
ms.date: 07/21/2023
keywords:
 - WDI_TLV_CONNECT_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_CONNECT\_PARAMETERS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

WDI\_TLV\_CONNECT\_PARAMETERS is a TLV that contains parameters for [OID\_WDI\_TASK\_CONNECT](./oid-wdi-task-connect.md) and [OID\_WDI\_TASK\_ROAM](./oid-wdi-task-roam.md).

## TLV Type

0x33

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- |
| [**WDI\_TLV\_CONNECTION\_SETTINGS**](wdi-tlv-connection-settings.md) |   |   | The settings for the connection. |
| [**WDI\_TLV\_SSID**](wdi-tlv-ssid.md) | X |   | List of SSIDs that the port is allowed to connect to. |
| [**WDI\_TLV\_HESSID_INFO**](wdi-tlv-hessid-info.md) |   | X | List of HESSIDs that the port is allowed to connect to. This is an additional requirement to the SSID list. |
| [**WDI\_TLV\_AUTH\_ALGO\_LIST**](wdi-tlv-auth-algo-list.md) |   |   | The list of authentication algorithms that the connection can use. |
| [**WDI\_TLV\_MULTICAST\_CIPHER\_ALGO\_LIST**](wdi-tlv-multicast-cipher-algo-list.md) |   |   | The list of multicast cipher algorithms that the connection can use. |
| [**WDI\_TLV\_UNICAST\_CIPHER\_ALGO\_LIST**](wdi-tlv-unicast-cipher-algo-list.md) |   |   | The list of unicast cipher algorithms that the connection can use. |
| [**WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES**](wdi-tlv-extra-association-request-ies.md) |   | X | The IE blobs that must be included in the association requests sent by the port. This is applicable to any BSSID that the device would associate with. It should be used in addition to the BSSID specific IEs. |
| [**WDI\_TLV\_PHY\_TYPE\_LIST**](wdi-tlv-phy-type-list.md) |   | X | The list of PHYs that are allowed to be used for the association. If not specified, any supported PHY can be used. If specified, the device must only use the listed PHYs. |
| [**WDI\_TLV\_DISALLOWED\_BSSIDS\_LIST**](wdi-tlv-disallowed-bssids-list.md) |   | X | The list of BSSIDs that are not allowed to be used for association. If specified, the adapter must not associate to any AP that is in this list. |
| [**WDI\_TLV\_ALLOWED\_BSSIDS\_LIST**](wdi-tlv-allowed-bssids-list.md) |   | X | The list of BSSIDs that are allowed to be used for association. If WDI specifies 255.255.255.255 then all BSSIDs are allowed. |
| [**WDI\_TLV\_OWE\_DH\_IE**](wdi-tlv-owe-dh-ie.md) |   | X | Diffie-Hellman Extension IE blob that must be included in the association request sent by the station when auth type is OWE. This is applicable to any BSSID that the device would associate with and should be included in addition to the other associated req vendor IEs. |
| [**WDI_TLV_UNAVAILABLE_BAND_LIST**](wdi-tlv-unavailable-band-list.md) |   | X | The list of bands on which the driver should not connect as they are used for Primary Sta connectivity. |
| [**WDI_TLV_RSNA_AKM_SUITE**](wdi-tlv-rsna-akm-suite.md) |   | X | The list of RSNA AKMs that the driver supports. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
