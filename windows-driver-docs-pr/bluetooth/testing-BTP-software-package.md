---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) overview.
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# Tools in the BTP software package

The BTP software package contains several tools to be used for testing the Bluetooth.


## Download the BTP Software Package ##
The Bluetooth Test Platform (BTP) software package contains test tools for hardware test engineers to test interoperability of their Bluetooth enabled peripherals and systems with the Microsoft Bluetooth driver stack. The included documentation provides a brief overview of the ways to configure your hardware and suggests topologies for best test coverage. The documentation also contains procedural information about how to run the tests, trace events in the Bluetooth driver stack, and capture information in the kernel debugger.

## Version Updates ##
Changes for version xx.yy
- Moving BTP from private preview to public.  Woohoo!!  ;)


## Tools in the package ##

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



### Known issues ###

- Power: If the device is plugged into a non-powered hub or VCC is not able to supply 5V intermittent failures may be seen. Please remedy by using a powered USB hub or use a 9V AC-DC Barrel adapter.

- Stress tests: If the test is run in a tight loop there an issue where the radios will not have finished disconnecting after the pairing test reports success before the next test attempts to pair resulting in a failure.