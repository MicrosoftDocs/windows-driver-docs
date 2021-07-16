---
title: WDI_TLV_FTM_RESPONSE (dot11wificxtypes.h)
description: WDI_TLV_FTM_RESPONSE is a WiFiCx TLV that contains Fine Timing Measurement (FTM) response information from a BSS target.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_FTM_RESPONSE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_FTM_RESPONSE (dot11wificxtypes.h)

**WDI_TLV_FTM_RESPONSE** is a TLV that contains Fine Timing Measurement (FTM) response information from a BSS target. 

This TLV is used in the payload data of an [NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE](ndis-status-wdi-indication-request-ftm-complete.md) task completion indication.

## TLV type

0x163

## Length

The sum (in bytes) of the sizes of all contained TLVs.

## Values

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_BSSID](wdi-tlv-bssid.md) | [**WDI_MAC_ADDRESS**](/windows-hardware/drivers/ddi/dot11wificxintf/ns-dot11wificxintf-wdi_mac_address) |  |   | The BSSID of the target to which this FTM response belongs. |
| [WDI_TLV_FTM_RESPONSE_STATUS](wdi-tlv-ftm-response-status.md) | [**WDI_FTM_RESPONSE_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_ftm_response_status) |  |   | The FTM response status. If success, the rest of the fields in this TLV are present. |
| [WDI_TLV_RETRY_AFTER](wdi-tlv-retry-after.md)| UINT16 |  |  | A duration, in seconds, that should pass before trying to request a new FTM from this target. |
| [WDI_TLV_FTM_NUMBER_OF_MEASUREMENTS](wdi-tlv-ftm-number-of-measurements.md) | UINT16 |  |   | The number of measurements used to provide the round trip time (RTT). If the FTM response status was a success, this field is mandatory. |
| [WDI_TLV_BSS_ENTRY_SIGNAL_INFO](wdi-tlv-bss-entry-signal-info.md) | INT32 |   |   | The received signal strength indicator (RSSI) from the FTM target. This is in units of decibels referenced to 1.0 milliwatts (dBm). If the FTM response status was a success, this field is mandatory. |
| Same as row above  | UINT32 |   |   | The link quality value of the FTM target, ranging from 0 through 100. A value of 100 specifies the highest link quality. If the FTM response status was a success, this field is mandatory. |
| [WDI_TLV_RTT](wdi-tlv-rtt.md) | UINT32 |   |   | The measured roundtrip time (RTT), in picoseconds. If the FTM response status was a success, this field is mandatory. |
| [WDI_TLV_RTT_ACCURACY](wdi-tlv-rtt-accuracy.md) | UINT32 |   |   | The accuracy, or expected degree of closeness, of the provided RTT measurement to the true value. The unit is in picoseconds. For more information, see the [WDI_TLV_RTT_ACCURACY](wdi-tlv-rtt-accuracy.md). |
| [WDI_TLV_RTT_VARIANCE](wdi-tlv-rtt-variance.md) | UINT64 |   |   | If more than one measurement was used to calculate the RTT, this field provides the statistical variance of the measurements used. |
| [WDI_TLV_LCI_REPORT_STATUS](wdi-tlv-lci-report-status.md) | [**WDI_LCI_REPORT_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_lci_report_status) |   |   | If an LCI report was requested, this field provides the status result. If successful, the following fields are present and mandatory. |
| [WDI_TLV_LCI_REPORT_BODY](wdi-tlv-lci-report-body.md) | TLV\<LIST\<UINT8>> |   |   | The Location Configuration Information (LCI) report, as defined in Section 9.4.2.22.10 of the [802-11-2016 standard](https://standards.ieee.org/standard/802_11-2016.html), including the LCI subelement and other Optional subelements available. In other words, this is the measurement report section of the Measurement Report element (as per Section 9.4.2.22 from the [802-11-2016 standard](https://standards.ieee.org/standard/802_11-2016.html)). |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|
