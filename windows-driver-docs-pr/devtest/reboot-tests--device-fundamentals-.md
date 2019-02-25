---
title: Reboot Tests (Device Fundamentals)
description: The Device Fundamentals Reboot tests run I/O on the specified devices, before and after, or during system restarts.
ms.assetid: 71EBEC60-C99F-412D-8FC5-2DD9209CC92D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reboot Tests (Device Fundamentals)


The Device Fundamentals Reboot tests run I/O on the specified devices, before and after, or during system restarts.

## <span id="reboot_tests"></span><span id="REBOOT_TESTS"></span>Reboot tests


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
<td align="left"><p><span id="Critical_Reboot_Restart_with_I_O_before_and_after"></span><span id="critical_reboot_restart_with_i_o_before_and_after"></span><span id="CRITICAL_REBOOT_RESTART_WITH_I_O_BEFORE_AND_AFTER"></span>Critical Reboot Restart with I/O before and after</p></td>
<td align="left"><p>This test runs I/O on devices before and after a critical system reboot.</p>
<p><strong>Test binary:</strong> Devfund_Critical_RebootRestart_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> Critical_Reboot_Restart_With_IO_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Critical_Reboot_Restart_with_I_O_during"></span><span id="critical_reboot_restart_with_i_o_during"></span><span id="CRITICAL_REBOOT_RESTART_WITH_I_O_DURING"></span>Critical Reboot Restart with I/O during</p></td>
<td align="left"><p>This test starts Simple I/O on devices, initiates a critical reboot with I/O running, and runs SimpleI/O again after the reboot.</p>
<p><strong>Test binary:</strong> Devfund_Critical_RebootRestart_With_IO_During.wsc</p>
<p><strong>Test method:</strong> Critical_Reboot_Restart_With_IO_During</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Reboot_Restart_with_I_O_before_and_after"></span><span id="reboot_restart_with_i_o_before_and_after"></span><span id="REBOOT_RESTART_WITH_I_O_BEFORE_AND_AFTER"></span>Reboot Restart with I/O before and after</p></td>
<td align="left"><p>This test runs I/O on devices before and after a system reboot.</p>
<p><strong>Test binary:</strong> Devfund_RebootRestart_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> Reboot_Restart_With_IO_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Reboot_restart_with_I_O_during"></span><span id="reboot_restart_with_i_o_during"></span><span id="REBOOT_RESTART_WITH_I_O_DURING"></span>Reboot restart with I/O during</p></td>
<td align="left"><p>This test starts Simple I/O on devices, initiates a reboot with I/O running, and runs SimpleI/O again after the reboot.</p>
<p><strong>Test binary:</strong> Devfund_RebootRestart_With_IO_During.wsc</p>
<p><strong>Test method:</strong> Reboot_Restart_With_IO_During</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p></td>
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

 

 






