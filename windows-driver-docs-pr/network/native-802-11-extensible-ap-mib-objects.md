---
title: Native 802.11 Extensible AP MIB objects
description: This section describes Native 802.11 Extensible AP MIB objects
keywords: ["Native 802.11 Extensible AP MIB objects", "Native 802.11 WLAN Extensible AP MIB objects", "WDK Native 802.11 Extensible AP MIB objects"]
ms.assetid: 6F80AF71-1CC0-44ED-AD91-DF8814190562
ms.author: windowsdriverdev
ms.date: 04/25/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Extensible AP MIB objects

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

Some of the Extensible Access Point (ExtAP) object identifiers (OIDs) are used to reference Extensible AP management information base (MIB) objects.

ExtAP objects are attributes of the IEEE 802.11 media access control (MAC) layer. The miniport driver must set these MIB objects to their default values whenever any of the following occur:

- The miniport driver's [MiniportInitializeEx](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.
- A method request of [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) is made to reset the MAC layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11_RESET_REQUEST structure is **TRUE**.

The following table lists the ExtAP OID name and the corresponding ExtAP MIB object name. For more information about an ExtAP MIB object, refer to the topic for the specific ExtAP OID.

| ExtAP OID name                                                                                     | Extensible AP MIB object name |
|---                                                                                                 |---                            |
| [OID_DOT11_ADDITIONAL_IE](https://msdn.microsoft.com/library/windows/hardware/ff569103)            | msDot11AdditionalIEs          |
| [OID_DOT11_AVAILABLE_CHANNEL_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569107)   | msDot11AvailableChannelList   |
| [OID_DOT11_AVAILABLE_FREQUENCY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569108) | msDot11AvailableFrequencyList |
| [OID_DOT11_WPS_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569436)              | msDot11WpsEnabled             |

Unless an ExtAP MIB object defines a specific default value, the Native 802.11 miniport driver defines its own default value for the MIB object.

>[!NOTE]
> When the miniport driver receives an [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) method request the miniport driver must reset an ExtAP MIB object to its default value under the following conditions:
   - When MIB values for the MAC and/or PHY are reset to their default values only if **bSetDefaultMIB** is set to **TRUE**. 
   - When MAC or PHY values are affected by the value of the **dot11ResetType** member. 
> For more information, refer to the topic for the specific ExtAP OID.

