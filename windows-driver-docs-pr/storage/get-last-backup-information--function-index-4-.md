---
title: Get Last Backup Information (Function Index 4)
description: This function returns information about the saved image.
ms.date: 11/18/2022
---

# Get Last Backup Information (Function Index 4)

This function returns information about the saved image.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Trigger Information** | 4 | 4 | Byte 0: *CSAVE_INFO0* (0, 0x80); Bytes 1-3: Reserved. | Information on whether or not there's a valid DRAM image saved in the non-volatile memory subsystem and the trigger source of the save operation.
| **Save Failure Information** | 4 | 8 | Byte 0: *SAVE_FAIL_INFO0* (0, 0x84); Byte 1: *CSAVE_FAIL_INFO1* (0, 0x85); Bytes 2-3: Reserved. | Failure information of the save operation. |
