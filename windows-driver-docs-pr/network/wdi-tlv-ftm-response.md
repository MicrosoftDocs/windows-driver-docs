---
title: WDI_TLV_FTM_RESPONSE
description: WDI_TLV_FTM_RESPONSE is a TLV that contains Fine Timing Measurement (FTM) response information from a BSS target.
ms.assetid: 7FD63544-F7FF-4593-A525-A6BEA2A56BB7
ms.date: 02/13/2019
keywords:
 - WDI_TLV_FTM_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_FTM_RESPONSE

**WDI_TLV_FTM_RESPONSE** is a TLV that contains Fine Timing Measurement (FTM) response information from a BSS target. This TLV is used in the payload data of an [NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE](ndis-status-wdi-indication-request-ftm-complete.md) task completion indication.

## TLV type

0x163

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| WDI_MAC_ADDRESS |  |   | The BSSID of the target to which this FTM response belongs. |
| [**WDI_FTM_RESPONSE_STATUS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wditypes/ne-wditypes-_wdi_ftm_response_status) | WDI_TLV_FTM_RESPONSE_STATUS |   |   | The FTM response status. If success, the rest of the fields in this TLV are present. |
| UINT16 |  | X | A duration, in seconds, that should pass before trying to request a new FTM from this target. |
| UINT16 |  |   | The number of measurements used to provide the round trip time (RTT). If the FTM response status was a success, this field is mandatory. |
| INT32 |   |   | The received signal strength indicator (RSSI) from the FTM target. This is in units of decibels referenced to 1.0 milliwatts (dBm). If the FTM response status was a success, this field is mandatory. |
| UINT32 |   |   |   | The link quality value of the FTM target, ranging from 0 through 100. A value of 100 specifies the highest link quality. If the FTM response status was a success, this field is mandatory. |
| UINT32 | WDI_TLV_RTT |   |   | The measured roundtrip time (RTT), in picoseconds. If the FTM response status was a success, this field is mandatory. |
| UINT32 |   |   | The accuracy, or expected degree of closeness, of the provided RTT measurement to the true value. The unit is in picoseconds. <p>For example, if the current RTT is 66712.82 picoseconds (10 meters away from the target AP), but it is known through hardware profiling that the measurement could be off by +/-1 meter, then the RTT accuracy is 6671.28 picoseconds. It is the responsibility of the IHV to provide as specific an accuracy as possible based on the profiling of its hardware and the matching conditions when the actual FTM is taken. There are multiple variables affecting FTM accuracy and multiple possibilities for which of these variables can be measured and considered. The reason a more specific accuracy is desirable is because this is useful information that upper layers can consume, such as preferring measurements with higher accuracy when computing a position or to vary the computed position error based off the FTM accuracies. When profiling, a minimum 90% CDF should be used. </p> |
| UINT64 |  |   |   | If more than one measurement was used to calculate the RTT, this field provides the statistical variance of the measurements used. |
| [**WDI_LCI_REPORT_STATUS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wditypes/ne-wditypes-_wdi_lci_report_status) |   |   | If an LCI report was requested, this field provides the status result. If successful, the following fields are present and mandatory. |
| TLV\<LIST\<UINT8>> |   |   | The Location Configuration Information (LCI) report, as defined in Section 9.4.2.22.10 of the [802-11-2016 standard](https://standards.ieee.org/standard/802_11-2016.html), including the LCI subelement and other Optional subelements available. In other words, this is the measurement report section of the Measurement Report element (as per Section 9.4.2.22 from the [802-11-2016 standard](https://standards.ieee.org/standard/802_11-2016.html)). |

## Requirements

|   |   |
| --- | --- |
| Minimum supported client | Windows 10, version 1903 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |