---
title: Select Firmware Image Slot (Function Index 25)
description: This function selects which firmware image is active.
ms.date: 11/18/2022
---

# Select Firmware Image Slot (Function Index 25)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function selects which firmware image is active. The selected image shall be loaded when the device resets.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Firmware Slot** | 1 | 0 | The firmware image slot that shall be selected as active when the device resets. |

> [!NOTE]
> The firmware shall write the **Firmware Slot** value to the lower 4 bits of the *FW_SLOT_INFO* (3, 0x42) register.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | This function can return the following Function-Specific Error Codes: 1: *Invalid slot number.* 2: *There is no image in this slot.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

## Related articles

[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md)

[Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)

[Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)
