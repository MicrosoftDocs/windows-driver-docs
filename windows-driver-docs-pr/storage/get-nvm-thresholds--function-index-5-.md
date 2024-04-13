---
title: Get NVM Thresholds (Function Index 5)
description: This function returns the lifetime percentage warning and error thresholds, which if hit or surpassed, indicate a problem with the NVDIMM-N.
ms.date: 11/18/2022
---

# Get NVM Thresholds (Function Index 5)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns the lifetime percentage warning and error thresholds, which if hit or surpassed, indicate a problem with the NVDIMM-N.  It should be implemented using an NVDIMM ACPI Namespace.

## Input

### Args3

None.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status**                                    | 4 | 0 | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **NVM Lifetime Percentage Warning Threshold** | 1 | 4 | The percentage value of the warning threshold for the non-volatile memory lifetime. *Byte 0: NVM_LIFETIME_WARNING_THRESHOLD* (0, 0x98) |
| **NVM Lifetime Percentage Error Threshold**   | 1 | 5 | The percentage value of the error threshold for the non-volatile memory lifetime. *Byte 0: NVM_LIFETIME_ERROR_THRESHOLD* (0, 0x90) |

## Related articles

[Set NVM Lifetime Percentage Warning Threshold (Function Index 6)](set-nvm-lifetime-percentage-warning-threshold--function-index-6-.md)
