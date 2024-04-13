---
title: Query Error Injection Status (Function Index 16)
description: This function returns the status of NVDIMM-N error injection.
ms.date: 11/18/2022
---

# Query Error Injection Status (Function Index 16)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns the status of NVDIMM-N error injection. The platform may choose to only enable error injection in specific scenarios, for example, after the user configures a BIOS setting.

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Error Injection Enabled** | 1 | 4 | Indicates whether error injection is enabled. If 0, error injection is disabled. If 1, error injection is enabled. |

## Related articles

[Inject Error (Function Index 17)](inject-error--function-index-17-.md)

[Get Injected Errors (Function Index 18)](get-injected-errors--function-index-18-.md)
