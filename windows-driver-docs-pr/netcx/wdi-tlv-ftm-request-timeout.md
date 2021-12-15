---
title: WDI_TLV_FTM_REQUEST_TIMEOUT (dot11wificxtypes.hpp)
description: WDI_TLV_FTM_REQUEST_TIMEOUT is a WiFiCx TLV that contains the maximum time, in milliseconds, to complete a Fine Timing Measurement (FTM).
ms.date: 07/31/2021
keywords:
 - WDI_TLV_FTM_REQUEST_TIMEOUT Network Drivers Starting with Windows Vista
---

# WDI_TLV_FTM_REQUEST_TIMEOUT (dot11wificxtypes.hpp)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]

**WDI_TLV_FTM_REQUEST_TIMEOUT** is a TLV that contains the maximum time, in milliseconds, to complete a Fine Timing Measurement (FTM).

This TLV is used in the task parameters of [OID_WDI_TASK_REQUEST_FTM](oid-wdi-task-request-ftm.md).

## TLV Type

0x161

## Length

The size (in bytes) of a UINT32.

## Values

| Type | Description |
| --- | --- |
| UINT32 | The maximum time, in milliseconds, to complete the FTM. The timeout is set to 150 ms multiplied by the number of targets. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

