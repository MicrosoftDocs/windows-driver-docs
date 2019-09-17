---
title: Component Firmware Update (CPU) standalone tool sample
description: Component Firmware Update (CPU) standalone tool sample TBD
ms.date: 09/10/2019
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Component Firmware Update (CPU) standalone tool sample

This tool reads an offer file, firmware image file in srec bin format and passes the firmware to a device.  The tool is also capable of searching for the device based on the protocol settings and requesting/printing FW Version information.
It requires a protocol settings text csv file to be passed as an argument.

## Usage
&nbsp;&nbsp;&nbsp;&nbsp;FwUpdateCfu.exe version \<protocolSettingsPath\> (to retrieve version of device)<br>
&nbsp;&nbsp;&nbsp;&nbsp;FwUpdateCfu.exe update \<protocolSettingsPath\> \<offerfile\> \<binfile\> [forceIgnoreVersion] [forceReset]<br><br>
  
## Example protocol settings doc
&nbsp;&nbsp;&nbsp;&nbsp;#instructions:<br>
&nbsp;&nbsp;&nbsp;&nbsp;#Fill in csv tag and the value in hex for each item<br>
&nbsp;&nbsp;&nbsp;&nbsp;#order not important<br>
&nbsp;&nbsp;&nbsp;&nbsp;#only the first 2 fields will be looked at so values after that are considered comments<br>
&nbsp;&nbsp;&nbsp;&nbsp;VID,0x045e,#mandatory (each vendor must maintain their own Vendor defined Utility Page collections)<br>
&nbsp;&nbsp;&nbsp;&nbsp;PID,0x07cd,#optional<br>
&nbsp;&nbsp;&nbsp;&nbsp;USAGEPAGE,0xFF07,#mandatory (each vendor must maintain their own Vendor defined Utility Page collections)<br>
&nbsp;&nbsp;&nbsp;&nbsp;USAGECOLLECTION,0x31,#optional (if you don't specify, the tool will attempt to talk to all devices with matching UsagePage/Vid/Pid on the usages specified below)<br>
&nbsp;&nbsp;&nbsp;&nbsp;VERSION_FEATURE_USAGE,0x62,#mandatory for all procedures<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONTENT_OUTPUT_USAGE,0x61,#mandatory for fwUpdate procedure<br>
&nbsp;&nbsp;&nbsp;&nbsp;CONTENT_RESPONSE_INPUT_USAGE,0x66,#mandatory for fwUpdate procedure<br>
&nbsp;&nbsp;&nbsp;&nbsp;OFFER_OUTPUT_USAGE,0x8e,#mandatory for fwUpdate procedure<br>
&nbsp;&nbsp;&nbsp;&nbsp;OFFER_RESPONSE_INPUT_USAGE,0x8a,#mandatory for fwUpdate procedure<br>

