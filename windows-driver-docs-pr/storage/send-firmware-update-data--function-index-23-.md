---
title: Send Firmware Update Data (Function Index 23)
description: This function sends firmware data to the device.
ms.date: 11/18/2022
---

# Send Firmware Update Data (Function Index 23)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function sends firmware data to the device.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Region Length** | 4 | 0 | The number of bytes being sent in this function. |
| **Region ID**     | 2 | 4 | The identification of the region that is being written. |
| **Block ID**      | 1 | 6 | The identification of the block being written inside the region. |
| **Firmware Data** | The number specified by *Region Length* | 7 | A region-sized packet of firmware image data. |

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | This function can return the following Function-Specific Error Codes: 1. *There is no firmware update operation in progress.* 2. *Invalid region size.* 3. *Transfer failed due to data corruption.* 4. *Operation timed out.* 5. *The firmware commit operation failed.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

> [!NOTE]
> This function shall compute the CRC of the Firmware Data and compare it with *FW_REGION_CRC0* (3, 0x40) and *FW_REGION_CRC1* (3, 0x41). If the values don’t match, the function shall fail with Function-Specific Error Code 3. Please refer to the Byte Addressable Energy Backed Interface JEDEC standard for the CRC algorithm specification.

## Related articles

[Start Firmware Update (Function Index 22)](start-firmware-update--function-index-22-.md)

[Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md)

[Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md)

[Get Firmware Info (Function Index 26)](get-firmware-info--function-index-26-.md)
