---
title: Native 802.11 Send Operations
description: Native 802.11 Send Operations
ms.assetid: 8ab93080-7ac1-4f3c-b4ce-01e7a9767151
keywords:
- send operations WDK Native 802.11
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Send Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

When the miniport driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function is called, the network data referenced through the *NetBufferLists* parameter are one of the following 802.11 packet types:

-   Media access control (MAC) service data unit (MSDU) packets.

-   MAC management protocol data unit (MMPDU) packets.

For more information about the frame format for these 802.11 packets, refer to Clause 8.2 of the IEEE 802.11-2012 standard.

Each transmitted 802.11 packet contains:

-   An 802.11 media access control (MAC) header. The operating system sets some of the fields within the MAC header while the 802.11 station sets other fields. For more information about the 802.11 MAC header, see [802.11 MAC Header Management](802-11-mac-header-management.md).

-   An 802.11 Frame Body field. For MSDU data packets, the Frame Body field contains the unencrypted protocol data unit (PDU) payload data. If necessary, the operating system encapsulates the PDU payload using the procedure described in [802.11 Payload Encapsulation](802-11-payload-encapsulation.md).

    If the miniport driver needs to extend and add fields to either the 802.11 MAC header or packet payload, the miniport driver must follow the guidelines described in [Extending Packet Data During Send Operations](extending-packet-data-during-send-operations.md).

-   Media-specific out-of-band (OOB) data referenced through the **NetBufferListInfo** member of the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure. The OOB data specifies transmit parameters used by the 802.11 station when sending the MSDU packet. For more information about the OOB data, see [Media-Specific OOB Data for Native 802.11 Send Operations](media-specific-oob-data-for-native-802-11-send-operations.md).

For more information about the methods used by the 802.11 station when performing a send operation, see [Guidelines for Native 802.11 Send Operations](guidelines-for-native-802-11-send-operations.md).

For more information about the methods used by the miniport driver to send packets, see [Miniport Driver Send and Receive Operations](miniport-driver-send-and-receive-operations.md).

**Note**  If the miniport driver is operating in Network Monitor (NetMon) mode, it must not transmit any packets. This includes packets originated by the driver or 802.11 station, or resulting from a call to the driver's [*MiniportSendNetBufferLists*](https://msdn.microsoft.com/library/windows/hardware/ff559440) function.

 

 

 





