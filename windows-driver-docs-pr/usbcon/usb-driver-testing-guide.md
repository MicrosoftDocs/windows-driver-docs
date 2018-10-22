---
Description: This section describes tools that you can use to test your USB hardware or software, capture traces of operations and other system events, and observe how the USB driver stack responds to a request sent by a client driver or an application.
title: Testing USB hardware, drivers, and apps in Windows
author: windows-driver-content
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Testing USB hardware, drivers, and apps in Windows


This section describes tools that you can use to test your USB hardware or software, capture traces of operations and other system events, and observe how the USB driver stack responds to a request sent by a client driver or an application.

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)</p></td>
<td><p>The Microsoft USB Test Tool (MUTT) is collection of devices for testing interoperability of your USB hardware with the Microsoft USB driver stack. This section provides a brief overview of the different types of MUTT devices, the tests you can run by using the device, and suggests topologies for controller, hub, device, and BIOS/UEFI testing.</p>
<p>To communicate with MUTT devices, you need the MUTT software package. This package contains several test tools and drivers that let hardware test engineers test interoperability of their USB controller or hub with the Microsoft USB driver stack. The test tools validate USB host controller software, hardware (including firmware) and any USB hub that is installed between the host controller and the device.</p></td>
</tr>
<tr class="even">
<td><p>[USB test tools](usb-test-tools.md)</p></td>
<td><p>Describes various tools you can use to test USB devices and drivers.</p></td>
</tr>
<tr class="odd">
<td><p>[Test USB Type-C systems with USB Type-C ConnEx](test-usb-type-c-systems-with-mutt-connex-c.md)</p></td>
<td><p>The USB Type-C Connection Exerciser (USB Type-C ConnEx) hardware board is a custom shield for the Arduino board. The shield provides a four-to-one switch to automate interoperability tests for USB Type-C scenarios.</p></td>
</tr>
<tr class="even">
<td><p>[USB Type-C manual interoperability test procedures](type.md)</p></td>
<td><p>This topic explains how to test the interoperability of USB Type-C enabled systems and Windows. It provides guidelines for device and system manufacturers to perform various functional and stress tests on systems and devices that expose a USB Type-C connector. It assumes that the reader is familiar with the official USB specification and xHCI interoperability test procedures, which can be downloaded from USB.ORG.</p></td>
</tr>
<tr class="odd">
<td><p>[How to prepare the test system to run MUTT test tools](mutt-testing-options.md)</p></td>
<td><p>Before using MUTT devices, you must prepare the test system.</p></td>
</tr>
<tr class="even">
<td><p>[How to run stress and transfer performance tests for MUTT devices](how-to-run-stress-and-transfer-and-super-mutt-performance-tests-for-mutt-devices.md)</p></td>
<td><p>Read how to run stress and transfer and SuperMUTT performance tests.</p>
<p>Stress and transfer tests are geared towards saturating the bus protocol and the host controller software. These tests perform several simultaneous I/O transfers and cancellations to the MUTT device. The MUTT firmware is programmed to fail transfers during these tests. These failures emulate error conditions that the controller or USB driver stack are exposed to under stressful USB conditions.</p></td>
</tr>
<tr class="odd">
<td><p>[How to run system power devfund tests in Visual Studio for MUTT devices](how-to-run-device-fundamental-tests-in-visual-studio-for-connected-mutt-devices.md)</p></td>
<td><p>Describes the Device Fundamental tests that you must run for MUTT devices that are attached to available ports, to perform stress and transfer tests and system power tests.</p>
<p>These tests perform simple device transfers at the same time that they perform system power events. Note that devfund tests can only be run on Windows 8. You cannot [run stress and transfer tests](how-to-run-stress-and-transfer-and-super-mutt-performance-tests-for-mutt-devices.md) and the system power tests simultaneously. Perform those tests on separate systems. However, you can switch between stress transfer and system power tests. To do so, complete the first set of tests, reboot the machine, and then follow the instructions of the next test.</p></td>
</tr>
<tr class="even">
<td><p>[BIOS/UEFI testing with the MUTT devices](how-to-run-bios-uefi-testing-with-the-mutt-device.md)</p></td>
<td><p>BIOS/UEFI testing validates USB boot and handoff of the controller to the operating system.</p></td>
</tr>
<tr class="odd">
<td><p>[Test USB hubs with MUTT devices](how-to-run-hub-testing-with-the-mutt-device.md)</p></td>
<td><p>The goal of hub testing is to generate a complete set of possible traffic patterns from devices. You can test disconnect scenarios by adding an upstream SuperMUTT Pack.</p></td>
</tr>
<tr class="even">
<td><p>[Test USB host controllers with MUTT devices](how-to-run-controller-and-device-testing-with-the-mutt-device.md)</p></td>
<td><p>The goal of controller testing is to generate a complete set of possible traffic patterns from hubs and devices. This allows the internal state of controller and its firmware to be fully tested. MUTT devices can help the test by providing an automated method to generate various possible protocol scenarios.</p></td>
</tr>
<tr class="odd">
<td><p>[Test USB devices with MUTT devices](tools-in-the-package.md)</p></td>
<td><p>The goal of device testing is to test device usage against various hub scenarios and systems power states. The MUTT Pack and SuperMUTT Pack devices can provide a way to expose the device to connect/disconnect scenarios across different hub and system power state scenarios. Test the device when it is attached to a USB 2.0 and 3.0 hubs in the MUTT Pack and SuperMUTT Pack devices, respectively.</p></td>
</tr>
<tr class="even">
<td><p>[Windows Hardware Lab Kit Tests for USB](windows-hardware-certification-kit-tests-for-usb.md)</p></td>
<td><p>The Windows Hardware Lab Kit (HLK) tests can be used for additional testing of Systems, USB host controllers, hubs, and devices. These tests cover basic device functionality, reliability, and compatibility with Windows.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[Universal Serial Bus (USB)](https://msdn.microsoft.com/library/windows/hardware/ff538930)  



