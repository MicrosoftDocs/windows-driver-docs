---
title: Reset to Factory Defaults (Function Index 21)
description: This function resets the NVDIMM-N back to the settings the vendor pre-configured.
ms.date: 11/18/2022
---

# Reset to Factory Defaults (Function Index 21)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function resets the NVDIMM-N back to the settings the vendor pre-configured.

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status**  | 4 | 0 | This function can return the following Function-Specific Error Code: *The operation timed out.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

> [!NOTE]
> The platform shall wait three times the maximum save timeout for the factory default operation to finish (For example, if the maximum save timeout is 60 seconds, the platform shall wait 180 seconds). If the operation takes longer than that interval, the platform shall abort the operation and return with the function-specific error code 1(the operation timed out).
