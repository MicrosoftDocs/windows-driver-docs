---
title: Driver Verifier Properties for  Driver Package Projects
description: Driver Verifier is a run-time verification tool that increases the effectiveness of your driver testing.
ms.date: 04/20/2017
---

# Driver Verifier Properties for Driver Package Projects

[Driver Verifier](../devtest/driver-verifier.md) is a run-time verification tool that increases the effectiveness of your driver testing. You can enable and configure Driver Verifier to run on all test computers when you deploy your driver for testing.

You should always set up a kernel mode debugging connection with the test computer when you enable Driver Verifier on the remote test computer. For information about configuring a target computer and setting up a debug cable, see [Getting Started with Windows Debugging](../debugger/getting-started-with-windows-debugging.md).

## <span id="Setting_Driver_Verifier_properties_for_driver_package_projects"></span><span id="setting_driver_verifier_properties_for_driver_package_projects"></span><span id="SETTING_DRIVER_VERIFIER_PROPERTIES_FOR_DRIVER_PACKAGE_PROJECTS"></span>Setting Driver Verifier properties for driver package projects


1.  Open the property pages for your driver package. Select and hold (or right-click) the driver package project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver package, select **Configuration Properties**, select **Driver Install**, and then select **Driver Verification**.
3.  Select the **Enable Driver Verification** option. When this option is selected, you can select the driver or drivers to verify on the test computer and you can select the [Driver Verifier](../devtest/driver-verifier.md) options to use.

## <span id="Project_Configuration_and_Platform"></span><span id="project_configuration_and_platform"></span><span id="PROJECT_CONFIGURATION_AND_PLATFORM"></span>Project Configuration and Platform


The configuration list and platform list let you apply different deployment settings for different project configuration and platform combinations. For example, you can deploy a driver to one test computer using a set of deployment options for debug builds and to a different test computer using deployment options for release builds.

## <span id="Enable_Driver_Verifier"></span><span id="enable_driver_verifier"></span><span id="ENABLE_DRIVER_VERIFIER"></span>Enable Driver Verifier


You can enable Driver Verifier on the test computer for all drivers on the computer, for the driver project only, or for a list of specified drivers. For example, you might want to enable Driver Verifier for the set of drivers on the stack for a particular device.

## <span id="Verify_Drivers"></span><span id="verify_drivers"></span><span id="VERIFY_DRIVERS"></span>Verify Drivers


Specifies which driver or drivers to verify on the test computer.

<span id="All_Drivers"></span><span id="all_drivers"></span><span id="ALL_DRIVERS"></span>**All Drivers**  
Specifies that Driver Verifier verifies all installed drivers on the remote test computer.

<span id="Project_Output"></span><span id="project_output"></span><span id="PROJECT_OUTPUT"></span>**Project Output**  
Specifies that Driver Verifier verifies the driver project installed on the remote test computer. This is the default option.

<span id="Driver_List"></span><span id="driver_list"></span><span id="DRIVER_LIST"></span>**Driver List**  
Specifies the driver or list of drivers that Driver Verifier verifies on the remote test computer. For example, you could list all of the drivers associated with a particular device. Specify the drivers by binary name, for example, Driver.sys. Use a semicolon to separate a list of drivers. Wildcard values, such as *n\*.sys*, are not supported.

## <span id="Driver_Verifier_Standard_Flags"></span><span id="driver_verifier_standard_flags"></span><span id="DRIVER_VERIFIER_STANDARD_FLAGS"></span>Driver Verifier Standard Flags


You can configure the following Driver Verifier options on the test computer.

-   [DDI compliance checking](../devtest/ddi-compliance-checking.md) (Windows 8)

    When this option is active, Driver Verifier applies a set of device driver interface (DDI) rules that check for the proper interaction between a driver and the kernel interface of the operating system.

-   [Deadlock detection](../devtest/deadlock-detection.md)

    When this option is active, Driver Verifier monitors the driver's use of spin locks, mutexes, and fast mutexes. This detects whether the driver's code has the potential for causing a deadlock at some point.

-   [DMA verification](../devtest/dma-verification.md)

    When this option is active, Driver Verifier monitors the driver's use of direct memory access (DMA) routines. This detects improper use of DMA buffers, adapters, and map registers.

-   [Force IRQL checking](../devtest/force-irql-checking.md)

    When this option is active, Driver Verifier places extreme memory pressure on the driver by invalidating pageable code. If the driver attempts to access paged memory at the wrong IRQL or while holding a spin lock, Driver Verifier detects this behavior.

