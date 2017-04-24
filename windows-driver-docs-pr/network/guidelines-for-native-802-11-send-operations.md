---
title: Guidelines for Native 802.11 Send Operations
description: Guidelines for Native 802.11 Send Operations
ms.assetid: 1526f484-2bd6-4fa4-b3e6-a07b25d0bf28
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Guidelines for Native 802.11 Send Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function is called, the *NetBufferLists* parameter is a pointer to a list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures. Each **NET\_BUFFER\_LIST** structure contains a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure that contains the 802.11 packet data.

Each 802.11 packet referenced by a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure is one of the following packet types:

-   Media access control (MAC) service data unit (MSDU) packet.

-   MAC management protocol data unit (MMPDU) packet.

When sending the 802.11 packet specified through the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, the 802.11 station must follow the procedures defined in the IEEE 802.11-2012 standard. The miniport driver and 802.11 station must also follow these guidelines:

-   The miniport driver must first access the media-specific parameters within the out-of-band (OOB) data of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. The driver accesses this OOB data through a pointer to a [**DOT11\_EXTSTA\_SEND\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548632) structure. For more information about the OOB data, see [Media-Specific OOB Data for Native 802.11 Send Operations](media-specific-oob-data-for-native-802-11-send-operations.md).

-   If the length of the 802.11 packet does not exceed the value of the IEEE 802.11 **dot11FragmentationThreshold** management information block (MIB) object, the 802.11 packet consists of a single MAC protocol data unit (MPDU) frame and does not require fragmentation.

    If the length of the 802.11 packet does exceed the value of the **dot11FragmentationThreshold** MIB object, the 802.11 station must fragment the 802.11 packet into multiple MPDU frames. Each MPDU frame must contain a copy of the 802.11 MAC header, which is accessed through the [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure of the 802.11 packet.

    For more information about the **dot11FragmentationThreshold** MIB object, see [OID\_DOT11\_FRAGMENTATION\_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569368).

-   The 802.11 station must set the fields within the 802.11 MAC header that the station is responsible for. The 802.11 station must do this for each MPDU frame of the 802.11 packet. For more information about the 802.11 MAC header, see [802.11 MAC Header Management](802-11-mac-header-management.md).

-   If the 802.11 station supports wireless Quality of Service (QoS) extensions not supported by the operating system, the station must add the appropriate QoS Control field to the MAC header. For more information about this, see [Extending Packet Data During Send Operations](extending-packet-data-during-send-operations.md).

-   If the 802.11 station supports IEEE 802.1p packet prioritization or 802.1Q virtual LAN (VLAN), the station must add the 802.1Q/p tag header after the 802.11 MAC and IEEE LLC/SNAP headers. The miniport driver returns its support for 802.1Q/p when queried by [OID\_GEN\_MAC\_OPTIONS](https://msdn.microsoft.com/library/windows/hardware/ff569597).

    The miniport driver accesses the data used for the 802.1Q/p tag header through the [**NDIS\_NET\_BUFFER\_LIST\_8021Q\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff566565) structure, which is referenced within a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure by calling the [**NET\_BUFFER\_LIST\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568401) macro with the **Ieee8021QNetBufferListInfo** identifier.

    For more information about the 802.1Q/p tag header, refer to Clause 9 of the IEEE 802.1Q-1998 standard.

-   If the 802.11 station is enabled for cipher operations, it must encrypt every MPDU frame of the 802.11 packet unless the **usExemptionActionType** member of the [**DOT11\_EXTSTA\_SEND\_CONTEXT**](https://msdn.microsoft.com/library/windows/hardware/ff548632) structure exempts the packet from encryption.

    When encrypting the MPDU payload, the 802.11 station must follow the guidelines defined in [Extensible Station Cipher Operations](extensible-station-cipher-operations.md).

 

 





