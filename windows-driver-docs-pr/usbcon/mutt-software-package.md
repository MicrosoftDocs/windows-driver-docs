---
title: Tools in the MUTT software package
description: The MUTT software package contains several tools to be used with MUTT devices. The suite of tools include a firmware upgrade application, driver installation package, and applications that send transfers to the device.
ms.date: 02/14/2023
---

# Tools in the MUTT software package

The MUTT software package contains several tools to be used with [MUTT devices](microsoft-usb-test-tool--mutt--devices.md). The suite of tools include a firmware upgrade application, driver installation package, and applications that send transfers to the device.

## Download MUTT Software Package

The Microsoft USB Test Tool (MUTT) software package contains test tools for hardware test engineers to test interoperability of their USB controller or hub with the Microsoft USB driver stack. The included documentation provides a brief overview of the different types of MUTT hardware and suggests topologies for controller, hub, device, and BIOS/UEFI testing. The documentation also contains procedural information about how to run the tests, trace events in the USB driver stack, and capture information in the kernel debugger.

**[Download the mutt software package.](https://go.microsoft.com/fwlink/p/?LinkId=786621)**

## Test tool descriptions

| Test Tool | Description | Filename |
|---|---|---|
| [USBTCD](usbtcd.md) | <ul><li>USBTCD is an application (USBTCD.exe) that communicates with a kernel-mode driver (USBTCD.sys) and performs common USB data transfer scenarios with various length transfer sizes.</li><li>The driver installation files are USBTCD .sys, and USBTCD.inf.</li><li>FX3Perf.bat measures the read performance of a USB controller to which a SuperMUTT device is attached.</li></ul> | USBTCD.exe<br><br>USBTCD.sys<br><br>USBTCD.inf<br><br>FX3Perf.bat<br><br>UsbTCDTransferTest.bat |
| [XHCIWMI](usb-xhciwmi.md) | <ul><li>Gathers information about the USB 3.0 host controllers and USB 3.0 hubs on the system to identify problematic firmware revisions and suggest updates.</li><li>We recommend that you run this test before any other test to filter known issues. Runs only on Windows 8.</li></ul> | xhciwmi.exe |
| [USBLPM](usblpm-tool.md) | <ul><li>Monitors the U0/U1/U2/U3 power states of USB 3.0 ports.</li><li>It verifies that transitions between U0/U1/U2 occur correctly.</li></ul> | UsbLPM.exe |
| [USBStress](usbstress.md) |  <ul><li>The USBStress application communicates with a kernel-mode driver (usbstress.sys) and performs common USB data transfer scenarios.</li><li>The driver installation files are usbstress.sys, and usbstress.inf.</li><li>The UsbStressTest file runs all data transfer tests after the driver is installed.</li></ul> | usbstress.exe<br><br>usbstress.inf<br><br>usbstress.sys<br><br>UsbStressTest.bat |
| [MuttUtil](muttutil.md) | <ul><li>Updates the firmware of the test devices.</li><li>Installs drivers for MUTT devices.</li><li>Verifies that the devices are installed without errors.</li><li>Changes the operating bus speed of the device.</li><li>Configures the device to send a resume wake signal after a specified time period.</li><li>For the MUTT Pack, it sets the hub to operate at full or high speed; as a single-TT or multi-TT hub.</li></ul> | MuttUtil.exe |
| [USB hardware verifier](how-to-retrieve-information-about-a-usb-device.md) | Displays all hardware events on the console. | USB3HWVerifierAnalyzer.exe |

## Related topics

- [USB](../index.yml)
- [Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)
