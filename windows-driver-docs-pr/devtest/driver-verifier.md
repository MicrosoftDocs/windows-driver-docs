---
title: Driver Verifier
description: Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system.
keywords:
- verifying drivers WDK , Driver Verifier
- driver verification WDK , Driver Verifier
- Driver Verifier WDK
- Driver Verifier WDK , about Driver Verifier
- illegal function calls WDK Driver Verifier
- stress testing WDK Driver Verifier
ms.date: 08/06/2021
---

# Driver Verifier

Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system. Driver Verifier can subject Windows drivers to a variety of stresses and tests to find improper behavior. You can configure which tests to run, which allows you to put a driver through heavy stress loads or through more streamlined testing. You can also run Driver Verifier on multiple drivers simultaneously, or on one driver at a time.

> [!Caution]
> <ul><li>Running Driver Verifier could cause the computer to crash.</li>
> <li>You should only run Driver Verifier on computers that you are using for testing and debugging.</li>
> <li>You must be in the Administrators group on the computer to use Driver Verifier.</li> </ul>


## Where can I download Driver Verifier?

You don't need to download Driver Verifier, because it is included with most versions of Windows in %WinDir%\system32\ as Verifier.exe. (Driver Verifier is not included with Windows 10 S, so we recommend testing driver behavior on Windows 10 instead.) Driver Verifier is not distributed separately as a download package.

For information about changes in Driver Verifier for Windows 10 and previous versions of Windows, see <a href="driver-verifier--what-s-new.md" data-raw-source="[Driver Verifier: What's New](driver-verifier--what-s-new.md)">Driver Verifier: What's New</a>.


## When to use Driver Verifier

Run Driver Verifier throughout development and testing of your driver. More specifically, use Driver Verifier for the following purposes:

-   To find problems early in the development cycle, when they are easier and less costly to correct.

-   For troubleshooting and debugging test failures and computer crashes.

-   To monitor behavior when you deploy a driver for testing using the WDK, Visual Studio, and the tests from the [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) (Windows HLK) or [Windows Hardware Certification Kit](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) (for Windows 8.1). For more information about testing drivers, see [Testing a Driver](../develop/testing-a-driver.md).


## How to start Driver Verifier

You should only run Driver Verifier on test computers, or on computers that you are testing and debugging. To get the most benefit from Driver Verifier, you should use a kernel debugger and connect to the test computer. For more information about debugging tools, see [Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)](../debugger/index.md).

1. Start a **Command Prompt** window by selecting **Run as administrator**, and type **verifier** to open **Driver Verifier Manager**.

