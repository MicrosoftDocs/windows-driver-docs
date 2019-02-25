---
title: Kernel synchronization delay fuzzing
description: The Kernel synchronization delay fuzzing option randomizes thread schedules to help detect concurrency bugs in drivers.
ms.assetid: B4BB3A75-C458-4718-8BE9-065CFC09E194
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel synchronization delay fuzzing


The Kernel synchronization delay fuzzing option randomizes thread schedules to help detect concurrency bugs in drivers.

**Caution**  This option is not intended for use when you are verifying all (or a large collection of) drivers on a computer. This option should be used only when you are doing targeted testing of individual drivers or their attached filter drivers. Using this option on a large number of drivers at the same time could cause unpredictable results, and could force crashes in components unrelated to the driver(s) you are testing.

 

**Note**  This option is available starting with Windows 8.1.

 

When the option is selected, Driver Verifier inserts random delays at various points in the threads. Like the [Power Framework Delay Fuzzing](concurrency-stress-test.md) option, the Kernel synchronization delay fuzzing option uses an algorithm that provides help improve the chances of finding errors in drivers. Kernel synchronization delay fuzzing improves upon traditional stress testing, where the test program is run for days or even weeks in hopes of catching problems in that can occur in concurrent execution.

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the Kernel synchronization delay fuzzing feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the Power Framework Delay Fuzzing option.

**Note**  The Kernel synchronization delay fuzzing option increases the probability of race conditions appearing at runtime by inserting randomized delays at various kernel API function calls. For these delays to be more effective, you can enable this option with other Driver Verifier options. Because of the delays that can be introduced, you can expect the computer to have slower response.

 

-   **At the command line**

    At the command line, the Kernel synchronization delay fuzzing is represented by **verifier /flags 0x00800000** (Bit 23). To activate Power Framework Delay Fuzzing, use a flag value of 0x00800000 or add 0x00800000 to the flag value. For example:

    ```
    verifier /flags 0x00800000 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **Kernel synchronization delay fuzzing**.
    5.  Restart the computer.

## <span id="Why_Kernel_synchronization_delay_fuzzing_"></span><span id="why_kernel_synchronization_delay_fuzzing_"></span><span id="WHY_KERNEL_SYNCHRONIZATION_DELAY_FUZZING_"></span>Why Kernel synchronization delay fuzzing?


Most driver routines are reentrant and concurrent. Bugs related to concurrency are notoriously hard to find. Bugs can include deadlocks and race conditions, caused by synchronization problems and bad timing between threads. Stress testing is the traditional testing technique for finding these bugs, but it can be slow and expensive, and the results are not always reproducible. The Kernel synchronization delay fuzzing option increases the probability of race conditions appearing at runtime by inserting randomized delays in various kernel API function calls. For example, if a race condition results in a driver accessing IRP after it has been cancelled, the Kernel synchronization delay fuzzing option increases the chances of this race condition in such a way that Driver Verifier will detect the error during testing. The Kernel synchronization delay fuzzing option enhances the power and effectiveness of Driver Verifier.

 

 





