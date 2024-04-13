---
title: Get Save Operation Requirements (Function Index 2)
description: This function returns information about hardware requirements for a save operation.
ms.date: 11/18/2022
---

# Get Save Operation Requirements (Function Index 2)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns information about hardware requirements for a save operation. This function shall succeed for all NVDIMM-Ns that support a host-managed Energy Source (ES) policy. It may return a failure status if the device supports device-managed ES policy and save operation requirements aren't available.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  This function can return the following Function-Specific Error Code: *The NVDIMM-N does not report save operation requirements.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Average Power Requirement** | 2 | 4 | Byte 0: *CSAVE_POWER_REQ0* (0, 0x29); Byte 1: *CSAVE_POWER_REQ1* (0, 0x2A) | The average power (in milliwatts) required for the save operation. |
| **Idle Power Requirement**    | 2 | 6 | Byte 0: *CSAVE_IDLE_POWER_REQ0* (0, 0x2B); Byte 1: *CSAVE_IDLE_POWER_REQ1* (0, 0x2C) | The average power (in milliwatts) the module requires after the save operation completes. |
| **Minimum Voltage Requirement** | 2 | 8 | Byte 0: *CSAVE_MIN_VOLT_REQ0* (0, 0x2D); Byte 1: *CSAVE_MIN_VOLT_REQ1* (0, 0x2E) | The minimum voltage (in millivolts) the ES has to service during a save operation. |
| **Maximum Voltage Requirement** | 2 | 10 | Byte 0: *CSAVE_MAX_VOLT_REQ0* (0, 0x2F); Byte 1: *CSAVE_MAX_VOLT_REQ1* (0, 0x30) | The maximum voltage (in millivolts) the ES has to service during a save operation. |
