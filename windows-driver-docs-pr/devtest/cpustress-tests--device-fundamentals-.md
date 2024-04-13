---
title: CPUStress Tests (Device Fundamentals)
description: The CpuStress tests perform device I/O testing with different processor utilization levels.
ms.date: 04/20/2017
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
<p><strong>Parameters:</strong> - see <a href="/windows-hardware/drivers" data-raw-source="[How to select and configure the Device Fundamentals tests](../develop/how-to-select-and-configure-the-device-fundamental-tests.md)">Device Fundamentals Test Parameters</a></p>
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
<p><strong>Parameters:</strong> - see <a href="/windows-hardware/drivers" data-raw-source="[How to select and configure the Device Fundamentals tests](../develop/how-to-select-and-configure-the-device-fundamental-tests.md)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>IOPeriod</em></p>
<p><em>PU</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Device_PNP_with_a_fixed_processor_utilization_level"></span><span id="device_pnp_with_a_fixed_processor_utilization_level"></span><span id="DEVICE_PNP_WITH_A_FIXED_PROCESSOR_UTILIZATION_LEVEL"></span>Device PNP with a fixed processor utilization level</p></td>
<td align="left"><p>This test does device PNP testing with the processor utilization (PU) level set to a fixed percentage.</p>
<p><strong>Test binary:</strong> Devfund_ProcUtil_PingPong_With_IO.wsc</p>
<p><strong>Test method:</strong> Device_PNP_With_Fixed_ProcUtil</p>
<p><strong>Parameters:</strong> - see <a href="/windows-hardware/drivers" data-raw-source="[How to select and configure the Device Fundamentals tests](../develop/how-to-select-and-configure-the-device-fundamental-tests.md)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>PU</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Sleep_with_fixed_processor_utilization_"></span><span id="sleep_with_fixed_processor_utilization_"></span><span id="SLEEP_WITH_FIXED_PROCESSOR_UTILIZATION_"></span>Sleep with fixed processor utilization</p></td>
<td align="left"><p>This test cycles the system through various sleep states with the processor utilization level set to a fixed percentage.</p>
<p><strong>Test binary:</strong> Devfund_ProcUtil_PingPong_With_IO.wsc</p>
<p><strong>Test method:</strong> Sleep_With_Fixed_ProcUtil</p>
<p><strong>Parameters:</strong> - see <a href="/windows-hardware/drivers" data-raw-source="[How to select and configure the Device Fundamentals tests](../develop/how-to-select-and-configure-the-device-fundamental-tests.md)">Device Fundamentals Test Parameters</a></p>
<p><em>TestCycles</em></p>
<p><em>PU</em></p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


[How to How to test a driver at runtime using Visual Studio](/windows-hardware/drivers)

[How to select and configure the Device Fundamentals tests](../develop/how-to-select-and-configure-the-device-fundamental-tests.md)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md)

[How to test a driver at runtime from a Command Prompt](/windows-hardware/drivers)

