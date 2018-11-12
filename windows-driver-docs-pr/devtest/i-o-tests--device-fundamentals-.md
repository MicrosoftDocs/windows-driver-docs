---
title: I/O Tests (Device Fundamentals)
description: The Device Fundamentals I/O tests perform basic I/O testing on the specified devices.
ms.assetid: 4FF125BE-846A-4A93-9B4F-C6BC469EA0AF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# I/O Tests (Device Fundamentals)


The Device Fundamentals I/O tests perform basic I/O testing on the specified devices.

## <span id="io_tests"></span><span id="IO_TESTS"></span>I/O tests


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Test</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Device_I_O_"></span><span id="device_i_o_"></span><span id="DEVICE_I_O_"></span>Device I/O</p></td>
<td align="left"><p>This test performs basic I/O testing on devices.</p>
<p><strong>Test binary:</strong> Devfund_Device_IO.wsc</p>
<p><strong>Test method:</strong> DeviceIO</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>IOPeriod</em></p>
<p><em>IOType</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Simple_I_O_stress_test_with_I_O_process_termination"></span><span id="simple_i_o_stress_test_with_i_o_process_termination"></span><span id="SIMPLE_I_O_STRESS_TEST_WITH_I_O_PROCESS_TERMINATION"></span>Simple I/O stress test with I/O process termination</p></td>
<td align="left"><p>This test performs simple I/O testing on devices in a separate process and terminates the I/O process after the specified I/O period and test cycles.</p>
<p><strong>Test binary:</strong> Devfund_SimpleIoStress_TermIoProc.wsc</p>
<p><strong>Test method:</strong> SimpleIOStress_TermIoProc</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

[How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398)

[How to test a driver at runtime from a Command Prompt](https://msdn.microsoft.com/windows-drivers/develop/how_to_test_a_driver_at_runtime_from_a_command_prompt)

 

 






