---
title: WDI_TLV_LCI_REPORT_STATUS
ms.topic: reference
description: WDI_TLV_LCI_REPORT_STATUS is a TLV that contains the status result of a Location Configuration Information (LCI) report, if one was requested during a Fine Timing Measurement (FTM) request.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_LCI_REPORT_STATUS Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# WDI_TLV_LCI_REPORT_STATUS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_LCI_REPORT_STATUS** is a TLV that contains the status result of a Location Configuration Information (LCI) report, if one was requested during a Fine Timing Measurement (FTM) request.

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15F

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| [**WDI_LCI_REPORT_STATUS**](/windows-hardware/drivers/ddi/wditypes/ne-wditypes-_wdi_lci_report_status) | The status of the LCI report. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
