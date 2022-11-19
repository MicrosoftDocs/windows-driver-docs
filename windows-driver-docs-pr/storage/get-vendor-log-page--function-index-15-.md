---
title: Get Vendor Log Page (Function Index 15)
description: This function returns the vendor log page.
ms.date: 10/18/2018
---

# Get Vendor Log Page (Function Index 15)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns the vendor log page. Call [Get Vendor Log Page Size (Function Index 14)](get-vendor-log-page-size--function-index-14-.md) to obtain the page size.

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status**                   | 4 | 0 |  See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). for more information. |
| **Vendor Log Page** | Call [Get Vendor Log Page Size (Function Index 14)](get-vendor-log-page-size--function-index-14-.md) to obtain. | 4 | The vendor log page. |
