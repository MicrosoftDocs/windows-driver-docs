---
title: Get Energy Source Thresholds (Function Index 7)
description: This function returns warning and error thresholds used to indicate a problem with the Energy Source (ES).
ms.date: 11/18/2022
---

# Get Energy Source Thresholds (Function Index 7)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns warning and error thresholds that indicate a problem with the Energy Source (ES) if they hit or surpassed. This function may return a failure status if the ES is host-managed and the platform doesn't support thresholds.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **ES Lifetime Percentage Warning Threshold** | 1 | 4 | Byte 0: *ES_LIFETIME_WARNING_THRESHOLD* (0, 0x99) | The percentage value of the warning threshold for the ES lifetime. |
| **ES Lifetime Percentage Error Threshold** | 1 | 5 | Byte 0: *ES_LIFETIME_ERROR_THRESHOLD* (0, 0x91) | The percentage value of the error threshold for the ES lifetime. |
| **ES Temperature Warning Threshold** | 1 | 6 | Byte 0: *ES_TEMP_WARNING_THRESHOLD* (0, 0x9A) | The percentage value of the warning threshold for the ES temperature. |
| **ES Temperature Error Threshold** | 1 | 7 | Byte 0: *ES_TEMP_ERROR_THRESHOLD* (0, 0x92) | The percentage value of the error threshold for the ES temperature. |

## Related articles

[Set Energy Source Lifetime Warning Threshold (Function Index 8)](set-energy-source-lifetime-warning-threshold--function-index-8-.md)

[Set Energy Source Temperature Warning Threshold (Function Index 9)](set-energy-source-temperature-warning-threshold--function-index-9-.md)
