---
title: Power Framework Delay Fuzzing
description: The Power Framework Delay Fuzzing option randomizes thread schedules to help detect concurrency bugs in drivers that use the power management framework (PoFx).
ms.assetid: A33DEA5B-4758-456A-B4CF-F036CB511A1F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power Framework Delay Fuzzing


The Power Framework Delay Fuzzing option randomizes thread schedules to help detect concurrency bugs in drivers that use the [power management framework (PoFx)](https://msdn.microsoft.com/library/windows/hardware/hh406637). This option is not recommended for drivers that do not directly utilize the power management framework (PoFx).

**Note**  This option is available starting with Windows 8.

 

When the option is selected, Driver Verifier inserts random delays at various points in the threads. The Power Framework Delay Fuzzing option uses an algorithm that provides probabilistic guarantees for finding errors in drivers. Power Framework Delay Fuzzing improves upon traditional stress testing, where the test program is run for days or even weeks in hopes of catching problems in that can occur in concurrent execution.

Most driver routines are reentrant and concurrent. Concurrency bugs are notoriously hard to find. Bugs can include deadlocks and race conditions, caused by synchronization problems and bad timing between threads. Stress testing is the traditional testing technique, but it can be slow and expensive, and the results are not always reproducible. The Power Framework Delay Fuzzing option increases the probability of race conditions appearing at runtime by inserting randomized delays at various power API function calls. For example, if a race condition results in a driver accessing IRP after it has been cancelled, the Power Framework Delay Fuzzing option increases the chances of this race condition in such a way that Driver Verifier will detect the error during testing. The Power Framework Delay Fuzzing option extends the power and usefulness of Driver Verifier.

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the Power Framework Delay Fuzzing feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the Power Framework Delay Fuzzing option.

**Note**  The Power Framework Delay Fuzzing option increases the probability of race conditions appearing at runtime by inserting randomized delays at various power API function calls. For these delays to be more effective, you can enable this option with other Driver Verifier options. Because of the delays that can be introduced, you can expect the computer to have slower response.

 

-   **At the command line**

    At the command line, the Power Framework Delay Fuzzing is represented by **verifier /flags 0x00008000 (Bit 15)**. To activate Power Framework Delay Fuzzing, use a flag value of 0x00008000 or add 0x00008000 to the flag value. For example:

    ```
    verifier /flags 0x00008000 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) Power Framework Delay Fuzzing.
    5.  Restart the computer.

 

 





