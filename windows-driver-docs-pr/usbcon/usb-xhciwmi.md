---
Description: XHCIWMI is a tool for diagnostic purposes. This tool only runs on Windows 8 and gathers information when the device is attached to an xHCI port and Windows loads the Microsoft USB 3.0 driver stack.
title: USB XHCIWMI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB XHCIWMI


XHCIWMI is a tool for diagnostic purposes. This tool only runs on Windows 8 and gathers information when the device is attached to an xHCI port and Windows loads the Microsoft USB 3.0 driver stack.

## XHCIWMI


Run the following command in an elevated Command Prompt window:

**Xhciwmi.exe**

The tool shows the current firmware revision and information about the controller in the command window. Run the following command to verify the firmware of the controller and hub against known issues:

**Xhciwmi.exe –verify**

We recommend using the **–verify** option for checking the controller and the connected hubs.

## Related topics
[USB test tools](usb-test-tools.md)  
[Tools in the MUTT software package](mutt-software-package.md)  
[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)  



