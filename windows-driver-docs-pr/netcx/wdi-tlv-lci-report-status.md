---
title: WDI_TLV_LCI_REPORT_STATUS (dot11wificxtypes.hpp)
description: WDI_TLV_LCI_REPORT_STATUS is a WiFiCx TLV that contains the status result of a Location Configuration Information (LCI) report, if one was requested during a Fine Timing Measurement (FTM) request.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_LCI_REPORT_STATUS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_LCI_REPORT_STATUS (dot11wificxtypes.hpp)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_LCI_REPORT_STATUS** is a TLV that contains the status result of a Location Configuration Information (LCI) report, if one was requested during a Fine Timing Measurement (FTM) request.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15F

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_LCI_REPORT_STATUS**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_lci_report_status) | The status of the LCI report. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
