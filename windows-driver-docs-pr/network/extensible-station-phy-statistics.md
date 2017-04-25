---
title: Extensible Station PHY Statistics
description: Extensible Station PHY Statistics
ms.assetid: ee4a9a5c-4b0e-4e1e-a8f2-94edac7610cb
keywords:
- ExtSTA mode WDK Native 802.11
- Extensible Station PHY statistics WDK Native 802.11
- PHY statistics WDK Native 802.11
- physical layer statistics WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Extensible Station PHY Statistics


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Physical layer (PHY) statistics are based on the number of packets and frames sent or received by the IEEE PHY layer of the 802.11 station, including:

-   Media access control (MAC) service data unit (MSDU) packets.

-   MAC management protocol data unit (MMPDU) frames.

-   MAC protocol data unit (MPDU) frames. Each MSDU packet or MMPDU frame consists of one or more MPDU frames sent or received by the 802.11 station.

When the [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420) object identifier (OID) is queried, the miniport driver returns the PHYstatistics through the [**DOT11\_PHY\_FRAME\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548733) structure. This structure contains various PHY statistical counters, including:

-   Total number of all MSDU packets and MPDU/MMPDU frames sent or received successfully by the PHY.

-   Total number of only multicast or broadcast MSDU packets and MPDU/MMPDU frames sent or received successfully by the PHY.

-   Total number of MPDU frames sent or received successfully by the PHY. These counters are incremented for each MPDU fragment sent or received of an MSDU packet or MMPDU frame.

-   Total number of received MPDU frames that were rejected by the PHY due to a duplicate sequence number in the 802.11 MAC header or incorrect frame check sequence (FCS) value in the MPDU frame.

The Native 802.11 miniport driver maintains separate sets of DOT11\_PHY\_FRAME\_STATISTICS structures for each PHY supported by the 802.11 station.

When the [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420) OID is queried, the miniport driver returns a list of [**DOT11\_PHY\_FRAME\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548733) structures through the **PhyCounters** member of the [**DOT11\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548779) structure. The miniport driver must sort this list of PHY statistics in the same order as the list of PHY types previously returned by the driver through a query request of [OID\_DOT11\_SUPPORTED\_PHY\_TYPES](https://msdn.microsoft.com/library/windows/hardware/ff569426).

For example, the following table shows the correct way of returning the list of [**DOT11\_PHY\_FRAME\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548733) structures for an 802.11 station that supports a direct-sequence spread spectrum (DSSS) PHY (**dot11\_phy\_type\_dsss**) and an orthogonal frequency division multiplexing (OFDM) PHY ( **dot11\_phy\_type\_ofdm)**.

List of PHY types
List of PHY statistics
Index
PHY type
Index
PHY statistics
0

**dot11\_phy\_type\_dsss**

0

Statistics for DSSS PHY

1

**dot11\_phy\_type\_ofdm**

1

Statistics for OFDM PHY

 

 

 





