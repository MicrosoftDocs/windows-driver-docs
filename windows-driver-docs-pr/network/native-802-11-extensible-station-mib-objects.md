---
title: Native 802.11 Extensible Station MIB objects
description: This section describes Native 802.11 Extensible Station MIB objects
keywords: ["Native 802.11 Extensible Station MIB objects", "Native 802.11 WLAN Extensible Station MIB objects", "WDK Native 802.11 Extensible Station MIB objects"]
ms.assetid: CAEB8DD4-9A81-4CF6-9C7D-6AD31CB466DE
ms.author: windowsdriverdev
ms.date: 04/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Extensible Station MIB objects

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

Some of the Extensible Station (ExtSTA) object identifiers (OIDs) are used to reference Extensible Station management information base (MIB) objects.

ExtSTA objects are attributes of the IEEE 802.11 media access control (MAC) layer. The miniport driver must set these MIB objects to their default values whenever any of the following occur:

- The miniport driver's [MiniportInitializeEx](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.
- A method request of [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11_RESET_REQUEST structure is **TRUE**.

The following table lists the ExtSTA OID name and the corresponding ExtSTA MIB object name. For more information about an ExtSTA MIB object, refer to the topic for the specific ExtSTA OID.

| ExtSTA OID name                                                                                                 | Extensible Station MIB object name |
|---                                                                                                                   |---                            |
| [OID_DOT11_ACTIVE_PHY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569102)                            | msDot11ActivePhyList          |
| [OID_DOT11_AUTO_CONFIG_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569106)                        | msDot11AutoConfigEnabled      |
| [OID_DOT11_CURRENT_PHY_ID](https://msdn.microsoft.com/library/windows/hardware/ff569135)                             | msDot11msDot11CurrentPhyID    |
| [OID_DOT11_DESIRED_BSSID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569141)                         | msDot11DesiredBSSIDList       |
| [OID_DOT11_DESIRED_COUNTRY_OR_REGION_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569143)        | msDot11DesiredCountryOrRegionString |
| [OID_DOT11_DESIRED_PHY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569144)                           | msDot11DesiredPhyList         |
| [OID_DOT11_DESIRED_SSID_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569145)                          | msDot11DesiredSSIDList        |
| [OID_DOT11_HIDDEN_NETWORK_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569371)                     | msDot11HiddenNetworkEnabled   |
| [OID_DOT11_ENABLED_AUTHENTICATION_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569356)           | msDot11EnabledAuthAlgo        |
| [OID_DOT11_ENABLED_MULTICAST_CARRIER_CIPHER_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569357)| msDot11EnabledMulticastCipherAlgo |
| [OID_DOT11_ENABLED_UNICAST_CARRIER_CIPHER_ALGORITHM](https://msdn.microsoft.com/library/windows/hardware/ff569358)   | msDot11EnabledUnicastCipherAlgo |
| [OID_DOT11_EXCLUDED_MAC_ADDRESS_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569364)                  | msDot11ExcludedMacAddressList |
| [OID_DOT11_HARDWARE_PHY_STATE](https://msdn.microsoft.com/library/windows/hardware/ff569370)                         | msDot11HardwarePHYState       |
| [OID_DOT11_MEDIA_STREAMING_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569386)                    | msDot11MediaStreamingEnabled  |
| [OID_DOT11_POWER_MGMT_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569402)                         | msDot11PowerSavingLevel       |
| [OID_DOT11_PRIVACY_EXEMPTION_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569404)                     | msDot11PrivacyExemptionList   |
| [OID_DOT11_QOS_PARAMS](https://msdn.microsoft.com/library/windows/hardware/ff569405)                                 | msDot11QoSParams              |
| [OID_DOT11_SAFE_MODE_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569412)                          | msDot11SafeModeEnabled        |
| [OID_DOT11_UNICAST_USE_GROUP_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569433)                  | msDot11UnicastUseGroupEnabled |
| [OID_DOT11_UNREACHABLE_DETECTION_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569434)        | msDot11UnreachableDetectionThreshold |

Unless an ExtSTA MIB object defines a specific default value, the Native 802.11 miniport driver defines its own default value for the MIB object.

>[!NOTE]
> When the miniport driver receives an [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) method request, the miniport driver must reset an ExtSTA MIB object to its default value under the following conditions:
   - When MIB values for the MAC and/or PHY are reset to their default values only if **bSetDefaultMIB** is set to **TRUE**. 
   - When MAC or PHY values are affected by the value of the **dot11ResetType** member. 
> For more information, refer to the topic for the specific ExtSTA OID.

