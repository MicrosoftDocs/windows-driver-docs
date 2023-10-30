---
title: Set Memory Error Counters (Function Index 31)
description: This function sets the counters that track correctable and uncorrectable memory error events to a caller-specified value. The purpose of this function is to enable software validation.
ms.date: 11/18/2022
---

# Set Memory Error Counters (Function Index 31)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function sets the counters that track correctable and uncorrectable memory error events to a caller-specified value. The purpose of this function is to enable software validation.

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Count of DRAM Uncorrectable ECC Errors** | 1 | 0 | The number of uncorrectable ECC errors detected by the platform from the NVDIMM-N module. The platform shall write this value to the *DRAM_ECC_ERROR_COUNT* (2, 0x80) register. |
| **Count of DRAM Correctable ECC Error Above Threshold Events** | 1 | 1 | The number of correctable ECC threshold-exceeded events detected by the platform from the NVDIMM-N module. The platform shall write this value to the *DRAM_THRESHOLD_ECC_COUNT* (2, 0x81) register. |

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

## Related articles

[Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md)
