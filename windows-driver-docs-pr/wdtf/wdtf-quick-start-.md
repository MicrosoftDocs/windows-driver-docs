---
title: WDTF Quick Start
author: windows-driver-content
description: The Windows Driver Kit 8.0 provides an integrated solution for writing, deploying, and running tests that use the Windows Driver Test Framework (WDTF).
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 77402D9A-DD21-4B7F-B052-43DB8C04EA1B
---

# WDTF Quick Start


The Windows Driver Kit 8.0 provides an integrated solution for writing, deploying, and running tests that use the Windows Driver Test Framework (WDTF). Using the WDK, you can configure a remote computer for deploying, testing, and debugging a driver. When you configure the remote computer, the Windows Driver Test Framework runtime is installed.

## <a href="" id="installing-wdtf--runtime-library"></a>Installing WDTF runtime library


**To install WDTF runtime library using Visual Studio and the WDK**

1.  Install Visual Studio and then install the WDK.

2.  Configure a remote computer for testing and deployment (**Driver** &gt; **Test** &gt; **Configure computers...**). When you configure the test computer, the Windows Driver Test Framework runtime is installed. For more information, see [Deploying a Driver to a Test Computer](https://msdn.microsoft.com/windows-drivers/develop/deploying_a_driver_to_a_test_computer) and see [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/library/windows/hardware/dn745909) or [Provision a computer for driver deployment and testing (WDK 8)](https://msdn.microsoft.com/library/windows/hardware/dn745909).

**To install WDTF runtime library manually**

-   When you install the WDK, the installation package for the Windows Driver Test Framework runtime is also installed. You need to copy the installation package to a test computer and run a command. For information, see [WDTF Runtime Library](https://msdn.microsoft.com/library/windows/hardware/hh831856) and "Manually installing WDTF runtime library on a test computer (alternative method)."

## <a href="" id="writing-tests-with-wdtf--"></a>Writing tests with WDTF


The WDK provides templates for writing tests with WDTF. See [How to write a driver test using a Driver Test template](https://msdn.microsoft.com/windows-drivers/develop/how_to_write_a_driver_test_). You can also use a template to create a WDTF SimpleIO plug-in for your target device. For information, see [Writing a WDTF SimpleIO plug-in for your device](writing-a-wdtf-simpleio-plug-in-for-your-device.md).

## Running WDTF tests


When you build your driver test in Visual Studio using a WDTF Driver test template, the new test will be available for deployment to a test computer. By default, the tests that you create will appear in the test category **My Test Category**. The names of the tests are based upon the test cases that you choose, and they will have names such as **My Plug and Play Surprise Remove Test**. During each build of the test, the tests will be overwritten and available to run in the Easily Run Tests feature. For more information, see [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20WDTF%20Quick%20Start%20%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


