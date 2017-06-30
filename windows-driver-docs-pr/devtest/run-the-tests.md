#Run the Tests
##Description of the Tests and Configuration File
The data-driven SysFund tests live at <unzipped EWDK root>\Program Files\Windows Kits\10\Testing\Tests\Additional Tests\x64\DevFund\DataDriven.  The data-driven test suite consists of the following files:
    -	Two test DLL’s which use the XML configuration file WDTFTest.xml:
        *	Sysfund_PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven.dll
        *	Sysfund_Sleep_With_IO_BeforeAndAfter_DataDriven.dll
    -	Two utility DLL’s which use the XML configuration file WDTFTest.xml:
        *	Utility_DeviceStatusCheck_DataDriven.dll
        *	Utility_EnableDisableDriverVerifier_DataDriven.dll
    -	The XML configuration file:
        *	WDTFTest.xml

**System - PNP (disable and enable) with IO Before and After (Reliability)**
Binary: Sysfund_PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven.dll
[Documentation](https://msdn.microsoft.com/de-de/library/windows/hardware/dn941373(v=vs.85).aspx)

**System - Sleep with IO Before and After (Reliability SysFund)** 
Binary: Sysfund_Sleep_With_IO_BeforeAndAfter_DataDriven.dll
[Documentation](https://msdn.microsoft.com/en-us/library/windows/hardware/dn940448(v=vs.85).aspx)

**Device Status Check**
Binary: Utility_DeviceStatusCheck_DataDriven.dll
This utility DLL verifies that the Problem Codes of the target devices are 0 (working properly).  It is generally used before running the SysFund tests to verify the target devices are working properly.

**Enable/Disable Driver Verifier**
Binary: Utility_EnableDisableDriverVerifier_DataDriven.dll
This utility enables or disables Driver Verifier for the drivers associated with the target devices.

**Data-driven Test Configuration File**
File: WDTFTest.xml
This file contains all of the configuration information for the data-driven SysFund tests and associated utilities.

##Configure the Tests

The data-driven test configuration file (WDTFTest.xml) contains several elements that define the parameters passed to the tests and utilities.  All of the data-driven tests and utilities share the same configuration file (WDTFTest.xml).  By default, the configuration file will configure the tests and utilities to target all devices on the system, but this can easily be customized to suit the requirements of the test pass.

As shown below, the configuration file can be customized so the tests and utilities will target any set of devices on the system, from one device or driver to all devices and drivers.

The tests and utilities will only use the elements they need and will ignore all other elements.
###Description of Parameters and Usage
####Configuring the SDEL Query
The [SDEL language] (https://msdn.microsoft.com/en-us/library/windows/hardware/ff538361%28v=vs.85%29.aspx) is used to create the query which returns the devices targeted by the tests and utilities.  The following parameters are ‘AND’ed together to create the complete query:

**SDEL**: the value IsDevice specifies the complete set of devices on the system.  Typically, this parameter is not edited unless you only want to test a specific driver or device.  The next SDEL-related parameters will create a subset of devices from this superset by specifying drivers or devices which should be excluded from testing, so this parameter can be left unchanged.
    <Parameter Name="SDEL">IsDevice</Parameter>

**SdelExcludeVMDevnode**: excludes device nodes that are critical to VM operation and cannot be disabled.  This parameter should be left unchanged as it will have no effect if the system is not a virtual machine.
    <Parameter Name="SdelExcludeVMDevnode">(DisplayName!='Microsoft Hyper-V Virtual Machine Bus')</Parameter>

**SdelExcludeDrivers**: this is the recommended place to use SDEL to exclude drivers and/or devices.  For example, this could be used to exclude drivers that have known bugs, or to narrow the scope of the test.  Running with the default of "(DriverBinaryNames!='')" will target all drivers of all devices on the system (except the “Microsoft Hyper-V Virtual Machine Bus” device node as noted above).
    <Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!='')</Parameter>

####General Test Configuration Parameters
**TestCycles**: specifies for how many iterations the test should run.
    <Parameter Name="TestCycles">1</Parameter>

**IOPeriod** specifies for how many minutes I/O should run.
    <Parameter Name="IOPeriod">1</Parameter>

**ResumeDelay**: specifies for how many seconds to wait before sending I/O after resuming from sleep.
    <Parameter Name="ResumeDelay">10</Parameter>

**Wpa2PskAesSsid**: specifies the name of the test WiFi access point.
    <Parameter Name="Wpa2PskAesSsid">WiFiRouterName</Parameter>

**Wpa2PskPassword**: specifies the password of the test WiFi access point.
    <Parameter Name="Wpa2PskPassword">WiFiRouterPassword</Parameter>

####The following parameters apply to utility_enabledisabledriververifier_datadriven.dll only:

**DriverVerifierLevel**: the default value of 0x209BB is equal to "standard flags" for Driver Verifier (hyperlink for doc writer: https://msdn.microsoft.com/en-us/windows/hardware/drivers/devtest/driver-verifier).
    <Parameter Name="DriverVerifierLevel">0x209BB</Parameter>

**AddOnly**: specifies that the resulting SDEL query results should add drivers to Driver Verifier without removing any.  This is useful if Driver Verifier is already enabled on a set of drivers which should be appended rather than replaced.
    <Parameter Name="AddOnly">false</Parameter>

**NoReboot**: specifies that the machine should not reboot automatically to enable Driver Verifier settings.  If the NoReboot parameter is set to true, the augmented Driver Verifier settings will not take effect until the machine is manually rebooted.
    <Parameter Name="NoReboot">false</Parameter>


###Enable Driver Verifier
To turn on Driver Verifier, run the following command:
    te.exe utility_enabledisabledriververifier_datadriven.dll /name:Utility_DriverVerifier#0::EnableDriverVerifier /rebootstatefile=state.xml 
In certain instances, the machine may not reboot.  This is a known technical limitation of the test framework.  If the machine does not begin rebooting within 30 seconds after changing Driver Verifier settings with this utility, you must manually reboot the machine for the updated Driver Verifier settings to take effect.

After the reboot, open a command prompt and run “verifier /querysettings” to ensure Driver Verifier has been enabled.

###Verify Devices are Working
The data-driven SysFund tests expect any devices targeted by the tests to have a Problem Code of 0 (working properly).  To ensure all devices being targeted are working properly, use the DeviceStatusCheck utility:
    te.exe Utility_DeviceStatusCheck_DataDriven.dll
This utility will use the SDEL queries defined in WDTFTest.xml to find the set of devices under test and verify they all have **Problem Code 0**.  A “Passed” result means that the set of devices queried are all working properly.  Review “TestTextLog.log” to investigate failures.  For an explanation of Device Manager problem codes, see https://docs.microsoft.com/en-us/windows-hardware/drivers/install/device-manager-error-messages

###Launch a Test
Launch either of the data-driven SysFund tests via the following commands:
    te.exe Sysfund_PNP_DisableEnable_With_IO_BeforeAndAfter_DataDriven.dll
    te.exe Sysfund_Sleep_With_IO_BeforeAndAfter_DataDriven.dll

###Refine the Configuration File
It is recommended that you back up the original copy of WDTFTest.xml before making any changes.

The test configuration file (WDTFTest.xml) can be refined based on the results of running the data-driven SysFund tests.  For example, if a data-driven SysFund tests is initially run targeting all devices on the system, and one particular device or driver fails the test, the test configuration file can be updated to filter-out testing of that device while the bug is investigated.  This allows testing to continue in parallel while bugs are investigated.

Filtering-out a specific device requires editing the **SdelExcludeDrivers** element in WDTFTest.xml.  To filter-out mydriver.sys because a bug has been discovered, do the following:
    <Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!=’mydriver.sys’)</Parameter>
Likewise, to filter-out a device based on the Device Instance Path, do the following
    <Parameter Name="SdelExcludeDrivers">(DeviceId!=’my\device\id’)</Parameter>
Complex SDEL queries can be created to filter-out multiple devices:
    <Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!=’mydriver1.sys’ AND DriverBinaryNames!=’mydriver2.sys’)</Parameter>
After the bugs in mydriver1.sys and mydriver2.sys are fixed, the **SdelExcludeDrivers** element in WDTFTest.xml can be reset to the default value to include these drivers and associated devices as targets:
    <Parameter Name="SdelExcludeDrivers">(DriverBinaryNames!='')</Parameter>
