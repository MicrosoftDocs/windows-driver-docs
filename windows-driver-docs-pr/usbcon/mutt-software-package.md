---
Description: The MUTT software package contains several tools to be used with MUTT devices. The suite of tools include firmware upgrade application, driver installation package, and applications that send transfers to the device.
title: Tools in the MUTT software package
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Tools in the MUTT software package


**Last updated:**

-   March, 2016

**Applies to:**

-   Windows 10
-   Windows 8.1
-   Windows 8

The MUTT software package contains several tools to be used with [MUTT devices](microsoft-usb-test-tool--mutt--devices.md). The suite of tools include firmware upgrade application, driver installation package, and applications that send transfers to the device.

## Download MUTT Software Package


The Microsoft USB Test Tool (MUTT) software package contains test tools for hardware test engineers to test interoperability of their USB controller or hub with the Microsoft USB driver stack. This paper provides a brief overview of the different types of MUTT hardware and suggests topologies for controller, hub, device, and BIOS/UEFI testing. The paper contains procedural information about how to run the tests, trace events in the USB driver stack, and capture information in the kernel debugger.

File name: muttv22.msi

4.82 MB

[![download the mutt software package](images/download.png)](http://go.microsoft.com/fwlink/p/?LinkId=786621)

## Version Updates


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
<td>[USBTCD](usbtcd.md)</td>
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
<td>[XHCIWMI](usb-xhciwmi.md)[USBLPM](usblpm-tool.md)</td>
<td><ul>
<li>Monitors the U0/U1/U2/U3 power states of USB 3.0 ports.</li>
<li>It verifies that transitions between U0/U1/U2 occur correctly.</li>
</ul></td>
<td>UsbLPM.exe</td>
</tr>
<tr class="even">
<td>[USBStress](usbstress.md)</td>
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
<td>[MuttUtil](muttutil.md)</td>
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
<td>[USB hardware verifier](how-to-retrieve-information-about-a-usb-device.md)</td>
<td>Displays all hardware events on the console.</td>
<td>USB3HWVerifierAnalyzer.exe</td>
</tr>
</tbody>
</table>

 

## Related topics
[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Tools%20in%20the%20MUTT%20software%20package%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


