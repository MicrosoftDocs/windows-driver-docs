---
ms.assetid: 50BF5B17-B7F0-49F2-9ED6-652DB32D638E
title: How to test a driver at runtime using Visual Studio
description: You can use WDK extensions in Visual Studio to conveniently build, deploy, install, and test a driver on a test computer on your network.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to test a driver at runtime using Visual Studio

The WDK extensions to Visual Studio provide a device testing interface that enables you to conveniently build, deploy, install, and test a driver on a test computer on your network. The WDK provides a collection of device driver tests that you can use to test the features and functions of your driver.

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   A Driver Package that is ready to install. You must first create and build your driver and then create a Driver Package for installation. For more information, see [Building a Driver](building-a-driver.md) and [Creating a Driver Package](creating-a-driver-package.md).
-   The driver must be test signed. For more information, see [Signing a Driver](signing-a-driver.md).
-   A test computer (or computers). The test computer must be on the same network as the computer that you are using for development. Both computers must be connected to the same domain, or both connected to the network under the same workgroup. The test computer should be running the version of Windows that you want to target for testing. You can also [install a checked build](https://msdn.microsoft.com/Library/Windows/Hardware/Ff547205) or partial checked build of Windows for testing and debugging purposes.
-   A device to be tested.
-   (*Recommended*) Set up a kernel mode debugging connection to the test computer. To use a network connection for kernel mode debugging, the target computer must be running Windows 8. On computers running Windows 7 or Windows Vista, you can set up a USB, 1394, or a serial connection for kernel mode debugging. For more information, see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909).

Instructions
------------

### <span id="Configure_computers_for_testing"></span><span id="configure_computers_for_testing"></span><span id="CONFIGURE_COMPUTERS_FOR_TESTING"></span>Step 1: Configure computers for testing

From Visual Studio, you can configure and provision computers for testing. When you configure the test computers, the WDK driver test framework automatically enables the test computer for remote debugging and transfers the necessary test binaries and support files.

1.  If you have not already done so, follow the instructions to [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/Library/Windows/Hardware/Dn745909).
2.  Connect the device that you want to test to the test computer or computers.

After you have configured and provisioned a test computer, you can use Visual Studio to deploy drivers, schedule tests, and debug drivers on the test computer. For information about deployment and about how you can deploy a driver automatically at build time, see [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md).

You can also enable and set options for [Driver Verifier](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545448), the runtime verification tool for drivers. Driver Verifier monitors your driver as you run tests on the test computer. For information about setting the Driver Verifier options for deployment, see [Driver Verifier Properties for Driver Projects](driver-verifier-properties-for--driver-projects.md).

You can also run tests outside of Visual Studio, for more information see [How to test a driver at runtime from a Command Prompt](how-to-test-a-driver-at-runtime-from-a-command-prompt.md). Starting in WDK 8.1, you can copy and run the HCK Test Suites on test computers using command scripts. See [How to run the HCK Test Suites in WDK 8.1](run-the-hck-test-suites-in-the-wdk.md).

### <span id="Select_an_HCK_Test_Suite_to_run_on_the_test_computer__using_WDK__8.1_"></span><span id="select_an_hck_test_suite_to_run_on_the_test_computer__using_wdk__8.1_"></span><span id="SELECT_AN_HCK_TEST_SUITE_TO_RUN_ON_THE_TEST_COMPUTER__USING_WDK__8.1_"></span>Step 2: Select an HCK Test Suite to run on the test computer (using WDK 8.1)

Starting with WDK 8.1, you can select HCK Test Suites to run on the test computer. The HCK Test Suites include the [Device Fundamentals Tests](https://msdn.microsoft.com/Library/Windows/Hardware/JJ673011), and Windows Hardware Certification kit (HCK) Basic tests for graphics, imaging, wireless LAN, mobile broadband (CDMA and GSM), and WiFi Direct devices.

-   See [How to run the HCK Test Suites in WDK 8.1](run-the-hck-test-suites-in-the-wdk.md).

### <span id="Select_the_tests_to_run_on_the_test_computer__WDK_8_and_WDK_8.1_"></span><span id="select_the_tests_to_run_on_the_test_computer__wdk_8_and_wdk_8.1_"></span><span id="SELECT_THE_TESTS_TO_RUN_ON_THE_TEST_COMPUTER__WDK_8_AND_WDK_8.1_"></span>Step 3: Select the tests to run on the test computer (WDK 8 and WDK 8.1)

To make driver testing on different test targets easier, tests are scheduled to run against test systems in units called *test groups*. A driver test group is a collection of tests that you select to run on the test computer. The driver test groups help you organize your tests and test results from each test pass. You can save your test results to separate folders. You can create and manage test groups, change parameters passed to the tests in the test groups, and schedule them to run against your test systems.

1.  From the **Driver** menu, click **Test** and then select **Test Group Explorer**.
2.  In the **Driver Test Group Explorer** window, click the **Create a new test group** button. Or, click **New Test Group** from the **Driver** menu.
3.  In the **Driver Test Group** window for the group that you created, type a name in **Test Group Name** text box to identify the group. The default name is Driver Test Group\_*nnnnn*, where *nnnnn* represents the number of the test group
4.  Click **Add/Remove Tests**.
5.  In the **Add or Remove Driver Tests** dialog box, you can specify the driver test category and architecture (All, x86, x64, ARM). By default all tests are shown. To view the test categories, click the folders in the Driver Test Categories drop-down list.

    For example, in WDK 8, to select all of the Device Fundamentals tests that are used in the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893), click **All Tests**, **Certification**, and **Device Fundamentals**. For information about the tests, see [How to select and configure the Device Fundamentals Tests](how-to-select-and-configure-the-device-fundamental-tests.md).

    In WDK 8.1, the Device Fundamentals tests are under **All Tests**, **HCK Tests**, **Certification**, and **Device Fundamentals** folder. In WDK 8.1 the Driver Test Categories include the HCK (Basic) Tests. See [How to run the HCK Test Suites in WDK 8.1](run-the-hck-test-suites-in-the-wdk.md) for more information.

