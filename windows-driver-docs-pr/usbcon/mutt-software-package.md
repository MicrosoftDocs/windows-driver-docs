---
Description: The MUTT software package contains several tools to be used with MUTT devices. The suite of tools include firmware upgrade application, driver installation package, and applications that send transfers to the device.
title: Tools in the MUTT software package
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tools in the MUTT software package


**Last updated:**

-   September, 2018

**Applies to:**

-   Windows 10
-   Windows 8.1
-   Windows 8

The MUTT software package contains several tools to be used with [MUTT devices](microsoft-usb-test-tool--mutt--devices.md). The suite of tools include firmware upgrade application, driver installation package, and applications that send transfers to the device.

## Download MUTT Software Package


The Microsoft USB Test Tool (MUTT) software package contains test tools for hardware test engineers to test interoperability of their USB controller or hub with the Microsoft USB driver stack. The included documentation provides a brief overview of the different types of MUTT hardware and suggests topologies for controller, hub, device, and BIOS/UEFI testing. The documentation also contains procedural information about how to run the tests, trace events in the USB driver stack, and capture information in the kernel debugger.

File name: muttv2_8.msi

7.0 MB

[![download the mutt software package](images/download.png)](http://go.microsoft.com/fwlink/p/?LinkId=786621)

## Version Updates

Changes for version 2.8

-   Updated USB Type-C SuperMUTT firmware for improved compatibility with HLK UCSI tests.

Changes for version 2.7

- Updated USB Type-C SuperMUTT firmware, tools, and documentation. Compatible with HLK UCSI tests.

Changes for version 2.4

-   Includes the initial drop of the USB Type-C SuperMUTT firmware, tools, and documentation.

Changes for version 2.2

-   Includes USB Connection Exerciser Tools

Changes for version 2.0

-   Updated SuperMUTT firmware to version 45.
-   Updated WinUSB transfer tests.

Changes for version 1.9.1

-   In version 1.9 and earlier, on some systems, the SuperMutt device enumerated at high speed (when connected to an xHCI controller) after the system resumed from S4. Version 1.9.1 corrects that issue.

Changes for version 1.9

-   SuperMUTT loads WinUSB driver by default by reading the MS OS descriptor of the device.
-   SuperMUTT with WinUSB supports selective suspend by default.

## Tools in the package


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Test Tool</th>
<th>Description</th>
<th>Filename</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="usbtcd.md" data-raw-source="[USBTCD](usbtcd.md)">USBTCD</a></td>
<td><ul>
<li>USBTCD is an application (USBTCD.exe) that communicates with a kernel-mode driver (USBTCD.sys) and performs common USB data transfer scenarios with various length transfer sizes.</li>
<li>The driver installation files are USBTCD .sys, and USBTCD.inf.</li>
<li>FX3Perf.bat measures the read performance of a USB controller to which a SuperMUTT device is attached.</li>
</ul></td>
<td><p>USBTCD.exe</p>
<p>USBTCD.sys</p>
<p>USBTCD.inf</p>
<p>FX3Perf.bat</p>
<p>UsbTCDTransferTest.bat</p></td>
</tr>
<tr class="even">
<td></td>
<td><ul>
<li>Gathers information about the USB 3.0 host controllers and USB 3.0 hubs on the system to identify problematic firmware revisions and suggest updates.</li>
<li>We recommend that you run this test before any other test to filter known issues. Runs only on Windows 8.</li>
</ul></td>
<td>xhciwmi.exe</td>
</tr>
<tr class="odd">
<td><a href="usb-xhciwmi.md" data-raw-source="[XHCIWMI](usb-xhciwmi.md)">XHCIWMI</a><a href="usblpm-tool.md" data-raw-source="[USBLPM](usblpm-tool.md)">USBLPM</a></td>
<td><ul>
<li>Monitors the U0/U1/U2/U3 power states of USB 3.0 ports.</li>
<li>It verifies that transitions between U0/U1/U2 occur correctly.</li>
</ul></td>
<td>UsbLPM.exe</td>
</tr>
<tr class="even">
<td><a href="usbstress.md" data-raw-source="[USBStress](usbstress.md)">USBStress</a></td>
<td><ul>
<li>The USBStress application communicates with a kernel-mode driver (usbstress.sys) and performs common USB data transfer scenarios.</li>
<li>The driver installation files are usbstress.sys, and usbstress.inf.</li>
<li>The UsbStressTest file runs all data transfer tests after the driver is installed.</li>
</ul></td>
<td><p>usbstress.exe</p>
<p>usbstress.inf</p>
<p>usbstress.sys</p>
<p>UsbStressTest.bat</p></td>
</tr>
<tr class="odd">
<td><a href="muttutil.md" data-raw-source="[MuttUtil](muttutil.md)">MuttUtil</a></td>
<td><ul>
<li>Updates the firmware of the test devices.</li>
<li>Installs drivers for MUTT devices.</li>
<li>Verifies that the devices are installed without errors.</li>
<li>Changes the operating bus speed of the device.</li>
<li>Configures the device to send a resume wake signal after a specified time period.</li>
<li>For the MUTT Pack, it sets the hub to operate at full or high speed; as a single-TT or multi-TT hub.</li>
</ul></td>
<td><p>MuttUtil.exe</p></td>
</tr>
<tr class="even">
<td><a href="how-to-retrieve-information-about-a-usb-device.md" data-raw-source="[USB hardware verifier](how-to-retrieve-information-about-a-usb-device.md)">USB hardware verifier</a></td>
<td>Displays all hardware events on the console.</td>
<td>USB3HWVerifierAnalyzer.exe</td>
</tr>
</tbody>
</table>

 

## Related topics
[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)  



