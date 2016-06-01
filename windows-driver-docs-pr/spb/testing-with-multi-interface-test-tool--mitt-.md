---
Description: 'The Multiple Interface Test Tool (MITT) is a test tool for validating hardware and software for simple peripheral buses, such as UART, I2C, SPI, and GPIO.'
MS-HAID: 'SPB.testing\_with\_multi\_interface\_test\_tool\_\_mitt\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: 'Test with Multi Interface Test Tool (MITT)'
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
<td><p>[Buy hardware for using MITT](buses.multi_interface_test_tool__mitt__)</p></td>
<td><p>To you use Multiple Interface Test Tool (MITT), order you need a MITT board and bus-specific adapter boards that plug into ports on the MITT board. The type of adapter board depends on the bus you want to test.</p></td>
</tr>
<tr class="even">
<td><p>[Get started with MITT](buses.get_started_with_mitt___)</p></td>
<td><p>To run MITT tests, you must install the MITT firmware on a new MITT board. These steps describe how to update the MITT firmware and prepare the host machine for running MITT tests.</p></td>
</tr>
<tr class="odd">
<td><p>[Audio playback fidelity tests in MITT](buses.audio_playback_fidelity_tests_in_mitt)</p></td>
<td><p>The audio module on the MITT board is used to detect errors that occur at the transport level of the audio device by detecting sine wave frequency accuracy (at zero cross) and counting instances where the frequency or offset is incorrect. Lack of a signal or missed packets results in a shifted waveform that is audible and detectable automatically via this mechanism.</p></td>
</tr>
<tr class="even">
<td><p>[Capacitive touch tests in MITT](buses.capacitive_touch_tests_in_mitt)</p></td>
<td><p>Capacitive touch tests in the MITT software package require MCATT (Microsoft Capacitive Applications Test Tool). It's an automation tool for validating capacitive based touch hardware (touchpads and touchscreens). MCATT includes a simple interface for programming the MCATT device and automated tests. You can use the tests to detect ghost points or determine the time table for the first touch input to propagate after system wake.</p></td>
</tr>
<tr class="odd">
<td><p>[GPIO tests in MITT](buses.gpio_tests_in_mitt)</p></td>
<td><p>GPIO test modules that are included in the MITT software package can be used to test the following buttons volume up, volume down, power, and rotation lock. You can use these tests to detect issues with the GPIO drivers and microcontrollers and determine if the systems response to a short or long push is the desired response. The lines attached to the buttons are physically pulled low by the MITT board.</p></td>
</tr>
<tr class="even">
<td><p>[I2C controller tests in MITT](buses.run_mitt_tests_for_an_i2c_controller_)</p></td>
<td><p>I²C test modules that are included in the MITT software package can be used to test data transfers for an I²C controller and its driver. The MITT board acts as a client device connected to the I²C bus.</p></td>
</tr>
<tr class="odd">
<td><p>[SPI tests in MITT](buses.spi_tests_in_mitt)</p></td>
<td><p>SPI test modules that are included in the MITT software package can be used to test data transfers for a SPI controller on the system under test and its driver. The MITT board acts as a client device connected to the SPI bus.</p></td>
</tr>
<tr class="even">
<td><p>[UART tests in MITT](buses.uart_tests_in_mitt)</p></td>
<td><p>The MITT software package includes tests for validating data transfers to a UART controller and its driver. The MITT board’s UART interface acts as a UART loopback device.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSPB\buses%5D:%20Test%20with%20Multi%20Interface%20Test%20Tool%20%28MITT%29%20%20RELEASE:%20%286/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



