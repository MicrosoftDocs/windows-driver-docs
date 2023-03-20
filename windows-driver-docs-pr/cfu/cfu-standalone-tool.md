---
title: Component Firmware Update (CFU) standalone tool
description: Provides information on the Component Firmware Update (CFU) standalone tool that sends firmware update image files to a device.
ms.date: 03/17/2023
---

# Component Firmware Update (CFU) standalone tool

The [CFU standalone tool](https://github.com/microsoft/CFU/tree/master/Tools/ComponentFirmwareUpdateStandAloneToolSample) sends firmware image update files to a device. It can be used to test your firmware update on your device during development and before uploading it to Windows Update.

> [!NOTE]
> CFU is available in Windows 10, version 2004 (Windows 10 May 2020 Update) and later versions.

Before sending the firmware image, the tool sends several commands to the device with firmware offers. Only if the device accepts, the tool sends the firmware payload. The communication between the tool and the device is in accordance with the [CFU protocol](cfu-specification.md), an open source specification (included with CFU) based on the HID protocol.

This tool reads an offer file and passes a firmware update image file to a device.  It is also capable of searching for the device based on the protocol settings and requesting/printing firmware version information.

It requires a protocol settings text .csv file to be passed as an argument.

## Tool usage command format examples

```console
FwUpdateCfu.exe version \<protocolSettingsPath\> (to retrieve version of device)
```

```console
FwUpdateCfu.exe update \<protocolSettingsPath\> \<offerfile\> \<binfile\> [forceIgnoreVersion] [forceReset]
```

## Example protocol settings (in .csv file)

```text
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
