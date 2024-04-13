---
title: Writing a WDTF Simple I/O Plug-In for your Device
description: To get the most benefit from the Device Fundamental tests, your device should have a Simple I/O plug-in that can perform simple I/O to your device.
ms.date: 04/20/2017
---

# Writing a WDTF Simple I/O plug-in for your device

To get the most benefit from the [Device Fundamental tests](../develop/how-to-select-and-configure-the-device-fundamental-tests.md), your device should have a Simple I/O plug-in that can perform simple I/O to your device. This can be one of the default Simple I/O plugs that come with WDTF or one that you wrote. To see if your device type is supported and to determine if there are specific requirements for testing, refer to [Provided WDTF Simple I/O plug-ins](provided-wdtf-simpleio-plug-ins.md).

If you have configured a test computer for testing using Visual Studio, you can run a test that returns a list of devices on the test computer that have WDTF Simple I/O support. If your device is not supported, you can create one in Visual Studio using the **WDTF Simple I/O Action Plug-in** template. For information, see [How to customize I/O for your device using the WDTF Simple I/O Action Plug-in](to-customize-i-o-for-your-device-using-the-wdtf-simple-i-o-action-plug-in.md). For information about setting up a test computer, see [Provision a computer for driver deployment and testing (WDK 10)](../gettingstarted/provision-a-target-computer-wdk-8-1.md).

## In this section

- [How to determine if a custom WDTF Simple I/O Action Plug-in is required for your device](test-your-device-to-see-if-you-need-to-customize-the-wdtf-simple-i-o-action-plug-in.md)

- [How to customize I/O for your device using the WDTF Simple I/O Action Plug-in](to-customize-i-o-for-your-device-using-the-wdtf-simple-i-o-action-plug-in.md)

- [Provided WDTF SimpleIO plug-ins](provided-wdtf-simpleio-plug-ins.md)
