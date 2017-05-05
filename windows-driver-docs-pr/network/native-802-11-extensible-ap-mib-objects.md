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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")