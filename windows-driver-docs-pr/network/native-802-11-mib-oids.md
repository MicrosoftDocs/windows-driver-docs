---
title: Native 802.11 MIB OIDs
description: This section describes Native 802.11 MIB OIDs and their characteristics.
keywords: ["Native 802.11 MIB OIDs", "Native 802.11 WLAN MIB OIDs", "WDK Native 802.11 MIB OIDs", "Native 802.11 MIB object identifiers"]
ms.assetid: F1ADCBDB-5591-4CAF-9EDA-8B5FEDFE55B9
ms.author: windowsdriverdev
ms.date: 04/26/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 MIB OIDs

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

The Native 802.11 management information base (MIB) object identifiers (OIDs) query and set the IEEE 802.11 MIB objects that are supported by the miniport driver. These objects are applicable to miniport drivers that support any of the Native 802.11 operation modes. For more information about the Native 802.11 operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md).

In the following table, these abbreviations are used to specify the requirements for Native 802.11 MIB OID query (Q) and set (S) requests:

- R   
Indicates that support for the object is required. The miniport driver must not fail set or query requests for the object by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- C   
Indicates that support for the object is conditionally required for certain hardware or software functionality. If the 802.11 station supports the functionality, the miniport driver must support query or set requests for the object. Otherwise, the miniport driver must fail the set or query requests by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- O   
Indicates that support for the object is optional. The miniport driver can either support query or set requests for the object, or the driver can fail the request by returning NDIS_STATUS_NOT_SUPPORTED from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function.
- X   
Indicates that the specified state of a Native 802.11 operating mode supports a set request for the object. If the miniport driver is not in the specified state, the miniport driver must fail the set request by returning NDIS_STATUS_INVALID_STATE from its [MiniportOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559416) function. 

OIDs that support query requests can be queried from any state of the miniport driver's operation mode.

For more information about Native 802.11 operation modes, see [Native 802.11 Operation Modes](native-802-11-operation-modes.md). For more information about Native 802.11 operating states, see [Native 802.11 Operating States](native-802-11-operating-states.md).

