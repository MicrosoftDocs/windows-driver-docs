---
title: Start Firmware Update (Function Index 22)
description: This function initiates a firmware update to a particular firmware slot.
ms.date: 11/18/2022
---

# Start Firmware Update (Function Index 22)

This [_DSM Interface for Byte Addressable Energy Backed Function Class (Function Interface 1)](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md) function initiates a firmware update to a particular firmware slot. There can only be one firmware update operation at any given time.

## Input

### Arg3

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Firmware Slot** | 1 | 0 | The firmware slot that is being updated. |

## Output

| Field | Byte length | Byte offset | Description |
| ----- | ----------- | ----------- | ----------- |
| **Status** | 4 | 0 | This function can return the following Function-Specific Error Code: *There is a firmware update operation currently in progress.* For more information, see [_DSM Method Output](-dsm-interface-for-byte-addressable-energy-backed-function-class--function-interface-1-.md). |

## Remarks

The host calls the following firmware functions in order to update & activate the firmware:

1. The host calls Start Firmware Update (Function Index 22) to start the firmware update operation. In this step, the host chooses which firmware slot it's updating.

2. The host repeatedly calls [Send Firmware Update Data (Function Index 23)](send-firmware-update-data--function-index-23-.md) to transfer the data to the device. Each call transmits a region-sized chunk of data; the host is responsible for padding if the last transfer isn't region-sized.

3. The host calls [Finish Firmware Update (Function Index 24)](finish-firmware-update--function-index-24-.md) to signal to the platform that the firmware update operation is over.

4. The host calls [Select Firmware Image Slot (Function Index 25)](select-firmware-image-slot--function-index-25-.md) in order to activate the new firmware image. The update will take effect on the next system reboot.
