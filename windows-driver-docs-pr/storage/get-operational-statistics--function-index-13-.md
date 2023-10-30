---
title: Get Operational Statistics (Function Index 13)
description: This function returns counters that track operations performed by the NVDIMM-N.
ms.date: 11/18/2022
---

# Get Operational Statistics (Function Index 13)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns counters that track operations performed by the NVDIMM-N.  It should be implemented using an NVDIMM ACPI Namespace.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Duration of Last Save Operation**    | 4 | 4 | Byte 0: *LAST_SAVE_DURATION0* (2, 0x04); Byte 1: *LAST_SAVE_DURATION1* (2, 0x05); Bytes 2-3: Reserved. | The last save operation duration (in milliseconds or seconds). |
| **Duration of Last Restore Operation** | 4 | 8 | Byte 0: *LAST_RESTORE_DURATION0* (2, 0x06); Byte 1: *LAST_RESTORE_DURATION1* (2, 0x07); Bytes 2-3: Reserved. | The last restore operation duration (in milliseconds or seconds). |
| **Duration of Last Erase Operation** | 4 | 12 | Byte 0: *LAST ERASE DURATION_TIME0* (2, 0x08); Byte 1: *LAST_ERASE DURATION_TIME1* (2, 0x09); Bytes 2-3: Reserved. | The last erase operation duration in milliseconds or seconds. |
| **Number of Save Operations Completed** | 4 | 16 | Byte 0: *NUM_SAVE_OPS_COUNT0* (2, 0x0A); Byte 1: *NUM_SAVE_OPS_COUNT1* (2, 0x0B); Bytes 2-3: Reserved. | The number of completed save operations over the NVDIMM-N module's lifetime. |
| **Number of Restore Operations Completed** | 4 | 20 | Byte 0: *NUM_RESTORE_OPS_COUNT0 0* (2, 0x0C); Byte 1: *NUM_RESTORE_OPS_COUNT1* (2, 0x0D); Byte 2-3: Reserved. | The number of completed restore operations over the NVDIMM-N module's lifetime. |
| **Number of Erase Operations Completed** | 4 | 24 | Byte 0: *NUM_ERASE_COUNTS0* (2, 0x0E); Byte 1: *NUM_ERASE_COUNTS1* (2, 0x0F); Bytes 2-3: Reserved. | The number of completed erase operations over the NVDIMM-N module's lifetime. |
| **Number of Module Power Cycles** | 4 | 28 | Byte 0: *NUM_MODULE_POWER_CYCLES0* (2, 0x10); Byte 1: *NUM_MODULE_POWER_CYCLES1* (2, 0x11); Bytes 2-3: Reserved. | The number of power cycles over the NVDIMM-N module's lifetime. |
