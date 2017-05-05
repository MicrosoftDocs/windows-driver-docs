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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")