---
title: WDI_TLV_RTT
description: WDI_TLV_RTT is a TLV that contains the measured roundtrip time (RTT), in picoseconds, for a Fine Timing Measurement (FTM) request. 
ms.date: 02/15/2019
keywords:
 - WDI_TLV_RTT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# WDI_TLV_RTT

**WDI_TLV_RTT** is a TLV that contains the measured roundtrip time (RTT), in picoseconds, for a Fine Timing Measurement (FTM) request. 

This TLV is used in [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md).

## TLV Type

0x15C

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
