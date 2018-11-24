---
title: Driver Verifier
description: Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system.
ms.assetid: a8a78dde-930f-4d0b-be46-f7d07b0bf21b
keywords:
- verifying drivers WDK , Driver Verifier
- driver verification WDK , Driver Verifier
- Driver Verifier WDK
- Driver Verifier WDK , about Driver Verifier
- illegal function calls WDK Driver Verifier
- stress testing WDK Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Verifier


Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system. Driver Verifier can subject the Windows drivers to a variety of stresses and tests to find improper behavior.

You can run Driver Verifier on multiple drivers simultaneously, or on one driver at a time. You can configure which tests to run, which allows you to put a driver through heavy stress loads or through more streamlined testing.

-   [Where can I download Driver Verifier?](#where-can-i-download-driver-verifier)
-   [When to use Driver Verifier](#when-to-use-driver-verifier)
-   [How to start Driver Verifier](#how-to-start-driver-verifier)
-   [How to control Driver Verifier](#how-to-control-driver-verifier)
-   [How to debug Driver Verifier violations](#how-to-debug-driver-verifier-violations)
-   [Related topics](#related-topics)



## Where can I download Driver Verifier?


<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>You don&#39;t need to download Driver Verifier (Verifier.exe) as it is included in every version of Windows after Windows 2000, except for Windows 10 S. There isn&#39;t a separate Driver Verifier download package, it is located in the %windir%\system32 directory. </p>
<ul>
<li>Open a <strong>Command Prompt</strong> window (<strong>Run as administrator</strong>).</li>
<li>Type <strong>verifier</strong> to open the Driver Verifier Manager, or type <strong>verifier /?</strong> to view command line options. See <a href="verifier-command-line.md" data-raw-source="[&lt;strong&gt;Driver Verifier Command Syntax&lt;/strong&gt;](verifier-command-line.md)"><strong>Driver Verifier Command Syntax</strong></a> for more information.</li>
</ul>
<p></p>
<div class="alert">
<strong>Caution</strong><br/><ul>
<li>Running Driver Verifier could cause the computer to crash.</li>
<li>You should only run Driver Verifier on computers you are using for testing and debugging.</li>
<li>You must be in the Administrators group on the computer to use Driver Verifier.</li>
<li>Driver verifier is not included in Windows 10 S. We recommend testing driver behavior in Windows 10 instead.</li>
</ul>
</div>
<div>

</div>
<p>For information about changes in Driver Version for Windows 8.1 and previous versions of Windows, see <a href="driver-verifier--what-s-new.md" data-raw-source="[Driver Verifier: What&#39;s New](driver-verifier--what-s-new.md)">Driver Verifier: What&#39;s New</a>.</p></td>
</tr>
</tbody>
</table>





## When to use Driver Verifier


Run Driver Verifier throughout the driver development and test process.

-   Use Driver Verifier to find problems early in the development life cycle, when they are easier and less costly to correct.

-   Use Driver Verifier when you deploy a driver for testing using the WDK, Visual Studio, and the [Windows Hardware Certification Kit](http://go.microsoft.com/fwlink/p/?linkid=254893) (HCK) tests. See [Testing a Driver](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver).

-   Use Driver Verifier for troubleshooting and debugging test failures and computer crashes.



## How to start Driver Verifier


You should only run Driver Verifier on test computers, or computers you are testing and debugging. To get the most benefit from Driver Verifier, you should use a kernel debugger and connect to the test computer. See [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

1. Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2. Select **Create standard settings** (default) and click **Next**.

   You can also choose **Create custom settings** to select from predefined settings, or to select individual options. See [Driver Verifier Options](driver-verifier-options.md) and [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) for more information.

3. Select a driver or drivers to verify.

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
   <td align="left"><p>Useful option for testing on computers running versions of Windows that don&#39;t require signed drivers.</p></td>
   </tr>
   <tr class="even">
   <td align="left"><strong>Automatically select drivers built for older versions of Windows</strong></td>
   <td align="left"><p>Useful option for testing driver compatibility with newer versions of Windows.</p></td>
   </tr>
   <tr class="odd">
   <td align="left"><strong>Automatically select all drivers installed on this computer</strong></td>
   <td align="left"><p>Provides maximum coverage in terms of the number of drivers that are tested on a system. This option is useful for test scenarios where a driver can interact with other devices or drivers on a system.</p>
   <p>This option can also exhaust the resources available for <a href="special-pool.md" data-raw-source="[Special Pool](special-pool.md)">Special Pool</a> and some resource tracking. Testing all drivers can also adversely affect system performance.</p></td>
   </tr>
   <tr class="even">
   <td align="left"><strong>Select driver names from a list</strong></td>
   <td align="left"><p>In most cases, you will want to specify which drivers to test.</p>
   <p>Selecting all drivers in a device stack allows the <a href="enhanced-i-o-verification.md" data-raw-source="[Enhanced I/O Verification](enhanced-i-o-verification.md)">Enhanced I/O Verification</a> option to track objects and check compliance as an IRP is passed between each of the drivers in the stack and allows for a greater level of detail to be provided should an error be found.</p>
   <p>Select a single driver if you are running a test scenario that measures system or driver performance metrics, or if you want to allocate the greatest number of resources available for detecting memory corruption or resource tracking issues (deadlocks, mutexs). The <a href="special-pool.md" data-raw-source="[Special Pool](special-pool.md)">Special Pool</a> and <a href="i-o-verification.md" data-raw-source="[I/O Verification](i-o-verification.md)">I/O Verification</a> options will be more effective when used on one driver at a time.</p></td>
   </tr>
   </tbody>
   </table>



4. Click **Finish** and reboot the computer.

**Note**  You can also run Driver Verifier in a Command Prompt window. For example, to run Driver Verifier with the standard settings on a driver called myDriver.sys, you would use the following command:



```
verifier  /standard /driver myDriver.sys
```

See [**Driver Verifier Command Syntax**](verifier-command-line.md) for more information.



## How to control Driver Verifier


**To stop or reset Driver Verifier**

1.  Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2.  Select **Delete existing settings**.
3.  Reboot the computer.

Or type the following command in a Command Prompt window and reboot the computer.

```
verifier  /reset
```

**To view Driver Verifier settings**

1.  Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2.  Select **Display existing settings**.

Or type the following command in a Command Prompt window.

```
verifier  /querysettings
```

**To view Driver Verifier statistics**

1.  Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2.  Select **Display information about the currently verified drivers**.

Or type the following command in a Command Prompt window.

```
verifier  /query
```



## How to debug Driver Verifier violations


To get the most benefit from Driver Verifier, you should use a kernel debugger and connect to the test computer. See [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) for more information.

If Driver Verifier detects a violation, it generates a bug check to stop the computer. This is to provide you with the most information possible for debugging the issue. When you have a kernel debugger connected to a test computer running Driver Verifier, if Driver Verifier detects a violation, Windows breaks into the debugger and displays a brief description of the error.

All Driver Verifier violations result in bug checks, the most common ones (although not necessarily all of them) are:

-   [**Bug Check 0xC1: SPECIAL\_POOL\_DETECTED\_MEMORY\_CORRUPTION**](https://msdn.microsoft.com/library/windows/hardware/ff560183)
-   [**Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560187)
-   [**Bug Check 0xC6: DRIVER\_CAUGHT\_MODIFYING\_FREED\_POOL**](https://msdn.microsoft.com/library/windows/hardware/ff560193)
-   [**Bug Check 0xC9: DRIVER\_VERIFIER\_IOMANAGER\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560205)
-   [**Bug Check 0xD6: DRIVER\_PAGE\_FAULT\_BEYOND\_END\_OF\_ALLOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff560267)
-   [**Bug Check 0xE6: DRIVER\_VERIFIER\_DMA\_VIOLATION**](https://msdn.microsoft.com/library/windows/hardware/ff560341)

For more information see [Handling a Bug Check When Driver Verifier is Enabled](https://msdn.microsoft.com/library/windows/hardware/hh450984). For tips about debugging Bug Check 0xC4, see [Debugging Bug Check 0xC4: DRIVER\_VERIFIER\_DETECTED\_VIOLATION](debugging-bug-check-0xc4--driver-verifier-detected-violation.md).

When you start a new debug session, use the debugger extension command [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112). In kernel mode, the **!analyze** command displays information about the most recent bug check. The **!analyze -v** command displays additional information and attempts to pinpoint the faulting driver.

```
kd> !analyze -v
```

In addition [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112), you can use the following debugger extensions to view information specific to Driver Verifier:

-   [**!verifier**](https://msdn.microsoft.com/library/windows/hardware/ff565591) dumps captured Driver Verifier statistics. Use **!verifier -?** to display all of the available options.

    ```
    kd> !verifier
    ```

-   [**!deadlock**](https://msdn.microsoft.com/library/windows/hardware/ff562326) displays information related to locks or objects tracked by Driver Verifier's deadlock detection feature. Use **!deadlock -?** to display all of the available options.

    ```
    kd> !deadlock
    ```

-   [**!iovirp**](https://msdn.microsoft.com/library/windows/hardware/ff563252) \[*address*\] displays information related to an IRP tracked by I/O Verifier. For example:

    ```
    kd> !iovirp 947cef68
    ```

-   [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) \[*RuleID*\] displays information related to the [DDI compliance checking](ddi-compliance-checking.md) rule that was violated (*RuleID* is always the first argument to the bug check. All DDI Compliance Checking *RuleID* are in the form 0x200nn). For example:

    ```
    kd> !ruleinfo 0x20005
    ```



## Related topics


[Driver Verifier: What's New](driver-verifier--what-s-new.md)

[Driver Verifier Options](driver-verifier-options.md)

[**Driver Verifier Command Syntax**](verifier-command-line.md)

[Using Driver Verifier](using-driver-verifier.md)

[Controlling Driver Verifier](controlling-driver-verifier.md)










