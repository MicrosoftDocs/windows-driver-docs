---
title: CPUStress Tests (Device Fundamentals)
description: The CpuStress tests perform device I/O testing with different processor utilization levels.
ms.assetid: E546C3A3-89E6-450B-90D3-4F349A3EC495
---

# CPUStress Tests (Device Fundamentals)


The CpuStress tests perform device I/O testing with different processor utilization levels.

## <span id="cpu_stress_tests"></span><span id="CPU_STRESS_TESTS"></span>CpuStress


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
<td align="left"><p><span id="Device_I_O_with_alternating_processor_utilization_levels"></span><span id="device_i_o_with_alternating_processor_utilization_levels"></span><span id="DEVICE_I_O_WITH_ALTERNATING_PROCESSOR_UTILIZATION_LEVELS"></span>Device I/O with alternating processor utilization levels</p></td>
<td align="left"><p>This test does device I/O testing while alternating between high (HPU) and low (LPU) processor utilization levels.</p>
<p><strong>Test binary:</strong> Devfund_ProcUtil_PingPong_With_IO.wsc</p>
<p><strong>Test method:</strong> Device_IO_With_Varying_ProcUtil</p>
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>DQ</em></p>
<p><em>PingPongPeriod</em></p>
<p><em>HPU</em></p>
<p><em>LPU</em></p>
<p><em>TestCycles</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Device_I_O_with_a_fixed_processor_utilization_level"></span><span id="device_i_o_with_a_fixed_processor_utilization_level"></span><span id="DEVICE_I_O_WITH_A_FIXED_PROCESSOR_UTILIZATION_LEVEL"></span>Device I/O with a fixed processor utilization level</p></td>
<td align="left"><p>This test does device I/O testing with the processor utilization (PU) level set to a fixed percentage.</p>
<p><strong>Test binary:</strong> Devfund_ProcUtil_PingPong_With_IO.wsc</p>
<p><strong>Test method:</strong> Device_IO_With_Fixed_ProcUtil</p>
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>DQ</em></p>
<p><em>IOPeriod</em></p>
<p><em>PU</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Device_PNP_with_a_fixed_processor_utilization_level"></span><span id="device_pnp_with_a_fixed_processor_utilization_level"></span><span id="DEVICE_PNP_WITH_A_FIXED_PROCESSOR_UTILIZATION_LEVEL"></span>Device PNP with a fixed processor utilization level</p></td>
<td align="left"><p>This test does device PNP testing with the processor utilization (PU) level set to a fixed percentage.</p>
<p><strong>Test binary:</strong> Devfund_ProcUtil_PingPong_With_IO.wsc</p>
<p><strong>Test method:</strong> Device_PNP_With_Fixed_ProcUtil</p>
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>PU</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Sleep_with_fixed_processor_utilization_"></span><span id="sleep_with_fixed_processor_utilization_"></span><span id="SLEEP_WITH_FIXED_PROCESSOR_UTILIZATION_"></span>Sleep with fixed processor utilization</p></td>
<td align="left"><p>This test cycles the system through various sleep states with the processor utilization level set to a fixed percentage.</p>
<p><strong>Test binary:</strong> Devfund_ProcUtil_PingPong_With_IO.wsc</p>
<p><strong>Test method:</strong> Sleep_With_Fixed_ProcUtil</p>
<p><strong>Parameters:</strong> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p>
<p><em>TestCycles</em></p>
<p><em>PU</em></p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20CPUStress%20Tests%20%28Device%20Fundamentals%29%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





