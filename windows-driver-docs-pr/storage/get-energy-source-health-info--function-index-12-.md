---
title: Get Energy Source Health Info (Function Index 12)
description: This function returns information about the health of the Energy Source (ES) module.
ms.date: 11/18/2022
---

# Get Energy Source Health Info (Function Index 12)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns information about the health of the Energy Source (ES) module. This function may return a failure status if the ES is host-managed and health information isn't available.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                | 4 | 0 |  | This function can return the following Function-Specific Error Code: 1. *The platform does not support ES health information.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **ES Lifetime Percentage** | 1 | 4 | Byte 0: *ES_LIFETIME* (1, 0x70) | The last known ES lifetime percentage.
| **ES Current Temperature** | 2 | 5 | Byte 0: *ES_TEMP0* (1, 0x71); Byte 1: *ES_TEMP1* (1, 0x72) | The ES temperature in degrees Celsius. The minimum value is 0. |
| **Total Runtime**          | 4 | 7 | Byte 0: *ES_RUNTIME0* (1, 0x73); Byte 1: *ES_RUNTIME1* (1, 0x74); Bytes 2-3: Reserved | The time (in hours) the ES has been operational since it was manufactured. |

## Related articles

[Get NVDIMM-N Health Info (Function Index 11)](get-nvdimm-n-health-info--function-index-11-.md)

[Get Energy Source Health Info (Function Index 12)](get-energy-source-health-info--function-index-12-.md)
