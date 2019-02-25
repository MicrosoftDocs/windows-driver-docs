---
title: Low Resources Simulation
description: Low Resources Simulation
ms.assetid: 2710fa23-26cd-493b-abb4-3a0969a98eb1
keywords:
- Low Resources Simulation option WDK Driver Verifier
- low-memory checks WDK Driver Verifier
- insufficient memory checks WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Low Resources Simulation


## <span id="ddk_low_resources_simulation_tools"></span><span id="DDK_LOW_RESOURCES_SIMULATION_TOOLS"></span>


When the Low Resources Simulation option (called *Randomized low resources simulation* in Windows 8.1) is active, Driver Verifier fails random instances of the driver's memory allocations, as might occur if the driver was running on a computer with insufficient memory. This tests the driver's ability to respond properly to low memory and other low-resource conditions.

The Low Resources Simulation test fails allocations requested by calls to several different functions, including [**ExAllocatePoolWithXXX**](https://msdn.microsoft.com/library/windows/hardware/ff544520), [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559), [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664), [**MmMapLockedPagesSpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554629), and [**MmMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff554618).

Starting with Windows Vista, the Low Resource Simulation test also injects faults into [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257), [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263), [**IoAllocateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff548276), [**IoAllocateErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548245), [**MmAllocateContiguousMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554460), [**MmAllocateContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554464), [**MmAllocatePagesForMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554482), and [**MmAllocatePagesForMdlEx**](https://msdn.microsoft.com/library/windows/hardware/ff554489). Moreover, starting with Windows Vista, when Low Resources Simulation is enabled, calls to [**KeWaitForMultipleObjects**](https://msdn.microsoft.com/library/windows/hardware/ff553324) or [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) with the *Alertable* parameter set to **TRUE** can return STATUS\_ALERTED when running in the context of non-privileged processes. This simulates a possible thread alert coming from another thread in the same non-privileged application.

The Low Resource Simulation test also injects faults into the following GDI functions: [**EngAllocMem**](https://msdn.microsoft.com/library/windows/hardware/ff564176), [**EngAllocUserMem**](https://msdn.microsoft.com/library/windows/hardware/ff564178), [**EngCreateBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff564199), [**EngCreateDeviceSurface**](https://msdn.microsoft.com/library/windows/hardware/ff564206), [**EngCreateDeviceBitmap**](https://msdn.microsoft.com/library/windows/hardware/ff564204), [**EngCreatePalette**](https://msdn.microsoft.com/library/windows/hardware/ff564212), [**EngCreateClip**](https://msdn.microsoft.com/library/windows/hardware/ff564202), [**EngCreatePath**](https://msdn.microsoft.com/library/windows/hardware/ff564755), [**EngCreateWnd**](https://msdn.microsoft.com/library/windows/hardware/ff564769), [**EngCreateDriverObj**](https://msdn.microsoft.com/library/windows/hardware/ff564207), [**BRUSHOBJ\_pvAllocRbrush**](https://msdn.microsoft.com/library/windows/hardware/ff538263), and [**CLIPOBJ\_ppoGetPath**](https://msdn.microsoft.com/library/windows/hardware/ff539423).

In Windows 7 and later versions of the Windows operating system, the Low Resources Simulation option supports memory that was allocated by using the following kernel APIs:

-   [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263)

-   [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) and the other routines that can allocate I/O request packet (IRP) data structures

-   [**RtlAnsiStringToUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff561729) and other run-time library (RTL) string routines

-   [**IoSetCompletionRoutineEx**](https://msdn.microsoft.com/library/windows/hardware/ff549686)

Starting with Windows 8.1, the Low Resources Simulation option also fails allocations requested by calls to MmAllocateNodePagesForMdlEx. In addition, for some functions, Driver Verifier now fills the allocated memory with a random pattern. But only in situations where the function returns uninitialized memory. These functions include:

-   [**MmAllocatePagesForMdlEx**](https://msdn.microsoft.com/library/windows/hardware/ff554489)
-   MmAllocateNodePagesForMdlEx
-   [**MmAllocateContiguousMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554460)
-   [**MmAllocateContiguousMemorySpecifyCache**](https://msdn.microsoft.com/library/windows/hardware/ff554464)
-   [**MmAllocateContiguousMemorySpecifyCacheNode**](https://msdn.microsoft.com/library/windows/hardware/ff554469)
-   [**MmAllocateContiguousNodeMemory**](https://msdn.microsoft.com/library/windows/hardware/jj602795)
-   [**MmAllocateNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554479)

### <span id="custom_settings_for_low_resources_simulation"></span><span id="CUSTOM_SETTINGS_FOR_LOW_RESOURCES_SIMULATION"></span>Custom Settings for Low Resources Simulation

On Windows Vista and later versions of Windows, you can specify the following custom settings.

-   **Probability** that a given allocation will fail. The default is 6%.

-   **Applications** affected. This setting limits the injected failed allocations to the specified applications. By default, all allocations are affected.

-   **Pool tags** affected. This setting limits the injected faults to allocations with the specified pool tags. By default, all allocations are affected.

-   **Delay** (in minutes) before allocations are failed. This delay allows the system to start up and stabilize before faults are injected. The default is eight minutes.

On operating systems prior to Windows Vista, you cannot customize these settings. The operating system uses the default values.

### <span id="low_resources_simulation_without_rebooting"></span><span id="LOW_RESOURCES_SIMULATION_WITHOUT_REBOOTING"></span>Low Resources Simulation without Rebooting

You can activate Low Resources Simulation on Windows 2000 and later versions of Windows without restarting the computer by using the **/volatile** parameter. The settings are effective immediately, but are lost if you shut down or restart the computer.

You can also store the Low Resources Simulation settings in the registry by omitting the **/volatile** parameter. These settings are effective only when you restart the computer, but they remain effective until you change them.

### <span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating This Option

You can activate the Low Resources Simulation option for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

-   **At the command line**

    At the command line, the Low Resources Simulation option is represented by **Bit 2 (0x4)**. To activate Low Resources Simulation, use a flags value of 0x4 or add 0x4 to the flags value. For example:

    ```
    verifier /flags 0x4 /driver MyDriver.sys
    ```

    The option will be active after the next boot.

    On Windows Vista and later versions of Windows, you can use the */faults* parameter or a flags value of **0x4** to activate Low Resources Simulation. To modify the settings for Low Resources Simulation, you must use **/faults**. For example:

    ```
    verifier /faults /driver MyDriver.sys
    ```

    On Windows 2000 and later versions of Windows, you can also activate and deactivate Low Resources Simulation without rebooting the computer by adding the **/volatile** parameter to the command. For example:

    ```
    verifier /volatile /flags 0x4 /adddriver MyDriver.sys
    ```

    This setting is effective immediately, but is lost when you shut down or reboot the computer. For details, see [Using Volatile Settings](using-volatile-settings.md).

    On Windows Vista, you can use the **/faults** parameter to represent Low Resources Simulation with the **/volatile** parameter to represent a setting that is effective without rebooting. The setting change will be displayed. For example:

    ```
    0>  verifier /volatile /faults /adddriver MyDriver.sys
    New Low Resources Simulation options:

    - Use default fault injection probability.
    - Allocations using any pool tag can be failed.
    - Simulate low resources conditions in any application.

    The new settings are in effect until you restart this computer
    or change them again.
    ```

-   **Using Driver Verifier Manager**
    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)**, and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select **Low resources simulation**.

### <span id="customizing_the_settings__windows_vista_and_later_"></span><span id="CUSTOMIZING_THE_SETTINGS__WINDOWS_VISTA_AND_LATER_"></span>Customizing the Settings (Windows Vista and later)

Starting with Windows Vista, you can change the default settings for the delay, probability, applications, and pool tags properties of the Low Resources Simulation option. You can change these settings by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

At the command line, the syntax for these settings is as follows:

**verifier** \[**/volatile**\] **/faults**\[*Probability*|*PoolTags*|*Applications*|*DelayMins*\]\[**/driver**|*DriverList*\]

**Note**  The custom settings parameters must appear in the order displayed. If you omit a value, type quotation marks to hold its place.



**Subparameters**

- **/faults**

  Enables the Low Resources Simulation option in Driver Verifier. (You cannot use /flags 0x4 with the custom setting subparameters.)

- *Probability*

  Specifies the probability that Driver Verifier will fail a given allocation. Type a number (in decimal or hexadecimal format) to represent the number of chances in 10,000 that Driver Verifier will fail the allocation. The default value, 600, means 600/10000, or 6%.

- *PoolTags*

  Limits the allocations that Driver Verifier can fail to allocations with the specified pool tags. You can use a wildcard character (**\\***) to represent multiple pool tags. To list multiple pool tags, separate the tags with spaces. By default, all allocations can fail.

- *Applications*

  Limits the allocations that Driver Verifier can fail to allocations for the specified program. Type the name of an executable file. To list programs, separate the program names with spaces. By default, all allocations can fail.

- *DelayMins*

  Specifies the number of minutes after booting during which Driver Verifier does not intentionally fail any allocations. This delay allows the drivers to load and the system to stabilize before the test begins. Type a number (in decimal or hexadecimal format). The default value is 8 (minutes).

For example, the following command enables Low Resources Simulation with a probability of 10% (1000/10000) and a delay of five minutes for the pool tags, Tag1 and Fred, and the application, Notepad.exe.

```
verifier /faults 1000 "Tag1 Fred" Notepad.exe 5
```

The following command enables Low Resources Simulation with the default values, except that it extends the delay to 10 minutes.

```
verifier /faults "" "" "" 0xa
```

**Using Driver Verifier Manager**

1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
2.  Select **Create custom settings (for code developers)**, and then click **Next**.

3.  Select **Select individual settings from a full list**.

4.  Select **Low resources simulation**, and then click **Next.**

5.  Change the settings for the delay, probability, applications, and pool tags properties as desired.

### <span id="viewing_the_results"></span><span id="VIEWING_THE_RESULTS"></span>Viewing the Results

You can monitor the number of times Driver Verifier intentionally fails resource allocations by displaying the Driver Verifier *Faults Injected* global counter. This counter displays the total number of resource allocations that Driver Verifier failed deliberately since the last boot.

You can view this counter in a Driver Verifier log file (**/log**), at the command line (**/query**) or in Driver Verifier Manager. In Windows 2000, to view global counters, select the **Global Counters** tab. In later versions of Windows, select **Display information about the currently verified drivers** task, and then press **Next** twice. For more information see [Monitoring Global Counters](monitoring-global-counters.md).

You can also display the number of intentionally failed allocations and the number of total allocations (to calculate the probability) by using the **!verifier** debugger extension. The following example shows a sample of the **!verifier** output.

In this example, **Inject random low-resource API failures** indicates that Low Resources Simulation is enabled. **Resource Allocations Failed Deliberately** represents the number of intentionally failed allocations and **Pool Allocations Attempted** represents the total number of allocations.

```
!verifier

Verify Level 5 ... enabled options are:
        Special pool
        Inject random low-resource API failures

Summary of All Verifier Statistics

RaiseIrqls                             0x2c671f
AcquireSpinLocks                       0xca1a02
Synch Executions                       0x10a623
Trims                                  0x0

Pool Allocations Attempted             0x862e0e
Pool Allocations Succeeded             0x8626e3
Pool Allocations Succeeded SpecialPool 0x768060
Pool Allocations With NO TAG           0x0
Pool Allocations Failed                0x34f
Resource Allocations Failed Deliberately   0x3f5
```

To display the stack traces for the allocations most recently failed by Driver Verifier, use **!verifier 4** in the kernel debugger.

The following example shows a sample of the output from **!verifier 4**. By default, **!verifier 4** displays stack traces from the four most recently failed allocations, but you can use its *Quantity* parameter to increase the number of stack traces displayed. For example, !verifier 0x80 displays the 128 most recently failed allocations.

In this example, note that Verifier has intercepted and replaced the driver's call to **ExAllocatePoolWithTag**. One of the most common causes of driver crashes occurs when a driver attempts to allocate memory and then uses the pointer that the allocation function returns before verifying that it is not **NULL**.

```
kd> !verifier 4
Resource fault injection history:
Tracker @ 8354A000 (# entries: 80, size: 80, depth: 8)

Entry @ 8354B258 (index 75)

    Thread: C2638220

    816760CB nt!VerifierExAllocatePoolWithTag+0x49
    A4720443 win32k!bDeleteAllFlEntry+0x15d
    A4720AB0 win32k!GreEnableEUDC+0x70
    A47218FA win32k!CleanUpEUDC+0x37
    A473998E win32k!GdiMultiUserFontCleanup+0x5
    815AEACC nt!MiDereferenceSession+0x74
    8146D3B4 nt!MmCleanProcessAddressSpace+0x112
    815DF739 nt!PspExitThread+0x603

Entry @ 8354B230 (index 74)

    Thread: 8436D770

    816760CB nt!VerifierExAllocatePoolWithTag+0x49
    A462141C win32k!Win32AllocPool+0x13
    A4725F94 win32k!StubGdiAlloc+0x10
```

Experience with the Low Resources Simulation test reveals that most driver crashes are caused by the most recently failed allocation. In the example above, the crash was in the path of **win32k!GreEnableEUDC**. Examine the code in the path of the allocation to find the cause of the crash.

For information about **!verifier**, see the *Debugging Tools for Windows* documentation.

To view the settings in the registry at the command line, use the **/querysettings** option. For example:

```
C:\>verifier /querysettings
Special pool: Disabled
Pool tracking: Disabled
Force IRQL checking: Disabled
I/O verification: Disabled
Enhanced I/O verification: Disabled
Deadlock detection: Disabled
DMA checking: Disabled
Security checks: Disabled
Force pending I/O requests: Disabled
Low resources simulation: Enabled
IRP Logging: Disabled
Miscellaneous checks: Disabled
Disk integrity checking: Disabled

Low Resources Simulation options:

- Fault injection probability: 1/10000.
- Fail only allocations using pool tags: Tag1 Tag2.
- Simulate low resources conditions only in applications: test1.exe test2.exe.
- Boot time delay: 2 minutes.

Verified drivers:

blah.sys
```









