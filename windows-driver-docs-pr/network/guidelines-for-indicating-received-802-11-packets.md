---
title: Guidelines for Indicating Received 802.11 Packets
description: Guidelines for Indicating Received 802.11 Packets
ms.assetid: e5a8106a-7838-4b2a-9100-630e77361b7d
keywords:
- indicating received packets WDK Native 802.11
- received packet indications WDK Native 802.11
- indications WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Guidelines for Indicating Received 802.11 Packets


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

In general, the Native 802.11 miniport driver indicates received packets similar to the process described in [Receiving Network Data](receiving-network-data.md). This section describes the additional requirements for indicating received 802.11 packets by a Native 802.11 miniport driver.

Before calling [**NdisMIndicateReceiveNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff563598) to indicate received 802.11 packet data, the miniport driver must do the following:

-   Allocate a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure for the received 802.11 packet. Each **NET\_BUFFER\_LIST** structure must include out-of-band (OOB) data. For more information about the OOB data, see [Media-Specific OOB Data for Received 802.11 Packets](media-specific-oob-data-for-received-802-11-packets.md).

-   Allocate one or more [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures for the packet data fragments. Each **NET\_BUFFER** structure specifies a buffer allocated by the miniport driver. All **NET\_BUFFER** structures that comprise the received packet data must be linked together, with the first **NET\_BUFFER** structure added to the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

    For management service data unit (MSDU) packets, the first [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure must specify a buffer that contains the 802.11 media access control (MAC), IEEE LLC/SNP, and EtherType data.

    For management media protocol data unit (MMPDU) frames, the miniport driver must allocate and link only one [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structure to the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure.

The type of 802.11 packet that the miniport driver indicates is dependent upon the current packet filter. Although the 802.11 station can receive certain types of 802.11 packets, such as MMPDU packets, the miniport driver must indicate the packet only if the corresponding packet filter is enabled. For more information about 802.11 packet filters, see [OID\_GEN\_CURRENT\_PACKET\_FILTER](https://msdn.microsoft.com/library/windows/hardware/ff569575).

Depending upon the current packet filter, the miniport driver indicates the following types of 802.11 packets:

-   Media access control (MAC) service data unit (MSDU) packets, which the 802.11 station has decrypted and reassembled from one or more MAC protocol data unit (MPDU) fragments. In this case, the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) contains only one [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376), because the MSDU packets were reassembled.

-   MAC management protocol data unit (MMPDU) packets, which the 802.11 station has decrypted and reassembled from one or more MPDU fragments. In this case, the [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) contains only one [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376), because the MPDU packets were reassembled.

-   802.11 Control frames.

-   Individual MPDU fragments if raw packet indications are enabled. For more information about raw packet indications, see [Indicating Raw 802.11 Packets](indicating-raw-802-11-packets.md).

**Note**  An 802.11 station operating in [Extensible Station Mode](extensible-station-operation-mode.md) indicates undecrypted MSDU packets when safe mode is enabled. In this case, the MSDU may consist of multiple MPDU fragments, each of which is contained in a [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) in the MSDU's [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388).

 

 

 





