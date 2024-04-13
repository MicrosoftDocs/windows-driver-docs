---
title: Finish Firmware Update (Function Index 24)
description: This function finishes the firmware update operation that a call to Start Firmware Update (Function Index 22) initiated.
ms.date: 11/18/2022
---

# Finish Firmware Update (Function Index 24)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function finishes the firmware update operation that a call to [Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md) initiated.

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | This function can return the following Function-Specific Error Codes: 1. *There is no firmware update operation in progress.* 2. *Invalid firmware image.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

## Related articles

[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)

[Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)

[Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)
