---
title: Sleep Tests (Device Fundamentals)
description: The Device Fundamentals Sleep tests run I/O and PnP operations on the specified devices, before and after, or during system sleep state transitions.
ms.assetid: 38B65078-B436-4C24-B973-032702DB9CBE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sleep Tests (Device Fundamentals)


The Device Fundamentals Sleep tests run I/O and PnP operations on the specified devices, before and after, or during system sleep state transitions. The Sleep tests ensure that the device under test permits the system to be cycled through all of the supported sleep states. Additionally, it ensures that the device is still functional after these state changes through Simple I/O stress testing.

## Sleep tests


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
<td align="left"><p><span id="Critical_Sleep_with_I_O_before_and_after"></span><span id="critical_sleep_with_i_o_before_and_after"></span><span id="CRITICAL_SLEEP_WITH_I_O_BEFORE_AND_AFTER"></span>Critical Sleep with I/O before and after</p></td>
<td align="left"><p>This test performs critical sleep state transitions on the system and performs I/O on devices before and after each sleep state cycle.</p>
<p><strong>Test binary:</strong> Devfund_Critical_Sleep_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> Critical_Reboot_Restart_With_IO_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ResumeDelay</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Critical_Sleep_with_I_O_during"></span><span id="critical_sleep_with_i_o_during"></span><span id="CRITICAL_SLEEP_WITH_I_O_DURING"></span>Critical Sleep with I/O during</p></td>
<td align="left"><p>This test performs critical sleep state transitions on the system and performs I/O on devices.</p>
<p><strong>Test binary:</strong> Devfund_Critical_Sleep_With_IO_During.wsc</p>
<p><strong>Test method:</strong> Critical_Sleep_With_IO_During</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ResumeDelay</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Sleep_and_PNP__disable_and_enable__with_I_O_Before_and_After"></span><span id="sleep_and_pnp__disable_and_enable__with_i_o_before_and_after"></span><span id="SLEEP_AND_PNP__DISABLE_AND_ENABLE__WITH_I_O_BEFORE_AND_AFTER"></span>Sleep and PNP (disable and enable) with I/O Before and After</p></td>
<td align="left"><p>This test cycles the system through various sleep states and performs I/O and basic PnP (disable/enable) on devices before and after each sleep state cycle.</p>
<p>For more information, see <a href="#about-the-sleep-and-pnp-disable-and-enable-with-io-before-and-after-test" data-raw-source="[About the Sleep and PNP disable and enable with IO Before and After test](#about-the-sleep-and-pnp-disable-and-enable-with-io-before-and-after-test)">About the Sleep and PNP disable and enable with IO Before and After test</a>.</p>
<p><strong>Test binary:</strong> Devfund_Sleep_PNP_DisableEnable_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> Sleep_PNP_DisableEnable_With_IO_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ResumeDelay</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Sleep_with_I_O_Before_and_After"></span><span id="sleep_with_i_o_before_and_after"></span><span id="SLEEP_WITH_I_O_BEFORE_AND_AFTER"></span>Sleep with I/O Before and After</p></td>
<td align="left"><p>This test cycles the system through various sleep states and performs I/O on devices before and after each sleep state cycle.</p>
<p>For more information, see <a href="#about-the-sleep-with-io-before-and-after-test" data-raw-source="[About the Sleep with IO Before And After test](#about-the-sleep-with-io-before-and-after-test)">About the Sleep with IO Before And After test</a>.</p>
<p><strong>Test binary:</strong> Devfund_Sleep_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> Sleep_With_Io_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ResumeDelay</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Sleep_with_I_O_during"></span><span id="sleep_with_i_o_during"></span><span id="SLEEP_WITH_I_O_DURING"></span>Sleep with I/O during</p></td>
<td align="left"><p>This test cycles the system through various sleep states and performs I/O on devices.</p>
<p><strong>Test binary:</strong> Devfund_Sleep_With_IO_During.wsc</p>
<p><strong>Test method:</strong> Sleep_With_IO_During</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ResumeDelay</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
</tbody>
</table>

 

## About the Sleep and PNP disable and enable with IO Before and After test


This test does the following:

1.  Verifies that the test device and its descendants are not reporting any device problem codes.
2.  Tests I/O on the test device and its descendants using the WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398) for more information.
3.  Sends the test system into its first supported sleep state and resumes the system from sleep after some time.
4.  Verifies that the test device and its descendants are not reporting any device problem codes.
5.  Tests I/O on the test device and its descendants using the WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398) for more information.
6.  If the test device is can be disabled, the test disables and enables the test device using WDTF PnP action interfaces, see [**IWDTFPNPAction2::DisableDevice**](https://msdn.microsoft.com/library/windows/hardware/hh451068) and [**IWDTFPNPAction2::EnableDevice**](https://msdn.microsoft.com/library/windows/hardware/hh451082) methods for more information.
7.  Verifies that the test device and its descendants are not reporting any device problem codes.
8.  Tests I/O on the test device and its descendants using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398) for more information.
9.  Repeats step 3-8 for each supported sleep state of the test system.
10. Repeats step 1-9 several times.

## About the Sleep with IO Before And After test


This test does the following:

1.  Verifies that there are no devices on the system reporting device problem codes.
2.  Tests I/O on every device on the system using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398) for more information.
3.  Sends the test system into its first supported sleep state and resumes the system from sleep after some time.
4.  Verifies that there are no devices on the system reporting device problem codes.
5.  Tests I/O on every device on the system using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398) for more information.
6.  Repeats steps 3 - 5 for each supported sleep state of the test system.
7.  Repeats steps 1 - 6 several times.

## Related topics


[How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

[How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398)

[How to test a driver at runtime from a Command Prompt](https://msdn.microsoft.com/windows-drivers/develop/how_to_test_a_driver_at_runtime_from_a_command_prompt)

 

 






