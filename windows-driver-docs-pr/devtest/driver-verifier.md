---
title: How to Use Driver Verifier for Driver Testing
description: "Learn how to use Driver Verifier to monitor and debug Windows drivers, identify issues early, and improve driver performance. Get step-by-step setup instructions and debugging techniques."
keywords:
- verifying drivers WDK , Driver Verifier
- driver verification WDK , Driver Verifier
- Driver Verifier WDK
- Driver Verifier WDK , about Driver Verifier
- illegal function calls WDK Driver Verifier
- stress testing WDK Driver Verifier
ms.date: 11/03/2025
ms.topic: concept-article
---

# Driver Verifier

Driver Verifier is a Windows testing tool that helps you identify driver issues before they cause system crashes or corruption. By monitoring kernel-mode drivers and graphics drivers in real time, Driver Verifier detects illegal function calls and problematic actions that could destabilize your system.

Whether you're developing new drivers or troubleshooting existing ones, Driver Verifier provides the early detection and debugging capabilities you need to build reliable, high-quality drivers. This comprehensive guide covers everything from basic setup to advanced debugging techniques.

- Learn when and why to use Driver Verifier
- Set up Driver Verifier for your testing environment  
- Configure verification options for your specific needs
- Debug violations and interpret results
- Apply best practices for driver testing workflows

> [!IMPORTANT]
> - Running Driver Verifier could cause the computer to crash. 
> - Only run Driver Verifier on computers that you use for testing and debugging. 
> - You must be in the Administrators group on the computer to use Driver Verifier.

## Where can I get Driver Verifier?

You don't need to get Driver Verifier, because most versions of Windows include it in %WinDir%\system32\ as Verifier.exe. (Driver Verifier isn't included with Windows 10 S, so we recommend testing driver behavior on Windows 10 instead.) Driver Verifier isn't distributed separately as a download package.

For information about changes in Driver Verifier for Windows 10 and previous versions of Windows, see <a href="driver-verifier--what-s-new.md" data-raw-source="[Driver Verifier: What's New](driver-verifier--what-s-new.md)">Driver Verifier: What's New</a>.

## When to use Driver Verifier

Use Driver Verifier throughout your driver development and testing process:

### Early development

- **Find problems early** in the development cycle when they're easier and less costly to correct
- **Prevent costly delays** by catching issues before they reach production

### Troubleshooting

- **Debug test failures** and computer crashes quickly
- **Identify root causes** of driver-related system instability

### Testing and deployment

- **Monitor driver behavior** when deploying for testing with WDK, Visual Studio, and [Windows Hardware Lab Kit](/windows-hardware/test/hlk/) (Windows HLK)
- **Ensure compatibility** with [Windows Hardware Certification Kit](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) requirements

For comprehensive driver testing guidance, see [Testing a Driver](../develop/testing-a-driver.md).

> [!IMPORTANT]
> Windows Hardware Compatibility Program requires CodeQL for Static Tool Logo (STL) Tests on our Client and Server Operating Systems. We continue to maintain support for SDV and CA on older products.  Partners are highly encouraged to review the CodeQL requirements for the [Static Tool Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae).
> For more information about using CodeQL, see [CodeQL and the Static Tools Logo Test](static-tools-and-codeql.md).

## How to start Driver Verifier

Run Driver Verifier only on test computers, or on computers that you're testing and debugging. To get the most benefit from Driver Verifier, use a kernel debugger to connect to the test computer. For more information about debugging tools, see [Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)](../debugger/index.md).

1. Start a **Command Prompt** window by selecting **Run as administrator**, and type **verifier** to open **Driver Verifier Manager**.

1. Select **Create standard settings** (the default task), and select **Next**.

   You can also choose **Create custom settings** to select from predefined settings, or to select individual options. For more information, see [Driver Verifier options and rule classes](driver-verifier-options.md) and [Selecting Driver Verifier Options](selecting-driver-verifier-options.md).

1. Under **Select what drivers to verify**, choose one of the selection schemes described in the following table:

    | Option | Recommended use |
    | ------ | --------------- |
    | **Automatically select unsigned drivers** | Useful for testing on computers that are running versions of Windows that don't require signed drivers. |
    | **Automatically select drivers built for older versions of Windows** | Useful for testing driver compatibility with newer versions of Windows. |
    | **Automatically select all drivers installed on this computer** | Provides maximum coverage in terms of the number of drivers that are tested on a system. This option is useful for test scenarios where a driver can interact with other devices or drivers on a system. <br><br> This option can also exhaust the resources available for Special Pool and some resource tracking. Testing all drivers can also adversely affect system performance. |
    | **Select driver names from a list** | In most cases, you want to specify which drivers to test.<br><br>Selecting all drivers in a device stack allows the [Enhanced I/O Verification](enhanced-i-o-verification.md) option to track objects and check compliance because an I/O request packet (IRP) is passed between each of the drivers in the stack, which allows for a greater level of detail to be provided when an error is detected.<br><br>Select a single driver if you're running a test scenario that measures system or driver performance metrics, or if you want to allocate the greatest number of resources available for detecting memory corruption or resource tracking issues (such as deadlocks or mutexes). The [Special Pool](special-pool.md) and [I/O Verification](i-o-verification.md) options are more effective when used on one driver at a time. |    

1. If you chose **Select driver names from a list**, select **Next**, then select one or more specific drivers.

1. Select **Finish**, then restart the computer.

>[!Note]
> When using driver verifier with Windows versions 20150 to 25126, if you select *ntoskrnl* you might receive an invalid state error.  
> To avoid this issue, either unselect *ntoskrnl* or upgrade to a version of Windows after build 25126.

