---
title: How to Collect IRP Coverage Data
description: How to Collect IRP Coverage Data
ms.assetid: f65422fe-f524-41c1-a532-a2c615d65f72
keywords:
- Driver Coverage Toolkit WDK , collecting data
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Collect IRP Coverage Data


**Note**  The Driver Coverage Toolkit is no longer needed in Windows 10 and the installer is no longer included in the WDK. To perform tasks described here in Windows 10, instead use [Driver Verifier](driver-verifier.md) and [IRP Logging](irp-logging.md).

 

The following steps describe how to collect coverage data of I/O request packets (IRPs) by using the Driver Coverage tools and [Driver Coverage filter driver](driver-coverage-filter-driver.md). The tools are available as part of the [Device Fundamentals Tests](device-fundamentals-tests.md), under the Coverage category.

For information about setting up the WDK and the Visual Studio test environment, see [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime). For information about selecting and configuring tests and tool parameters, see [How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests) and [Device Fundamentals Test Parameters](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests).

1.  Install the [Driver Coverage filter driver](driver-coverage-filter-driver.md) on the test computer.

    -   To install the filter driver and enable IRP coverage on specified device(s), run the **Enable IRP coverage data collection** tool. The tool is available as part of the [Device Fundamentals Tests](device-fundamentals-tests.md), under Coverage.

    -   To install the filter driver and enable IRP coverage on specified device(s), use the *DQ* parameter to specify the device(s) to monitor.

    -   To install the Driver Coverage filter driver as an upper-filter driver or a lower-filter driver for the device(s) use the *UpperFilter* parameter. For information about the coverage filter driver and guidelines about how to install the driver, see [Driver Coverage filter driver](driver-coverage-filter-driver.md)

    For information running the tools, see [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime) and [How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests).

2.  Erase the current IRP coverage data.

    Before you start your code coverage tests on one or more devices, first clear the IRP coverage data that has already been collected by the [Driver Coverage filter driver](driver-coverage-filter-driver.md). To do this, run the **Clear IRP Coverage Data** tool on the test computer.

3.  Restart the test computer.

    After you have installed the [Driver Coverage filter driver](driver-coverage-filter-driver.md) on one or more devices, restart the test computer to load the Driver Coverage filter driver and start IRP coverage.

4.  Verify the [Driver Coverage filter driver](driver-coverage-filter-driver.md) installation.

    After the test computer has restarted, verify that the filter driver is installed and the correct devices are enabled for IRP coverage. To do this, run the **Display Devices enabled for IRP coverage data collection** tool on the test computer.

    ```
    Drvcov /D
    ```

    The following example shows sample output from this tool:

    ```
    |------------------------------------------------------------------
    | List of devices we can get coverage data from.
    |------------------------------------------------------------------
    |  Device # : 1 
    |  Devnode #: 3884 Class:  USB Desc:  USB Root Hub
    |  Device ID: " USB\ROOT_HUB\4&413399C&0"
    |------------------------------------------------------------------
    | 1 device(s) found.
    |------------------------------------------------------------------
    ```

5.  Collect the IRP coverage data.

    You are now ready to collect IRP coverage data for your device(s). First run your code coverage tests on the test computer. When you are finished running your code coverage tests, you can view IRP coverage reports. To do this, run the **Display collected IRP coverage data** tool on the test computer.

    For information about how to analyze the IRP coverage data, see [How to Analyze IRP Coverage Data](how-to-analyze-irp-coverage-data.md).

6.  Disable IRP Coverage and uninstall the [Driver Coverage filter driver](driver-coverage-filter-driver.md).

    After you have fully exercised your code coverage tests, you can disable IRP coverage all devices by running the **Disable IRP coverage data collection** tool on the test computer.

    When the last device has been disabled for IRP coverage, the filter driver will no longer load whenever you restart the test computer. However, to unload the filter driver from memory, you must restart the test computer.

 

 





