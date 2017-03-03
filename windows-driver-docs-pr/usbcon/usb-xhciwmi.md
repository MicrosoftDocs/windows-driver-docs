---
Description: 'XHCIWMI is a tool for diagnostic purposes. This tool only runs on Windows 8 and gathers information when the device is attached to an xHCI port and Windows loads the Microsoft USB 3.0 driver stack.'
MS-HAID: 'buses.usb\_xhciwmi'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB XHCIWMI
author: windows-driver-content
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20XHCIWMI%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