2. Select **Create standard settings** (the default task), and select **Next**.

   You can also choose **Create custom settings** to select from predefined settings, or to select individual options. For more information, see [Driver Verifier options and rule classes](driver-verifier-options.md) and [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

3. Under **Select what drivers to verify**, choose one of the selection schemes described in the following table.

   <table>
   <colgroup>
   <col width="50%" />
   <col width="50%" />
   </colgroup>
   <thead>
   <tr class="header">
   <th align="left">Option</th>
   <th align="left">Recommended use</th>
   </tr>
   </thead>
   <tbody>
   <tr class="odd">
   <td align="left"><strong>Automatically select unsigned drivers</strong></td>
   <td align="left"><p>Useful for testing on computers that are running versions of Windows that do not require signed drivers.</p></td>
   </tr>
   <tr class="even">
   <td align="left"><strong>Automatically select drivers built for older versions of Windows</strong></td>
   <td align="left"><p>Useful for testing driver compatibility with newer versions of Windows.</p></td>
   </tr>
   <tr class="odd">
   <td align="left"><strong>Automatically select all drivers installed on this computer</strong></td>
   <td align="left"><p>Provides maximum coverage in terms of the number of drivers that are tested on a system. This option is useful for test scenarios where a driver can interact with other devices or drivers on a system.</p>
   <p>This option can also exhaust the resources available for <a href="special-pool.md" data-raw-source="[Special Pool](special-pool.md)">Special Pool</a> and some resource tracking. Testing all drivers can also adversely affect system performance.</p></td>
   </tr>
   <tr class="even">
   <td align="left"><strong>Select driver names from a list</strong></td>
   <td align="left"><p>In most cases, you will want to specify which drivers to test.</p>
   <p>Selecting all drivers in a device stack allows the <a href="enhanced-i-o-verification.md" data-raw-source="[Enhanced I/O Verification](enhanced-i-o-verification.md)">Enhanced I/O Verification</a> option to track objects and check compliance because an I/O request packet (IRP) is passed between each of the drivers in the stack, which allows for a greater level of detail to be provided when an error is detected.</p>
   <p>Select a single driver if you are running a test scenario that measures system or driver performance metrics, or if you want to allocate the greatest number of resources available for detecting memory corruption or resource tracking issues (such as deadlocks or mutexes). The <a href="special-pool.md" data-raw-source="[Special Pool](special-pool.md)">Special Pool</a> and <a href="i-o-verification.md" data-raw-source="[I/O Verification](i-o-verification.md)">I/O Verification</a> options are more effective when used on one driver at a time.</p></td>
   </tr>
   </tbody>
   </table>


4. If you chose **Select driver names from a list**, select **Next**, and then select one or more specific drivers.

5. Select **Finish**, and then restart the computer.



>[!Note]
> You can also run Driver Verifier in a Command Prompt window without starting Driver Verifier Manager. For example, to run Driver Verifier with the standard settings on a driver called *myDriver.sys*, you would use the following command:
> ```console
> verifier /standard /driver myDriver.sys
> ```
>
> For more information about command line options, see [**Driver Verifier Command Syntax**](verifier-command-line.md).



## How to control Driver Verifier

You can use either Driver Verifier Manager or a command line to control Driver Verifier. To start Driver Verifier Manager, see [How to start Driver Verifier](#how-to-start-driver-verifier), earlier in this topic.

For each of the following actions, you can use Driver Verifier Manager or enter a command line.


**To stop or reset Driver Verifier**

1. In **Driver Verifier Manager**, select **Delete existing settings**, and then select **Finish**.

    or

    Enter the following command at a command prompt:

    ```console
    verifier /reset
    ```

2. Restart the computer.


**To view Driver Verifier statistics**

- In **Driver Verifier Manager**, select **Display information about the currently verified drivers**, and then select **Next**. Continuing to select **Next** displays additional information.

  or

  Enter the following command at a command prompt:

  ```console
  verifier /query
  ```


**To view Driver Verifier settings**

- In **Driver Verifier Manager**, select **Display existing settings**, and then select **Next**.

  or

  Enter the following command at a command prompt:

  ```console
  verifier /querysettings
  ```


## How to debug Driver Verifier violations

To get the most benefit from Driver Verifier, you should use a kernel debugger and connect it to the test computer. For an overview of debugging tools for Windows, see [Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)](../debugger/index.md).

If Driver Verifier detects a violation, it generates a bug check to stop the computer. This is to provide you with the most information possible for debugging the issue. When you have a kernel debugger connected to a test computer that is running Driver Verifier, and Driver Verifier detects a violation, Windows breaks into the debugger and displays a brief description of the error.

All violations detected by Driver Verifier result in bug checks. Common bug check codes include the following:

-   [**Bug Check 0xC1: SPECIAL\_POOL\_DETECTED\_MEMORY\_CORRUPTION**](../debugger/bug-check-0xc1--special-pool-detected-memory-corruption.md)
-   [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md)
-   [**Bug Check 0xC6: DRIVER\_CAUGHT\_MODIFYING\_FREED\_POOL**](../debugger/bug-check-0xc6--driver-caught-modifying-freed-pool.md)
-   [**Bug Check 0xC9: DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION**](../debugger/bug-check-0xc9--driver-verifier-iomanager-violation.md)
-   [**Bug Check 0xD6: DRIVER\_PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION**](../debugger/bug-check-0xd6--driver-page-fault-beyond-end-of-allocation.md)
-   [**Bug Check 0xE6: DRIVER\_VERIFIER\_DMA\_VIOLATION**](../debugger/bug-check-0xe6--driver-verifier-dma-violation.md)

For more information, see [Handling a Bug Check When Driver Verifier is Enabled](../debugger/handling-a-bug-check-when-driver-verifier-is-enabled.md). For tips about debugging Bug Check 0xC4, see [Debugging Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION](debugging-bug-check-0xc4--driver-verifier-detected-violation.md).

When you start a new debugging session, use the debugger extension command, [**!analyze**](../debugger/-analyze.md). In kernel mode, the **!analyze** command displays information about the most recent bug check. To display *additional* information, to help identify the faulting driver, add option **-v** to the command at the **kd>** prompt:

```dbgcmd
kd> !analyze -v
```

In addition to **!analyze**, you can enter the following debugger extensions at the **kd>** prompt to view information that is specific to Driver Verifier:

-   [**!verifier**](../debugger/-verifier.md) dumps captured Driver Verifier statistics. Use **!verifier -?** to display all of the available options.

    ```dbgcmd
    kd> !verifier
    ```

-   [**!deadlock**](../debugger/-deadlock.md) displays information related to locks or objects tracked by Driver Verifier's deadlock detection feature. Use **!deadlock -?** to display all of the available options.

    ```dbgcmd
    kd> !deadlock
    ```

-   [**!iovirp**](../debugger/-iovirp.md) \[*address*\] displays information related to an IRP tracked by I/O Verifier. For example:

    ```dbgcmd
    kd> !iovirp 947cef68
    ```

-   [**!ruleinfo**](../debugger/-ruleinfo.md) \[*RuleID*\] displays information related to the [DDI compliance checking](ddi-compliance-checking.md) rule that was violated. (*RuleID* is always the first argument to the bug check.) All rule IDs from DDI compliance checking are in the form 0x200*nn*. For example:

    ```dbgcmd
    kd> !ruleinfo 0x20005
    ```


## Related topics

[Driver Verifier: What's New](driver-verifier--what-s-new.md)

[Driver Verifier Options](driver-verifier-options.md)

[**Driver Verifier Command Syntax**](verifier-command-line.md)

[Using Driver Verifier](using-driver-verifier.md)

[Controlling Driver Verifier](controlling-driver-verifier.md)
