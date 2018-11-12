---
title: Controlling Exceptions and Events
description: Controlling Exceptions and Events
ms.assetid: cc8067f3-07de-4ee2-b028-94f9ac088891
keywords: ["exceptions", "exceptions, overview", "exceptions, handling", "events", "events, overview", "events, handling"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Controlling Exceptions and Events


## <span id="ddk_controlling_exceptions_and_events_dbg"></span><span id="DDK_CONTROLLING_EXCEPTIONS_AND_EVENTS_DBG"></span>


You can catch and handle exceptions in user-mode and kernel-mode applications by a variety of methods. An active debugger, a postmortem debugger, or an internal error handling routine are all common ways to handle exceptions.

For more information about the precedence order of these various exception handlers, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

When the Microsoft Windows operating system allows a debugger to handle an exception, the application that generated the exception *breaks into* the debugger. That is, the application stops and the debugger becomes active. The debugger can then handle the exception in some way or analyze the situation. The debugger can then end the process or let it resume running.

If the debugger ignores the exception and lets the application continue running, the operating system looks for other exception handlers as if no debugger was present. If the exception is handled, the application continues running. However, if the exception remains unhandled, the debugger is then given a second opportunity to deal with the situation.

### <span id="using_the_debugger_to_analyze_an_exception"></span><span id="USING_THE_DEBUGGER_TO_ANALYZE_AN_EXCEPTION"></span>Using the Debugger to Analyze an Exception

When an exception or event breaks into the debugger, you can use the debugger to examine the code that is being executed and the memory that the application is using. By altering certain quantities or jumping to a different point in the application, you might be able to remove the cause of the exception.

You can resume execution by issuing a [**gh (Go with Exception Handled)**](gh--go-with-exception-handled-.md) or [**gn (Go with Exception Not Handled)**](gn--gn--go-with-exception-not-handled-.md) command.

If you issue the **gn** command in the debugger's second opportunity to handle the exception, the application ends.

### <span id="kernel_mode_exceptions"></span><span id="KERNEL_MODE_EXCEPTIONS"></span>Kernel-Mode Exceptions

Exceptions that occur in kernel-mode code are more serious than user-mode exceptions. If kernel-mode exceptions are not handled, a [bug check](bug-checks--blue-screens-.md) is issued and the system stops.

As with user-mode exceptions, if a kernel-mode debugger is attached to the system, the debugger is notified before the *bug check screen* (also known as a *blue screen*) appears. If no debugger is attached, the bug check screen appears. In this case, the operating system might create a [crash dump file](crash-dump-files.md).

### <span id="controlling_exceptions_and_events_from_the_debugger"></span><span id="CONTROLLING_EXCEPTIONS_AND_EVENTS_FROM_THE_DEBUGGER"></span>Controlling Exceptions and Events from the Debugger

You can configure the debugger to react to specified exceptions and events in a specific way.

The debugger can set the break status for each exception or event:

-   The event can cause a break into the debugger as soon as it occurs (the "first chance").

-   The event can break in after other error handlers have been given an opportunity to respond (the "second chance").

-   The event can also send the debugger a message but continue executing.

-   The debugger can ignore the event.

The debugger can also set the handling status for each exception and event. The debugger can treat the event like a handled exception or an unhandled exception. (Of course, events that are not actually errors do not require any handling.)

You can control the break status and handling status by doing one of the following:

-   Use the [**SXE**](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md), **SXD**, **SXN**, or **SXI** command in the [Debugger Command window](debugger-command-window.md).

-   (CDB and NTSD) Use the **-x**, **-xe**, **-xd**, **-xn**, or **-xi** option on the [**command line**](cdb-command-line-options.md).

-   (CDB, NTSD, and KD) Use the **sxe** or **sxd** keyword in the [Tools.ini](configuring-tools-ini.md) file.

-   (WinDbg only) Click [Event Filters](debug---event-filters.md) on the **Debug** menu to open the **Event Filters** dialog box, and then choose the options that you want.

The **SX\\*** command, the **-x\\*** command-line option, and the **sx\\*** Tools.ini keyword typically set the break status of the specified event. You can add the **-h** option to cause the handling status to be set instead.

There are four special event codes (**cc**, **hc**, **bpec**, and **ssec**) that always specify handling status instead of break status.

You can display the most recent exception or event by using the [**.lastevent (Display Last Event)**](-lastevent--display-last-event-.md) command.

### <span id="controlling_break_status"></span><span id="CONTROLLING_BREAK_STATUS"></span>Controlling Break Status

When you set the break status of an exception or event, you can use the following options.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Status name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p></p>
<strong>SXE</strong>
or
<strong>-xe</strong></td>
<td align="left"><p><strong>Break</strong></p>
<p>(<strong>Enabled</strong>)</p></td>
<td align="left"><p>When this exception occurs, the target immediately breaks into the debugger. This break in occurs before any other error handlers are activated. This method is called <em>first-chance handling</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<strong>SXD</strong>
or
<strong>-xd</strong></td>
<td align="left"><p><strong>Second chance break</strong></p>
<p>(<strong>Disabled</strong>)</p></td>
<td align="left"><p>The debugger does not break in for this kind of first-chance exception (although a message is displayed). If other error handlers cannot address this exception, execution stops and the target breaks into the debugger. This method is called <em>second-chance handling</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p></p>
<strong>SXN</strong>
or
<strong>-xn</strong></td>
<td align="left"><p><strong>Output</strong></p>
<p>(<strong>Notify</strong>)</p></td>
<td align="left"><p>When this exception occurs, the target application does not break into the debugger at all. However, a message is displayed that informs the user of this exception.</p></td>
</tr>
<tr class="even">
<td align="left"><p></p>
<strong>SXI</strong>
or
<strong>-xi</strong></td>
<td align="left"><p><strong>Ignore</strong></p></td>
<td align="left"><p>When this exception occurs, the target application does not break into the debugger, and no message is displayed.</p></td>
</tr>
</tbody>
</table>

 

If an exception is not anticipated by an **SX**\* setting, the target application breaks into the debugger on the second chance. The default status for events is listed in the following "Event Definitions and Defaults" section of this topic.

To set break status by using the WinDbg graphical interface, [Event Filters](debug---event-filters.md) on the **Debug** menu, click the event that you want from the list in the **Event Filters** dialog box, and then select **Enabled**, **Disabled**, **Output**, or **Ignore**.

### <span id="controlling_handling_status"></span><span id="CONTROLLING_HANDLING_STATUS"></span>Controlling Handling Status

All events are considered unhandled, unless you use the [**gh (Go with Exception Handled)**](gh--go-with-exception-handled-.md) command.

All exceptions are considered unhandled, unless you use the [**sx\\***](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md) command together with the **-h** option.

Additionally, **SX**\* options can configure the handling status for invalid handles, STATUS\_BREAKPOINT break instructions, and single-step exceptions. (This configuration is separate from their break configuration.) When you configure their break status, these events are named **ch**, **bpe**, and **sse**, respectively. When you configure their handling status, these events are named **hc**, **bpec**, and **ssec**, respectively. (For the full listing of events, see the following "Event Definitions and Defaults" section.)

You can configure the handling status for the CTRL+C event (**cc**), but not its break status. If an application receives a CTRL+C event, the application always breaks into the debugger.

When you use the **SX**\* command on **cc**, **hc**, **bpec**, and **ssec** events, or when you use the **SX**\* command together with the **-h** option on an exception, the following actions occur.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Command</th>
<th align="left">Status name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>SXE</strong></p></td>
<td align="left"><p><strong>Handled</strong></p></td>
<td align="left"><p>The event is considered handled when execution resumes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SXD,SXN,SXI</strong></p></td>
<td align="left"><p><strong>Not Handled</strong></p></td>
<td align="left"><p>The event is considered not handled when execution resumes.</p></td>
</tr>
</tbody>
</table>

 

To set handling status by using the WinDbg graphical interface, click [Event Filters](debug---event-filters.md) on the **Debug** menu, click the event that you want from the list in the **Event Filters** dialog box, and then select **Handled** or **Not Handled**.

### <span id="automatic_commands"></span><span id="AUTOMATIC_COMMANDS"></span>Automatic Commands

The debugger also enables you to set commands that are automatically executed if the event or exception causes a break into the debugger. You can set a command string for the first-chance break and a command string for the second-chance break. You can set these strings with the [**SX\\***](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md) command or the [Debug | Event Filters](debug---event-filters.md) command. Each command string can contain multiple commands that are separated with semicolons.

These commands are executed regardless of the break status. That is, if the break status is "Ignore," the command is still executed. If the break status is "Second-chance break," the first-chance command is executed when the exception first occurs, before any other exception handlers are involved. The command string can end with an execution command such as [**g (Go)**](g--go-.md), [**gh (Go with Exception Handled)**](gh--go-with-exception-handled-.md), or [**gn (Go with Exception Not Handled)**](gn--gn--go-with-exception-not-handled-.md).

### <span id="event_definitions_and_defaults"></span><span id="EVENT_DEFINITIONS_AND_DEFAULTS"></span>Event Definitions and Defaults

You can change the break status or handling status of the following exceptions. Their default break status is indicated.

The following exceptions' default handling status is always "Not Handled". Be careful about changing this status. If you change this status to "Handled", all first-chance and second-chance exceptions of this type are considered handled, and this configuration bypasses all of the exception-handling routines.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event code</th>
<th align="left">Meaning</th>
<th align="left">Default break status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>asrt</strong></p></td>
<td align="left"><p>Assertion failure</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>av</strong></p></td>
<td align="left"><p>Access violation</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>dm</strong></p></td>
<td align="left"><p>Data misaligned</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>dz</strong></p></td>
<td align="left"><p>Integer division by zero</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>c000008e</strong></p></td>
<td align="left"><p>Floating point division by zero</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>eh</strong></p></td>
<td align="left"><p>C++ EH exception</p></td>
<td align="left"><p>Second-chance break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>gp</strong></p></td>
<td align="left"><p>Guard page violation</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ii</strong></p></td>
<td align="left"><p>Illegal instruction</p></td>
<td align="left"><p>Second-chance break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>iov</strong></p></td>
<td align="left"><p>Integer overflow</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ip</strong></p></td>
<td align="left"><p>In-page I/O error</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>isc</strong></p></td>
<td align="left"><p>Invalid system call</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>lsq</strong></p></td>
<td align="left"><p>Invalid lock sequence</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>sbo</strong></p></td>
<td align="left"><p>Stack buffer overflow</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>sov</strong></p></td>
<td align="left"><p>Stack overflow</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>wkd</strong></p></td>
<td align="left"><p>Wake debugger</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>aph</strong></p></td>
<td align="left"><p>Application hang</p>
<p>This exception is triggered if the Windows operating system concludes that a process has stopped responding (that is, <em>is hung</em>).</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>3c</strong></p></td>
<td align="left"><p>Child application termination</p></td>
<td align="left"><p>Second-chance break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>chhc</strong></p></td>
<td align="left"><p>Invalid handle</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>Number</em></p></td>
<td align="left"><p>Any numbered exception</p></td>
<td align="left"><p>Second-chance break</p></td>
</tr>
</tbody>
</table>

 

**Note**   You can override the **asrt** break status for a specific address by using the [**ah (Assertion Handling)**](ah--assertion-handling-.md) command. The **ch** and **hc** event codes refer to the same exception. When you are controlling its break status, use **sx\* ch**. When you are controlling its handling status, use **sx\* hc**.

 

You can change the break status or handling status of the following exceptions. Their default break status is indicated.

The following exceptions' default handling status is always "Handled". Because these exceptions are used to communicate with the debugger, you should not typically change their status to "Not Handled". This status causes other exception handlers to catch the exceptions if the debugger ignores them.

An application can use DBG\_COMMAND\_EXCEPTION (**dbce**) to communicate with the debugger. This exception is similar to a breakpoint, but you can use the **SX**\* command to react in a specific way when this exception occurs.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event code</th>
<th align="left">Meaning</th>
<th align="left">Default break status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>dbce</strong></p></td>
<td align="left"><p>Special debugger command exception</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>vcpp</strong></p></td>
<td align="left"><p>Special Visual C++ exception</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>wos</strong></p></td>
<td align="left"><p>WOW64 single-step exception</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>wob</strong></p></td>
<td align="left"><p>WOW64 breakpoint exception-</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ssessec</strong></p></td>
<td align="left"><p>Single-step exception</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bpebpec</strong></p></td>
<td align="left"><p>Breakpoint exception</p></td>
<td align="left"><p>Break</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ccecc</strong></p></td>
<td align="left"><p>CTRL+C or CTRL+BREAK</p>
<p>This exception is triggered if the target is a console application and CTRL+C or CTRL+BREAK is passed to it.</p></td>
<td align="left"><p>Break</p></td>
</tr>
</tbody>
</table>

 

**Note**   The final three exceptions in the preceding table have two different event codes. When you are controlling their break status, use **sse**, **bpe**, and **cce**. When you are controlling their handling status, use **ssec**, **bpec**, and **cc**.

 

### <span id="The_following_exceptions_are_useful_when_you_are_debugging_managed_code."></span><span id="the_following_exceptions_are_useful_when_you_are_debugging_managed_code."></span><span id="THE_FOLLOWING_EXCEPTIONS_ARE_USEFUL_WHEN_YOU_ARE_DEBUGGING_MANAGED_CODE."></span>The following exceptions are useful when you are debugging managed code.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event code</th>
<th align="left">Meaning</th>
<th align="left">Default status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>clr</strong></p></td>
<td align="left"><p>Common Language Runtime exception</p></td>
<td align="left"><p>Second-chance break</p>
<p>Not handled</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>clrn</strong></p></td>
<td align="left"><p>Common Language Runtime notification exception</p></td>
<td align="left"><p>Second-chance break</p>
<p>Handled</p></td>
</tr>
</tbody>
</table>

 

You can change the break status of the following events. Because these events are not exceptions, their handling status is irrelevant.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Event code</th>
<th align="left">Meaning</th>
<th align="left">Default break status</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>ser</strong></p></td>
<td align="left"><p>System error</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>cpr</strong>[<strong>:</strong><em>Process</em>]</p></td>
<td align="left"><p>Process creation</p>
<p>Setting the break status of this event applies only to user-mode debugging. This event does not occur in kernel mode.</p>
<p>You can control this event only if you have activated debugging of child processes in CDB or WinDbg, either through the -o<strong><a href="cdb-command-line-options.md" data-raw-source="[command-line option](cdb-command-line-options.md)">command-line option</a></strong> or through the <strong><a href="-childdbg--debug-child-processes-.md" data-raw-source="[.childdbg (Debug Child Processes)](-childdbg--debug-child-processes-.md)">.childdbg (Debug Child Processes)</a></strong> command.</p>
<p>The process name can include an optional file name extension and an asterisk (<em>) or question mark (?) as wildcard characters. The debugger remembers only the most recent <strong>cpr</strong> setting. Separate settings for separate processes are not supported. Include a colon or a space between <strong>cpr</strong> and <em>Process</em>.</p>
<p>If <em>Process</em> is omitted, the setting applies to any child process creation.</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>epr</strong>[<strong>:</strong><em>Process</em>]</p></td>
<td align="left"><p>Process exit</p>
<p>Setting the break status of this event applies only to user-mode debugging. This event does not occur in kernel mode.</p>
<p>You can control this event only if you have activated debugging of child processes in CDB or WinDbg, either through the -o<strong><a href="cdb-command-line-options.md" data-raw-source="[command-line option](cdb-command-line-options.md)">command-line option</a></strong> or through the <strong><a href="-childdbg--debug-child-processes-.md" data-raw-source="[.childdbg (Debug Child Processes)](-childdbg--debug-child-processes-.md)">.childdbg (Debug Child Processes)</a></strong> command.</p>
<p>The process name can include an optional file name extension and an asterisk (</em>) or question mark (?) as wildcard characters. The debugger remembers only the most recent <strong>epr</strong> setting. Separate settings for separate processes are not supported. Include a colon or a space between <strong>epr</strong> and <em>Process</em>.</p>
<p>If <em>Process</em> is omitted, the setting applies to any child process exit.</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ct</strong></p></td>
<td align="left"><p>Thread creation</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>et</strong></p></td>
<td align="left"><p>Thread exit</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>ld</strong>[<strong>:</strong><em>Module</em>]</p></td>
<td align="left"><p>Load module</p>
<p>If you specify <em>Module</em>, the break occurs when the module with this name is loaded. <em>Module</em> can specify the name or the address of the module. If the name is used, <em>Module</em> might contain a variety of wildcard characters and specifiers. (For more information about the syntax, see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a>.)</p>
<p>The debugger remembers only the most recent l<strong>d</strong> setting. Separate settings for separate modules are not supported. Include a colon or a space between <strong>ld</strong> and <em>Module</em>.</p>
<p>If <em>Module</em> is omitted, the event is triggered when any module is loaded.</p></td>
<td align="left"><p>Output</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ud</strong>[<strong>:</strong><em>Module</em>]</p></td>
<td align="left"><p>Unload module</p>
<p>If you specify <em>Module</em>, the break occurs when the module with this name, or at this base address, is unloaded. <em>Module</em> can specify the name or the address of the module. If the name is used, <em>Module</em> can be an exact name or include wildcard characters. If <em>Module</em> is an exact name, it is immediately resolved to a base address by using the current debugger module list and it is stored as an address. If <em>Module</em> contains wildcard characters, the pattern string is kept for later matching when unload events occur.</p>
<p>Rarely, the debugger does not have name information for unload events and matches only by the base address. Therefore, if <em>Module</em> contains wildcard characters, the debugger cannot perform a name match in this particular unload case and breaks when any module is unloaded.</p>
<p>The debugger remembers only the most recent <strong>ud</strong> setting. Separate settings for separate modules are not supported. Include a colon or a space between <strong>ud</strong> and <em>Module</em>.</p>
<p>If <em>Module</em> is omitted, the event is triggered when any module is loaded.</p></td>
<td align="left"><p>Output</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>out</strong>[<strong>:</strong><em>Output</em>]</p></td>
<td align="left"><p>Target application output</p>
<p>If you specify <em>Output</em>, the break occurs only when output that matches the specified pattern is received. <em>Output</em> can contain a variety of wildcard characters and specifiers. (For more information about the syntax, see <a href="string-wildcard-syntax.md" data-raw-source="[String Wildcard Syntax](string-wildcard-syntax.md)">String Wildcard Syntax</a>.) However, <em>Output</em> cannot contain a colon or spaces. The match is not case sensitive. Include a colon or space between <strong>out</strong> and <em>Output</em>.</p></td>
<td align="left"><p>Ignore</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>ibp</strong></p></td>
<td align="left"><p>Initial break point</p>
<p>(This event occurs at the beginning of the debug session and after you restart the target computer.)</p></td>
<td align="left"><p><strong>In user mode:</strong> Break. You can change this status to &quot;Ignore&quot; by using the <strong>-g</strong><a href="command-line-options.md" data-raw-source="[command-line option](command-line-options.md)">command-line option</a>.</p>
<p><strong>In kernel mode:</strong> Ignore. You can change this status to &quot;Enabled&quot; by a variety of methods. For more information about how to change this status, see <a href="crashing-and-rebooting-the-target-computer.md" data-raw-source="[Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md)">Crashing and Rebooting the Target Computer</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>iml</strong></p></td>
<td align="left"><p>Initial module load</p>
<p>(Kernel mode only)</p></td>
<td align="left"><p>Ignore. You can change this status to &quot;Break&quot; by a variety of methods. For more information about how to change this status, see <a href="crashing-and-rebooting-the-target-computer.md" data-raw-source="[Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md)">Crashing and Rebooting the Target Computer</a>.</p></td>
</tr>
</tbody>
</table>

 

 

 





