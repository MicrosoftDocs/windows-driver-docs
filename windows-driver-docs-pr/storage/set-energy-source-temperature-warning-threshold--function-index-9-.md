---
title: Set Energy Source Temperature Warning Threshold (Function Index 9)
description: This function sets the warning threshold for operating Energy Source (ES) temperature.
ms.date: 11/18/2022
---

# Set Energy Source Temperature Warning Threshold (Function Index 9)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function sets the warning threshold for operating Energy Source (ES) temperature. This function may return a failure status if the ES is host-managed and thresholds aren't supported by the platform.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **ES Lifetime Temperature Warning Threshold** | 1 | 0 | The new value (in degrees Celsius) of the warning threshold. The platform shall write this value to the *ES_TEMP_WARNING_THRESHOLD* (0, 0x99) register. |

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**   | 4 | 0 |  | This function can return the following Function-Specific Error Code: *The platform does not support ES thresholds.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

## Related articles

[Set Energy Source Lifetime Warning Threshold (Function Index 8)](set-energy-source-lifetime-warning-threshold--function-index-8-.md)

[Get Energy Source Thresholds (Function Index 7)](get-energy-source-thresholds--function-index-7-.md)
