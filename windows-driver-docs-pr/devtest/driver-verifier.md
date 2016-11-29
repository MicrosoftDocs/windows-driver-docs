---
title: Driver Verifier
description: Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system.
ms.assetid: a8a78dde-930f-4d0b-be46-f7d07b0bf21b
keywords: ["verifying drivers WDK , Driver Verifier", "driver verification WDK , Driver Verifier", "Driver Verifier WDK", "Driver Verifier WDK , about Driver Verifier", "illegal function calls WDK Driver Verifier", "stress testing WDK Driver Verifier"]
---

# Driver Verifier


Driver Verifier monitors Windows kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system. Driver Verifier can subject the Windows drivers to a variety of stresses and tests to find improper behavior.

You can run Driver Verifier on multiple drivers simultaneously, or on one driver at a time. You can configure which tests to run, which allows you to put a driver through heavy stress loads or through more streamlined testing.

-   [Where can I download Driver Verifier?](#where-can-i-download-driver-verifier-)
-   [When to use Driver Verifier](#when-to-use-dv)
-   [How to start Driver Verifier](#how-to-start-dv)
-   [How to control Driver Verifier (stop, reset, and view settings and status)](#how-to-control-dv)
-   [How to debug Driver Verifier violations](#how-to-debug-dv)
-   [Related topics](#related-topics)

 

## <span id="Where_can_I_download_Driver_Verifier_"></span><span id="where_can_i_download_driver_verifier_"></span><span id="WHERE_CAN_I_DOWNLOAD_DRIVER_VERIFIER_"></span>Where can I download Driver Verifier?


<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>You don't need to. Driver Verifier (Verifier.exe) is included in every version of Windows, starting with Windows 2000 (in the %windir%\system32 directory). There isn't a separate Driver Verifier download package.</p>
<ul>
<li>Open a <strong>Command Prompt</strong> window (<strong>Run as administrator</strong>).</li>
<li>Type <strong>verifier</strong> to open the Driver Verifier Manager, or type <strong>verifier /?</strong> to view command line options. See [<strong>Driver Verifier Command Syntax</strong>](verifier-command-line.md) for more information.</li>
</ul>
<p></p>
<div class="alert">
<strong>Caution</strong>  
<ul>
<li>Running Driver Verifier could cause the computer to crash.</li>
<li>You should only run Driver Verifier on computers you are using for testing and debugging.</li>
<li>You must be in the Administrators group on the computer to use Driver Verifier.</li>
</ul>
</div>
<div>
 
</div>
<p>For information about changes in Driver Version for Windows 8.1 and previous versions of Windows, see [Driver Verifier: What's New](driver-verifier--what-s-new.md).</p></td>
</tr>
</tbody>
</table>

 

 

## <span id="when_to_use_dv"></span><span id="WHEN_TO_USE_DV"></span>When to use Driver Verifier


Run Driver Verifier throughout the driver development and test process.

-   Use Driver Verifier to find problems early in the development life cycle, when they are easier and less costly to correct.

-   Use Driver Verifier when you deploy a driver for testing using the WDK, Visual Studio, and the [Windows Hardware Certification Kit](http://go.microsoft.com/fwlink/p/?linkid=254893) (HCK) tests. See [Testing a Driver](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver).

-   Use Driver Verifier for troubleshooting and debugging test failures and computer crashes.

 

## <span id="how_to_start_dv"></span><span id="HOW_TO_START_DV"></span>How to start Driver Verifier


You should only run Driver Verifier on test computers, or computers you are testing and debugging. To get the most benefit from Driver Verifier, you should use a kernel debugger and connect to the test computer. See [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063).

1.  Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2.  Select **Create standard settings** (default) and click **Next**.

    You can also choose **Create custom settings** to select from predefined settings, or to select individual options. See [Driver Verifier Options](driver-verifier-options.md) and [Selecting Driver Verifier Options](selecting-driver-verifier-options.md) for more information.

3.  Select a driver or drivers to verify.

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
    <td align="left"><p>Useful option for testing on computers running versions of Windows that don't require signed drivers.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><strong>Automatically select drivers built for older versions of Windows</strong></td>
    <td align="left"><p>Useful option for testing driver compatibility with newer versions of Windows.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><strong>Automatically select all drivers installed on this computer</strong></td>
    <td align="left"><p>Provides maximum coverage in terms of the number of drivers that are tested on a system. This option is useful for test scenarios where a driver can interact with other devices or drivers on a system.</p>
    <p>This option can also exhaust the resources available for [Special Pool](special-pool.md) and some resource tracking. Testing all drivers can also adversely affect system performance.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><strong>Select driver names from a list</strong></td>
    <td align="left"><p>In most cases, you will want to specify which drivers to test.</p>
    <p>Selecting all drivers in a device stack allows the [Enhanced I/O Verification](enhanced-i-o-verification.md) option to track objects and check compliance as an IRP is passed between each of the drivers in the stack and allows for a greater level of detail to be provided should an error be found.</p>
    <p>Select a single driver if you are running a test scenario that measures system or driver performance metrics, or if you want to allocate the greatest number of resources available for detecting memory corruption or resource tracking issues (deadlocks, mutexs). The [Special Pool](special-pool.md) and [I/O Verification](i-o-verification.md) options will be more effective when used on one driver at a time.</p></td>
    </tr>
    </tbody>
    </table>

     

4.  Click **Finish** and reboot the computer.

**Note**  You can also run Driver Verifier in a Command Prompt window. For example, to run Driver Verifier with the standard settings on a driver called myDriver.sys, you would use the following command:

 

``` syntax
verifier  /standard /driver myDriver.sys
```

See [**Driver Verifier Command Syntax**](verifier-command-line.md) for more information.

 

## <span id="how_to_control_dv"></span><span id="HOW_TO_CONTROL_DV"></span>How to control Driver Verifier (stop, reset, and view settings and status)


**To stop or reset Driver Verifier**

1.  Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2.  Select **Delete existing settings**.
3.  Reboot the computer.

Or type the following command in a Command Prompt window and reboot the computer.

``` syntax
verifier  /reset
```

**To view Driver Verifier settings**

1.  Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2.  Select **Display existing settings**.

Or type the following command in a Command Prompt window.

``` syntax
verifier  /querysettings
```

**To view Driver Verifier statistics**

1.  Open a **Command Prompt** window (**Run as administrator**) and type **verifier** to open the Driver Verifier Manager.
2.  Select **Display information about the currently verified drivers**.

Or type the following command in a Command Prompt window.

``` syntax
verifier  /query
```

 

## <span id="how_to_debug_dv"></span><span id="HOW_TO_DEBUG_DV"></span>How to debug Driver Verifier violations


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

``` syntax
kd> !analyze -v
```

In addition [**!analyze**](https://msdn.microsoft.com/library/windows/hardware/ff562112), you can use the following debugger extensions to view information specific to Driver Verifier:

-   [**!verifier**](https://msdn.microsoft.com/library/windows/hardware/ff565591) dumps captured Driver Verifier statistics. Use **!verifier -?** to display all of the available options.

    ``` syntax
    kd> !verifier
    ```

-   [**!deadlock**](https://msdn.microsoft.com/library/windows/hardware/ff562326) displays information related to locks or objects tracked by Driver Verifier's deadlock detection feature. Use **!deadlock -?** to display all of the available options.

    ``` syntax
    kd> !deadlock
    ```

-   [**!iovirp**](https://msdn.microsoft.com/library/windows/hardware/ff563252) \[*address*\] displays information related to an IRP tracked by I/O Verifier. For example:

    ``` syntax
    kd> !iovirp 947cef68
    ```

-   [**!ruleinfo**](https://msdn.microsoft.com/library/windows/hardware/dn265374) \[*RuleID*\] displays information related to the [DDI compliance checking](ddi-compliance-checking.md) rule that was violated (*RuleID* is always the first argument to the bug check. All DDI Compliance Checking *RuleID* are in the form 0x200nn). For example:

    ``` syntax
    kd> !ruleinfo 0x20005
    ```

## <span id="ddk_driver_verifier_tools"></span><span id="DDK_DRIVER_VERIFIER_TOOLS"></span>


## <span id="related_topics"></span>Related topics


[Driver Verifier: What's New](driver-verifier--what-s-new.md)

[Driver Verifier Options](driver-verifier-options.md)

[**Driver Verifier Command Syntax**](verifier-command-line.md)

[Using Driver Verifier](using-driver-verifier.md)

[Controlling Driver Verifier](controlling-driver-verifier.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Driver%20Verifier%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





