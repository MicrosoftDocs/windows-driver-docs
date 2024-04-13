---
title: How to Test a Driver At Runtime from a Command Prompt
description: The WDK provides device testing components that enable you to test a driver on a test computer on your network.
ms.date: 04/20/2017
---

# How to test a driver at runtime from a Command Prompt

The WDK provides device testing components that enable you to test a driver on a test computer on your network. You can use these components outside of Visual Studio by copying and installing the necessary files. You can use these components to run the same collection of device driver tests that are available in Visual Studio to test the features and functions of your driver.

Starting in WDK 8.1, you can copy and run the HCK Test Suites on test computers using command scripts. See [How to run the HCK Test Suites in WDK 8.1](run-the-hck-test-suites-in-the-wdk.md).

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   Install Visual Studio and the WDK on the computer you use for development.
-   From Visual Studio, you can configure and provision computers for testing. When you configure the test computer, the WDK driver test framework automatically enables the test computer for remote debugging and transfers the necessary test binaries and support files. If you have not already done so, follow the instructions in [Provision a computer for driver deployment and testing (WDK 8.1)](../gettingstarted/provision-a-target-computer-wdk-8-1.md)
-   Although it is not recommended, you can also install the necessary test components manually. Follow the instructions to install the [Test Authoring and Execution Framework (TAEF)](../taef/index.md) and WDTF on the test computer. See [Manually installing and uninstalling TAEF on a test computer](../taef/getting-started.md#manually-installing-and-uninstalling-taef-on-a-test-computer) and [WDTF Quick Start](../wdtf/wdtf-quick-start-.md).

## Instructions

### <span id="Copy_the_tests_to_the_test_computer"></span><span id="copy_the_tests_to_the_test_computer"></span><span id="COPY_THE_TESTS_TO_THE_TEST_COMPUTER"></span>Step 1: Copy the tests to the test computer

-   Copy the [Device Fundamentals Tests](../devtest/device-fundamentals-tests.md) from the computer you use for development. Copy the folder %ProgramFiles%\\Windows Kits\\8.0\\Testing\\Tests\\Device Fundamentals to the test computer.

### <span id="Run_the_tests"></span><span id="run_the_tests"></span><span id="RUN_THE_TESTS"></span>Step 2: Run the tests

The TAEF command to run the tests uses the following syntax:

```cpp
Te.exe [/name:<Test Method>] [<Test Name>.dll | <Test Name.wsc> ]  [/rebootStateFile=<file> ] [/enablewttlogging]  [/P:"DQ= <>" ]  
```

## Remarks

You must specify the test binary (.dll) or script (.wsc) file. The test method (**/name:**_&lt;test method&gt;_) is optional. For the test names and test methods, see the [Device Fundamentals Tests](../devtest/device-fundamentals-tests.md). For information about specifying test parameters, see [Device Fundamentals Test Parameters](how-to-select-and-configure-the-device-fundamental-tests.md) and [Te.exe Command Options](../taef/te-exe-command-line-parameters.md) .

For example, to run all PnP tests in the Devfund\_PnPDTest.dll on a device with a specific device ID.

```cpp
Te.exe  Devfund_PnPDTest.dll /P:"DQ=DeviceID='USB\ROOT_HUB\4&1CD5D022&0'"
```

For example, to run PnP Surprise Remove test on a device with a specific device ID.

```cpp
Te.exe /name:"*PNPSurpriseRemoveAndRestartDevice" Devfund_PnPDTest.dll /P:"DQ=DeviceID='USB\ROOT_HUB\4&1CD5D022&0'"
```

## <span id="related_topics"></span>Related topics


* [Device Fundamentals Tests](../devtest/device-fundamentals-tests.md)
* [Device Fundamentals Test Parameters](how-to-select-and-configure-the-device-fundamental-tests.md)
* [How to run the HCK Test Suites in WDK 8.1](run-the-hck-test-suites-in-the-wdk.md)
* [Test Authoring and Execution Framework (TAEF)](../taef/index.md)
* [Te.exe Command Options](../taef/te-exe-command-line-parameters.md)
