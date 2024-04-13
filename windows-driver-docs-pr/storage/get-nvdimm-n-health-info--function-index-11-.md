---
title: Get NVDIMM-N Health Info (Function Index 11)
description: This function returns information about the health of the NVDIMM-N module.
ms.date: 11/18/2022
---

# Get NVDIMM-N Health Info (Function Index 11)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns information about the health of the NVDIMM-N module.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Module Health** | 2 | 4 | Byte 0: *MODULE_HEALTH_STATUS0* (0, 0xA1); Byte 1: *MODULE_HEALTH_STATUS1* (0, 0xA2) | Detailed information regarding the NVDIMM-N module's health. |
| **Module Current Temperature** | 2 | 6 | | The module temperature in degrees Celsius. The minimum value is 0. This information is retrieved from the temperature sensor on the NVDIMM-N’s Serial Presence Detect EEPROM. |
| **Error Threshold Status** | 1 | 8 | Byte 0: *ERROR_THRESHOLD_STATUS* (0, 0xA5) | Status regarding the error thresholds on the NVDIMM-N module. |
| **Warning Threshold Status** | 1 | 9 | Byte 0: *WARNING_THRESHOLD_STATUS* (0, 0xA7) | Status regarding the warning thresholds on the NVDIMM-N module. |
| **NVM Lifetime** | 1 | 10 | Byte 0: *NVM_LIFETIME* (0, 0xC0) | The last known non-volatile memory lifetime percentage value. |
| **Count of DRAM Uncorrectable ECC Errors** | 1 | 11 | Byte 0: *DRAM_ECC_ERROR_COUNT* (2, 0x80) | The number of uncorrectable ECC errors detected by the platform from the NVDIMM-N module. |
| **Count of DRAM Correctable ECC Error Above Threshold Events** | 1 | 12 | Byte 0: *DRAM_THRESHOLD_ECC_COUNT* (2, 0x81)| The number of correctable ECC threshold-exceeded events detected by the platform from the NVDIMM-N module. |

## Related articles

[Get Critical Health Info (Function Index 10)](get-critical-health-info--function-index-10-.md)

[Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md)
