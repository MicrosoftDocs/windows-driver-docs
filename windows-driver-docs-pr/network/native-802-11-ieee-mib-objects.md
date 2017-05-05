---
title: Native 802.11 Operational MIB objects
description: This section describes Native 802.11 Operational MIB objects
keywords: ["Native 802.11 Operational MIB objects", "Native 802.11 WLAN Operational MIB objects", "WDK Native 802.11 Operational MIB objects"]
ms.assetid: 3D86500A-4D20-47D7-AD00-D0267B3CEB62
ms.author: windowsdriverdev
ms.date: 04/26/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Native 802.11 Operational MIB objects

>[!IMPORTANT]
> The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

Native 802.11 MIB OIDs are used to reference IEEE 802.11 management information base (MIB) objects.

The following table lists the Native 802.11 IEEE OID name, the corresponding IEEE 802.11 MIB object name, and the IEEE 802.11 standard that defines the MIB object. For more information about a MIB object, refer to Annex D of the specified IEEE 802.11 standard.

| Native 802.11 IEEE OID name                                                                      | IEEE 802.11 MIB object name | IEEE 802.11 standard |
|---                                                                                                             |---                |---               |
| [OID_DOT11_BEACON_PERIOD](https://msdn.microsoft.com/library/windows/hardware/ff569109) | dot11BeaconPeriod | IEEE 802.11-2012 |
| [OID_DOT11_CCA_MODE_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569110) | dot11CCAModeSupported | IEEE 802.11b-1999 |
| [OID_DOT11_CCA_WATCHDOG_COUNT_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569112) | dot11CCAWatchdogCountMax | IEEE 802.11-2012 |
| [OID_DOT11_CCA_WATCHDOG_COUNT_MIN](https://msdn.microsoft.com/library/windows/hardware/ff569113) | dot11CCAWatchdogCountMin | IEEE 802.11-2012 |
| [OID_DOT11_CCA_WATCHDOG_TIMER_MAX](https://msdn.microsoft.com/library/windows/hardware/ff569114) | dot11CCAWatchdogTimerMax | IEEE 802.11-2012 |
| [OID_DOT11_CCA_WATCHDOG_TIMER_MIN](https://msdn.microsoft.com/library/windows/hardware/ff569115) | dot11CCAWatchdogTimerMin | IEEE 802.11-2012 |
| [OID_DOT11_CF_POLLABLE](https://msdn.microsoft.com/library/windows/hardware/ff569116) | dot11CFPollable | IEEE 802.11-2012 |
| [OID_DOT11_CHANNEL_AGILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569117) | dot11ChannelAgilityEnabled | IEEE 802.11-1999/Corrigendum 1-2001 |
| [OID_DOT11_CHANNEL_AGILITY_PRESENT](https://msdn.microsoft.com/library/windows/hardware/ff569118) | dot11ChannelAgilityPresent | IEEE 802.11-1999/Corrigendum 1-2001 |
| [OID_DOT11_COUNTRY_STRING](https://msdn.microsoft.com/library/windows/hardware/ff569123) | dot11CountryString | IEEE 802.11d-2001 |
| [OID_DOT11_CURRENT_CCA_MODE](https://msdn.microsoft.com/library/windows/hardware/ff569126) | dot11CurrentCCAMode | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_CHANNEL](https://msdn.microsoft.com/library/windows/hardware/ff569127) | dot11CurrentChannel | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_CHANNEL_NUMBER](https://msdn.microsoft.com/library/windows/hardware/ff569128) | dot11CurrentChannelNumber | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_DWELL_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569129) | dot11CurrentDwellTime | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_FREQUENCY](https://msdn.microsoft.com/library/windows/hardware/ff569130) | dot11CurrentFrequency | IEEE 802.11a-1999 |
| [OID_DOT11_CURRENT_INDEX](https://msdn.microsoft.com/library/windows/hardware/ff569131) | dot11CurrentIndex | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569134) | dot11CurrentPattern | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_REG_DOMAIN](https://msdn.microsoft.com/library/windows/hardware/ff569136) | dot11CurrentRegDomain | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_SET](https://msdn.microsoft.com/library/windows/hardware/ff569137) | dot11CurrentSet | IEEE 802.11-2012 |
| [OID_DOT11_CURRENT_TX_POWER_LEVEL](https://msdn.microsoft.com/library/windows/hardware/ff569138) | dot11CurrentTxPowerLevel | IEEE 802.11-2012 |
| [OID_DOT11_DIVERSITY_SELECTION_RX](https://msdn.microsoft.com/library/windows/hardware/ff569148) | dot11DiversitySelectionRx | IEEE 802.11-2012 |
| [OID_DOT11_DIVERSITY_SUPPORT](https://msdn.microsoft.com/library/windows/hardware/ff569149) | dot11DiversitySupport | IEEE 802.11-2012 |
| [OID_DOT11_DSS_OFDM_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569150) | dot11DSSSOFDMOptionEnabled | IEEE 802.11g-2003 |
| [OID_DOT11_DSS_OFDM_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569151) | dot11DSSSOFDMOptionImplemented | IEEE 802.11g-2003 |
| [OID_DOT11_DTIM_PERIOD](https://msdn.microsoft.com/library/windows/hardware/ff569152) | dot11DTIMPeriod | IEEE 802.11-2012 |
| [OID_DOT11_ED_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569153) | dot11EDThreshold | IEEE 802.11-2012 |
| [OID_DOT11_EHCC_CAPABILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569154) | dot11EHCCCapabilityEnabled | IEEE 802.11d-2001 |
| [OID_DOT11_EHCC_CAPABILITY_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569155) | dot11EHCCCapabilityImplemented | IEEE 802.11d-2001 |
| [OID_DOT11_EHCC_NUMBER_OF_CHANNELS_FAMILY_INDEX](https://msdn.microsoft.com/library/windows/hardware/ff569156) | dot11EHCCNumberOfChannelsFamilyIndex | IEEE 802.11d-2001 | 
| [OID_DOT11_EHCC_PRIME_RADIX](https://msdn.microsoft.com/library/windows/hardware/ff569355) | dot11EHCCPrimeRadix | IEEE 802.11d-2001 | 
| [OID_DOT11_ERP_PBCC_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569362) | dot11ERPPBCCOptionEnabled | IEEE 802.11g-2003 |
| [OID_DOT11_ERP_PBCC_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569363) | dot11ERPPBCCOptionImplemented | IEEE 802.11g-2003 |
| [OID_DOT11_FRAGMENTATION_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569368) | dot11FragmentationThreshold | IEEE 802.11-2012 |
| [OID_DOT11_FREQUENCY_BANDS_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569369) | dot11FrequencyBandsSupported | IEEE 802.11a-1999 |
| [OID_DOT11_HOP_ALGORITHM_ADOPTED](https://msdn.microsoft.com/library/windows/hardware/ff569373) | dot11HopAlgorithmAdopted | IEEE 802.11d-2001 |
| [OID_DOT11_HOP_MODULUS](https://msdn.microsoft.com/library/windows/hardware/ff569374) | dot11HopModulus | IEEE 802.11d-2001 |
| [OID_DOT11_HOP_OFFSET](https://msdn.microsoft.com/library/windows/hardware/ff569375) | dot11HopOffset | IEEE 802.11d-2001 |
| [OID_DOT11_HOP_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569376) | dot11HopTime | IEEE 802.11-2012 |
| [OID_DOT11_HOPPING_PATTERN](https://msdn.microsoft.com/library/windows/hardware/ff569372) | dot11HoppingPatternEntry | IEEE 802.11d-2001 |
| [OID_DOT11_HR_CCA_MODE_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569377) | dot11HRCCAModeSupported | IEEE 802.11-2012/Corrigendum 1-2001 |
| [OID_DOT11_LONG_RETRY_LIMIT](https://msdn.microsoft.com/library/windows/hardware/ff569380) | dot11LongRetryLimit | IEEE 802.11-2012 |                
| [OID_DOT11_MAC_ADDRESS](https://msdn.microsoft.com/library/windows/hardware/ff569381) | dot11MACAddress | IEEE 802.11-2012 |
| [OID_DOT11_MAX_DWELL_TIME](https://msdn.microsoft.com/library/windows/hardware/ff569383) | dot11MaxDwellTime | IEEE 802.11-2012 |
| [OID_DOT11_MAX_RECEIVE_LIFETIME](https://msdn.microsoft.com/library/windows/hardware/ff569384) | dot11MaxReceiveLifetime | IEEE 802.11-2012 |
| [OID_DOT11_MAX_TRANSMIT_MSDU_LIFETIME](https://msdn.microsoft.com/library/windows/hardware/ff569385) | dot11MaxTransmitMSDULifetime | IEEE 802.11-2012 |
| [OID_DOT11_MULTI_DOMAIN_CAPABILITY](https://msdn.microsoft.com/library/windows/hardware/ff569389) | dot11MultiDomainCapabilityEntry | IEEE 802.11d-2001 |
| [OID_DOT11_MULTI_DOMAIN_CAPABILITY_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569390) | dot11MultiDomainCapabilityEnabled | IEEE 802.11d-2001 |
| [OID_DOT11_MULTI_DOMAIN_CAPABILITY_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569391) | dot11MultiDomainCapabilityImplemented | IEEE 802.11d-2001 |
| [OID_DOT11_NUMBER_OF_HOPPING_SETS](https://msdn.microsoft.com/library/windows/hardware/ff569394) | dot11NumberOfHoppingSets | IEEE 802.11d-2001 |      
| [OID_DOT11_OPERATIONAL_RATE_SET](https://msdn.microsoft.com/library/windows/hardware/ff569395) | dot11OperationalRateSet | IEEE 802.11-2012 |
| [OID_DOT11_PBCC_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569398) | dot11PBCCOptionImplemented | IEEE 802.11b-1999 |
| [OID_DOT11_RANDOM_TABLE_FLAG](https://msdn.microsoft.com/library/windows/hardware/ff569406) | dot11RandomTableFlag | IEEE 802.11d-2001 |
| [OID_DOT11_REG_DOMAINS_SUPPORT_VALUE](https://msdn.microsoft.com/library/windows/hardware/ff569408) | dot11RegDomainsSupportEntry | IEEE 802.11-2012 |
| [OID_DOT11_RTS_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569411) | dot11RTSThreshold | IEEE 802.11-2012 |
| [OID_DOT11_SHORT_PREAMBLE_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569414) | dot11ShortPreambleOptionImplemented | IEEE 802.11b-1999 |
| [OID_DOT11_SHORT_RETRY_LIMIT](https://msdn.microsoft.com/library/windows/hardware/ff569415) | dot11ShortRetryLimit | IEEE 802.11-2012 |
| [OID_DOT11_SHORT_SLOT_TIME_OPTION_ENABLED](https://msdn.microsoft.com/library/windows/hardware/ff569416) | dot11ShortSlotTimeOptionEnabled | IEEE 802.11g-2003 |
| [OID_DOT11_SHORT_SLOT_TIME_OPTION_IMPLEMENTED](https://msdn.microsoft.com/library/windows/hardware/ff569417) | dot11ShortSlotTimeOptionImplemented | IEEE 802.11g-2003 |
| [OID_DOT11_STATION_ID](https://msdn.microsoft.com/library/windows/hardware/ff569419) | dot11StationID | IEEE 802.11-2012 |
| [OID_DOT11_TEMP_TYPE](https://msdn.microsoft.com/library/windows/hardware/ff569431) | dot11TempType | IEEE 802.11-2012 |
| [OID_DOT11_TI_THRESHOLD](https://msdn.microsoft.com/library/windows/hardware/ff569432) | dot11TIThreshold | IEEE 802.11a-1999 |

If the IEEE 802.11 standard that defines the IEEE 802.11 MIB object also defines a default value for the MIB object, the Native 802.11 miniport driver must use the specified default value. Otherwise, the Native 802.11 miniport driver defines its own default value for the MIB object.

>[!NOTE]
> When the miniport driver receives an [OID_DOT11_RESET_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff569409) method request, the miniport driver must reset an IEEE MIB object to its default value under the following conditions:
   - When MIB values for the MAC and/or PHY are reset to their default values only if **bSetDefaultMIB** is set to **TRUE**. 
   - When MAC or PHY values are affected by the value of the **dot11ResetType** member. 
> For more information, refer to the topic for the specific Native 802.11 MIB OID.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")