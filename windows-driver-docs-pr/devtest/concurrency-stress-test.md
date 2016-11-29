---
title: Power Framework Delay Fuzzing
description: The Power Framework Delay Fuzzing option randomizes thread schedules to help detect concurrency bugs in drivers that use the power management framework (PoFx).
ms.assetid: A33DEA5B-4758-456A-B4CF-F036CB511A1F
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Power%20Framework%20Delay%20Fuzzing%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




