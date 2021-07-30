---
title: WDI_TLV_PHY_STATISTICS (dot11wificxtypes.h)
description: WDI_TLV_PHY_STATISTICS is a WiFiCx TLV that contains per-PHY statistics for OID_WDI_GET_STATISTICS.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_PHY_STATISTICS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_PHY\_STATISTICS (dot11wificxtypes.h)


WDI\_TLV\_PHY\_STATISTICS is a TLV that contains per-PHY statistics for [OID\_WDI\_GET\_STATISTICS](./oid-wdi-get-statistics.md).

## TLV Type


0xA7

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


|Type|Description|
|--- |--- |
|[**WDI_PHY_TYPE**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_phy_type)|The type for this PHY.|
|UINT64|The number of MSDU packets and MMPDU frames that the IEEE PHY layer of the 802.11 station has successfully transmitted.|
|UINT64|The number of multicast or broadcast MSDU packets and MMPDU frames that the IEEE PHY layer of the 802.11 station has successfully transmitted.|
|UINT64|The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit after exceeding the retry limits defined by the 802.11 IEEE dot11ShortRetryLimit or dot11LongRetryLimit MIB counters.|
|UINT64|The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after one or more attempts.|
|UINT64|The number of MSDU packets and MMPDU frames that the 802.11 station successfully transmitted after more than one retransmission attempts. For MSDU packets, the port must increment this counter for each packet that was transmitted successfully after one or more of its MPDU fragments required retransmission.|
|UINT64|The number of MSDU packets and MMPDU frames that the 802.11 station failed to transmit because of a timeout as defined by the IEEE 802.11 dot11MaxTransmitMSDULifetime MIB object.|
|UINT64|The number of MPDU frames that the 802.11 station transmitted and acknowledged through a received 802.11 ACK frame.|
|UINT64|The number of times that the 802.11 station received a Clear To Send (CTS) frame in response to a Request To Send (RTS) frame. If this cannot be maintained per port, it can be maintained per channel.|
|UINT64|The number of times that the 802.11 station did not receive a CTS frame in response to an RTS frame. If this cannot be maintained per port, it can be maintained per channel.|
|UINT64|The number of times that the 802.11 station expected and did not receive an Acknowledgment (ACK) frame. If this cannot be maintained per port, it can be maintained per channel.|
|UINT64|The number of MSDU packets and MMPDU frames that the 802.11 station has successfully received. For MSDU packets, the port must increment this counter for each packet whose MPDU fragments were received and passed frame check sequence (FCS) verification and replay detection. The port must increment this member regardless of whether the received MSDU packet or MPDU fragment fail MAC-layer cipher decryption.|
|UINT64|The number of multicast or broadcast MSDU packets and MMPDU frames that the 802.11 station has successfully received. For MSDU packets, the port must increment this counter for each packet whose MPDU fragments were received and passed FCS verification and replay detection. The port must increment this member regardless of whether the received MSDU packet or MPDU fragment fail MAC-layer cipher decryption.|
|UINT64|The number of MSDU packets or MMPDU frames received by the 802.11 station when a promiscuous packet filter is enabled. If this cannot be maintained per port, it can be maintained per channel.|
|UINT64|The number if MSDU packets and MMPDU frames that the 802.11 station discarded because of a timeout as defined by the IEEE 802.11 dot11MaxReceiveLifetime MIB object. If this cannot be maintained per port, it can be maintained per channel.|
|UINT64|The number of duplicate MPDU frames that the 802.11 station received. The 802.11 station determines duplicate frames through the Sequence Control field of the 802.11 MAC header. If this cannot be maintained per port, it can be maintained per channel.|
|UINT64|The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames.|
|UINT64|The number of MPDU frames received by the 802.11 station for MSDU packets or MMPDU frames when a promiscuous packet filter was enabled.|
|UINT64|The number of MPDU frames that the 802.11 station received with FCS errors. If this cannot be maintained per port, it can be maintained per channel.|

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