-   [I/O verification](../devtest/i-o-verification.md)

    When this option is active, Driver Verifier allocates the driver's Interrupt Request Packets (IRPs) from a special pool, and monitors the driver's I/O handling. This detects illegal or inconsistent use of I/O routines. Driver Verifier also monitors the calls of several I/O Manager routines and performs stress testing of Plug-and-Play (PnP) IRPs, power IRPs and WMI IRPs.

-   [Miscellaneous checks](../devtest/miscellaneous-checks.md)

    When this option is active, Driver Verifier looks for common causes of driver crashes, such as the mishandling of freed memory.

-   [Pool tracking](../devtest/pool-tracking.md)

    When this option is active, Driver Verifier checks to see whether the driver has freed all of its memory allocations when it is unloaded. This reveals memory leaks.

-   [Security checks](../devtest/security-checks.md)

    When this option is active, Driver Verifier looks for common errors that can result in security vulnerabilities, such as a reference to user-mode addresses by kernel-mode routines.

-   [Special pool checking](../devtest/special-pool.md)

    When this option is active, Driver Verifier allocates most of the driver's memory requests from a special pool. This special pool is monitored for memory overruns, memory underruns, and memory that is accessed after it is freed.

## <span id="Driver_Verifier_Scenario_Specific_Settings"></span><span id="driver_verifier_scenario_specific_settings"></span><span id="DRIVER_VERIFIER_SCENARIO_SPECIFIC_SETTINGS"></span>Driver Verifier Scenario Specific Settings


-   [Low resources simulation](../devtest/low-resources-simulation.md)

    When this option is active, Driver Verifier randomly fails pool allocation requests and other resource requests. By injecting these allocation faults into the system, Driver Verifier tests the driver's ability to cope with a low-resource situation.

-   [Force pending I/O requests](../devtest/force-pending-i-o-requests.md)

    When this option is active, Driver Verifier tests the driver's response to STATUS\_PENDING return values by returning STATUS\_PENDING for random calls to [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

-   [IRP logging](../devtest/irp-logging.md)

    When this option is active, Driver Verifier monitors a driver's use of IRPs and creates a log of IRP use.

-   [Invariant MDL Checking for Stack](../devtest/invariant-mdl-checking-for-stack.md) (Windows 8)

    The [Invariant MDL Checking for Stack](../devtest/invariant-mdl-checking-for-stack.md) option monitors how the driver handles invariant MDL buffers across the driver stack. Driver Verifier can detect illegal modification of invariant MDL buffers. To use this option, I/O Verification must be enabled on at least one driver.

-   [Invariant MDL Checking for Driver](../devtest/invariant-mdl-checking-for-driver.md) (Windows 8)

    The [Invariant MDL Checking for Driver](../devtest/invariant-mdl-checking-for-driver.md) option monitors how the driver handles invariant MDL buffers on a per-driver basis. This option detects illegal modification of invariant MDL buffers. To use this option, you must enable I/O Verification on at least one driver.

-   [Power Framework Delay Fuzzing](../devtest/concurrency-stress-test.md) (Windows 8)

    When this option is active, Driver Verifier randomizes thread schedules to help flush out concurrency errors in the driver.

-   [Stack Based Failure Injection](../devtest/stack-based-failure-injection.md) (Windows 8)

    The [Stack Based Failure Injection](../devtest/stack-based-failure-injection.md) option injects resource failures in kernel-mode drivers. This option uses a special driver, KmAutoFail.sys, in conjunction with [Driver Verifier](../devtest/driver-verifier.md) to penetrate driver error handling paths.

    **Note**  You cannot combine [Stack Based Failure Injection](../devtest/stack-based-failure-injection.md) with [Low resources simulation](../devtest/low-resources-simulation.md).

     

## <span id="Driver_Verifier_options_that_require_I_O_Verification"></span><span id="driver_verifier_options_that_require_i_o_verification"></span><span id="DRIVER_VERIFIER_OPTIONS_THAT_REQUIRE_I_O_VERIFICATION"></span>Driver Verifier options that require I/O Verification


There are four options that require you to first enable [I/O Verification](../devtest/i-o-verification.md). If I/O Verification is not enabled, these options are not enabled.

-   [Force Pending I/O Requests](../devtest/force-pending-i-o-requests.md)
-   [IRP Logging](../devtest/irp-logging.md)
-   [Invariant MDL Checking for Stack](../devtest/invariant-mdl-checking-for-stack.md)
-   [Invariant MDL Checking for Driver](../devtest/invariant-mdl-checking-for-driver.md)

## <span id="related_topics"></span>Related topics


* [Driver Verifier](../devtest/driver-verifier.md)
* [How to test a driver at runtime using Visual Studio](testing-a-driver-at-runtime.md)
* [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
* [Getting Started with Windows Debugging](../debugger/getting-started-with-windows-debugging.md)
 

