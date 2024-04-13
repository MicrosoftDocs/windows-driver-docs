---
title: Arm NVDIMM-N (Function Index 20)
description: This function arms the NVDIMM-N for save operations if there's a power loss.
ms.date: 11/18/2022
---

# Arm NVDIMM-N (Function Index 20)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function arms the NVDIMM-N for save operations if there's a power loss. The platform is responsible for choosing the appropriate save trigger.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status**    | 4 | 0 |  This function can return the following Function-Specific Error Code: 1. *The operation timed out.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

> [!NOTE]
> This is a synchronous function. It returns only when the arm operation has finished or timed out. If the operation takes longer than the timeout defined in *Arm_TIMEOUT0* (0, 0x20) and *Arm_TIMEOUT1* (0, 0x21), the platform shall abort this function before it returns.
