---
title: WDTF Quick Start
description: The Windows Driver Kit provides an integrated solution for writing, deploying, and running tests that use the Windows Driver Test Framework (WDTF).
ms.assetid: 77402D9A-DD21-4B7F-B052-43DB8C04EA1B
ms.date: 10/22/2018
ms.localizationpriority: medium
---

# WDTF Quick Start

The Windows Driver Kit provides an integrated solution for writing, deploying, and running tests that use the Windows Driver Test Framework (WDTF). Using the WDK, you can configure a remote computer for deploying, testing, and debugging a driver. When you configure the remote computer, the Windows Driver Test Framework runtime is installed.

## Installing WDTF runtime library

### To install WDTF runtime library using Visual Studio and the WDK

1. Install Visual Studio and then install the WDK.

2. Configure a remote computer for testing and deployment. In Visual Studio, on the **Driver** menu, point to **Test** and then click **Configure computers...**.

3. When you configure the test computer, the Windows Driver Test Framework runtime is installed.

- For more information, see:

  - [Deploying a Driver to a Test Computer](https://docs.microsoft.com/windows-hardware/drivers/develop/deploying-a-driver-to-a-test-computer)

  - [Provision a computer for driver deployment and testing (WDK 10)](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1)  

### Installing the WDTF runtime library manually

When you install the WDK, the installation package for the Windows Driver Test Framework runtime is also installed. You need to copy the installation package to a test computer and run a command. For information, see [Manually installing WDTF runtime library on a test computer (alternative method)](https://docs.microsoft.com/windows-hardware/drivers/wdtf/wdtf-runtime-library#manually-installing-wdtf-on-a-test-computer-alternative-method) in the [WDTF Runtime Library](wdtf-runtime-library.md).

## Writing tests with WDTF

The WDK provides templates for writing tests with WDTF. See [How to write a driver test using a Driver Test template](https://docs.microsoft.com/windows-hardware/drivers/develop/how-to-write-a-driver-test-). You can also use a template to create a WDTF Simple I/O plug-in for your target device. For information, see [Writing a WDTF Simple I/O plug-in for your device](writing-a-wdtf-simpleio-plug-in-for-your-device.md).

## Running WDTF tests

When you build your driver test in Visual Studio using a WDTF Driver test template, the new test will be available for deployment to a test computer. By default, the tests that you create will appear in the test category **My Test Category**. The names of the tests are based upon the test cases that you choose, and they will have names such as **My Plug and Play Surprise Remove Test**. During each build of the test, the tests will be overwritten and available to run in the Easily Run Tests feature. For more information, see [How to test a driver at runtime using Visual Studio](https://docs.microsoft.com/windows-hardware/drivers/develop/testing-a-driver-at-runtime).
