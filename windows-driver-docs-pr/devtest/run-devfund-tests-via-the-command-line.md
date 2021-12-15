---
title: How to run the DevFund Tests via the command-line
description: The WDK provides the test binaries and tools which make it easy to run the Device Fundamentals tests from the command-line.
keywords:
- DevFund tests
- command line
ms.date: 06/29/2018
---

# How to run the DevFund Tests via the command-line

**Overview**

There are several ways to run the DevFund and SysFund tests via the command-line.  The instructions on this page are for running the tests via the command-line with Visual Studio and the Windows Driver Kit (WDK), but without provisioning the test system via Visual Studio.

Other methods for running the DevFund and SysFund tests include:

- Hardware Lab Kit (HLK): The tests can be run from the command line on an [HLK client test machine](/windows-hardware/test/hlk/testref/reproduce-the-test-failure-by-running-the-test-from-the-command-line)

- Test machine "provisioned" through Visual Studio: [Running test via the command-line](../develop/how-to-test-a-driver-at-runtime-from-a-command-prompt.md)

- Enterprise Windows Driver Kit (EWDK- does not require Visual Studio): If Visual Studio is not installed and will not be used, [use the EWDK to run tests on the command-line](./configure-the-machine-for-testing.md)

**Setup**


Note that the following commands must be executed from an elevated/administrator command prompt because WDTF installation installs drivers on the system. The instructions below assume the system architecture is x64. The following steps may need to be adjusted for other architectures.

**Step 1** : [Install Visual Studio and the Windows Driver Kit (WDK)](../download-the-wdk.md)

**Step 2** : The tests use the [TAEF](../taef/index.md) service.  

To install the TAEF service (Te.service), go to ```%PROGRAMFILES(X86)%\Windows Kits\10\Testing\Runtimes\TAEF\x64``` and run the following commands to get the service started:

1. ```wex.services.exe /install:te.service``` (Verify te.service was installed successfully)

2. ```sc start te.service``` (Verify 'STATE' is 'START\_PENDING')

3. ```sc query te.service``` (Verify 'STATE' is 'RUNNING')

4. ```sc qc te.service``` (Verify 'START\_TYPE' is 'AUTO\_START')

Add this directory to the system PATH environment variable and restart the elevated command prompt.

**Step 3** : Install [WDTF](../wdtf/index.md) by navigating to the location of the WDTF MSI (```%PROGRAMFILES(X86)%\Windows Kits\10\Testing\Runtimes\```) and installing the package for the desired architecture. Specify a location and name for the installation log file, **%USERPROFILE%\Desktop\WDTFInstall.log** in this example:

 
``` 
cd %PROGRAMFILES(X86)%\Windows Kits\10\Testing\Runtimes\
```

```
msiexec /i "Windows Driver Testing Framework (WDTF) Runtime Libraries-x64\_en-us.msi" /l\* "%USERPROFILE%\Desktop\WDTFInstall.log"
```

The WDTF MSI installs WDTF to **%PROGRAMFILES%\Windows Kits\10\Testing\Runtimes\WDTF** since this example is using the 64-bit WDTF MSI even though the WDTF MSI was under **%PROGRAMFILES(X86)%**


**Step 4** : Configure the machine for testing:

- Configure the machine to collect full dumps or attach a kernel debugger.

- Because the tests can potentially reboot the machine and need to control the sleep cycles, configure the machine to never sleep, never turn off display, and autologon to a test account (netplwiz.exe). Note that autologon should be used with caution.

**Step 5** : Run the test.  The DevFund tests are located at **%PROGRAMFILES(X86)%\Windows Kits\10\Testing\Tests\Additional Tests\x64\DevFund**.

The basic command for running a DevFund test is of the form:

```
Te.exe Devfund_<testname>.dll /name:"<test case name>" /p:"DQ=DeviceID='<Device Instance Path of device under test from Device Manager>'" /RebootStateFile:state.xml
```

Where &lt;_test case name_&gt; is the name of the test in the test binary.

The / **name** switch is optional. Since some test binaries contain multiple tests, the / **name** switch specifies which tests should be run. If unspecified, all tests contained in the test binary are executed in sequence. The list of tests in a test binary can be obtained by running the following command:

```
Te.exe Devfund\<testname>.dll /list
```

For example, the Devfund\_PnPDTest.dll contains most of the PnP-related tests:

```
Te.exe Devfund_PnPDTest_WLK_Functional.dll /list

Test Authoring and Execution Framework v10.21 for x64

    Devfund_PnPDTest_WLK_Functional.dll

        PNPDTest

            PNPDTest::PNPDisableAndEnableDevice

            PNPDTest::PNPRemoveAndRestartDevice

            PNPDTest::PNPCancelRemoveDevice

            PNPDTest::PNPCancelStopDevice

            PNPDTest::PNPTryStopAndRestartDevice

            PNPDTest::PNPTryStopDeviceRequestNewResourcesAndRestartDevice

            PNPDTest::PNPTryStopDeviceAndFailRestart

            PNPDTest::PNPSurpriseRemoveAndRestartDevice

            PNPDTest::PNPDIFRemoveAndRescanParentDevice

            PNPDTest::DisableEnhancedDeviceTestingSupport
```


The command to run a single test from this test binary might look like this:

```
c:\temp\Te.exe Devfund_PnPDTest_WLK_Functional.dll /name:PNPDTest::PNPSurpriseRemoveAndRestartDevice* /p:"DQ=DeviceID='my\device\id'" /RebootStateFile:state.xml
```
