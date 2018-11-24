---
title: Run the tests
description: Description of the tests and configuration file for the data-driven SysFund tests for Windows drivers
keywords:
- Sysfund tests
- data-driven tests
- SDEL query
ms.date: 11/20/2017
ms.localizationpriority: medium
---

# Run the tests
## Description of the tests and configuration file
You can find the data-driven SysFund tests at \<unzipped EWDK root>\Program Files\Windows Kits\10\Testing\Tests\Additional Tests\x64\DevFund\DataDriven.  The data-driven test suite consists of the following files:

- Five test DLL’s which use the XML configuration file WDTFTest.xml:

  *   Sysfund_Device_IO_DataDriven.dll
  *   Sysfund_PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven.dll
  *   Sysfund_PNP_RemoveAndRestartDevice_DataDriven.dll
  *   Sysfund_RebootRestart_With_IO_During_DataDriven.dll
  *   Sysfund_Sleep_With_IO_BeforeAndAfter_DataDriven.dll
- Two utility DLL’s which use the XML configuration file WDTFTest.xml:
  *   Utility_DeviceStatusCheck_DataDriven.dll
  *   Utility_EnableDisableDriverVerifier_DataDriven.dll
- The XML configuration file:
      *   WDTFTest.xml

**System - Device I/O Test**
-	Binary: Sysfund_Device_IO_DataDriven.dll
-	This test sends I/O to all devices on the system

