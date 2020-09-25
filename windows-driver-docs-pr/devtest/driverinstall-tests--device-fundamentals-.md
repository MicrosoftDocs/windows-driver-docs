---
title: Driver Install Tests (Device Fundamentals)
description: The Driver Install test category includes tests that uninstall and reinstall a driver several times to test install functionality.
ms.assetid: 3FC00D4B-6520-45F1-805C-A5F8B6AACAC8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Install Tests (Device Fundamentals)


The Driver Install test category includes tests that uninstall and reinstall a driver several times to test install functionality. The tests initiate I/O testing against the driver and device after each reinstall. The tests are designed to improve the overall experience for end users who need to install and reinstall a device driver or a device.

## <span id="driverinstall_tests"></span><span id="DRIVERINSTALL_TESTS"></span>DriverInstall tests


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
<td align="left"><p><span id="Reinstall_with_IO_Before_and_After"></span><span id="reinstall_with_io_before_and_after"></span><span id="REINSTALL_WITH_IO_BEFORE_AND_AFTER"></span>Reinstall with IO Before and After</p></td>
<td align="left"><p>This test uninstalls and reinstalls the drivers for selected devices, and runs I/O testing on devices.</p>
<p><strong>Test binary:</strong> Devfund_Reinstall_With_IO_BeforeAndAfter.wsc</p>
<p><strong>Test method:</strong> Reinstall_With_IO_Before_And_After</p>
<p><strong>Parameters:</strong> - see <a href="/windows-hardware/drivers" data-raw-source="[Device Fundamentals Test Parameters](/windows-hardware/drivers)">Device Fundamentals Test Parameters</a></p>
<p><em>DQ</em></p>
<p><em>IOPeriod</em></p></td>
</tr>
</tbody>
</table>

 

## <span id="About_the_ReInstall_with_I_O_Before_and_After_test"></span><span id="about_the_reinstall_with_i_o_before_and_after_test"></span><span id="ABOUT_THE_REINSTALL_WITH_I_O_BEFORE_AND_AFTER_TEST"></span>About the ReInstall with I/O Before and After test


This test does the following:

1.  Verifies that the test device and its descendants are not reporting any device problem codes.
2.  Tests I/O on the test device and its descendants using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md) for more information.
3.  Reinstalls the original driver on the test device using [**IWDTFDriverSetupAction2::UpdateDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-updatedriver) method.
4.  Verifies that the test device and its descendants are not reporting any device problem codes.
5.  Tests I/O on the test device and its descendants using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md) for more information.
6.  Reboots the system if step \#3 requires a reboot.
7.  Installs NULL driver on the test device using [**IWDTFDriverSetupAction2::UnInstallDriverPermanently**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-uninstalldriverpermanently) method Reboots the system if a reboot is required.
8.  Reinstalls the original driver on device under test using [**IWDTFDriverSetupAction2::UpdateDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-updatedriver) method.
9.  Verifies that the test device and its descendants are not reporting any device problem codes.
10. Tests I/O on the test device and its descendants using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md) for more information.
11. Repeats step 1 - 10 several times.

### <span id="Debug_installation_failures_using_the_Setup_API_logs"></span><span id="debug_installation_failures_using_the_setup_api_logs"></span><span id="DEBUG_INSTALLATION_FAILURES_USING_THE_SETUP_API_LOGS"></span>Debug installation failures using the Setup API logs

The Setup API logs (setupapi.app.log and setupapi.dev.log) contain useful information to debug driver installation failures logged by this test. The Setup API logs can be found under %windir%\\inf\\ directory on the test system.

To increase the verbosity and potential usefulness of these logs, set the following registry key to 0x2000FFFF before running the Reinstall test:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Setup\LogLevel
```

## <span id="related_topics"></span>Related topics


[How to How to test a driver at runtime using Visual Studio](/windows-hardware/drivers)

[How to select and configure the Device Fundamentals tests](/windows-hardware/drivers)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](/windows-hardware/drivers)

[Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md)

[How to test a driver at runtime from a Command Prompt](/windows-hardware/drivers)

