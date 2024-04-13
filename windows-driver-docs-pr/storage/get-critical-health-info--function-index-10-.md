---
title: Get Critical Health Info (Function Index 10)
description: This function returns critical health-related information.
ms.date: 11/17/2022
---

# Get Critical Health Info (Function Index 10)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns critical health-related information. Call [Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md) and [Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md) to obtain further health-related information.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**               | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Critical Health Info** | 1 | 4 | Byte 0: *MODULE_HEALTH* (0, 0xA0) | A high level status report of any issues with the NVDIMM-N module. |
