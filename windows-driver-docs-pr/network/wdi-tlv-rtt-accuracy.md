---
title: WDI_TLV_RTT_ACCURACY
description: WDI_TLV_RTT_ACCURACY is a TLV that contains the accuracy, or expected degree of closeness, of a roundtrip time (RTT) measurement to the true value for a Fine Timing Measurement (FTM) request.
ms.date: 02/15/2019
keywords:
 - WDI_TLV_RTT_ACCURACY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_RTT_ACCURACY

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

**WDI_TLV_RTT_ACCURACY** is a TLV that contains the accuracy, or expected degree of closeness, of a roundtrip time (RTT) measurement to the true value for a Fine Timing Measurement (FTM) request. The unit is in picoseconds.

For example, if the current RTT is 66712.82 picoseconds (10 meters away from the target AP), but it is known through hardware profiling that the measurement could be off by +/-1 meter, then the RTT accuracy is 6671.28 picoseconds. It is the responsibility of the IHV to provide as specific an accuracy as possible based on the profiling of its hardware and the matching conditions when the actual FTM is taken. There are multiple variables affecting FTM accuracy and multiple possibilities for which of these variables can be measured and considered. The reason a more specific accuracy is desirable is because this is useful information that upper layers can consume, such as preferring measurements with higher accuracy when computing a position or to vary the computed position error based off the FTM accuracies. When profiling, a minimum 90% CDF should be used. 

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15D

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| UINT32 | The RTT. |

## Requirements

**Minimum supported client**: Windows 10, version 1903
**Minimum supported server**: Windows Server 2016
**Header**: Wditypes.hpp
