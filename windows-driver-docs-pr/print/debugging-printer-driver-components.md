---
title: Debugging Printer Driver Components
description: Debugging Printer Driver Components
ms.assetid: 550cc8fe-5520-4521-8c4e-9c8c80521357
keywords:
- debugging drivers WDK printer
- printer drivers WDK , debugging
- user-mode debugging WDK printer
- macros WDK printer
- global variables WDK debugging
ms.date: 05/17/2017
ms.localizationpriority: medium
---

# Debugging Printer Driver Components





If you are developing a printer driver rendering plug-in or user interface plug-in, you can enable debug messages in these components. As explained in the Global Debug Variable section, you can use a global debug variable to control the level of detail in messages appearing in the debugger window.

You can use the macros discussed in the Debug Message Macros section to send messages to the debugger window under a variety of conditions. In addition, you can use the information in this section to enable debug messages in the Microsoft Universal Printer Driver (Unidrv) or PostScript Printer Driver (Pscript) renderers, provided that you have checked builds of these DLLs.

Steps for debugging a user-mode driver and some general debugging tips are included in the next two sections.

### Preparing for User-Mode Debugging

To start debugging printer drivers and their components:

1.  Install the latest debugging tools. See [Download Debugging Tools for Windows](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugger-download-tools)

2.  Install the correct symbols from [Windows Symbol Packages](https://docs.microsoft.com/windows-hardware/drivers/debugger/debugger-download-symbols)

**Note**   It is very important that you use the latest version of the debugger.



It is advisable to install the checked build of only the components that you are interested in debugging. Typically you would replace the following retail binaries with their corresponding checked builds:

-   Unidrv.dll

-   Unidrvui.dll

-   Unires.dll

You should also install the checked build of the Oemuni sample or the printer driver that you are debugging. The advantage of using this approach, as opposed to installing an entire checked build system, is that you won't slow down the entire system.

### Starting a User-Mode Debugging Session

To begin user-mode debugging, on the **File** menu in Windbg debugger select **Attach to a Process**. The process that you attach the debugger to depends on the scenario that you are attempting to debug. For printer drivers, you must attach the debugger to either the printing application or to the spooler process (Spoolsv.exe). Keep in mind that the printing application loads the configuration/user interface module, while the spooler process loads the rendering module. However, there are differences for "FILE:" printing, where spooling does not take place and as a result, the rendering module is also loaded by the printing application. You must therefore ensure that you attach to the correct process.

**Note**   You do not require two separate machines for user-mode debugging.



The following procedure will get you ready to debug the Oemuni sample.

1.  Install the Oemuni sample on the "FILE:" port.

2.  Launch the WordPad application by clicking the **Start** menu, selecting **All Programs**, selecting **Accessories**, and then selecting **WordPad**.

3.  On the WinDbg **File** menu, select **Attach to a Process**. In the list of available processes, select **WordPad.exe**.

4.  Start a print job from WordPad. You are now ready to debug the Oemuni sample.

You can enable verbose debugging by turning on the giDebugLevel variable. Its default value is 3, which denotes WARNING. If set to 1, it denotes VERBOSE. To set the latter value with Unidrv.dll, type the following command in the debugger:

```cpp
> ed unidrv!giDebugLevel 1
```

When you are running the Oemuni sample, the same debugging variable also applies, so to enable verbose debugging, type the following command:

```cpp
> ed oemuni!giDebugLevel 1
```

You can also add your own debug statements to the Oemuni sample.

For more information about setting debugging values, see the WinDbg documentation, which describes the available commands and outlines steps required to set up user-mode debugging. To access the documentation, on the WinDbg **Help** menu, select **Contents**.

### Global Debug Variable

The giDebugLevel global variable is declared by the Oemui and Oemuni samples in their Debug.h and Debug.cpp files. The value of giDebugLevel can be modified by:

-   Changing its value in the debugger.

-   Redefining its value in the plug-in.

You can set giDebugLevel to any of the following values:

```cpp
#define DBG_VERBOSE 1
#define DBG_TERSE   2
#define DBG_WARNING 3
#define DBG_ERROR   4
#define DBG_RIP     5
```

### Debug Message Macros

The following macros are used for debugging purposes. Several of them take action only if the giDebugLevel global variable, which controls which debug messages are emitted, is set to a specific value. The macros expand to white spaces on a free build. Here are brief descriptions of what they do and their parameters.

<a href="" id="assert-cond-"></a>**ASSERT**(*cond*)
Verifies whether the Boolean expression in *cond* is **TRUE**. If it is not, the macro forces a breakpoint.

<a href="" id="assertmsg-cond---msg--"></a>**ASSERTMSG**(*cond,* (*msg*))
Verifies whether the Boolean expression in *cond* is **TRUE**. If it is not, the macro displays the message in *msg,* and forces a breakpoint.

<a href="" id="err--msg--"></a>**ERR**((*msg*))
Displays the message in *msg* if the current debug level is &lt;= DBG\_ERROR. The message format is:

```cpp
ERR filename (linenumber): msg
```

<a href="" id="rip--msg--"></a>**RIP**((*msg*))
Displays the message in *msg* and forces a breakpoint.

<a href="" id="terse--msg--"></a>**TERSE**((*msg*))
Displays the message in *msg* if the current debug level is &lt;= DBG\_TERSE.

<a href="" id="verbose--msg--"></a>**VERBOSE**((*msg*))
Displays the message in *msg* if the current debug level is &lt;= DBG\_VERBOSE.

<a href="" id="warning--msg--"></a>**WARNING**((*msg*))
Displays the message in *msg* if the current debug level is &lt;= DBG\_WARNING. The message format is:

```cpp
WRN filename (linenumber): msg
```

Note that all of the macros with a *msg* argument require an extra pair of parentheses surrounding this argument. Here are two examples that illustrate this requirement:

-   <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><pre><code>ASSERTMSG(x &gt; 0, (&quot;x is less than 0\n&quot;));</code></pre></td>
    </tr>
    </tbody>
    </table>

-   <span codelanguage=""></span>
    <table>
    <colgroup>
    <col width="100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><pre><code>WARNING( (&quot;App passed NULL pointer, ignoring...\n&quot;) );</code></pre></td>
    </tr>
    </tbody>
    </table>

The macros that contain a *msg* argument are defined by the Oemui and Oemuni samples in their Debug.h headers.








