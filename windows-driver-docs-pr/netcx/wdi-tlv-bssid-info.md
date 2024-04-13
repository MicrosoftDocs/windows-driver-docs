---
title: WDI_TLV_BSSID_INFO (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_BSSID_INFO is a WiFiCx TLV that contains BSSID information.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_BSSID_INFO Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_BSSID\_INFO (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WDI\_TLV\_BSSID\_INFO is a TLV that contains BSSID information.

## TLV Type


0x120

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type  | Description                                                                                                                                                                                                                                                                                                                               |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT8 | AP reachability. Valid values are 1 (not reachable), 2 (unknown), and 3 (reachable).                                                                                                                                                                                                                                                      |
| UINT8 | Security. If this is set to 1, it indicates that the AP identified by this BSSID supports the same security provisioning as used by the STA in its current association. If this is set to 0, it indicates that either this AP does not support the same security provisioning, or the security information is not available at this time. |
| UINT8 | Key scope bit. If it is set to 1, it indicates the AP indicated by this BSSID has the same authenticator as the AP sending the report. If this bit is set to 0, it indicates a distinct authenticator or the information is not available.                                                                                                |
| UINT8 | This is set to 1 if dot11SpectrumManagementRequired is true.                                                                                                                                                                                                                                                                              |
| UINT8 | This is set to 1 if dot11QosOptionImplemented is true.                                                                                                                                                                                                                                                                                    |
| UINT8 | An AP sets the APSD subfield to 1 within the Capability Information field when dot11APSDOptionImplemented is true, and sets it to 0 otherwise.                                                                                                                                                                                            |
| UINT8 | This is set to 1 if dot11RadioMeasurementActivated is true.                                                                                                                                                                                                                                                                               |
| UINT8 | This is set to 1 if dot11DelayedBlockAckOptionImplemented is true.                                                                                                                                                                                                                                                                        |
| UINT8 | This is set to 1 if dot11ImmediateBlockAckOptionImplemented is true.                                                                                                                                                                                                                                                                      |
| UINT8 | This is set to 1 if the AP represented by this BSSID includes an MDE in its Beacon frames.                                                                                                                                                                                                                                                |
| UINT8 | This is set to 1 to indicate that the AP represented by this BSSID is an HT AP, including the HT Capabilities element in its Beacon.                                                                                                                                                                                                      |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

 




