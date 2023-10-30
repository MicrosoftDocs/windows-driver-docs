---
title: Get Energy Source Identification (Function Index 3)
description: This function returns identification information about the Energy Source (ES), which can be host-managed or device-managed.
ms.date: 11/18/2022
---

# Get Energy Source Identification (Function Index 3)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns identification information about the Energy Source (ES), which can be host-managed or device-managed.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Energy Source Policy** | 1 | 4 | Byte 0: *ENERGY_SOURCE_POLICY* (0, 0x14) | Information regarding the Energy Source policy supported by the module. |
| **Device-Managed ES Identification** | 11 | 5 | | This field contains valid data only if the current ES policy is device-managed (that is, if bit 2 of *SET_ES_POLICY_STATUS* (0, 0x70) is set). For all other ES policies, this field shall be 0. See Device-Managed ES Identification below for information. |
| **Host-Managed ES Identification** | 3 | 16 | | This field contains valid data only if the current ES policy is host-managed (that is, if bit 3 of SET_ES_POLICY_STATUS (0, 0x70) is set). For all other ES policies, this field shall be 0. See Host-Managed ES Identification below for information. |

### Device-Managed ES Identification

If the value of ES policy is 0, the Device-Managed ES Identification field is valid and has the following fields:

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **ES Hardware Revision**             | 2 | 5  | Byte 0: *ES_HWREV* (1, 0x04); Byte 1: Reserved. | The ES hardware revision. |
| **ES Firmware Revision**             | 2 | 7  | Byte 0: *ES_FWREV0* (1, 0x06); Byte 1: *ES_FWREV1* (1, 0x07) | The ES firmware revision. |
| **ES Health Check Frequency**        | 1 | 9  | Byte 0: *AUTO_ES_HEALTH_CHECK_FREQUENCY* (0, 0xA9) | The current frequency of the module's ES health assessment. 
| **ES Charge Timeout**                | 2 | 10 | Byte 0: *ES_CHARGE_TIMEOUT0* (1, 0x10); Byte 1: *ES_CHARGE_TIMEOUT1* (1, 0x11) | The worst case (in seconds) ES charge time. The value shall be greater than 0. |
| **ES Minimum Operating Temperature** | 1 | 12 | Byte 0: *MIN_ES_OPERATING_TEMP* (1, 0x12) | The minimum operating temperature (in degrees Celsius) of the ES. The minimum value supported shall be 0. |
| **ES Maximum Operating Temperature** | 1 | 13 | Byte 0: *MAX_ES_OPERATING_TEMP* (1, 0x13) | The maximum operating temperature (in degrees Celsius) of the ES. |
| **ES Attributes**                    | 1 | 14 | Byte 0: *ES_ATTRIBUTES* (1, 0x14) | Attributes regarding the ES. |
| **ES Technology**                    | 1 | 15 | Byte 0: *ES_TECH* (1, 0x15) | The technology used in the ES. |

### Host-Managed ES Identification

If the value of ES policy is 1, the Host-Managed ES Identification field is valid and has the following fields:

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **ES Health Check Frequency** | 1 | 16 | Byte 0: *AUTO_ES_HEALTH_FREQUENCY* (0, 0xA9) | The current frequency of the platform's ES health assessment. |
| **ES Attributes** | 1 | 17 | Byte 0: *HOST_MANAGED_ES_ATTRIBUTES* (2, 0x82) | Attributes for the host-managed Energy Source. |
| **ES Technology** | 1 | 18 | | Bitmask; see below. |

The **ES Technology** bitmask definition follows.

| Bit | Definition |
| --- | ---------- |
| [0] | Undefined |
| [1] | Super capacitor |
| [2] | Battery |
| [3] | Hybrid capacitor |
| [7:4] | Reserved |
