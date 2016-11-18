---
title: I/O Tests (Device Fundamentals)
description: The Device Fundamentals I/O tests perform basic I/O testing on the specified devices.
ms.assetid: 4FF125BE-846A-4A93-9B4F-C6BC469EA0AF
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
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
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
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20I/O%20Tests%20%28Device%20Fundamentals%29%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





