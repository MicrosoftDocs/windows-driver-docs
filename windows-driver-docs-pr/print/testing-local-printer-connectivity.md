---
title: Testing Local Printer Connectivity
author: windows-driver-content
description: Testing Local Printer Connectivity
ms.assetid: 08a16c04-fc64-4e19-b7f2-7a078bc151a2
keywords: ["testing drivers WDK printer", "printer drivers WDK , testing", "local printer testing WDK", "connections WDK printer"]
---

# Testing Local Printer Connectivity


This section provides general guidelines for how to test the connectivity of a printer that is connected locally. You can apply these principles to any bus or port to which you connect a print device, although some principles might not apply due to the inherent nature of your bus or port.

**Note**   The following information describes testing on Microsoft Windows XP. Features of other operating system versions, such as control panel applications and menu options, might differ slightly.

 

### Setting Up Device Testing

Before proceeding with any testing of your device, make sure you set up your debugging session as follows to catch any problems you might encounter. See [Debugging Printer Drivers and Spooler Components](debugging-printer-drivers-and-spooler-components.md) for how to properly set up your test environment.

1.  Set up Application Verifier, with the default settings enabled, to monitor Spoolsv.exe. Testing on a wide variety of hardware, including 32- and 64-bit machines, is recommended.

2.  Use the Driver Verifier tool to monitor any kernel-mode drivers that you are using. For printer drivers, be sure to include Win32k.sys. See [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) for information about setting up your test environment to use the tool.

3.  For power management testing, before a device is attached, make sure that your test environment supports all possible system power states and that the device can enter and wake from all states successfully.

The following sections describe the common test scenarios to address when testing a port-connected device.

-   [Device Installation](device-installation.md)

-   [Device Functionality](testing-device-functionality.md)

-   [Device Error States](device-error-states.md)

-   [Power Management](power-management.md)

-   [Stress Testing](stress-testing.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Testing%20Local%20Printer%20Connectivity%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


