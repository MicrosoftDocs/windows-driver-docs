---
title: Get Firmware Info (Function Index 26)
description: This function retrieves information about a firmware image slot.
ms.date: 11/18/2022
---

# Get Firmware Info (Function Index 26)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function retrieves information about a firmware image slot. Call [Get NVDIMM-N Identification (Function Index 1)](get-nvdimm-n-identification--function-index-1-.md) to retrieve the current slot number.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Firmware Slot** | 1 | 0 | The firmware image slot to report information for. |

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **ES Lifetime Percentage Warning Threshold** | 1 | 4 | Byte 0: *ES_LIFETIME_WARNING_THRESHOLD* (0, 0x99) | The percentage value of the warning threshold for the ES lifetime. |
| **Version** | 2 | 4 | Byte 0: *SLOTX_FWVER0* (0, 0x07/0x09); Byte 1: *SLOTX_FWVER1* (0, 0x08/0x0A) | Firmware version of the firmware image in the specified slot. |

## Related articles

[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)

[Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)

[Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)
