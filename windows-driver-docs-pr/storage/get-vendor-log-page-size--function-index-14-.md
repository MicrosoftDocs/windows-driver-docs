---
title: Get Vendor Log Page Size (Function Index 14)
description: This function returns the size of the vendor log page so that the host knows the size of the buffer it needs to allocate to read the vendor log page.
ms.date: 11/18/2022
---

# Get Vendor Log Page Size (Function Index 14)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns the size of the vendor log page. The host needs this value to know the size of the buffer it needs to allocate to read the vendor log page.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Vendor Log Page Size** | 4 | 4 | Byte 0: *VENDOR_LOG_PAGE_SIZE* (0, 0x31) | The size of the vendor log page in multiples of 32 bytes. |

## Related articles

[Get Vendor Log Page (Function Index 15)](get-vendor-log-page--function-index-15-.md)
