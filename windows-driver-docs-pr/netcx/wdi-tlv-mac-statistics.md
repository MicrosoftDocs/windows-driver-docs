---
title: WDI_TLV_MAC_STATISTICS (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_MAC_STATISTICS is a WiFiCx TLV that contains per-peer MAC statistics for OID_WDI_GET_STATISTICS.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_MAC_STATISTICS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_MAC\_STATISTICS (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_MAC\_STATISTICS is a TLV that contains per-peer MAC statistics for [OID\_WDI\_GET\_STATISTICS](./oid-wdi-get-statistics.md).

## TLV Type


0xA6

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values

|Type|Description|
|--- |--- |
|[**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address)|The MAC address of the peer that these counts are set for. For multicast and broadcast packets, this value is set to FF-FF-FF-FF-FF-FF-FF.|
|UINT64|The number of MSDU packets and MMPDU frames that the IEEE MAC layer of the 802.11 station successfully transmitted.|
|UINT64|The number of MSDU packets and MMPDU frames that the IEEE MAC layer of the 802.11 station successfully received. This member should not be incremented for received packets that failed cipher decryption or MIC validation.|
|UINT64|The number of unencrypted received MPDU frames that the MAC layer discarded when the IEEE 802.11 dot11ExcludeUnencrypted management information base (MIB) object is enabled. MPDU frames are considered unencrypted when the Protected Frame subfield of the Frame Control field in the IEEE 802.11 MAC header is set to zero.|
|UINT64|The number of received MSDU packets that the 802.11 station discarded because of MIC failures.|
|UINT64|The number of received MPDU frames that the 802.11 station discarded because of the TKIP replay protection procedure.|
|UINT64|The number of encrypted MPDU frames that the 802.11 station failed to decrypt because of a TKIP ICV error.|
|UINT64|The number of received MPDU frames that the 802.11 discarded because of an invalid AES-CCMP format.|
|UINT64|The number of received MPDU frames that the 802.11 station discarded because of the AES-CCMP replay protection procedure.|
|UINT64|The number of received MPDU frames that the 802.11 station discarded because of errors detected by the AES-CCMP decryption algorithm.|
|UINT64|The number of encrypted MPDU frames received for which a WEP decryption key was not available on the 802.11 station.|
|UINT64|The number of encrypted MPDU frames that the 802.11 station failed to decrypt because of a WEP ICV error.|
|UINT64|The number of received encrypted packets that the 802.11 station successfully decrypted. For the WEP and TKIP cipher algorithms, the port must increment this counter for each received encrypted MPDU that was successfully decrypted. For the AES-CCMP cipher algorithm, the port must increment this counter on each received encrypted MSDU packet that was successfully decrypted.|
|UINT64|The number of encrypted packets that the 802.11 station failed to decrypt. For the WEP and TKIP cipher algorithms, the port must increment this counter for each received encrypted MPDU that was not successfully decrypted. For the AES-CCMP cipher algorithm, the port must increment this counter on each received encrypted MSDU packet that was not successfully decrypted. The port must not increment this counter for packets that are decrypted successfully, but are discarded for other reasons. For example, the port must not increment this counter for packets that are discarded because of TKIP MIC failures or TKIP/CCMP replays.| 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

