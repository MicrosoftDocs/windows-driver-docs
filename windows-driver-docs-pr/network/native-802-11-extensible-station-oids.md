---
title: Native 802.11 Extensible Station OIDs
description: This section describes Native 802.11 Extensible Station OIDs and their characteristics.
keywords: ["Native 802.11 Extensible Station OIDs", "Native 802.11 WLAN Extensible Station OIDs", "WDK Native 802.11 Extensible Station OIDs", "Native 802.11 Extensible Station object identifiers"]
ms.assetid: 34851A43-112C-40B7-BFB6-42E559BD3956
ms.author: windowsdriverdev
ms.date: 04/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Extensible Station OIDs

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The Native 802.11 Extensible Station (ExtSTA) object identifiers (OIDs) are applicable to miniport drivers that support the Native 802.11 ExtSTA operation mode. For more information about the ExtSTA operation mode, see [Extensible Station Operation Mode](extensible-station-operation-mode.md).

In the following table, these abbreviations are used to specify the requirements for Native 802.11 ExtSTA OID query (Q), set (S), and NDIS 6.0 method (M) requests:

- R   
Indicates that support for the object is required. The miniport driver must not fail set or query requests for the object by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- C   
Indicates that support for the object is conditionally required for certain hardware or software functionality. If the 802.11 station supports the functionality, the miniport driver must support query or set requests for the object. Otherwise, the miniport driver must fail the set or query requests by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- O   
Indicates that support for the object is optional. The miniport driver can either support query or set requests for the object, or the driver can fail the request by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- X   
Indicates that the specified state of a Native 802.11 operating mode supports a set request for the object. If the miniport driver is not in the specified state, the miniport driver must fail the set request by returning NDIS_STATUS_INVALID_STATE from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. 

OIDs that support query requests can be queried from any state of the miniport driver's operation mode.

For more information about Native 802.11 operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md). For more information about Native 802.11 operating states, see [Native 802.11 Operating States](native-802-11-operating-states.md).

| Name                                                                                                                | Q | S | M | ExtSTA INIT| ExtSTA OP|
|---                                                                                                                  |---|---|---|---         |---       |
| [OID_DOT11_ACTIVE_PHY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569102)                           | R |   |   |            |          |
| [OID_DOT11_ASSOCIATION_PARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569104)                        |   | R |   | X          |          |
| [OID_DOT11_AUTO_CONFIG_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569106)                       | R | R |   | X          |          |
| [OID_DOT11_CIPHER_DEFAULT_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569119)                        |   | C |   | X          | X        |
| [OID_DOT11_CIPHER_DEFAULT_KEY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569120)                     | C | C |   | X          | X        |
| [OID_DOT11_CIPHER_KEY_MAPPING_KEY](https://msdn.microsoft.com/library/windows/hardware/ff569121)                    |   | R |   | X          | X        |
| [OID_DOT11_CONNECT_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569122)                           |   | R |   | X          |          |
| [OID_DOT11_CURRENT_PHY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135)                            | R | R |   | X          | X        |
| [OID_DOT11_DESIRED_BSS_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569142)                          | R | R |   | X          |          |
| [OID_DOT11_DESIRED_BSSID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569141)                        | R | R |   | X          |          |
| [OID_DOT11_DESIRED_COUNTRY_OR_REGION_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569143)          | C | C |   | X          |          |
| [OID_DOT11_DESIRED_PHY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144)                          | R | R |   | X          |          |
| [OID_DOT11_DESIRED_SSID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569145)                         | R | R |   | X          |          |
| [OID_DOT11_DISCONNECT_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569147)                        |   | R |   |            | X        |
| [OID_DOT11_ENABLED_AUTHENTICATION_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569356)          | R | R |   | X          |          |
| [OID_DOT11_ENABLED_MULTICAST_CARRIER_CIPHER_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569357)| C | C |   | X          |          |
| [OID_DOT11_ENABLED_UNICAST_CARRIER_CIPHER_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569358)  | C | C |   | X          |          |
| [OID_DOT11_ENUM_ASSOCIATION_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569359)                     | R |   |   |            |          |
| [OID_DOT11_ENUM_BSS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569360)                             |   |   | R |            |          |
| [OID_DOT11_EXCLUDE_UNENCRYPTED](https://msdn.microsoft.com/library/windows/hardware/ff569365)                       | C | C |   | X          |          |
| [OID_DOT11_EXCLUDED_MAC_ADDRESS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569364)                 | R | R |   | X          | X        |
| [OID_DOT11_EXTSTA_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569366)                         | O |   |   |            |          |
| [OID_DOT11_FLUSH_BSS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569367)                            |   | R |   | X          |          |
| [OID_DOT11_HARDWARE_PHY_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569370)                        | O |   |   |            |          |
| [OID_DOT11_HIDDEN_NETWORK_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569371)                    | R | R |   | X          |          |
| [OID_DOT11_IBSS_PARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569378)                               | R | R |   | X          |          |
| [OID_DOT11_MEDIA_STREAMING_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569386)                   | R | R |   | X          | X        |
| [OID_DOT11_PMKID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569400)                                | C | C |   | X          | X        |
| [OID_DOT11_PORT_STATE_NOTIFICATION](https://msdn.microsoft.com/library/windows/hardware/ff569401)                   |   | O |   |            | X        |
| [OID_DOT11_POWER_MGMT_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569402)                        | R | R |   | X          | X        |
| [OID_DOT11_PRIVACY_EXEMPTION_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569404)                    | C | C |   | X          |          |
| [OID_DOT11_QOS_PARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569405)                                | C | C |   | X          |          |
| [OID_DOT11_SAFE_MODE_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569412)                         | R | R |   | X          |          |
| [OID_DOT11_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420)                                | R |   |   |            |          |
| [OID_DOT11_SUPPORTED_COUNTRY_OR_REGION_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569421)        | O |   |   |            |          |
| [OID_DOT11_SUPPORTED_MULTICAST_ALGORITHM_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569424)        | O |   |   |            |          |
| [OID_DOT11_SUPPORTED_UNICAST_ALGORITHM_PAIR](https://msdn.microsoft.com/library/windows/hardware/ff569430)          | O |   |   |            |          |
| [OID_DOT11_UNICAST_USE_GROUP_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569433)                 | C | C |   | X          |          |
| [OID_DOT11_UNREACHABLE_DETECTION_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569434)           | R | R |   | X          | X        |

Some of the ExtSTA OIDs are used to reference IEEE 802.11 management information base (MIB) objects. The following table lists the ExtSTA OID name, the corresponding IEEE 802.11 MIB object name, and the IEEE 802.11 standard that defines the MIB object. For more information about an MIB object, refer to Annex D of the specified IEEE 802.11 Standard.

| ExtSTA OID name                                                                                 | IEEE 802.11 MIB object name | IEEE 802.11 standard |
|---                                                                                              |---                          |---                   |
| [OID_DOT11_CIPHER_DEFAULT_KEY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569120) | dot11DefaultKeyID           | IEEE 802.11-2012     |
| [OID_DOT11_DESIRED_BSS_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569142)      | dot11DesiredBSSType         | IEEE 802.11-2012     |
| [OID_DOT11_EXCLUDE_UNENCRYPTED](https://msdn.microsoft.com/library/windows/hardware/ff569365)   | dot11ExcludeUnencrypted     | IEEE 802.11-2012     |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")