| Name                                                                                                                | Q | S | ExtSTA INIT | ExtSTA OP |
|---                                                                                                                  |---|---|---          |---       |
| [OID_DOT11_BEACON_PERIOD](https://msdn.microsoft.com/library/windows/hardware/ff569109)                             | R | O | X           |          |
| [OID_DOT11_CCA_MODE_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569110)                        | O |   |             |          |
| [OID_DOT11_CCA_WATCHDOG_COUNT_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569112)                    | O |   |             |          |
| [OID_DOT11_CCA_WATCHDOG_COUNT_MIN](https://msdn.microsoft.com/library/windows/hardware/ff569113)                    | O |   |             |          |
| [OID_DOT11_CCA_WATCHDOG_TIMER_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569114)                    | O |   |             |          |
| [OID_DOT11_CCA_WATCHDOG_TIMER_MIN](https://msdn.microsoft.com/library/windows/hardware/ff569115)                    | O |   |             |          |
| [OID_DOT11_CF_POLLABLE](https://msdn.microsoft.com/library/windows/hardware/ff569116)                               | O |   |             |          |
| [OID_DOT11_CHANNEL_AGILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569117)                   | O |   |             |          |
| [OID_DOT11_CHANNEL_AGILITY_PRESENT](https://msdn.microsoft.com/library/windows/hardware/ff569118)                   | O |   |             |          |
| [OID_DOT11_COUNTRY_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569123)                            | C |   | X           |          |
| [OID_DOT11_CURRENT_CCA_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569126)                          | O |   |             |          |
| [OID_DOT11_CURRENT_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/ff569127)                           | C | C | X           |          |
| [OID_DOT11_CURRENT_CHANNEL_NUMBER](https://msdn.microsoft.com/library/windows/hardware/ff569128)                    | O |   |             |          |
| [OID_DOT11_CURRENT_DWELL_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569129)                        | O |   |             |          |
| [OID_DOT11_CURRENT_FREQUENCY](https://msdn.microsoft.com/library/windows/hardware/ff569130)                         | C | C | X           |          |
| [OID_DOT11_CURRENT_INDEX](https://msdn.microsoft.com/library/windows/hardware/ff569131)                             | O |   |             |          |
| [OID_DOT11_CURRENT_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569134)                           | O |   |             |          |
| [OID_DOT11_CURRENT_REG_DOMAIN](https://msdn.microsoft.com/library/windows/hardware/ff569136)                        | R |   |             |          |
| [OID_DOT11_CURRENT_SET](https://msdn.microsoft.com/library/windows/hardware/ff569137)                               | O |   |             |          |
| [OID_DOT11_CURRENT_TX_POWER_LEVEL](https://msdn.microsoft.com/library/windows/hardware/ff569138)                    | O |   |             |          |
| [OID_DOT11_DIVERSITY_SELECTION_RX](https://msdn.microsoft.com/library/windows/hardware/ff569148)                    | O |   |             |          |
| [OID_DOT11_DIVERSITY_SUPPORT](https://msdn.microsoft.com/library/windows/hardware/ff569149)                         | O |   |             |          |
| [OID_DOT11_DSS_OFDM_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569150)                   | O |   |             |          |
| [OID_DOT11_DSS_OFDM_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569151)               | O |   |             |          |
| [OID_DOT11_DTIM_PERIOD](https://msdn.microsoft.com/library/windows/hardware/ff569152)                               | R | O |             |          |
| [OID_DOT11_ED_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569153)                              | O |   |             |          |
| [OID_DOT11_EHCC_CAPABILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569154)                   | O |   |             |          |
| [OID_DOT11_EHCC_CAPABILITY_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569155)               | O |   |             |          |
| [OID_DOT11_EHCC_NUMBER_OF_CHANNELS_FAMILY_INDEX](https://msdn.microsoft.com/library/windows/hardware/ff569156)      | O |   |             |          |
| [OID_DOT11_EHCC_PRIME_RADIX](https://msdn.microsoft.com/library/windows/hardware/ff569355)                          | O |   |             |          |
| [OID_DOT11_ERP_PBCC_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569362)                   | O |   |             |          |
| [OID_DOT11_ERP_PBCC_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569363)               | O |   |             |          |
| [OID_DOT11_FRAGMENTATION_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569368)                   | R | R | X           |          |
| [OID_DOT11_FREQUENCY_BANDS_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569369)                 | O |   |             |          |
| [OID_DOT11_HOP_ALGORITHM_ADOPTED](https://msdn.microsoft.com/library/windows/hardware/ff569373)                     | O |   |             |          |
| [OID_DOT11_HOP_MODULUS](https://msdn.microsoft.com/library/windows/hardware/ff569374)                               | O |   |             |          |
| [OID_DOT11_HOP_OFFSET](https://msdn.microsoft.com/library/windows/hardware/ff569375)                                | O |   |             |          |
| [OID_DOT11_HOP_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569376)                                  | O |   |             |          |
| [OID_DOT11_HOPPING_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569372)                           | O |   |             |          |
| [OID_DOT11_HR_CCA_MODE_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569377)                     | O |   |             |          |
| [OID_DOT11_LONG_RETRY_LIMIT](https://msdn.microsoft.com/library/windows/hardware/ff569380)                          | O |   |             |          |
| [OID_DOT11_MAC_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569381)                               | O |   |             |          |
| [OID_DOT11_MAX_DWELL_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569383)                            | O |   |             |          |
| [OID_DOT11_MAX_RECEIVE_LIFETIME](https://msdn.microsoft.com/library/windows/hardware/ff569384)                      | O |   |             |          |
| [OID_DOT11_MAX_TRANSMIT_MSDU_LIFETIME](https://msdn.microsoft.com/library/windows/hardware/ff569385)                | O |   |             |          |
| [OID_DOT11_MULTI_DOMAIN_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569389)                   | O |   |             |          |
| [OID_DOT11_MULTI_DOMAIN_CAPABILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569390)           | C | C | X           |          |
| [OID_DOT11_MULTI_DOMAIN_CAPABILITY_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569391)       | O |   |             |          |
| [OID_DOT11_NUMBER_OF_HOPPING_SETS](https://msdn.microsoft.com/library/windows/hardware/ff569394)                    | C |   |             |          |
| [OID_DOT11_OPERATIONAL_RATE_SET](https://msdn.microsoft.com/library/windows/hardware/ff569395)                      | R | R | X           |          |
| [OID_DOT11_PBCC_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569398)                   | O |   |             |          |
| [OID_DOT11_RANDOM_TABLE_FLAG](https://msdn.microsoft.com/library/windows/hardware/ff569406)                         | C |   |             |          |
| [OID_DOT11_REG_DOMAINS_SUPPORT_VALUE](https://msdn.microsoft.com/library/windows/hardware/ff569408)                 | R |   |             |          |
| [OID_DOT11_RTS_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569411)                             | R | R | X           | X        |
| [OID_DOT11_SHORT_PREAMBLE_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569414)         | O |   |             |          |
| [OID_DOT11_SHORT_RETRY_LIMIT](https://msdn.microsoft.com/library/windows/hardware/ff569415)                         | O |   |             |          |
| [OID_DOT11_SHORT_SLOT_TIME_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569416)            | O |   |             |          |
| [OID_DOT11_SHORT_SLOT_TIME_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569417)        | O |   |             |          |
| [OID_DOT11_STATION_ID](https://msdn.microsoft.com/library/windows/hardware/ff569419)                                | O |   |             |          |
| [OID_DOT11_SUPPORTED_DSSS_CHANNEL_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569423)               | O |   | X           | X        |
| [OID_DOT11_SUPPORTED_OFDM_FREQUENCY_LIST](https://msdn.microsoft.com/library/windows/hardware/ff569425)             | O |   | X           | X        |
| [OID_DOT11_TEMP_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569431)                                 | O |   |             |          |
| [OID_DOT11_TI_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569432)                              | O |   |             |          |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")