**System - PNP (disable and enable) with IO before and after (Reliability)**
-	Binary: Sysfund_PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven.dll
-	[Documentation](https://msdn.microsoft.com/de-de/library/windows/hardware/dn941373(v=vs.85).aspx)

**System - PNP Remove Device Test (Reliability)**
-	Binary: Sysfund_PNP_RemoveAndRestartDevice_DataDriven.dll
-	[Documentation](https://docs.microsoft.com/windows-hardware/test/hlk/testref/ead2222e-4485-4bfc-84cd-43ac0d2e8181)

**System - Reboot Restart with IO During (Reliability)**
-	Binary: Sysfund_RebootRestart_With_IO_During_DataDriven.dll
-	[Documentation](https://docs.microsoft.com/windows-hardware/test/hlk/testref/6d6ed5ec-1765-4569-a7ac-20ed7869d89a)

**System - Sleep with IO before and after (Reliability SysFund)** 
-	Binary: Sysfund_Sleep_With_IO_BeforeAndAfter_DataDriven.dll
-	[Documentation](https://msdn.microsoft.com/library/windows/hardware/dn940448(v=vs.85).aspx)

**Device status check**
-	Binary: Utility_DeviceStatusCheck_DataDriven.dll
-	This utility DLL verifies that the Problem Codes of the target devices are 0 (working properly).  It is generally used before running the SysFund tests to verify the target devices are working properly.

**Enable/disable Driver Verifier**
-	Binary: Utility_EnableDisableDriverVerifier_DataDriven.dll
-	This utility enables or disables Driver Verifier for the drivers associated with the target devices.

**Data-driven test configuration file**
-	File: WDTFTest.xml
-	This file contains all of the configuration information for the data-driven SysFund tests and associated utilities.

## Configure the tests

The data-driven test configuration file (WDTFTest.xml) contains several elements that define the parameters passed to the tests and utilities.  All of the data-driven tests and utilities share the same configuration file (WDTFTest.xml).  By default, the configuration file configures the tests and utilities to target all devices on the system, but this can easily be customized to suit the requirements of the test pass.

As shown below, the configuration file can be customized so the tests and utilities will target any set of devices on the system, from one device or driver to all devices and drivers.

The tests and utilities will use only the elements required and will ignore all other elements.
### WDTFTest.xml parameter descriptions and use
#### Configuring the SDEL query
The [SDEL language](https://msdn.microsoft.com/library/windows/hardware/ff538361%28v=vs.85%29.aspx) is used to create the query that returns the devices targeted by the tests and utilities. Bring the following SDEL-related parameters together using AND statements to create the complete query:

**SDEL**: The value *IsDevice* specifies the complete set of devices on the system.  Typically, this parameter is not edited unless you only want to test a specific driver or device.  The next SDEL-related parameters will create a subset of devices from this superset by specifying drivers or devices which should be excluded from testing, so this parameter can be left unchanged.
```
    <Parameter Name="SDEL">IsDevice</Parameter>
```

**SdelExcludeVMDevnode**: Excludes device nodes that are critical to VM operation and cannot be disabled.  This parameter should be left unchanged as it has no effect if the system is not a virtual machine.
```
    <Parameter Name="SdelExcludeVMDevnode">(DisplayName!='Microsoft Hyper-V Virtual Machine Bus')</Parameter>
```

**SdelExcludeDrivers**: this is the recommended place to use SDEL to exclude drivers and/or devices.  For example, you could use this to exclude drivers that have known bugs or to narrow the scope of the test.  Running with the default of ```(DriverBinaryNames!='')``` targets all drivers of all devices on the system (except the “Microsoft Hyper-V Virtual Machine Bus” device node as noted above).
```
    <Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!='')</Parameter>
```

#### General test configuration parameters
**TestCycles**: Specifies how many iterations the test should run.
```
    <Parameter Name="TestCycles">1</Parameter>
```

**IOPeriod** Specifies how many minutes I/O should run.
```
    <Parameter Name="IOPeriod">1</Parameter>
```

**ResumeDelay**: Specifies how many seconds to wait before sending I/O after resuming from sleep.
```
    <Parameter Name="ResumeDelay">10</Parameter>
```

**Wpa2PskAesSsid**: Specifies the name of the test WiFi access point.
```
    <Parameter Name="Wpa2PskAesSsid">WiFiRouterName</Parameter>
```

**Wpa2PskPassword**: Specifies the password of the test WiFi access point.
```
    <Parameter Name="Wpa2PskPassword">WiFiRouterPassword</Parameter>
```

#### Parameters that apply to ```utility_enabledisabledriververifier_datadriven.dll``` only:

**DriverVerifierLevel**: The default value of 0x209BB is equal to "standard flags" for [Driver Verifier](https://msdn.microsoft.com/windows/hardware/drivers/devtest/driver-verifier).
```
    <Parameter Name="DriverVerifierLevel">0x209BB</Parameter>
```

**AddOnly**: Specifies that the resulting SDEL query results should add drivers to Driver Verifier without removing any.  This is useful if Driver Verifier is already enabled on a set of drivers which should be appended rather than replaced.
```
    <Parameter Name="AddOnly">false</Parameter>
```

**NoReboot**: Specifies that the machine should not reboot automatically to enable Driver Verifier settings.  If the *NoReboot* parameter is set to true, the augmented Driver Verifier settings will not take effect until the machine is manually rebooted.
```
    <Parameter Name="NoReboot">false</Parameter>
```

### Enable Driver Verifier
To turn on Driver Verifier, run the following command:
```
    te.exe utility_enabledisabledriververifier_datadriven.dll /name:Utility_DriverVerifier#0::EnableDriverVerifier /rebootstatefile=state.xml 
```
In certain instances, the machine may not reboot.  This is a known technical limitation of the test framework.  If the machine does not begin rebooting within 30 seconds after changing Driver Verifier settings with this utility, you must manually reboot the machine for the updated Driver Verifier settings to take effect.

After the reboot, open a command prompt and run **verifier /querysettings** to ensure Driver Verifier has been enabled.

### Verify devices are working
The data-driven SysFund tests expect any devices targeted by the tests to have a Problem Code of 0 (working properly).  To ensure all devices being targeted are working properly, use the DeviceStatusCheck utility:
```
    te.exe Utility_DeviceStatusCheck_DataDriven.dll
```
This utility uses the SDEL queries defined in WDTFTest.xml to find the set of devices under test and verify they all have **Problem Code 0**.  A “Passed” result means that the set of devices queried are all working properly. Review **TestTextLog.log** to investigate failures.  For an explanation of Device Manager problem codes, see [Device Manager Error Messages](https://docs.microsoft.com/windows-hardware/drivers/install/device-manager-error-messages).

### Launch a test
To launch either of the data-driven SysFund tests, use the following commands:
```
    te.exe Sysfund_PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven.dll
```
```
    te.exe Sysfund_Sleep_With_IO_BeforeAndAfter_DataDriven.dll
```
### Refine the configuration file
You should back up the original copy of WDTFTest.xml before making any changes.

The test configuration file (WDTFTest.xml) can be refined based on the results of the data-driven SysFund tests.  For example, if a data-driven SysFund test is initially run targeting all devices on the system, and one particular device or driver fails the test, the test configuration file can be updated to filter-out testing of that device while the bug is investigated.  This allows testing to continue in parallel while bugs are investigated.

To filter-out a specific device, edit the **SdelExcludeDrivers** element in WDTFTest.xml.  The following code filters-out *mydriver.sys*, for example: 
```
<Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!=’mydriver.sys’)</Parameter>
```

Likewise, the following code filters-out a device based on the Device Instance Path:
```
<Parameter Name="SdelExcludeDrivers">(DeviceId!=’my\device\id’)</Parameter>
```
You can create complex SDEL queries to filter-out multiple devices:
```
<Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!=’mydriver1.sys’ AND DriverBinaryNames!=’mydriver2.sys’)</Parameter>
```

After you fix the bugs in mydriver1.sys and mydriver2.sys, you can reset the **SdelExcludeDrivers** element in WDTFTest.xml to the default value to include these drivers and associated devices as targets:
```
    <Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!='')</Parameter>
```

## Troubleshooting Problems
### Malformed SDEL Query in the Configuration File
The following error message is indicative of a poorly formed SDEL query contained in the WDTFTest.xml configuration file:
```
    Error: Verify: SUCCEEDED(m_pDeviceDepot->Query(CComBSTR(DQ), &m_pTestTargets)) - Value (0x80070057) [File: onecore\base\tools\wdtf\tests\devfund\datadriven\sysfund_pnp_disableenable_with_io_beforeandafter_datadriven\test.cpp, Function: PNP_DisableEnable_With_IO_BeforeAndAfter::PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven_Test, Line: 231]
    EndGroup: PNP_DisableEnable_With_IO_BeforeAndAfter::PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven_Test#0 [Failed]
```
The HRESULT '0x80070057' means "E_INVALIDARG: One or more arguments are not valid". Carefully check the WDTFTest.xml configuration file against the [SDEL documentation](https://msdn.microsoft.com/library/windows/hardware/ff538361%28v=vs.85%29.aspx) and look for a malformed query that could be causing this error.

### Test is Blocked Because it Might Reboot the Machine
Certain SysFund tests can reboot the machine during testing. In order to run a test which can reboot the machine, the "/rebootstatefile" parameter must be used:
```
    te.exe <testname> /rebootstatefile=state.xml
```
If the /rebootstatefile parameter is not passed to the test, the following message will be displayed and the test will be blocked:
```
    TestBlocked: TAEF: This test cannot be run as it might reboot the machine.
    EndGroup: Sysfund_RebootRestart_With_IO_During::Sysfund_RebootRestart_With_IO_During_DataDriven_Test#0 [Blocked]
```

### Test is Blocked Because the SDEL Query Contains '&' Characters
When specifing an SDEL query which targets a device based on its Device Instance Path value, '&' characters in the path must be replace with "&amp\;". The following message is indicative of a WDTFTest.xml configuration file which contains '&' characters in the device instance path:
```
    TestBlocked: TAEF: [HRESULT: 0xC00CEE22] Error while getting value for 'SDEL' in table 'DataDrivenSysfundTable' in DataSource 'WDTFTest.xml' on line 24.
    EndGroup: PNP_DisableEnable_With_IO_BeforeAndAfter::PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven_Test#error [Blocked]
```
This is the XML from the WDTFTest.xml configuration file which generated the error message above:
```
    <Parameter Name="SDEL">IsDevice AND deviceid='PCI\VEN_11AB&DEV_2B38&SUBSYS_045E0003&REV_00\4&91A2562&0&00E8'</Parameter>
```
This is the well-formed value for deviceid which fixes the error:
```
    <Parameter Name="SDEL">IsDevice AND deviceid='PCI\VEN_11AB&amp;DEV_2B38&amp;SUBSYS_045E0003&amp;REV_00\4&amp;91A2562&amp;0&amp;00E8'</Parameter>
```

### Other Issues
For help with troubleshooting other issues not listed here, see [Device.DevFund Additional Documentation](https://docs.microsoft.com/windows-hardware/test/hlk/testref/device-devfund-additional-documentation).
