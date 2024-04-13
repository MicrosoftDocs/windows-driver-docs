---
title: Get Injected Errors (Function Index 18)
description: This function returns information about errors currently being injected.
ms.date: 11/18/2022
---

# Get Injected Errors (Function Index 18)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns information about errors currently being injected.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Operation Failures Injected** | 2 | 4 | Byte 0: *INJECT_OPS_FAILURES* (2, 0x60); Byte 1: If *INJECT_BAD_BLOCKS* is ‘1’ (bit 7 of Byte 0), this field is *INJECT_BAD_BLOCK_CAP* (2, 0x67). Otherwise, this field shall be 0. | Information about which operation or non-volatile memory errors are currently injected. |
| **Energy Source Failures Injected** | 1 | 6 | Byte 0: *INJECT_ES_FAILURES* (2, 0x64) | Information about which Energy Source (ES) errors are currently injected. |
| **Firmware Update Failures Injected** | 1 | 7 | Byte 0: *INJECT_FW_FAILURES* (2, 0x65) | Information about which firmware operation errors are currently injected. |

## Remarks

If the platform disabled error injections, this function shall succeed and return the same information as if there were no errors currently injected.

## Related articles

[Inject Error (Function Index 17)](inject-error--function-index-17-.md)

[Query Error Injection Status (Function Index 16)](query-error-injection-status--function-index-16-.md)
