---
title: WDI_TLV_STATION_CAPABILITIES
description: WDI_TLV_STATION_CAPABILITIES is a TLV that contains the capabilities of a station.
ms.date: 05/07/2021
keywords:
 - WDI_TLV_STATION_CAPABILITIES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI\_TLV\_STATION\_CAPABILITIES

WDI\_TLV\_STATION\_CAPABILITIES is a TLV that contains the capabilities of a station.

## TLV Type

0x11

## Length

The sum (in bytes) of the sizes of all contained elements.

## Values

| Type | Description |
| --- | --- |
| UINT32 | The scan SSID list size. |
| UINT32 | The desired BSSID list size. |
| UINT32 | The desired SSID list size. |
| UINT32 | The privacy exemption list size. |
| UINT32 | The key mapping table size. |
| UINT32 | The default key table size. |
| UINT32 | The maximum length of the WEP key value. |
| UINT32 | The maximum number per STA default key tables. |
| UINT8 | Supported QoS flags. Specifies whether the device supports WMM.<br />Valid values are 0 (not supported) and 1 (supported).|
| UINT8 | Specifies whether host-FIPS mode is implemented.<br /><br />If the field is set to [DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_OID_SUPPORTED](/windows-hardware/drivers/ddi/windot11/ns-windot11-dot11_extsta_attributes#revision--dot11_extsta_attributes_revision_2-or-higher) with no other bits set, the driver implements the 802.11 safe mode of operation.<br /><br />If the field is set to DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_CERTIFIED, the NIC has received a validation certificate from the National Institute of Standards and Technology (NIST) under Federal Information Processing Standards (FIPS) Publication 140-2, Security Requirements for Cryptographic Modules. In this mode, the hardware is responsible for ensuring compliance to FIPS standard.<br /><br />If the field is set to zero (0), FIPS mode is not implemented by the NIC. |
| UINT8 | Specifies whether 802.11w MFP capability is supported.<br />Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether auto power save is supported.<br />Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether the adapter maintains the Station BSS List cache.<br />Valid values are 0 (no) and 1 (yes). |
| UINT8 | Specifies whether the adapter may attempt association to a BSSID that is not specified in the Preferred BSSID list during a Station connect.<br/>Valid values are 0 (no) and 1 (yes). |
| UINT32 | The maximum supported Network Offload List size. |
| UINT8 | Specifies whether or not the adapter can track HESSIDs associated with SSIDs and connect/roam only to those APs that match the specified SSID+HESSID.<br />Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether the adapter can offload connectivity to networks belonging to specific HESSIDs. |
| UINT8 | Specifies whether disconnected standby is supported.<br />Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | Specifies whether the driver supports the Fine Time Measurement (FTM) protocol as an initiator.<br />Valid values are 0 (not supported) and 1 (supported). |
| UINT8 | The maximum number of target STAs that can be queried per FTM request task. |
| UINT8 | Specifics whether the driver supports the FIPS mode.<br /><br />If the field is set to DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_OID_SUPPORTED with no other bits set, the driver implements the 802.11 safe mode of operation.<br /><br />If the field is set to DOT11_EXTSTA_ATTRIBUTES_SAFEMODE_CERTIFIED the NIC has received a validation certificate from the National Institute of Standards and Technology (NIST) under Federal Information Processing Standards (FIPS) Publication 140-2, Security Requirements for Cryptographic Modules. In this mode the hardware is responsible for ensuring compliance to FIPS standard.<br /><br />If the field is set to zero (0), FIPS mode is not implemented by the NIC.<br /><br />**Operating system support for FIPS is anticipated in a future release of Windows.**<br /><br />**NOTE** that FIPS mode requires the driver to indicate support for WDI_AUTH_ALGO_WPA3 auth and WDI_CIPHER_ALGO_GCMP_256 cipher pairs in the unicast and multicast algo pairs. It must also indicate support for WDI_AUTH_ALGO_WPA3 auth and WDI_CIPHER_ALGO_BIP_GMAC_256 cipher in the Multicast Management algo pairs. |

## Requirements

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Wditypes.hpp |
