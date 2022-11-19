---
title: Get NVDIMM-N Identification (Function Index 1)
description: This function returns device-specific information.
ms.date: 11/18/2022
---

# Get NVDIMM-N Identification (Function Index 1)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function returns device-specific information. It should be implemented using an NVDIMM ACPI Namespace.

Registers are defined in the [Byte Addressable Energy Backed Interface specification](https://www.jedec.org/category/keywords/nvdimm-n).

## Input

### Arg3

None.

## Output

| Field | Byte length | Byte offset | Register | Description |
| ----- | ----------- | ----------- | -------- | ----------- |
| **Status**                   | 4 | 0 |  | See [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |
| **Specification Revision**   | 1 | 4 | Byte 0: *SPECREV* (0, 0x06) | The specification version supported by the module. |
| **Number of Standard Pages** | 1 | 5 | Byte 0: *STD_NUM_PAGES* (0, 0x01) | The number of standard defined pages supported by the module. |
| **First Vendor Page**        | 1 | 6 | Byte 0: *VENDOR_START_PAGES* (0, 0x02) | The starting page number for vendor-specific pages. |
| **Number of Vendor Pages**   | 1 | 7 | Byte 0: *VENDOR_NUM_PAGES* (0, 0x03) |The number of vendor-specific pages supported by the module.
| **Hardware Revision**        | 4 | 8 | Byte 0: *HWREV* (0, 0x04); Bytes 1-3: Reserved. | The controller hardware revision. |
| **Firmware Revision**        | 2 | 12 | Byte 0: *SLOTX_FWREV0* (0, 0x07/0x09); Byte 1: *SLOTX_FWREV1* (0, 0x08/0x0A) | Firmware version of the active firmware slot. |
| **Current Firmware Slot**    | 1 | 14 | Byte 0: Bits [7:4] of *FW_SLOT_INFO* (3, 0x42) register (*RUNNING_FW_SLOT*). | The slot number of the running firmware image. |
| **Firmware Slot Count**      | 1 | 15 |  | The number of firmware slots available. For JEDEC-compliant devices, this field shall be 2. |
| **Capabilities**             | 1 | 16 | Byte 0: *CAPABILITIES0* (0, 0x10); Byte 1: *CAPABILITIES1* (0, 0x11) | Information regarding the capabilities supported by the module. |
| **Supported Backup Triggers**     | 1 | 17 | Byte 0: *CSAVE_TRIGGER_SUPPORT* (0, 0x16) | The module's supported save triggers. |
| **Maximum Operation Retry Count** | 1 | 18 | Byte 0: *HOST_MAX_OPERATION_RETRY* (0, 0x15) | The recommended retry count to the host if a save, restore or erase operation fails or exceeds the maximum timeout value. |
| **Supported Notification Events** | 1 | 19 | Byte 0: *EVENT_NOTIFICATION_SUPPORT* (0, 0x17) | Event information the module will generate notifications for. |
| **Save Operation Timeout**        | 4 | 20 | Byte 0: *CSAVE_TIMEOUT0* (0, 0x18); Byte 1: *CSAVE_TIMEOUT1* (0, 0x19); Bytes 2-3: Reserved. | The worst case Save completion latency in milliseconds or seconds.
| **Restore Operation Timeout**     | 4 | 24 | Byte 0: *RESTORE_TIMEOUT0* (0, 0x1C); Byte 1: *RESTORE_TIMEOUT1* (0, 0x1D); Bytes 2-3: Reserved. | The worst case Restore completion latency in milliseconds or seconds. |
| **Erase Operation Timeout**       | 4 | 28 | Byte 0: *ERASE_TIMEOUT0* (0, 0x1E); Byte 1: *ERASE_TIMEOUT1* (0, 0x1F); Bytes 2-3: Reserved. | The worst case Erase completion latency in milliseconds or seconds. |
| **Arm Operation Timeout**         | 4 | 32 | Byte 0: *ARM_TIMEOUT0* (0, 0x20); Byte 1: *ARM_TIMEOUT1* (0, 0x21); Bytes 2-3: Reserved. | The worst case Arm completion latency in milliseconds or seconds. |
| **Firmware Operations Timeout**   | 4 | 36 | Byte 0: *FIRMWARE_OPS_TIMEOUT0* (0, 0x22); Byte 1: *FIRMWARE_OPS_TIMEOUT1* (0, 0x23); Bytes 2-3: Reserved. | The worst case Firmware Operations completion latency in milliseconds or seconds.
| **Abort Operation Timeout**       | 4 | 40 | Byte 0: *ABORT_CMD_TIMEOUT* (0, 0x24); Byte 1: Reserved; Bytes 2-3: Reserved. | Maximum time to abort a running command, in milliseconds or seconds. |
| **Minimum Operating Temperature** | 2 | 44 | Byte 0: *MIN_OPERATING_TEMP0* (0, 0x38); Byte 1: *MIN_OPERATING_TEMP1* (0, 0x39) | The minimum operating temperature in degrees Celsius. |
| **Maximum Operation Temperature** | 2 | 46 | Byte 0: *MAX_OPERATING_TEMP0* (0, 0x3A); Byte 1: *MAX_OPERATING_TEMP1* (0, 0x3B) | The maximum operating temperature in degrees Celsius.
| **Region Block Size** | 4 | 48 | Byte 0: *REGION_BLOCK_SIZE* (0, 0x32) | The region size in multiples of 32 bytes. |
