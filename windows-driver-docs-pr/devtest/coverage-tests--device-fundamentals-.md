---
title: Coverage Tests (Device Fundamentals)
description: The Device Fundamental Coverage tests monitor and report on the various I/O request packets (IRPs) that enter or leave a driver stack for specified devices.
ms.assetid: 950B124B-8B2D-4A54-AFC3-E90BBDD8D1AF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Coverage Tests (Device Fundamentals)


The Device Fundamental Coverage tests monitor and report on the various I/O request packets (IRPs) that enter or leave a driver stack for specified devices. The data from the Coverage tests can help identify coverage weaknesses during driver test and verification.

### <span id="coverage_tests"></span><span id="COVERAGE_TESTS"></span>Coverage tests

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
<td align="left"><p><span id="Clear_IRP_coverage_data_"></span><span id="clear_irp_coverage_data_"></span><span id="CLEAR_IRP_COVERAGE_DATA_"></span>Clear IRP coverage data</p></td>
<td align="left"><p>Clears the IRP coverage data.</p>
<p><strong>Test binary:</strong> DriverCoverageClearCoverageData.dll</p>
<p><strong>Test method:</strong> ClearCoverageData</p>
<p><strong>Parameters:</strong> None</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Disable_IRP_coverage_data_collection"></span><span id="disable_irp_coverage_data_collection"></span><span id="DISABLE_IRP_COVERAGE_DATA_COLLECTION"></span>Disable IRP coverage data collection</p></td>
<td align="left"><p>Disables the IRP coverage data collection for device specified by the <em>DQ</em> parameter.</p>
<p><strong>Test binary:</strong> DriverCoverageDisableSupport.dll</p>
<p><strong>Test method:</strong> DisableCoverageDataCollection</p>
<p><strong>Parameters:</strong></p>
<p><em>DQ</em> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Display_collected_IRP_coverage_data._"></span><span id="display_collected_irp_coverage_data._"></span><span id="DISPLAY_COLLECTED_IRP_COVERAGE_DATA._"></span>Display collected IRP coverage data.</p></td>
<td align="left"><p>Displays the IRP coverage data collected up to this point for all devices.</p>
<p><strong>Test binary:</strong> DriverCoverageDisplayCoverage.dll</p>
<p><strong>Test method:</strong> DisplayCoverageData</p>
<p><strong>Parameters:</strong> None</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Display_IRP_coverage_enabled_devices"></span><span id="display_irp_coverage_enabled_devices"></span><span id="DISPLAY_IRP_COVERAGE_ENABLED_DEVICES"></span>Display IRP coverage enabled devices</p></td>
<td align="left"><p>Displays the devices that currently have IRP coverage data collection enabled for them.</p>
<p><strong>Test binary:</strong> DriverCoverageDisplayEnabledDevices.dll</p>
<p><strong>Test method:</strong> DisplayEnabledDevices</p>
<p><strong>Parameters:</strong> None</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_IRP_coverage_data_collection"></span><span id="enable_irp_coverage_data_collection"></span><span id="ENABLE_IRP_COVERAGE_DATA_COLLECTION"></span>Enable IRP coverage data collection</p></td>
<td align="left"><p>Enables IRP coverage data collection for the device specified by the <em>DQ</em> parameter.</p>
<p><strong>Test binary:</strong> DriverCoverageEnableSupport.dll</p>
<p><strong>Test method:</strong> EnableCoverageDataCollection</p>
<p><strong>Parameters:</strong> None</p>
<p><em>DQ</em> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p></td>
</tr>
</tbody>
</table>

 

### <span id="About_the_Coverage_tests"></span><span id="about_the_coverage_tests"></span><span id="ABOUT_THE_COVERAGE_TESTS"></span>About the Coverage tests

The Device Fundamentals coverage tests are based upon the Driver Coverage Toolkit, which was previously available as stand-alone tool in the WDK. For information about how the coverage tests are implemented, see [Driver Coverage Toolkit](driver-coverage-toolkit.md).

## <span id="related_topics"></span>Related topics


[How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

[How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398)

[How to test a driver at runtime from a Command Prompt](https://msdn.microsoft.com/windows-drivers/develop/how_to_test_a_driver_at_runtime_from_a_command_prompt)

 

 






