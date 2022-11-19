---
title: Inject Error (Function Index 17)
description: This function injects errors in the NVDIMM-N module firmware. The purpose of this function is to enable software validation.
ms.date: 11/18/2022
---

# Inject Error (Function Index 17)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function injects errors in the NVDIMM-N module firmware. The purpose of this function is to enable software validation. The platform may choose to only enable error injection in specific scenarios; for example, after the user configures a BIOS setting. The host may call [Query Error Injection Status (Function Index 16)](query-error-injection-status--function-index-16-.md) to learn whether or not the error injection functions are enabled.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Inject Operation Failures** | 2 | 0 | Byte 0: *INJECT_OPS_FAILURES* (2, 0x60); Byte 1: If *INJECT_BAD_BLOCKS* is 1 (bit 7 of Byte 0), this field is *INJECT_BAD_BLOCK_CAP* (2, 0x67). Otherwise, it shall be 0. | Specifies which operation or non-volatile memory errors will be injected. |
| **Inject Energy Source Failures** | 1 | 2 | Byte 0: *INJECT_ES_FAILURES* (2, 0x64) | Specifies which Energy Source (ES) errors will be injected. |
| **Inject Firmware Update Failures** | 1 | 3 | Byte 0: *INJECT_FW_FAILURES* (2, 0x65) | Specifies which firmware operation errors will be injected. |

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | This function can return the following Function-Specific Error Codes: 1: *Error injection is disabled.* 2: *One or more errors could not be injected because they are not supported.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

> [!NOTE]
> Any errors that were successfully injected will remain injected when returning Function-Specific Error Code 2. If this function returns the Function-Specific Error Code 2, call [Get Injected Errors (Function Index 18)](get-injected-errors--function-index-18-.md) to retrieve which errors could not be injected.

## Remarks

Some error injection features are optional and may not be supported by the device. Refer to the appropriate Byte Addressable Energy Backed Interface JEDEC specification for the list of optional error injections.

The platform must detect if the host attempted to inject an error that isn't supported. It does that by writing to the error injection register and then reading the same register & verifying whether or not all the intended bits are set. For example, the platform does the following to inject operational failures:

1. Writes the value of Byte 0 of the **Inject Operation Failures** field to the *INJECT_OPS_FAILURES* register.

2. Reads the *INJECT_OPS_FAILURES* register.

3. If the new value of *INJECT_OPS_FAILURES* matches Byte 0 of the **Inject Operation Failures** field, return success. Otherwise, return the Function-Specific Error Code 2.
