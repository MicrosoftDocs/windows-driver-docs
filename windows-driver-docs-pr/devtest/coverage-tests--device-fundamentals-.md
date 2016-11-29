---
title: Coverage Tests (Device Fundamentals)
description: The Device Fundamental Coverage tests monitor and report on the various I/O request packets (IRPs) that enter or leave a driver stack for specified devices.
ms.assetid: 950B124B-8B2D-4A54-AFC3-E90BBDD8D1AF
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
<p><em>DQ</em> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p></td>
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
<p><em>DQ</em> - see [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Coverage%20Tests%20%28Device%20Fundamentals%29%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





