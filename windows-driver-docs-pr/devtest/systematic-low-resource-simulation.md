---
title: Systematic low resources simulation
description: The Systematic low resources simulation option injects resource failures in kernel mode drivers.
ms.assetid: A8351715-8407-4FEF-9050-2F1F2E7FC2FD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Systematic low resources simulation


The Systematic low resources simulation option injects resource failures in kernel mode drivers. This option penetrates driver error handling paths. Testing these paths has historically been very difficult. The Systematic low resources simulation option injects resource failures in a predictable manner, which makes the issues it finds reproducible. Because the error paths are easy to reproduce, it also makes it easy to verify fixes to these issues.

To help you determine the root cause of the error, a debugger extension is provided that can tell you exactly which failures have been injected and in what order.

**Caution**  This option is not intended for use when you are verifying all (or a large collection of) drivers on a computer. This option should be used only when you are doing targeted testing of individual drivers or their attached filter drivers. Using this option on a large number of drivers at the same time could cause unpredictable results, and could force crashes in components unrelated to the driver(s) you are testing.

 

**Note**  For Windows 8.1, the [Stack Based Failure Injection](stack-based-failure-injection.md) feature, which was available in the WDK 8, has been integrated into Driver Verifier. On computers running Windows 8.1, use the Systematic low resources simulation option.

 

When the Systematic low resources simulation option is enabled on a specific driver, it intercepts some calls from that driver to the kernel and Ndis.sys. Systematic low resources simulation looks at the call stack—specifically, at the portion of the call stack that comes from the driver it is enabled on. If this is the first time it has ever seen that stack, it will fail the call according to the semantics of that call. Otherwise, if it has seen that call before, it will pass it through untouched. Systematic low resources simulation contains logic to deal with the fact that a driver can be loaded and unloaded multiple times. It will recognize that a call stack is the same even if the driver is reloaded into a different memory location.

## <span id="Activating_this_option"></span><span id="activating_this_option"></span><span id="ACTIVATING_THIS_OPTION"></span>Activating this option


You can activate the Systematic low resources simulation feature for one or more drivers by using Driver Verifier Manager or the Verifier.exe command line. For details, see [Selecting Driver Verifier Options](selecting-driver-verifier-options.md). You must restart the computer to activate or deactivate the Systematic low resources simulation option.

-   **At the command line**

    At the command line, Systematic low resources simulation is represented by **verifier /flags 0x040000** (Bit 18). To Systematic low resources simulation, use a flag value of 0x040000 or add 0x040000 to the flag value. For example:

    ```
    verifier /flags 0x040000 /driver MyDriver.sys
    ```

    The feature will be active after the next boot.

    When you enable the Systematic low resources simulation option, you can use the **/faultssystematic** *OPTION* command line option to further control the Systematic low resources simulation.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">OPTION</th>
    <th align="left">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>enableboottime</p></td>
    <td align="left"><p>Enables fault injections across computer reboots.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>disableboottime</p></td>
    <td align="left"><p>Disables fault injections across computer reboots (this is the default setting).</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>recordboottime</p></td>
    <td align="left"><p>Enables fault injections in <em>what if</em> mode across computer reboots.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>resetboottime</p></td>
    <td align="left"><p>Disables fault injections across computer reboots and clears the stack exclusion list.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>enableruntime</p></td>
    <td align="left"><p>Dynamically enables fault injections.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>disableruntime</p></td>
    <td align="left"><p>Dynamically disables fault injections.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>recordruntime</p></td>
    <td align="left"><p>Dynamically enables fault injections in <em>what if</em> mode.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>resetruntime</p></td>
    <td align="left"><p>Dynamically disables fault injections and clears the previously faulted stack list.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>querystatistics</p></td>
    <td align="left"><p>Shows the current fault injection statistics.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>incrementcounter</p></td>
    <td align="left"><p>Increments the test pass counter used to identify when a fault was injected.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>getstackid <em>COUNTER</em></p></td>
    <td align="left"><p>Retrieves the indicated injected stack identifier.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>excludestack <em>STACKID</em></p></td>
    <td align="left"><p>Excludes the stack from fault injection.</p></td>
    </tr>
    </tbody>
    </table>

     

-   **Using Driver Verifier Manager**

    1.  Start Driver Verifier Manager. Type **Verifier** in a Command Prompt window.
    2.  Select **Create custom settings (for code developers)** and then click **Next**.
    3.  Select **Select individual settings from a full list**.
    4.  Select (check) **Systematic low resources simulation**.
    5.  Restart the computer.

## <span id="Debugging_bug_checks_caused_by_Systematic_low_resources_simulation"></span><span id="debugging_bug_checks_caused_by_systematic_low_resources_simulation"></span><span id="DEBUGGING_BUG_CHECKS_CAUSED_BY_SYSTEMATIC_LOW_RESOURCES_SIMULATION"></span>Debugging bug checks caused by Systematic low resources simulation


Most of the issues found with Systematic low resources simulation result in bug checks. To help determine the cause of these code bugs, the [Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063) tools for Windows 8.1 provides the debugger extension (kdexts.dll) and the necessary symbols.

**To run the debugger extension**

-   From the debugger command prompt, type the following command:

    ```
    !verifier 0x800
    ```

This will dump information to your debugger showing the call stacks from the most recent failures injected.

 

 





