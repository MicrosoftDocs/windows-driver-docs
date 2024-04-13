---
title: Recommendations for Testing Driver Code and Driver Package.
description: When should you start testing? As soon as you have the requirements for your driver, you can begin to design test cases to test that the critical requirements have been implemented.
ms.date: 04/20/2017
---

# Tips for testing drivers during development

**When should you start testing?** As soon as you have the requirements for your driver, you can begin to design test cases to test that the critical requirements have been implemented. Studies show that finding and fixing defects in code becomes more expensive the longer the defects remain in the code. Finding and fixing defects early in the development cycle is less costly and disruptive than finding defects after the code has been released and distributed. Creating your test cases early can also help you find problems in your design.

## <span id="suggestions_for_testing_drivers"></span><span id="SUGGESTIONS_FOR_TESTING_DRIVERS"></span>Suggestions for testing during development


Use the following suggestions for testing your driver code and driver package.

**To help you find bugs at compile time:**

-   Declare your driver-supplied callback functions and dispatch routines using function-role types. This helps to improve the accuracy of the code analysis and verification tools and the effectiveness of your test time. For more information about how to declare your driver-supplied functions, see [Using Function Role Type Declarations](../devtest/using-function-role-type-declarations.md).

-   Compile your code using the **Level4 (/W4)** Warnings option. Fixing warnings that are detected by the compiler will increase the quality of the driver code and help eliminate additional defects earlier in the development cycle.
-   Annotate your code using the Microsoft source code annotation language (SAL) 2.0. The annotations describe how a function uses its parameters—the assumptions it makes about them, and the guarantees it makes when it finishes. The annotations also improve the accuracy of the code analysis tools. For more information about the driver-specific annotations, see [SAL 2.0 Annotations for Drivers](../devtest/sal-2-annotations-for-windows-drivers.md).
-   Use the [tools for verifying drivers](../devtest/tools-for-verifying-drivers.md) while you are developing your driver. For guidelines about when to use specific verification tools, see [Analyzing a Driver using Code Analysis and Verification Tools](analyzing-driver-quality-by-using-code-analysis-tools.md).

**To test your driver package:**

-   Create the INF file and your driver package early in the development process and use it throughout testing.

-   Use the [InfVerif](../devtest/infverif.md) tool to verify the structure and syntax of the INF file, and to help you diagnose the INF file and other installation related issues.

-   Use the [**Inf2Cat**](../devtest/inf2cat.md) tool (with the **/nocat** option) to do additional INF file verification. **Inf2Cat** can verify that the files referenced by the INF are present and placed in the package directory as the INF expects them to be.

-   Sign drivers to facilitate the installation and testing of drivers, as described in [Signing Drivers during Development and Test](../install/introduction-to-test-signing.md).

-   Run the **DriverInstall** test that is included as part of the Device Fundamental tests that are provided in the WDK. See [How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md) and [How to select and configure the Device Fundamental Tests](how-to-select-and-configure-the-device-fundamental-tests.md). The **DriverInstall** test can be run after the driver has been deployed to the test computer. You can add the **DriverInstall** test to a Driver Test Group. The **DriverInstall** test appears in the **Driver Test Categories** under All Tests\\Basic\\Device Fundamentals\\DriverInstall.

-   [Troubleshoot device installation](../install/troubleshooting-device-and-driver-installations.md) problems by using Device Manager to view system information about drivers and devices and by consulting the SetupAPI log. The SetupAPI log contains information about the sequence of operations that occurred during the installation of a device or driver.

    Using Visual Studio and the WDK, you can test and troubleshoot driver package installation when you deploy your driver to a test computer, see [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md). Select the **Install and Verify** option from the [Deployment Properties for Driver Package Projects](deployment-properties-for-driver-projects.md). When you select this option and specify the **Default Driver Package Installation Task (possible reboot)** or **Default Printer Driver Package Installation Task (possible reboot)**, the test reads the driver's INF file and installs the driver. The test then verifies that the driver is up and running. Upon completion, the test provides detailed information about the success or failure of the installation task. The results show in the **Driver Test Group Explorer**, under Driver Test Groups &gt; Driver Installation. The task name is **Default Driver Package Installation Task**.

**To test your driver at run time:**

-   Run the Device Fundamental tests that are included in the WDK. See [How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md) and [How to select and configure the Device Fundamental Tests](how-to-select-and-configure-the-device-fundamental-tests.md).

-   Set up a debugger so that you can troubleshoot and debug the test results. For more information, see [Getting Started with Windows Debugging](../debugger/getting-started-with-windows-debugging.md).
 
-   Enable Driver Verifier on the test computers you use for deployment, see [Driver Verifier Properties for Driver Projects](driver-verifier-properties-for--driver-projects.md). Select the [DDI Compliance checking](../devtest/ddi-compliance-checking.md) option. If your driver fails DDI Compliance checking, run [Static Driver Verifier](../devtest/static-driver-verifier.md) and specify the rule or rules that caused the failure. The Static Driver Verifier can help you locate the cause of the bug in your source files.
-   Test your driver and device on as many different hardware configurations as you possibly can. Varying the hardware can help you find conflicts between devices and other errors in device interactions. For example, you should test your driver and device on computers that have different processor architectures and on computers that are running 32-bit and 64-bit versions of Windows.

-   Test your driver and device on multiprocessor systems. Race conditions and other timing problems appear on multiprocessor systems that would not otherwise be found. See [How to select and configure the Device Fundamental Tests](how-to-select-and-configure-the-device-fundamental-tests.md) and [Boot Parameters to Test Drivers for Multiple Processor Group Support](../devtest/boot-parameters-to-test-drivers-for-multiple-processor-group-support.md).

-   Test your driver and device for specific system and hardware conditions, particularly edge conditions. For example, these conditions might include "D3 hot" and "D3 cold." Make sure your driver and device can return correctly from device power state "D3 hot" (without losing power) and "D3 cold" (when power is removed from the device). For more information, see [How to select and configure the Device Fundamental Tests](how-to-select-and-configure-the-device-fundamental-tests.md).
