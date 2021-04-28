---
title: Download the MITT software package
description: Download the MITT software package.
ms.date: 04/27/2021
ms.localizationpriority: medium
---

# Download the MITT software package

The MITT software package contains several tools to be used to test simple peripheral buses such as I2C, SPI, and GPIO with the MITT board. The suite of tools include utilities to update firmware, send requests to simulate test cases, and test driver packages, test the functionality of the bus, its controller and devices connected to the bus.

**Filename**: MITT.msi

**Size**: 20.2 MB

[**Download the MITT software package**](https://download.microsoft.com/download/7/7/0/7703f03c-9d1f-45fc-a625-9647dc495ee2/mitt.msi)

## Tools in the software package

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Modules</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>MuttUtil</p></td>
<td><p>MuttUtil.exe</p>
<ul>
<li>Sends requests to communicate with various programmable blocks on the MITT board, such as the GPIO, I2C, SPI interfaces.</li>
<li>Updates the firmware on the MITT board.</li>
</ul>
<p>MuttUtil.dll is the user mode library that sends requests to the MITT board, which are initiated by MuttUtil.exe.</p></td>
</tr>
<tr class="even">
<td><p>MITTI2CTest.dll</p>
<p>MITTSPITest.dll</p>
<p>WITTTest driver package</p>
<p>SPBCmd.exe</p></td>
<td><ul>
<li><p>MITTI2CTest.dll</p>
<p>Test binary for I2C controller and bus verification.</p></li>
<li><p>MITTSPITTest.dll</p>
<p>Test binary for SPI controller and bus that validates bus-level activity.</p></li>
<li><p>WITTTest driver package</p>
<p>Installation (.inf), catalog (.cat), and binary (.sys) for the test driver for devices connected to simple peripheral buses.</p></li>
<li><p>SPBCmd.exe</p>
<p>Sends requests to the test driver to manually validate data transfers over I2C and SPI buses.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>WinUSB driver package</p></td>
<td><p>Installation (.inf), catalog (.cat), and binary (.sys) for the WinUSB driver required to update MITT firmware to run tests included in the MITT software package.</p></td>
</tr>
<tr class="even">
<td><p>WDTFMittSimpleIoAction.dll</p>
<p>AudioUnitSimpleIo.dll</p>
<p>SimpleIO_MITT_Audio_Sample.vbs</p>
<p>GpioSimpleIoExtension.dll</p>
<p>SimpleIO_MITT_GPIO_Sample.vbs</p>
<p>McattSimpleIoExtension.dll</p>
<p>SimpleIO_MITT_MCATT_Sample.vbs</p></td>
<td><ul>
<li>WDTFMittSimpleIoAction.dll is a helper module.</li>
<li>SimpleIO module for audio testing.</li>
<li>SimpleIO module for GPIO button testing.</li>
<li>SimpleIO module for MCATT testing.</li>
</ul></td>
</tr>
</tbody>
</table>

> [!NOTE]
> To run the VBS files, you must install Windows Device Testing Framework (WDTF). WDTF is installed with the Windows Driver Kit (WDK).

## Related topics

[Get started with MITT](/windows-hardware/drivers/spb/get-started-with-mitt---)
