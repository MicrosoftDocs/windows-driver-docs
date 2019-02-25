---
title: Penetration Tests (Device Fundamentals)
description: The Device Fundamentals Penetration tests perform various forms of input attacks, which are a critical component of security testing. Attack and Penetration testing can help identify vulnerabilities in software interfaces.
ms.assetid: 53EBAF4B-2CEF-492B-98B8-DA199FDFBC46
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Penetration Tests (Device Fundamentals)


The Device Fundamentals Penetration tests perform various forms of input attacks, which are a critical component of security testing. Attack and Penetration testing can help identify vulnerabilities in software interfaces.

## Penetration


The Penetration tests include two categories of tests: Fuzz tests and [I/O Spy](iospy.md) and [I/O Attack](ioattack.md) tests. The Fuzz tests were also a feature of the **Device Path Exceriser** test tool.

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
<td align="left"><p><span id="Disable_I_O_Spy"></span><span id="disable_i_o_spy"></span><span id="DISABLE_I_O_SPY"></span>Disable I/O Spy</p></td>
<td align="left"><p>Disable <a href="iospy.md" data-raw-source="[I/O Spy](iospy.md)">I/O Spy</a> on 1 or more devices.</p>
<p><strong>Test binary:</strong> Devfund_IOSpy_DisableSupport.wsc</p>
<p><strong>Test method:</strong> DisableIoSpy</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="display_i_o_spy-enabled_device"></span>Display I/O Spy-enabled Device</p></td>
<td align="left"><p>Display devices that have <a href="iospy.md" data-raw-source="[I/O Spy](iospy.md)">I/O Spy</a> enabled on them.</p>
<p><strong>Test binary:</strong> Devfund_IOSpy_DisplayEnabledDevices.wsc</p>
<p><strong>Test method:</strong> DisplayIoSpyDevices</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_I_O_Spy_"></span><span id="enable_i_o_spy_"></span><span id="ENABLE_I_O_SPY_"></span>Enable I/O Spy</p></td>
<td align="left"><p>Enable <a href="iospy.md" data-raw-source="[I/O Spy](iospy.md)">I/O Spy</a> on one or more devices.</p>
<p><strong>Test binary:</strong> Devfund_IOSpy_EnableSupport.wsc</p>
<p><strong>Test method:</strong> EnableIoSpy</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>DFD</em> - specifies the path to the IoSpy data file. The default location is %SystemDrive%\DriverTest\IoSpy</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="fuzz_misc_api_test"></span>Fuzz Misc API test</p></td>
<td align="left"><p>The Fuzz Misc API tests are tests that determine whether the driver can handle a variety of common calls from kernel mode drivers.</p>
<p>The tests includes the following tests:</p>
<ul>
<li><p>Calls to <a href="https://msdn.microsoft.com/library/windows/hardware/ff567072" data-raw-source="[&lt;strong&gt;ZwReadFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567072)"><strong>ZwReadFile</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567121" data-raw-source="[&lt;strong&gt;ZwWriteFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567121)"><strong>ZwWriteFile</strong></a>, specifying valid data buffer pointers, varying lengths (including zero), and varying byte offsets, including zero, -1 and 64-bit bytes offsets.</p></li>
<li><p>Calls to cancel I/0 and flush buffers.</p></li>
<li><p>A series of directory query calls using common file information classes with valid user data buffer pointers and varying buffer lengths (including zero).</p></li>
<li><p>Directory query calls similar to those issued by programs running under control of the Virtual DOS Machine (VDM).</p></li>
<li><p>Calls to retrieve the extended attributes of a file with varying buffer sizes and lengths.</p></li>
<li><p>Calls to create and close section objects, with varying section page protection and sectional allocation attributes (committed section, image file section).</p></li>
<li><p>Calls to lock and unlock files.</p></li>
<li><p>Calls to retrieve quota entries for a volume.</p></li>
<li><p>File Attributes Test, a series of file attribute queries with valid pointers to an <strong>ObjectAttributes</strong> structure.</p>
<p>The File Attributes Test has an optional zero-length test. While retrieving the extended attributes of a file, the Fuzz test passes a blank (zero-length) query and an invalid buffer address to the driver.</p></li>
</ul>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test method:</strong> DoMiscAPITest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Fuzz_Misc_API_with_zero-length_query_test"></span><span id="fuzz_misc_api_with_zero-length_query_test"></span><span id="FUZZ_MISC_API_WITH_ZERO-LENGTH_QUERY_TEST"></span>Fuzz Misc API with zero-length query test</p></td>
<td align="left"><p>This test performs the same tests as Fuzz Misc API test and this time passes a blank (zero-length) query and an invalid buffer address to the driver while trying to retrieve the extended attributes of a file.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test method:</strong> DoMiscAPIWithZeroLengthTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="fuzz_open_and_close_test"></span>Fuzz open and close test</p></td>
<td align="left"><p>This test performs thousands of create-open-close sequences.</p>
<p>For detailed information about this test, see <a href="#about-the-fuzz-open-and-close-test" data-raw-source="[About the Fuzz open and close test](#about-the-fuzz-open-and-close-test)">About the Fuzz open and close test</a>.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test method:</strong> DoOpenCloseTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Fuzz_Query_and_Set_File_Information_test_"></span><span id="fuzz_query_and_set_file_information_test_"></span><span id="FUZZ_QUERY_AND_SET_FILE_INFORMATION_TEST_"></span>Fuzz Query and Set File Information test</p></td>
<td align="left"><p>This test issues calls to retrieve and change the object, file, and volume information of devices.</p>
<p>During the <em>Query and Set File Information Test</em>, the Fuzz test issue calls to retrieve and change the object, file, and volume information of devices opened by the <a href="#basic-open-operations" data-raw-source="[Basic Open Operations](#basic-open-operations)">Basic Open Operations</a> and other open operations, including the operations performed by the Fuzz Sub-opens test.</p>
<p>The Fuzz test issues each query or set call at least 1024 times with a valid buffer and a variety of buffer lengths and file information classes. One request of each type is also sent with an invalid buffer pointer and a zero buffer length.</p>
<p>If you use the <em>ChangeBufferProtectionFlags</em> parameter, which sets the protection option, the Fuzz test varies the security setting on the buffer in each query and set call.</p>
<p>This test also performs the Fuzz Sub-opens test.</p>
<p>This test uses the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567052" data-raw-source="[&lt;strong&gt;ZwQueryInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567052)"><strong>ZwQueryInformationFile</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567096" data-raw-source="[&lt;strong&gt;ZwSetInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567096)"><strong>ZwSetInformationFile</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff567070" data-raw-source="[&lt;strong&gt;ZwQueryVolumeInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567070)"><strong>ZwQueryVolumeInformationFile</strong></a>, and <a href="https://msdn.microsoft.com/library/windows/hardware/ff567112" data-raw-source="[&lt;strong&gt;ZwSetVolumeInformationFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567112)"><strong>ZwSetVolumeInformationFile</strong></a> functions.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test method:</strong> DoQueryAndSetFileInformationTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Fuzz_Query_and_Set_Security_test"></span><span id="fuzz_query_and_set_security_test"></span><span id="FUZZ_QUERY_AND_SET_SECURITY_TEST"></span>Fuzz Query and Set Security test</p></td>
<td align="left"><p>This test issues calls to retrieve the security descriptor and change the security state of devices.</p>
<p>During the <em>Query and Set Security Test</em>, the Fuzz test issues calls to retrieve the security descriptor and change the security state of devices opened by the <a href="#basic-open-operations" data-raw-source="[Basic Open Operations](#basic-open-operations)">Basic Open Operations</a> and other open operations, including the operations performed by the Fuzz Sub-opens test.</p>
<p>the Fuzz test issues each query or set call at least 1024 times with a valid buffer and a variety of buffer lengths and security information types (OWNER_SECURITY_INFORMATION, GROUP_SECURITY_INFORMATION, DACL_SECURITY_INFORMATION, SACL_SECURITY_INFORMATION, and no information type). One request of each type is also sent with an invalid buffer pointer and a zero buffer length.</p>
<p>If you use the <em>ChangeBufferProtectionFlags</em> parameter, which sets the protection option, the Fuzz test varies the security setting on the buffer in each query and set call.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test method:</strong> DoQueryAndSetSecurityTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Fuzz_Random_FSCTL_test___Fuzz_Random_IOCTL_test_"></span><span id="fuzz_random_fsctl_test___fuzz_random_ioctl_test_"></span><span id="FUZZ_RANDOM_FSCTL_TEST___FUZZ_RANDOM_IOCTL_TEST_"></span>Fuzz Random FSCTL test / Fuzz Random IOCTL test</p></td>
<td align="left"><p>This test issues a series of calls to the DeviceIoControl function with function codes, device types, data transfer methods, and access requirements that are selected at random from a specified range of values. The calls include input and output buffers with valid and invalid buffer pointers and lengths, and randomly generated content.</p>
<p>During random tests, the Fuzz test issues a series of calls to the <strong>DeviceIoControl</strong> function with function codes, device types, data transfer methods, and access requirements that are selected at random from a specified range of values. The calls include input and output buffers with valid and invalid buffer pointers and lengths, and randomly generated content.</p>
<p>The Fuzz test performs the random tests on all devices opened during the <a href="#basic-open-operations" data-raw-source="[Basic Open Operations](#basic-open-operations)">Basic Open Operations</a> and additional open tests. You can customize this test by using the following parameters:</p>
<ul>
<li><p>Use <em>MinFunctionCode</em> and <em>MaxFunctionCode</em> to specify the range of IOCTL or FSCTL function codes used in the calls</p></li>
<li><p>Use <em>MinDeviceType</em> and <em>MaxDeviceType</em> to specify the range of device types used in the calls</p></li>
<li><p>Use <em>SeedNumber</em> to specify a seed number for the random number generating routine.</p></li>
</ul>
<p>The function that the Fuzz test uses to generate random numbers for the test uses a <em>seed number</em>, a starting number for the random-number-generating algorithm. To reproduce the test conditions, use the <em>seed number</em> parameter to specify the seed number that was used in the original test trial.</p>
<p>A <em>Tailored Random Test</em> is included as part of the random test. The tailored random test uses the results of the random test to examine the drivers response to IOCTL or FSCTL requests in more detail. The tailored random test probes areas that the random test missed and those on which the driver did not respond as expected based on the status returned by the random test calls.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test methods:</strong> DoRandomIOCTLTest, DoRandomFSCTLTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>MinInBuffer</em></p>
<p><em>MaxInBuffer</em></p>
<p><em>MinOutBuffer</em></p>
<p><em>MaxOutBuffer</em></p>
<p><em>MaxRandomCalls</em></p>
<p><em>MaxTailoredCalls</em></p>
<p><em>SeedNumber</em></p>
<p><em>MinDeviceType</em></p>
<p><em>MaxDeviceType</em></p>
<p><em>MinFunctionCode</em></p>
<p><em>MaxFunctionCode</em></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="fuzz_sub-opens_test"></span>Fuzz Sub-opens test</p></td>
<td align="left"><p>The test performs a rapid series of calls to open objects in the device&#39;s namespace. In these calls, it passes a path that begins with the device and includes arbitrary names and nonsense strings of varying length and content.</p>
<p>During a <em>Relative Open Test</em>, (also known as a <em>Sub-open Test</em>) the Fuzz test attempts to open objects in the device&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff542068" data-raw-source="[namespace](https://msdn.microsoft.com/library/windows/hardware/ff542068)">namespace</a>.</p>
<p>During this test, the Fuzz test performs a rapid series of calls to open objects in the namespace of the devices opened by using <a href="#basic-open-operations" data-raw-source="[Basic Open Operations](#basic-open-operations)">Basic Open Operations</a> and other open operations. In these calls, the Fuzz test passes a path that begins with the device and includes arbitrary names and nonsense strings of varying length and content.</p>
<p>This test determines how the driver or file system manages open requests in its namespace. In particular, if the driver does not support open requests in its namespace, it must prevent unauthorized access, either by failing the requests, or by setting the FILE_DEVICE_SECURE_OPEN device characteristic when it uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff548397" data-raw-source="[&lt;strong&gt;IoCreateDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548397)"><strong>IoCreateDevice</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff548407" data-raw-source="[&lt;strong&gt;IoCreateDeviceSecure&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548407)"><strong>IoCreateDeviceSecure</strong></a> to create the device object.</p>
<p>For more information about the namespace of a device, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542068" data-raw-source="[Controlling Device Namespace Access](https://msdn.microsoft.com/library/windows/hardware/ff542068)">Controlling Device Namespace Access</a>.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test method:</strong> DoSubOpensTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Fuzz_Sub-opens_with_Streams_test"></span><span id="fuzz_sub-opens_with_streams_test"></span><span id="FUZZ_SUB-OPENS_WITH_STREAMS_TEST"></span>Fuzz Sub-opens with Streams test</p></td>
<td align="left"><p>This test tries to open a variety of named data streams on the device. The test uses a series of arbitrary stream names with content and characters that might be valid for other uses on some devices.</p>
<p>During the <em>Streams Test</em>, the Fuzz test tries to open a variety of named data streams on the device. The tests use a series of arbitrary stream names with content and characters that might be valid for other uses on some devices. This test determines whether the driver can properly handle data stream requests, especially if the driver exports a device that does not support or anticipate data streams.</p>
<p>A <em>named data stream</em> is an attribute of a file object. You specify a named data stream by writing the name of the file, a colon, and the name of the data stream, for example, &quot;File01.txt:AccessDate&quot; where <em>AccessDate</em> is a named data stream, that is, an attribute of the File01.txt file.</p>
<p>The Fuzz test records the stream names used in the test.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test method:</strong> DoSubOpensWithStreamsTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DoPoolCheck</em></p>
<p><em>DQ</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Fuzz_Zero-Length_Buffer_FSCTL_test___Fuzz_Zero-Length_Buffer_IOCTL_test"></span><span id="fuzz_zero-length_buffer_fsctl_test___fuzz_zero-length_buffer_ioctl_test"></span><span id="FUZZ_ZERO-LENGTH_BUFFER_FSCTL_TEST___FUZZ_ZERO-LENGTH_BUFFER_IOCTL_TEST"></span>Fuzz Zero-Length Buffer FSCTL test / Fuzz Zero-Length Buffer IOCTL test</p></td>
<td align="left"><p>This test issues a series of calls to the <a href="https://msdn.microsoft.com/library/windows/desktop/aa363216" data-raw-source="[&lt;strong&gt;DeviceIoControl function&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa363216)"><strong>DeviceIoControl function</strong></a> with input and/or output buffer lengths of 0. The test generates varying file system control codes by using different function codes, device types, data transfer methods, and access requirements.</p>
<p>During the Zero-Length Buffer Test, the Fuzz test issues a series of calls to the <a href="https://msdn.microsoft.com/library/windows/desktop/aa363216" data-raw-source="[&lt;strong&gt;DeviceIoControl function&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa363216)"><strong>DeviceIoControl function</strong></a> with input and/or output buffer lengths of 0. The test generates varying I/O control codes by using different function codes, device types, data transfer methods, and access requirements. For information about the contents of I/O control codes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff543023" data-raw-source="[Defining I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff543023)">Defining I/O Control Codes</a>.</p>
<p>To test the driver&#39;s handling of invalid buffer pointers, the buffer pointers in these user-mode calls specify addresses high in kernel virtual address space, such as 0xFFFFFC00).</p>
<p>The Fuzz test performs the Zero-Length Buffer test on all devices opened during the basic and additional open tests. You can customize this test by using the <em>MinFunctionCode</em> and <em>MaxFunctionCode</em> command parameters to specify the range of IOCTL or FSCTL function codes used in the calls and <em>MinDeviceType</em> and <em>MaxDeviceType</em> to specify the range of device types used in the calls.</p>
<p><strong>Test binary:</strong> Devfund_DevicePathExerciser.dll</p>
<p><strong>Test methods:</strong> DoZeroLengthBufferIOCTLTest, DoZeroLengthBufferFSCTLTest</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>MinDeviceType</em></p>
<p><em>MaxDeviceType</em></p>
<p><em>MinFunctionCode</em></p>
<p><em>MaxFunctionCode</em></p>
<p><em>DoPoolCheck</em></p>
<p><em>TestCycles</em></p>
<p><em>ChangeBufferProtectionFlags</em></p>
<p><em>Impersonate</em></p>
<p><em>FillZeroPageWithNull</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Run_I_O_Attack"></span><span id="run_i_o_attack"></span><span id="RUN_I_O_ATTACK"></span>Run I/O Attack</p></td>
<td align="left"><p>Runs <a href="ioattack.md" data-raw-source="[I/O Attack](ioattack.md)">I/O Attack</a> on the specified device or devices.</p>
<p><strong>Test binary:</strong> Devfund_IOAttack_DeleteDataFile.wsc</p>
<p><strong>Test method:</strong> RunIoAttack</p>
<p><strong>Parameters:</strong> - see <a href="https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests" data-raw-source="[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p></td>
</tr>
</tbody>
</table>

 

## About the Fuzz open and close test


The Fuzz open and close test employs several different ways of opening and closing instances of the specified device or devices: [Basic Open Operations](#basic-open-operations), [Direct Device Open Operations](#direct-device-open-operations), and an [Open and Close test](#open-and-close-test).

### Basic Open Operations

During the *Basic Open Operations*, the Fuzz test repeatedly opens (creates) instances of the specified devices or the devices exported by the specified driver by using different methods and options.

The Fuzz test always performs the Basic Open Operations. You do not need to select them and you cannot exclude them from a test session.

The Fuzz test performs all open operations in user mode by calling system services ([ZwXxx Routines](https://msdn.microsoft.com/library/windows/hardware/ff567122)) that are appropriate to the device. If an open call returns a handle to the device, the Fuzz test uses the handle to perform the other device tests selected for the test session.

There are five types of Basic Open Operations:

-   **Standard open.** the Fuzz test opens the device asynchronously and specifies only the native device name.

-   **Open with added backslash.** the Fuzz test issues an open call for the device name followed by a backslash (\), such as \\device\\cdrom\\, as though the call were to open a root directory within the device.

    This operation determines how the driver or file system manages open requests in its namespace. In particular, if the device does not support open requests in its namespace, the driver must prevent unauthorized access, either by failing the requests, or by setting the FILE\_DEVICE\_SECURE\_OPEN device characteristic when it calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) to create the device object.

-   **Open as a named pipe.** the Fuzz test opens the device and establishes a named pipe to the device. The access parameter (ShareAccess) is initially set to read and write, but is adjusted if the request fails. If the device does not support named pipes, it should fail the request.

-   **Open as a mailslot.** the Fuzz test opens the device as a mailslot. If the device does not support this type of connection, it should fail the request.

-   **Open as a tree connection.** the Fuzz test opens the device as a tree connection for use in remote network access. The access parameter (ShareAccess) is initially set to read and write, but is adjusted if the request fails. If the device does not support this type of connection, it should fail the request.

The parameters used in the open calls vary to accommodate the characteristics of the device and make it likely that the calls succeed. For example, if a basic open operation fails because the call did not meet the security requirements of the device, the Fuzz test repeats the open operation with a request for lesser access. For example, if an open operation that requested write access returns a security violation error, the open is repeated with a request for read access.

### Direct Device Open Operations

During the *Direct Device Open Operations*, the Fuzz test opens the device directly, as a device, not as a file in a file system. Direct Device Open Operations are always synchronous. If the call is successful, the Fuzz test uses the handle provided to perform other selected tests.

### Open and Close Test

During the *Open and Close Test*, the Fuzz test creates several threads, each of which performs thousands of create-open-close sequences. This tests the driver's ability to handle an extraordinary volume of otherwise simple and anticipated calls.

The Open and Close Test uses the same options used in [Basic Open Operations](#basic-open-operations) and Open with Added Backslash tests and are performed just prior to these tests.

## Related topics


[How to How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

[How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests)

[Provided WDTF Simple I/O plug-ins](https://msdn.microsoft.com/library/windows/hardware/hh781398)

[How to test a driver at runtime from a Command Prompt](https://msdn.microsoft.com/windows-drivers/develop/how_to_test_a_driver_at_runtime_from_a_command_prompt)

 

 






