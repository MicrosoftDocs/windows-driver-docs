---
title: Extensible Station MAC Statistics
description: Extensible Station MAC Statistics
ms.assetid: 5810caf4-112f-465d-9326-b71a3439b6c5
keywords: ["ExtSTA mode WDK Native 802.11", "Extensible Station MAC statistics WDK Native 802.11", "MAC statistics WDK Native 802.11", "media access control statistics WDK Native 802.11"]
---

# Extensible Station MAC Statistics


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Media access control (MAC) statistics are based on the number of packets and frames sent or received by the IEEE MAC sublayer of the 802.11 station, including:

-   MAC service data unit (MSDU) packets.

-   MAC management protocol data unit (MMPDU) frames.

-   MAC protocol data unit (MPDU) frames. Each MSDU packet or MMPDU frame consists of one or more MPDU frames sent or received by the 802.11 station.

When the [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420) object identifier (OID) is queried, the miniport driver returns the MAC statistics through the [**DOT11\_MAC\_FRAME\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548684) structure. This structure contains various MAC statistical counters, including:

-   Total number of MSDU packets and MMPDU frames sent or received successfully by the MAC.

-   Total number of encrypted MPDU frames received by the MAC that were decrypted successfully.

-   Total number of encrypted MPDU frames received by the MAC that failed to decrypt successfully.

-   Separate counters for each cipher algorithm (such as wireless equivalency privacy (WEP) or AES-CCMP) supported by the 802.11 station. These counters record the numbers of received MPDU frames rejected by the cipher algorithm due to decryption failures or replay protection.

The Native 802.11 miniport driver maintains two sets of [**DOT11\_MAC\_FRAME\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548684) structures:

-   One set for unicast MSDU packets and MPDU/MMPDU frames sent or received by the MAC. When the [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420) OID is queried, the miniport driver returns this structure through the **MacUcastCounters** member of the [**DOT11\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548779) structure.

-   One set for multicast or broadcast MSDU packets and MPDU/MMPDU frames sent or received by the MAC. When the [OID\_DOT11\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569420) OID is queried, the miniport driver returns this structure through the **MacMcastCounters** member of the [**DOT11\_STATISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff548779) structure.

 

 





