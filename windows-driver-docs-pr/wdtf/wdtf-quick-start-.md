---
title: WDTF Quick Start
author: windows-driver-content
description: The Windows Driver Kit 8.0 provides an integrated solution for writing, deploying, and running tests that use the Windows Driver Test Framework (WDTF).
ms.assetid: 77402D9A-DD21-4B7F-B052-43DB8C04EA1B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDTF Quick Start


The Windows Driver Kit 8.0 provides an integrated solution for writing, deploying, and running tests that use the Windows Driver Test Framework (WDTF). Using the WDK, you can configure a remote computer for deploying, testing, and debugging a driver. When you configure the remote computer, the Windows Driver Test Framework runtime is installed.

## Installing WDTF runtime library


**To install WDTF runtime library using Visual Studio and the WDK**

1.  Install Visual Studio and then install the WDK.

2.  Configure a remote computer for testing and deployment (**Driver** &gt; **Test** &gt; **Configure computers...**). When you configure the test computer, the Windows Driver Test Framework runtime is installed. For more information, see [Deploying a Driver to a Test Computer](https://msdn.microsoft.com/windows-drivers/develop/deploying_a_driver_to_a_test_computer) and see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909) or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/dn745909).

**To install WDTF runtime library manually**

-   When you install the WDK, the installation package for the Windows Driver Test Framework runtime is also installed. You need to copy the installation package to a test computer and run a command. For information, see [WDTF Runtime Library](https://msdn.microsoft.com/library/windows/hardware/hh831856) and "Manually installing WDTF runtime library on a test computer (alternative method)."

## Writing tests with WDTF


The WDK provides templates for writing tests with WDTF. See [How to write a driver test using a Driver Test template](https://msdn.microsoft.com/windows-drivers/develop/how_to_write_a_driver_test_). You can also use a template to create a WDTF SimpleIO plug-in for your target device. For information, see [Writing a WDTF SimpleIO plug-in for your device](writing-a-wdtf-simpleio-plug-in-for-your-device.md).

## Running WDTF tests


When you build your driver test in Visual Studio using a WDTF Driver test template, the new test will be available for deployment to a test computer. By default, the tests that you create will appear in the test category **My Test Category**. The names of the tests are based upon the test cases that you choose, and they will have names such as **My Plug and Play Surprise Remove Test**. During each build of the test, the tests will be overwritten and available to run in the Easily Run Tests feature. For more information, see [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime).

 

 




