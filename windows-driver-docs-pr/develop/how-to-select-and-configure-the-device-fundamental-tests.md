---
ms.assetid: DDAF6D33-46D8-4A04-A3DC-C9FE26ABD003
title: How to select and configure the Device Fundamentals tests
description: The WDK for Windows 8 provides a driver testing framework that includes a set of tests called the Device Fundamentals tests.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to select and configure the Device Fundamentals tests

The WDK for Windows 8 provides a driver testing framework that includes a set of tests called the Device Fundamentals tests. The Device Fundamentals tests are a collection of tests that are used both internally at Microsoft for testing the drivers and driver samples that ship with Windows and the WDK, and externally as part of the [Windows Certification Program for Hardware](http://go.microsoft.com/fwlink/p/?linkid=8705). You can run the tests from your development environment. When you run the tests, you can use the same parameters that are used for Windows Certification testing, or you can configure and customize the run-time parameters according to your testing and debugging needs.

## <span id="Getting_the_most_from_the_Device_Fundamentals_tests"></span><span id="getting_the_most_from_the_device_fundamentals_tests"></span><span id="GETTING_THE_MOST_FROM_THE_DEVICE_FUNDAMENTALS_TESTS"></span>Getting the most from the Device Fundamentals tests


To get the most benefit from the Device Fundamentals tests, your device must be supported by the default I/O plug-ins. To see whether your device type is supported and to determine whether there are specific requirements for testing, refer to [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/Library/Windows/Hardware/Hh781398). The Device Fundamentals test also include a utility you can use to test your device to see whether it is supported. If your device is not supported, you can create a WDTF Simple I/O plug-in. in Visual Studio. For more information, see [How to customize I/O for your device using the WDTF Simple I/O Action Plug-in](https://msdn.microsoft.com/Library/Windows/Hardware/Hh706277).

## <span id="About_the_Device_Fundamentals_Tests"></span><span id="about_the_device_fundamentals_tests"></span><span id="ABOUT_THE_DEVICE_FUNDAMENTALS_TESTS"></span>About the Device Fundamentals Tests


The WDK provides the Device Fundamentals tests in two configurations, Basic and Certification. In both configurations, you can edit the test parameters to vary the length of the test, the number of test cycles to perform, and other test parameters, depending upon how you want to test the targeted devices or drivers. The Basic configuration is intended for general driver and device testing and debugging. Use the Basic configuration early on and throughout the development cycle. The tests in the Basic configuration have the same settings that are used in the Windows Certification testing, with the exception of having a shorter run time. In the Certification configuration, the tests have the same settings that are used in the Windows Certification testing. Use the Certification configuration to verify readiness for testing your device or driver for the [Windows Certification Program for Hardware](http://go.microsoft.com/fwlink/p/?linkid=8705).

The [Device Fundamentals Tests](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673011) include tests in the following categories.

-   [CHAOS Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673008)
-   [Coverage Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673009)
-   [CPUStress Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673010)
-   [Driver Install Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673012)
-   [I/O Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673013)
-   [Penetration Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673014)
-   [PNP Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673015)
-   [Reboot Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673016)
-   [Sleep Tests (Device Fundamentals)](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673017)
-   [Utility](#utility_tests)
-   [Driver Verifier](#utility_tests)

### <span id="Setting_the_run-time_test_parameters"></span><span id="setting_the_run-time_test_parameters"></span><span id="SETTING_THE_RUN-TIME_TEST_PARAMETERS"></span>Setting the run-time test parameters

You can edit the run-time parameters for many of the Device Fundamentals tests. In the Driver Test Group window, an arrow (») next to a test name indicates that the test has parameters that you can change. Click the arrow (») to display the run-time parameters.

One of the most useful parameters is *DQ*, which specifies the target device to test. The default value (**IsDevice**) tests all of the devices on the target computer. The *DQ* parameter takes a [**WDTF**](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547) [SDEL](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539571) query that identifies the target devices. You can specify a particular device for testing, for example:

**DeviceID=’USB\\ROOT\_HUB\\4&1CD5D022&0’** selects only the device for testing with the specified **DeviceID**.

For more information about *DQ* and the other run-time parameters, see [Device Fundamentals test parameters](#DevFund_Params).

## <span id="DevFund_Params"></span><span id="devfund_params"></span><span id="DEVFUND_PARAMS"></span>Device Fundamentals Test Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="DQ"></span><span id="dq"></span><em>DQ</em></p></td>
<td align="left"><p>Identifies the device or devices that should be used for testing. The <em>DQ</em> parameter takes a <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547" data-raw-source="[&lt;strong&gt;WDTF&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547)"><strong>WDTF</strong></a><a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff539571" data-raw-source="[SDEL](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539571)">SDEL</a> query that identifies the target devices. This query can be very flexible and it can be used to express any number of devices, from a single device to all devices in the system.</p>
<p>Common examples:</p>
<p></p>
<dl>
<dt><span id="To_test_all_devices_that_were_installed_with_a_specific_INF_File_"></span><span id="to_test_all_devices_that_were_installed_with_a_specific_inf_file_"></span><span id="TO_TEST_ALL_DEVICES_THAT_WERE_INSTALLED_WITH_A_SPECIFIC_INF_FILE_"></span>To test all devices that were installed with a specific INF File:</dt>
<dd><p><strong>INF::FileName=</strong><em>INF_File_Name</em></p>
<p>For example, <strong>INF::OriginalInfFileName=&#39;%InfFileName%&#39;</strong></p>
<p>This is the default value.</p>
</dd>
<dt><span id="To_test_a_device_with_a_specific_Device_Id__"></span><span id="to_test_a_device_with_a_specific_device_id__"></span><span id="TO_TEST_A_DEVICE_WITH_A_SPECIFIC_DEVICE_ID__"></span>To test a device with a specific Device Id: </dt>
<dd><p><strong>DeviceId=’</strong><em>DeviceId</em><strong>’</strong></p>
<p>For example, <strong>DeviceID=’USB\ROOT_HUB\4&amp;1CD5D022&amp;0’</strong></p>
</dd>
<dt><span id="_To_test_a_device_with_a_specific_interface_"></span><span id="_to_test_a_device_with_a_specific_interface_"></span><span id="_TO_TEST_A_DEVICE_WITH_A_SPECIFIC_INTERFACE_"></span> To test a device with a specific interface:</dt>
<dd><p><strong>Interfaces::</strong><em>InterfaceGUID</em></p>
</dd>
<dt><span id="To_test_a_device_with_a_specific_driver_letter_"></span><span id="to_test_a_device_with_a_specific_driver_letter_"></span><span id="TO_TEST_A_DEVICE_WITH_A_SPECIFIC_DRIVER_LETTER_"></span>To test a device with a specific driver letter:</dt>
<dd><p><strong>Volume::DriverLetter=’</strong><em>DriveLetter</em><strong>’</strong></p>
<p>For example, <strong>Volume::DriverLetter=’c:\’</strong></p>
</dd>
<dt><span id="To_test_a_device_with_a_specific_driver____"></span><span id="to_test_a_device_with_a_specific_driver____"></span><span id="TO_TEST_A_DEVICE_WITH_A_SPECIFIC_DRIVER____"></span>To test a device with a specific driver: </dt>
<dd><p><strong>DriverBinaryNames=</strong><em>mydriver.sys</em></p>
</dd>
<dt><span id="____To_test_all_device_of_a_specific_device_Class___________________"></span><span id="____to_test_all_device_of_a_specific_device_class___________________"></span><span id="____TO_TEST_ALL_DEVICE_OF_A_SPECIFIC_DEVICE_CLASS___________________"></span> To test all device of a specific device Class: </dt>
<dd><p>For example, <strong>Class=CDROM</strong> would test all device of class CDROM.</p>
<p>For example, <strong>ClassGUID= {36fc9e60-c465-11cf-8056-444553540000}</strong> would test all the devices whose class GUID matches the specified GUID. In this case, the GUID is for the USB class.</p>
</dd>
</dl></td>
</tr>
<tr class="even">
<td align="left"><p><span id="DoPoolCheck"></span><span id="dopoolcheck"></span><span id="DOPOOLCHECK"></span><em>DoPoolCheck</em></p></td>
<td align="left"><p>True or False. Monitors the driver&#39;s use of the paged and nonpaged system memory pools by using pool tags and lookaside lists. This option also monitors changes in the number of exceptions handled which might indicate errors in exception handling.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="ChangeBufferProtectionFlags"></span><span id="changebufferprotectionflags"></span><span id="CHANGEBUFFERPROTECTIONFLAGS"></span><em>ChangeBufferProtectionFlags</em></p></td>
<td align="left"><p>True or False. Changes the memory protection flags of buffers passed to the tested device. The memory protection flags alternates between no access, read-only, and read-only with page guard.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="DoSimpleIO"></span><span id="dosimpleio"></span><span id="DOSIMPLEIO"></span><em>DoSimpleIO</em></p></td>
<td align="left"><p>True or False. Runs SimpleI/O (if found) on test devices before and after performing PNP operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="DoConcurrentIO"></span><span id="doconcurrentio"></span><span id="DOCONCURRENTIO"></span><em>DoConcurrentIO</em></p></td>
<td align="left"><p>True or False. Uses <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547" data-raw-source="[WDTF](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547)">WDTF</a> concurrent I/O interface to send I/O requests to target device stacks while performing PnP operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="FillZeroPageWithNull"></span><span id="fillzeropagewithnull"></span><span id="FILLZEROPAGEWITHNULL"></span><em>FillZeroPageWithNull</em></p></td>
<td align="left"><p>True or False. Maps the zero page and fills it with NULL values. This test identifies drivers that do not verify a pointer reference before dereferencing the pointer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="FuzzTestPeriod"></span><span id="fuzztestperiod"></span><span id="FUZZTESTPERIOD"></span><em>FuzzTestPeriod</em></p></td>
<td align="left"><p>Fuzz test period in minutes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="HPU"></span><span id="hpu"></span><em>HPU</em></p></td>
<td align="left"><p>Specifies the high processor utilization percentage.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Impersonate"></span><span id="impersonate"></span><span id="IMPERSONATE"></span><em>Impersonate</em></p></td>
<td align="left"><p>True or False. Runs the test as a user without administrator privileges.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="IOPeriod"></span><span id="ioperiod"></span><span id="IOPERIOD"></span><em>IOPeriod</em></p></td>
<td align="left"><p>Specifies the I/O period in minutes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="IOType"></span><span id="iotype"></span><span id="IOTYPE"></span><em>IOType</em></p></td>
<td align="left"><p>Specifies the type of I/O stress test: SimpleIOStressEx or SimpleIOStressProc (I/O in a separate process).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="LPU"></span><span id="lpu"></span><em>LPU</em></p></td>
<td align="left"><p>Specifies the low processor utilization percentage</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MaxInBuffer"></span><span id="maxinbuffer"></span><span id="MAXINBUFFER"></span><em>MaxInBuffer</em></p></td>
<td align="left"><p>Specifies the maximum size, in bytes, of the input buffers that the test passes to the driver in FSCTLs (or IOCTLs for IOCTL tests).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="MinInBuffer"></span><span id="mininbuffer"></span><span id="MININBUFFER"></span><em>MinInBuffer</em></p></td>
<td align="left"><p>Specifies the minimum size, in bytes, of the input buffers that the test passes to the driver in FSCTLs (or IOCTLs for IOCTL tests).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MaxOutBuffer"></span><span id="maxoutbuffer"></span><span id="MAXOUTBUFFER"></span><em>MaxOutBuffer</em></p></td>
<td align="left"><p>Specifies the maximum size, in bytes, of the output buffers that the test passes to the driver in FSCTLs (or IOCTLs for IOCTL tests).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="MinOutBuffer"></span><span id="minoutbuffer"></span><span id="MINOUTBUFFER"></span><em>MinOutBuffer</em></p></td>
<td align="left"><p>Specifies the minimum size, in bytes, of the output buffers that the test passes to the driver in FSCTLs (or IOCTLs for IOCTL tests).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MaxRandomCalls"></span><span id="maxrandomcalls"></span><span id="MAXRANDOMCALLS"></span><em>MaxRandomCalls</em></p></td>
<td align="left"><p>Specifies the maximum number of calls that the test issues.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="MaxTailoredCalls"></span><span id="maxtailoredcalls"></span><span id="MAXTAILOREDCALLS"></span><em>MaxTailoredCalls</em></p></td>
<td align="left"><p>Specifies the maximum number of calls that the test issues during the tailored random test.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MaxDeviceType"></span><span id="maxdevicetype"></span><span id="MAXDEVICETYPE"></span><em>MaxDeviceType</em></p></td>
<td align="left"><p>Specifies the maximum value of the DeviceType field in the FSCTLs (or IOCTLs for IOCTL tests). The maximum possible value is 65535.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="MinDeviceType"></span><span id="mindevicetype"></span><span id="MINDEVICETYPE"></span><em>MinDeviceType</em></p></td>
<td align="left"><p>Specifies the minimum value of the DeviceType field in the FSCTLs (or IOCTLs for IOCTL tests). The minimum possible value is 0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MaxFunctionCode"></span><span id="maxfunctioncode"></span><span id="MAXFUNCTIONCODE"></span><em>MaxFunctionCode</em></p></td>
<td align="left"><p>Specifies the maximum value of the FunctionCode field in the FSCTLs (or IOCTLs for IOCTL tests). The maximum possible value is 4095.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="MinFunctionCode"></span><span id="minfunctioncode"></span><span id="MINFUNCTIONCODE"></span><em>MinFunctionCode</em></p></td>
<td align="left"><p>Specifies the minimum value of the FunctionCode field in the FSCTLs (or IOCTLs for IOCTL tests). The minimum possible value is 0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="PU"></span><span id="pu"></span><em>PU</em></p></td>
<td align="left"><p>Specifies the processor utilization percentage</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="PingPongPeriod"></span><span id="pingpongperiod"></span><span id="PINGPONGPERIOD"></span><em>PingPongPeriod</em></p></td>
<td align="left"><p>Specifies the ping pong period in minutes; the time the processor alternates between high (HPU) and low (LPU) processor utilization levels.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="ResumeDelay"></span><span id="resumedelay"></span><span id="RESUMEDELAY"></span><em>ResumeDelay</em></p></td>
<td align="left"><p>The delay time (in seconds) after the machine resumes from sleep mode and before the next I/O cycle starts. The delay time is necessary to allow devices to restore their working state (renew IP address for network card and so on).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="TestCycles"></span><span id="testcycles"></span><span id="TESTCYCLES"></span><em>TestCycles</em></p></td>
<td align="left"><p>Specifies the number of test cycles (iterations) to perform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="WDTFREMOTESYSTEM"></span><span id="wdtfremotesystem"></span><em>WDTFREMOTESYSTEM</em></p></td>
<td align="left"><p>This parameter is required only if the device under test, or one of its child devices, is a wired network adapter that does not have an IPv6 gateway address. If this parameter is required on your network, you must provide an IPv6 address that the test network adapter can ping to test network.</p>
<p>Example: <strong>fe80::78b6:810:9c12:46cd</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Wpa2PskAesSsid"></span><span id="wpa2pskaesssid"></span><span id="WPA2PSKAESSSID"></span><em>Wpa2PskAesSsid</em></p></td>
<td align="left"><p>This parameter is required only if the device under test or one of its child devices is a WiFi adapter. Provide the SSID of a WPA2 AES WiFi network that the test can use to test the WiFi adapter.</p>
<p>Default value: <strong>kitstestssid</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Wpa2PskPassword"></span><span id="wpa2pskpassword"></span><span id="WPA2PSKPASSWORD"></span><em>Wpa2PskPassword</em></p></td>
<td align="left"><p>This parameter is required only if the device under test or one of its child devices is a WiFi adapter. Provide password of the WPA2 AES WiFi network that is specified by using the Wpa2PskAesSsid parameter.</p>
<p>Default value: <strong>password</strong></p></td>
</tr>
</tbody>
</table>

 

## <span id="utility_tests"></span><span id="UTILITY_TESTS"></span>Utility tests


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
<td align="left"><p><span id="Display_devices_that_have_WDTF_Simple_I_O_plug-ins"></span><span id="display_devices_that_have_wdtf_simple_i_o_plug-ins"></span><span id="DISPLAY_DEVICES_THAT_HAVE_WDTF_SIMPLE_I_O_PLUG-INS"></span>Display devices that have WDTF Simple I/O plug-ins</p></td>
<td align="left"><p><strong>Parameters:</strong> None</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Display_devices_that_have_Driver_Verifier_enabled"></span><span id="display_devices_that_have_driver_verifier_enabled"></span><span id="DISPLAY_DEVICES_THAT_HAVE_DRIVER_VERIFIER_ENABLED"></span>Display devices that have Driver Verifier enabled</p></td>
<td align="left"><p><strong>Parameters:</strong> None</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Display_devices"></span><span id="display_devices"></span><span id="DISPLAY_DEVICES"></span>Display devices</p></td>
<td align="left"><p><strong>Parameters:</strong> None</p></td>
</tr>
</tbody>
</table>

 

## <span id="dvrf_tests"></span><span id="DVRF_TESTS"></span>Driver Verifier


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
<td align="left"><p><span id="Disable_Driver_Verifier"></span><span id="disable_driver_verifier"></span><span id="DISABLE_DRIVER_VERIFIER"></span>Disable Driver Verifier</p></td>
<td align="left"><p>Disables <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448)">Driver Verifier</a> on the test computer.</p>
<p><strong>Parameters:</strong> None</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Enable_Driver_Verifier"></span><span id="enable_driver_verifier"></span><span id="ENABLE_DRIVER_VERIFIER"></span>Enable Driver Verifier</p></td>
<td align="left"><p>You can use this test to enable <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448)">Driver Verifier</a> for all drivers of a device (or devices) on the test computer.</p>
<p><strong>Parameters:</strong> - See <a href="https://msdn.microsoft.com/library/windows/hardware/ff545470" data-raw-source="[Driver Verifier Options](https://msdn.microsoft.com/library/windows/hardware/ff545470)">Driver Verifier Options</a>.</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


* [How to How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md)
* [Device Fundamentals Tests](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673011)
* [Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/Library/Windows/Hardware/Hh781398)
* [How to customize I/O for your device using the WDTF Simple I/O Action Plug-in](https://msdn.microsoft.com/Library/Windows/Hardware/Hh706277)
 

 