### Run driver verifier at a command prompt

You can also run Driver Verifier in a Command Prompt window without starting Driver Verifier Manager. For example, to run Driver Verifier with the standard settings on a driver called *myDriver.sys*, use the following command:

```console
verifier /standard /driver myDriver.sys
```

For more information about command line options, see [**Driver Verifier Command Syntax**](verifier-command-line.md).

## How to control Driver Verifier

Choose your preferred method to control Driver Verifier:

- **Driver Verifier Manager** (GUI) - Easier for beginners, visual interface
- **Command line** - Faster for experienced users, scriptable

> [!NOTE]
> To start Driver Verifier Manager, see [How to start Driver Verifier](#how-to-start-driver-verifier) preceding section.

### Common Driver Verifier tasks

For each of the following actions, you can use Driver Verifier Manager or enter a command line.

To stop or reset Driver Verifier

1. In **Driver Verifier Manager**, select **Delete existing settings**, then select **Finish**.

    or

    Enter the following command at a command prompt:

    ```console
    verifier /reset
    ```

1. Restart the computer.

To view Driver Verifier statistics

In **Driver Verifier Manager**, select **Display information about the currently verified drivers**, then select **Next**. Continuing to select **Next** displays additional information.

  or

  Enter the following command at a command prompt:

  ```console
  verifier /query
  ```

To view Driver Verifier settings

In **Driver Verifier Manager**, select **Display existing settings**, then select **Next**.

  or

  Enter the following command at a command prompt:

  ```console
  verifier /querysettings
  ```

## How to debug Driver Verifier violations

To get the most benefit from Driver Verifier, use a kernel debugger and connect it to the test computer. For an overview of debugging tools for Windows, see [Debugging Tools for Windows (WinDbg, KD, CDB, NTSD)](../debugger/index.md).

If Driver Verifier detects a violation, it generates a bug check to stop the computer. This action provides you with the most information possible for debugging the issue. When you connect a kernel debugger to a test computer running Driver Verifier and Driver Verifier detects a violation, Windows breaks into the debugger and displays a brief description of the error.

All violations detected by Driver Verifier result in bug checks. This bug check is typically a Bug Check 0xC4. For more information, see [Debugging Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION](debugging-bug-check-0xc4--driver-verifier-detected-violation.md) and [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](../debugger/bug-check-0xc4--driver-verifier-detected-violation.md).

Other common bug check codes include the following codes:

- [**Bug Check 0xC1: SPECIAL\_POOL\_DETECTED\_MEMORY\_CORRUPTION**](../debugger/bug-check-0xc1--special-pool-detected-memory-corruption.md)
- [**Bug Check 0xC6: DRIVER\_CAUGHT\_MODIFYING\_FREED\_POOL**](../debugger/bug-check-0xc6--driver-caught-modifying-freed-pool.md)
- [**Bug Check 0xC9: DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION**](../debugger/bug-check-0xc9--driver-verifier-iomanager-violation.md)
- [**Bug Check 0xD6: DRIVER\_PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION**](../debugger/bug-check-0xd6--driver-page-fault-beyond-end-of-allocation.md)
- [**Bug Check 0xE6: DRIVER\_VERIFIER\_DMA\_VIOLATION**](../debugger/bug-check-0xe6--driver-verifier-dma-violation.md)

For more information, see [Handling a Bug Check When Driver Verifier is Enabled](../debugger/handling-a-bug-check-when-driver-verifier-is-enabled.md).

When you start a new debugging session, use the debugger extension command, [**!analyze**](../debuggercmds/-analyze.md). In kernel mode, the **!analyze** command displays information about the most recent bug check. To display *additional* information to help identify the faulting driver, add option **-v** to the command at the **kd>** prompt:

```dbgcmd
kd> !analyze -v
```

In addition to **!analyze**, you can enter the following debugger extensions at the **kd>** prompt to view information that is specific to Driver Verifier:

- [**!verifier**](../debuggercmds/-verifier.md) dumps captured Driver Verifier statistics. Use **!verifier -?** to display all of the available options.

    ```dbgcmd
    kd> !verifier
    ```

- [**!deadlock**](../debuggercmds/-deadlock.md) displays information related to locks or objects tracked by Driver Verifier's deadlock detection feature. Use **!deadlock -?** to display all of the available options.

    ```dbgcmd
    kd> !deadlock
    ```

- [**!iovirp**](../debuggercmds/-iovirp.md) \[*address*\] displays information related to an IRP tracked by I/O Verifier. For example:

    ```dbgcmd
    kd> !iovirp 947cef68
    ```

- Look up the [DDI compliance checking](ddi-compliance-checking.md) rule that was violated. (*RuleID* is always the first argument to the bug check.) All rule IDs from DDI compliance checking are in the form 0x200*nn*. 

## Next steps

Now that you understand the basics of Driver Verifier, explore these related topics:

- **[Driver Verifier Options](driver-verifier-options.md)** - Configure advanced testing scenarios
- **[Using Driver Verifier](using-driver-verifier.md)** - Advanced usage patterns and best practices  
- **[DDI compliance checking](ddi-compliance-checking.md)** - Understand compliance rules and violations
- **[Debugging Tools for Windows](../debugger/index.md)** - Set up kernel debugging for Driver Verifier

### Get Help

- **[Driver Verifier Command Syntax](verifier-command-line.md)** - Complete command reference
- **[Controlling Driver Verifier](controlling-driver-verifier.md)** - Advanced control techniques
