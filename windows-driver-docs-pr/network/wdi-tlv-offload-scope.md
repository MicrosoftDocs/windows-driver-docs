---
title: WDI_TLV_OFFLOAD_SCOPE
description: WDI_TLV_OFFLOAD_SCOPE is a TLV that contains Rx coalesce offload capabilities.
ms.assetid: 2E00659F-4A41-4907-AEA6-92EAFBFF2149
ms.date: 10/05/2017
keywords:
 - WDI_TLV_OFFLOAD_SCOPE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_OFFLOAD_SCOPE


WDI_TLV_OFFLOAD_SCOPE is a TLV that contains the scope for network offloads.

## TLV Type


0x143

## Length


The size (in bytes) of the below values.

## Values

| Type | Description |
| --- | --- |
| UINT8 | Specifies whether checksum offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
| UINT8 | Specifies whether LsoV1 offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
| UINT8 | Specifies whether LsoV2 offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
| UINT8 | Specifies whether RSC offload parameters are applicable on all ports. <p>Possible values:</p> <ul><li>0: Not applicable</li><li>1: Applicable</li></ul> |
 

## Requirements

| | |
| --- | --- |
| Minimum supported client | Windows 10, version 1709 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |



