---
title: Component Firmware Update (CPU) standalone tool sample
description: Component Firmware Update (CPU) standalone tool sample
ms.date: 07/21/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Component Firmware Update (CPU) standalone tool sample

The CFU tool sample sends firmware image files to a device in need of an update. Before sending the firmware image, the tool sends several commands to the device with firmware offers. Only if the device accepts, the tool sends the firmware payload. The communication between the tool and the device is in accordance with the [CFU protocol](https://github.com/Microsoft/CFU/tree/master/Documentation/CFU-Protocol), an open source specification (included with CFU) based on the HID protocol.

This tool reads an offer file, firmware image file in SREC bin format, and passes the firmware to a device.  It is also capable of searching for the device based on the protocol settings and requesting/printing firmware version information.

It requires a protocol settings text csv file to be passed as an argument.

## Usage

`FwUpdateCfu.exe version \<protocolSettingsPath\>` (to retrieve version of device)

`FwUpdateCfu.exe update \<protocolSettingsPath\> \<offerfile\> \<binfile\> [forceIgnoreVersion] [forceReset]`
  
## Example protocol settings

```
#instructions:
#Fill in csv tag and the value in hex for each item
#order not important
#only the first 2 fields will be looked at so values after that are considered comments
VID,0x045e,#mandatory (each vendor must maintain their own Vendor defined Utility Page collections)
PID,0x07cd,#optional
USAGEPAGE,0xFF07,#mandatory (each vendor must maintain their own Vendor defined Utility Page collections)
USAGECOLLECTION,0x31,#optional (if you don't specify, the tool will attempt to talk to all devices with matching UsagePage/Vid/Pid on the usages specified below)
VERSION_FEATURE_USAGE,0x62,#mandatory for all procedures
CONTENT_OUTPUT_USAGE,0x61,#mandatory for fwUpdate procedure
CONTENT_RESPONSE_INPUT_USAGE,0x66,#mandatory for fwUpdate procedure
OFFER_OUTPUT_USAGE,0x8e,#mandatory for fwUpdate procedure
OFFER_RESPONSE_INPUT_USAGE,0x8a,#mandatory for fwUpdate procedure
```
