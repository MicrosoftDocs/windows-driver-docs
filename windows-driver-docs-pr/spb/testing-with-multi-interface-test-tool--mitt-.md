---
title: Test with Multi Interface Test Tool (MITT)
description: The MITT is a test tool for validating hardware and software for simple peripheral buses, such as UART, I2C, SPI, and GPIO.
ms.assetid: B847568F-4872-4FF7-BB73-E45A6FFF8249
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Test with Multi Interface Test Tool (MITT)


The Multiple Interface Test Tool (MITT) is a test tool for validating hardware and software for simple peripheral buses, such as UART, I2C, SPI, and GPIO. MITT uses the FPGA development board and includes a software package with firmware, test binaries, and drivers that provide an inexpensive test solution.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919811" data-raw-source="[Buy hardware for using MITT](https://msdn.microsoft.com/library/windows/hardware/dn919811)">Buy hardware for using MITT</a></p></td>
<td><p>To you use Multiple Interface Test Tool (MITT), order you need a MITT board and bus-specific adapter boards that plug into ports on the MITT board. The type of adapter board depends on the bus you want to test.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919779" data-raw-source="[Get started with MITT](https://msdn.microsoft.com/library/windows/hardware/dn919779)">Get started with MITT</a></p></td>
<td><p>To run MITT tests, you must install the MITT firmware on a new MITT board. These steps describe how to update the MITT firmware and prepare the host machine for running MITT tests.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919776" data-raw-source="[Audio playback fidelity tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919776)">Audio playback fidelity tests in MITT</a></p></td>
<td><p>The audio module on the MITT board is used to detect errors that occur at the transport level of the audio device by detecting sine wave frequency accuracy (at zero cross) and counting instances where the frequency or offset is incorrect. Lack of a signal or missed packets results in a shifted waveform that is audible and detectable automatically via this mechanism.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919778" data-raw-source="[Capacitive touch tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919778)">Capacitive touch tests in MITT</a></p></td>
<td><p>Capacitive touch tests in the MITT software package require MCATT (Microsoft Capacitive Applications Test Tool). It&#39;s an automation tool for validating capacitive based touch hardware (touchpads and touchscreens). MCATT includes a simple interface for programming the MCATT device and automated tests. You can use the tests to detect ghost points or determine the time table for the first touch input to propagate after system wake.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919780" data-raw-source="[GPIO tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919780)">GPIO tests in MITT</a></p></td>
<td><p>GPIO test modules that are included in the MITT software package can be used to test the following buttons volume up, volume down, power, and rotation lock. You can use these tests to detect issues with the GPIO drivers and microcontrollers and determine if the systems response to a short or long push is the desired response. The lines attached to the buttons are physically pulled low by the MITT board.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919852" data-raw-source="[I2C controller tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919852)">I2C controller tests in MITT</a></p></td>
<td><p>I²C test modules that are included in the MITT software package can be used to test data transfers for an I²C controller and its driver. The MITT board acts as a client device connected to the I²C bus.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919873" data-raw-source="[SPI tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919873)">SPI tests in MITT</a></p></td>
<td><p>SPI test modules that are included in the MITT software package can be used to test data transfers for a SPI controller on the system under test and its driver. The MITT board acts as a client device connected to the SPI bus.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/dn919875" data-raw-source="[UART tests in MITT](https://msdn.microsoft.com/library/windows/hardware/dn919875)">UART tests in MITT</a></p></td>
<td><p>The MITT software package includes tests for validating data transfers to a UART controller and its driver. The MITT board’s UART interface acts as a UART loopback device.</p></td>
</tr>
</tbody>
</table>

 

 

 