6.  Be sure that you select the tests that match the architecture of the intended test computer (x86, x64, ARM). Use the **Architecture Filter** to show only those tests that will run on your test computer.
7.  Click **&gt;&gt;** to add the selected tests.

### <span id="Configure_test_parameters"></span><span id="configure_test_parameters"></span><span id="CONFIGURE_TEST_PARAMETERS"></span>Step 4: Configure test parameters

After you select the tests for your test group, you can configure any of the runtime parameters that are passed to the driver tests. For example, many of the Device Fundamentals Tests have a parameter *DQ*, which stands for Device Query. This is a [Simple Data Evaluation Language](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539607) (SDEL) query. The [Windows Driver Test Framework](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547) provides SDEL as a query language to simplify the task of collecting targets based on attributes or relationships.

For example, to run the tests for USB devices only, use the device query: class='usb'. You can change the value of each test parameter in the test group.

1.  You can view and edit the all of the runtime test parameters for a test by clicking on the name of the test in the **Driver Test Group** window. The **Driver Test Group** window provides a description of the selected test and also provides a description of the test parameters that you select. For information about setting the test parameters, see [How to select and configure the Device Fundamentals Tests](how-to-select-and-configure-the-device-fundamental-tests.md)
2.  After you select the tests, set the parameters, and name the group, click **Save**.

    When you save the test group, the test group will become the currently selected test group, and the name of the test group will appear in the Driver Test toolbar. You can now run tests against the currently selected remote test computer (also shown in the Driver Test toolbar).

### <span id="Build_and_deploy_the_driver"></span><span id="build_and_deploy_the_driver"></span><span id="BUILD_AND_DEPLOY_THE_DRIVER"></span>Step 5: Build and deploy the driver

-   From the **Build** menu, click **Deploy Solution**.

For information about deploying a driver automatically at build time, see [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md). For information about automatically setting the Driver Verifier options on the test computer, see [Driver Verifier Properties for Driver Projects](driver-verifier-properties-for--driver-projects.md). You should always enable Driver Verifier on your test computer.

### <span id="Run_the_tests_on_the_test_computer"></span><span id="run_the_tests_on_the_test_computer"></span><span id="RUN_THE_TESTS_ON_THE_TEST_COMPUTER"></span>Step 6: Run the tests on the test computer

-   From the **Driver** menu, click **Test &gt; Run test**. By default, the Run test command runs all of the tests in the currently selected test group.

Remarks
-------

For information about the driver tests and test categories, see [How to select and configure the Device Fundamentals Tests](how-to-select-and-configure-the-device-fundamental-tests.md). For information about the testing framework, see [Test Authoring and Execution Framework](https://msdn.microsoft.com/Library/Windows/Hardware/Hh439725) (TAEF) and [Windows Driver Test Framework](https://msdn.microsoft.com/Library/Windows/Hardware/Ff539547) (WDTF).

You can write your own driver tests and deploy those tests on test computers. For more information, see [How to write a driver test](how-to-write-a-driver-test-.md).

Running the Device Fundamentals tests in Visual Studio early in the development cycle will help you when are finally ready to test your driver using the [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893).

## <span id="related_topics"></span>Related topics


* [How to run the HCK Test Suites in WDK 8.1](run-the-hck-test-suites-in-the-wdk.md)
* [How to select and configure the Device Fundamentals Tests](how-to-select-and-configure-the-device-fundamental-tests.md)
* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
* [Setting Up Kernel-Mode Debugging in Visual Studio](https://msdn.microsoft.com/windows/hardware/hh439376)
* [Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016)
* [Windows Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=254893)
* [How to test a driver at runtime from a Command Prompt](how-to-test-a-driver-at-runtime-from-a-command-prompt.md)
 

 






