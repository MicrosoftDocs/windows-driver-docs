---
title: WDI_TLV_RTT_ACCURACY (dot11wificxtypes.hpp)
ms.topic: reference
description: WDI_TLV_RTT_ACCURACY is a WiFiCx TLV that contains the accuracy, or expected degree of closeness, of a RTT measurement to the true value for a FTM request.
ms.date: 10/30/2021
keywords:
 - WDI_TLV_RTT_ACCURACY Network Drivers Starting with Windows Vista
---

# WDI_TLV_RTT_ACCURACY (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_RTT_ACCURACY** is a TLV that contains the accuracy, or expected degree of closeness, of a roundtrip time (RTT) measurement to the true value for a Fine Timing Measurement (FTM) request. The unit is in picoseconds.

For example, if the current RTT is 66712.82 picoseconds (10 meters away from the target AP), but it is known through hardware profiling that the measurement could be off by +/-1 meter, then the RTT accuracy is 6671.28 picoseconds. It is the responsibility of the IHV to provide as specific an accuracy as possible based on the profiling of its hardware and the matching conditions when the actual FTM is taken. There are multiple variables affecting FTM accuracy and multiple possibilities for which of these variables can be measured and considered. The reason a more specific accuracy is desirable is because this is useful information that upper layers can consume, such as preferring measurements with higher accuracy when computing a position or to vary the computed position error based off the FTM accuracies. When profiling, a minimum 90% CDF should be used. 

## TLV Type

0x15D

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| UINT32 | The RTT. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|
