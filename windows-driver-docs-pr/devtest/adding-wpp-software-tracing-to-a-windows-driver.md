---
title: Adding WPP Software Tracing to a Windows Driver
description: To use WPP software tracing in a trace provider, such as a kernel-mode driver or a user-mode application, you need to add code (or instrument) the driver source files and modify the driver project. This section will describe those steps.
ms.assetid: 487BA8AA-950A-4F3C-9E3E-EBE1DA35D4B1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding WPP Software Tracing to a Windows Driver

To use WPP software tracing in a trace provider, such as a kernel-mode driver or a user-mode application, you need to add code (or *instrument*) the driver source files and modify the driver project. This section will describe those steps.

**Tip**  The easiest way to add WPP tracing to your driver is to use one of the KMDF or UMDF driver templates in Visual Studio. If you use the templates, much of the code you need to add is already done for you. In Visual Studio, click **File &gt; New &gt; Project**, and then select the Windows Driver (user-mode or kernel mode) WDF project. The WPP macros are defined in the Trace.h header file that is included as part of the project. If you use one of the templates, you can skip ahead to [Step 5](#step-5-instrument-the-driver-code-to-generate-trace-messages-at-appropriate-points). 

-   [Step 1: Define the control GUID and trace flags](#step-1-define-the-control-guid-and-trace-flags)
-   [Step 2: Choose which trace message functions you intend to use and define the WPP macros for those functions](#step-2-choose-which-trace-message-functions-you-intend-to-use-and-define-the-wpp-macros-for-those-functions)
-   [Step 3: Include the associated trace header files (.h and .tmh) in your C or C++ source files](#step-3-include-the-associated-trace-header-files-h-and-tmh-in-your-c-or-c-source-files)
-   [Step 4: Add macros to the appropriate callback functions to initialize and clean up WPP](#step-4-add-macros-to-the-appropriate-callback-functions-to-initialize-and-clean-up-wpp)
-   [Step 5: Instrument the driver code to generate trace messages at appropriate points](#step-5-instrument-the-driver-code-to-generate-trace-messages-at-appropriate-points)
-   [Step 6: Modify the Visual Studio project to run the WPP preprocessor and build the solution](#step-6-modify-the-visual-studio-project-to-run-the-wpp-preprocessor-and-build-the-solution)
-   [Step 7: Start a trace session to capture and verify your trace messages](#step-7-start-a-trace-session-to-capture-and-verify-your-trace-messages)

## Step 1: Define the control GUID and trace flags

Every trace provider (such as a driver, or user-mode app) must be uniquely defined. You do this by adding the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro that defines a control GUID, an identifier, and trace flags. This is done so that you can identify and control when and what you want to trace. While each driver typically has a separate control GUID, a driver could have multiple control GUIDs, or multiple drivers could share one control GUID.

For convenience, the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro is typically defined in a common header file. The header file must be included (\#include) in any source file that you intend to instrument for tracing.

**To add WPP\_CONTROL\_GUIDS macro to your driver:**

1.  Add a new C++ header file to your Visual Studio project that you can use for defining the WPP trace macros. For example, right-click the driver in Solution Explorer, and click **Add &gt; New Item**. Save the file (as Trace.h, for example).

2.  Add a [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro to specify friendly name for the trace provider, define a control GUID, and to define the trace flags that you can use to qualify specific trace messages.

    The [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro has the following syntax:

    **Syntax for WPP\_CONTROL\_GUIDS**

    ```ManagedCPlusPlus
    #define WPP_CONTROL_GUIDS \
        WPP_DEFINE_CONTROL_GUID(GUIDFriendlyName, (ControlGUID),  \
            WPP_DEFINE_BIT(NameOfTraceFlag1)  \
            WPP_DEFINE_BIT(NameOfTraceFlag2)  \
            .............................   \
            .............................   \
            WPP_DEFINE_BIT(NameOfTraceFlag31) 
    ```

    For example, the following code uses myDriverTraceGuid as the *GUIDFriendlyName*. Note that *ControlGUID* has a slightly different format than the standard form of a 32-digit hexadecimal GUID. The *ControlGUID* has the five fields, but they are separated by commas and bracketed by parentheses, instead of the usual hyphens and curly braces. For example, you specify (**(84bdb2e9,829e,41b3,b891,02f454bc2bd7)** instead of {84bdb2e9-829e-41b3-b891-02f454bc2bd7}.

    **Example of a WPP\_CONTROL\_GUIDS statement**

    ```ManagedCPlusPlus
    #define WPP_CONTROL_GUIDS                                              \
        WPP_DEFINE_CONTROL_GUID(                                           \
            myDriverTraceGuid, (84bdb2e9,829e,41b3,b891,02f454bc2bd7), \
            WPP_DEFINE_BIT(MYDRIVER_ALL_INFO)        /* bit  0 = 0x00000001 */ \
            WPP_DEFINE_BIT(TRACE_DRIVER)             /* bit  1 = 0x00000002 */ \
            WPP_DEFINE_BIT(TRACE_DEVICE)             /* bit  2 = 0x00000004 */ \
            WPP_DEFINE_BIT(TRACE_QUEUE)              /* bit  3 = 0x00000008 */ \
            )                             
    ```

    **Tip**  You can copy this code snippet into a header file. Be sure to change the control GUID and the friendly name. You can use GUIDgen.exe to generate the control GUID. The Guidgen.exe is included with Visual Studio (**Tools &gt; Create GUID**). You could also use the Uuidgen.exe tool, which is available from the Visual Studio Command prompt window (type **uuigen.exe /?** for more information).



3.  Define the [Trace Flags](trace-flags.md) for your trace provider.

    The WPP\_DEFINE\_BIT elements of the WPP\_CONTROL\_GUIDS macro define the trace flags for the trace provider. Typically, the flags represent increasingly detailed reporting levels, but you can use flags as any way you like as conditions for generating trace messages. In the WPP\_CONTROL\_GUIDS example, the WPP\_DEFINE\_BIT defines four trace flags (MYDRIVER\_ALL\_INFO, TRACE\_DRIVER, TRACE\_DEVICE, and TRACE\_QUEUE).

    You can define up to 31 trace flags. WPP assigns bit values to the elements in the order they appear, for example, bit 0 (0x1), bit 1 (0x2), bit 2 (0x4), bit 3 (0x8) and so on. You use the trace flags when you add trace message functions to your source code (described in [Step 5: Instrument the driver code to generate trace messages at appropriate points](#step-5-instrument-the-driver-code-to-generate-trace-messages-at-appropriate-points)).

    **Note**  Using the trace flags you can control when to trace specific components (for example, specific I/O requests, or activities of device or driver objects). You add the trace flag to your trace message statement (for example, `DoTraceMessage (TRACE_DRIVER, "Hello World!\n")`. When you create a trace session with a trace controller, like [Tracelog](tracelog.md), you specify the **-flag** option to use for the trace provider in that session, in this case, the flag is bit 1 (0x1), which corresponds to the TRACE\_DRIVER flag. When you start the trace session, all the trace messages that specify that trace flag are written to the log.



## Step 2: Choose which trace message functions you intend to use and define the WPP macros for those functions


Like a debug print function, a trace message function is a function (or macro) you add to your code to write trace messages.

**Choosing a trace message function**

1.  The default trace message function is the [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro. If you use the default function you can control when to generate messages using the [Trace Flag](trace-level.md) values for your provider. The Trace Flags values are the flags you defined when you created the control GUID in Step 1. If you use **DoTraceMessage**, the default WPP macros are already defined for you (WPP\_LEVEL\_ENABLED and WPP\_LEVEL\_LOGGER), so you can skip the rest of this step and go to [Step 5](#step-5-instrument-the-driver-code-to-generate-trace-messages-at-appropriate-points).

2.  If you are using one of the KMDF or UMDF templates, the **TraceEvents** function and the necessary WPP macros are already defined to enable that function, so you can skip ahead to [Step 5](#step-5-instrument-the-driver-code-to-generate-trace-messages-at-appropriate-points).

3.  If you are creating your own trace message function, or converting existing debug print function, continue with the rest of this step.

**Creating or customizing a trace message function**

1.  If you are using custom trace message functions, or want to convert debug print functions (for example, [**KdPrint**](https://msdn.microsoft.com/library/windows/hardware/ff548092)) to generate trace messages, you need to define WPP macros that identify and enable the trace message functions in your trace provider. Put these macros in the Trace.h header file that you added to your project.

2.  Define the WPP macros to enable the trace function.

    Each trace message function that you use must have a corresponding pair of macros. These macros identify the trace provider and specify the conditions that generate the messages. You typically define a pair of macros, **WPP\_*&lt;condition&gt;*\_LOGGER** and **WPP\_*&lt;condition&gt;*\_ENABLED** in terms of the default WPP\_LEVEL\_ENABLED and WPP\_LEVEL\_LOGGER macros.

Each trace message function that you use must have a corresponding pair of macros. These macros identify the trace provider and specify the conditions that generate the messages. You typically define a pair of macros, **WPP\_*&lt;condition&gt;*\_LOGGER** and **WPP\_*&lt;condition&gt;*\_ENABLED** in terms of the default WPP\_LEVEL\_ENABLED and WPP\_LEVEL\_LOGGER macros.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="WPP_CONDITIONS_LOGGER"></span><span id="wpp_conditions_logger"></span><strong>WPP_<em>CONDITIONS</em><em>LOGGER</strong></p></td>
<td align="left"><p>Used to find the trace session associated with the provider and returns a handle to the session.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="WPP_CONDITIONS_ENABLED"></span><span id="wpp_conditions_enabled"></span><strong>WPP</em><em>CONDITIONS</em>_ENABLED</strong></p></td>
<td align="left"><p>Used to determine whether logging is enabled with the specified condition.</p></td>
</tr>
</tbody>
</table>



For the WPP macros you define, the *CONDITIONS* represent the conditions the trace message function supports, in the order they appear in the function's parameter list, separated by underscores. For example, the default trace message function, [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918), only supports [Trace Flag](trace-level.md) as the condition, so there is only one parameter in the macro names (WPP\_LEVEL\_ENABLED).

**Note**  Unfortunately, the names of the default macros (WPP\_LEVEL\_ENABLED and WPP\_LEVEL\_LOGGER) seems to indicate the [Trace Level](trace-level.md) parameter, but they actually refer to the Trace Flag.



If you use a custom trace message function, you can set additional qualifiers, such as the [Trace Level](trace-level.md). The Trace Level are defined in Evntrace.h file, and the trace levels provide a convenient way of classifying the trace messages as error, warning, and informational messages.

For example, you can add the following code snippet to the header file that you added to your project. The following code defines the custom WPP macros for a trace message function that supports both [Trace Level](trace-level.md) and a Trace Flag parameters as conditions to generate trace messages. The **WPP\_LEVEL\_FLAGS\_ENABLED** macro returns TRUE if logging is enabled for the specified FLAGS value and the enabled LEVEL value is greater than or equal to the level argument used in the trace message function call.

```ManagedCPlusPlus
#define WPP_LEVEL_FLAGS_LOGGER(lvl,flags) \
           WPP_LEVEL_LOGGER(flags)

#define WPP_LEVEL_FLAGS_ENABLED(lvl, flags) \
           (WPP_LEVEL_ENABLED(flags) && WPP_CONTROL(WPP_BIT_ ## flags).Level >= lvl)
```

Next, you need to specify the custom trace functions in the WPP configuration block (**begin\_wpp config** and **end\_wpp**) For example, if you use the template for UMDF or KMDF Driver projects in Visual Studio, the template defines the WPP macros for a custom trace message function called **TraceEvents**. The **TraceEvents** macro function uses [Trace Level](trace-level.md) and Trace Flag as conditions for generating messages. If you have defined the **WPP\_LEVEL\_FLAGS\_ENABLED** macro in your Trace.h header file, you can add the following macro definition.

```ManagedCPlusPlus
//
// This comment block is scanned by the trace preprocessor to define the 
// TraceEvents function.
//
// begin_wpp config
// FUNC TraceEvents(LEVEL, FLAGS, MSG, ...);
// end_wpp
//
```

You can also convert existing debug print statements to trace messages statements by added a similar **FUNC** declaration in WPP configuration block. For example, the following example adds the code to convert the existing [**KdPrint**](https://msdn.microsoft.com/library/windows/hardware/ff548092) statements. The **FUNC** declaration also globally defines the **KdPrint** to use the specified trace level and flag {LEVEL=TRACE\_LEVEL\_INFORMATION, FLAGS=TRACE\_DRIVER}. Instead of sending the output to the debugger, the debug print statements are sent to the trace log.

```ManagedCPlusPlus
//
// This comment block is scanned by the trace preprocessor to define the
// TraceEvents function and conversion for KdPrint. Note the double parentheses for the KdPrint message, for compatiblility with the KdPrint function.
//
// begin_wpp config
// FUNC TraceEvents(LEVEL, FLAGS, MSG, ...);
// FUNC KdPrint{LEVEL=TRACE_LEVEL_INFORMATION, FLAGS=TRACE_DRIVER}((MSG, ...));
// end_wpp
//
```

**Note**  If you want to convert [**KdPrintEx**](https://msdn.microsoft.com/library/windows/hardware/ff548100) to a trace message function, you need to take a few extra steps. Compared to [**KdPrint**](https://msdn.microsoft.com/library/windows/hardware/ff548092), the **KdPrintEx** function takes two additional arguments. To convert the **KdPrintEx** function, you need to define a **WPP\_DEFINE\_BIT** for the *ComponentID*, and define custom **WPP\_*&lt;condition&gt;*\_LOGGER** and **WPP\_*&lt;condition&gt;*\_ENABLED** macros. The second parameter for **KdPrintEx** specifies the level of is similar to the [Trace Level](trace-level.md) values, so you don't necessarily need to redefine them.



```ManagedCPlusPlus

#define WPP_CONTROL_GUIDS                                              \
    WPP_DEFINE_CONTROL_GUID(\
    myDriverTraceGuid, (11C3AAE4, 0D88, 41b3, 43BD, AC38BF747E19), \    /* change GUID for your provider */
        WPP_DEFINE_BIT(MYDRIVER_ALL_INFO)        /* bit  0 = 0x00000001 */ \
        WPP_DEFINE_BIT(TRACE_DRIVER)             /* bit  1 = 0x00000002 */ \
        WPP_DEFINE_BIT(TRACE_DEVICE)             /* bit  2 = 0x00000004 */ \
        WPP_DEFINE_BIT(TRACE_QUEUE)              /* bit  3 = 0x00000008 */ \
        WPP_DEFINE_BIT(DPFLTR_IHVDRIVER_ID)      /* bit  4 = 0x00000010 */\         /* Added for the ComponentID param of KdPrintEx */
    )

#define WPP_Flags_LEVEL_LOGGER(Flags, level)                                  \
    WPP_LEVEL_LOGGER(Flags)

#define WPP_Flags_LEVEL_ENABLED(Flags, level)                                 \
    (WPP_LEVEL_ENABLED(Flags) && \
    WPP_CONTROL(WPP_BIT_ ## Flags).Level >= level)



//
// This comment block is scanned by the trace preprocessor to convert the KdPrintEx function.
// Note the double parentheses for the KdPrint message, for compatiblility with the KdPrintEx function.
//
// begin_wpp config
// FUNC KdPrintEx((Flags, LEVEL, MSG, ...));   
// end_wpp
//
```

## Step 3: Include the associated trace header files (.h and .tmh) in your C or C++ source files


If you defined the control GUID and trace flags for your driver in a header file (for example, trace.h), you need to include the header file in the source files where you will initialize and unload WPP (Step 4) or call trace message functions.

In addition, you need to add an **\#include** statement for [Trace Message Header File](trace-message-header-file.md) (.tmh). When you build the driver or application, the WPP preprocessor generates the trace message header files (.tmh) for each source file that contains trace message functions.

```ManagedCPlusPlus
/* -- driver.c  - include the *.tmh file that is generated by WPP --*/

#include "trace.h"     /* file that defines WPP_CONFIG_GUIDS and trace flags */
#include "driver.tmh"  /* this file is auto-generated */
```

## Step 4: Add macros to the appropriate callback functions to initialize and clean up WPP


**To initialize WPP on driver entry**

-   Add the [WPP\_INIT\_TRACING](https://msdn.microsoft.com/library/windows/hardware/ff556191) macro to the *DriverEntry* routine of a kernel-mode driver or UMDF 2.0 driver, or to the *DLLMain* routine of a user-mode driver (UMDF 1.x) or application.

**To clean up WPP resources on driver exit**

-   Add the [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179) macro to the driver unload routine (for example, *DriverContextCleanup* or *DriverUnload*) of a kernel-mode driver or UMDF 2.0 driver.

    For a user-mode driver (UMDF 1.x) or application, add the [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179) macro to the *DLLMain* routine.

    You should also add the [WPP\_CLEANUP](https://msdn.microsoft.com/library/windows/hardware/ff556179) macro to the *DriverEntry* routine in case the *DriverEntry* fails. For example, if the *DriverEntry* fails, the driver unload routine will not be called. See the call to [**WdfDriverCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547175) in the following example.

Example of a kernel-mode driver using WPP\_INIT\_TRACING and WPP\_CLEANUP in *DriverEntry*

```ManagedCPlusPlus

NTSTATUS
DriverEntry(
    _In_ PDRIVER_OBJECT  DriverObject,
    _In_ PUNICODE_STRING RegistryPath
    )
{  

          //  ... 

                //
    // Initialize WPP Tracing in DriverEntry
    //
    WPP_INIT_TRACING( DriverObject, RegistryPath );

                //  ...


 //
    // Create a framework driver object to represent our driver.
    //
    status = WdfDriverCreate(
        DriverObject,
        RegistryPath,
        &attributes, // Driver Object Attributes
        &config,          // Driver Config Info
        WDF_NO_HANDLE // hDriver
        );

    if (!NT_SUCCESS(status)) {

        TraceEvents(TRACE_LEVEL_ERROR, DBG_INIT,
                "WdfDriverCreate failed with status 0x%x\n", status);
        //
        // Cleanup tracing here because DriverContextCleanup will not be called
        // as we have failed to create WDFDRIVER object itself.
        // Please note that if you return failure from DriverEntry after the
        // WDFDRIVER object is created successfully, you don&#39;t have to
        // call WPP cleanup because in those cases DriverContextCleanup
        // will be executed when the framework deletes the DriverObject.
        //
        WPP_CLEANUP(DriverObject);

    }

                return status;

}
```

Example of a kernel-mode driver using WPP\_CLEANUP in DriverContextCleanup

```ManagedCPlusPlus


VOID
DriverContextCleanup(
       PDRIVER_OBJECT DriverObject
       )
{
    // ...

    // Clean up WPP resources on unload
    //
    WPP_CLEANUP(DriverObject);

   // ...

}
```

Example for UMDF 2.0 driver using WPP\_INIT\_TRACING in DriverEntry

```ManagedCPlusPlus

/
// Driver specific #defines in trace header file (trace.h)
//
#define MYDRIVER_TRACING_ID      L"Microsoft\\UMDF2.0\\UMDF2_0Driver1 V1.0"
```

```ManagedCPlusPlus

 // Initialize WPP Tracing in the DriverEntry routine
 //
    WPP_INIT_TRACING( MYDRIVER_TRACING_ID );
```

Example for UMDF 1.0 driver use of WPP\_INIT\_TRACING and WPP\_CLEANUP macros in DLLMain

```ManagedCPlusPlus
/
// Driver specific #defines in trace header file (for example, trace.h)
//
#define MYDRIVER_TRACING_ID      L"Microsoft\\UMDF1.X\\UMDF1_XDriver1"


//
// DLL Entry Point - UMDF 1.0 example in the source file where you implement the DLL exports.
// 

extern "C"
BOOL
WINAPI
DllMain(
    HINSTANCE hInstance,
    DWORD dwReason,
    LPVOID lpReserved
    )
{
    if (dwReason == DLL_PROCESS_ATTACH) {
        WPP_INIT_TRACING(MYDRIVER_TRACING_ID);              // Initialize WPP tracing

        g_hInstance = hInstance;
        DisableThreadLibraryCalls(hInstance);

    } else if (dwReason == DLL_PROCESS_DETACH) {
        WPP_CLEANUP();                                                                                                              // Deactivate and cleanup WPP tracing
    }

    return _AtlModule.DllMain(dwReason, lpReserved);
}
```

## Step 5: Instrument the driver code to generate trace messages at appropriate points


You can use any trace message function you choose, provided the trace message function, the trace flags, and levels are defined appropriately. The default trace message function is the [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro. You can add this macro to your code to write messages to the log file. The following table lists some of the predefined trace message functions and the debug print functions you can use to create trace messages.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Example trace message functions</th>
<th align="left">When to use</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff544918" data-raw-source="[&lt;strong&gt;DoTraceMessage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544918)"><strong>DoTraceMessage</strong></a></td>
<td align="left"><p>This is the default trace message function. The advantage of using <a href="https://msdn.microsoft.com/library/windows/hardware/ff544918" data-raw-source="[&lt;strong&gt;DoTraceMessage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544918)"><strong>DoTraceMessage</strong></a> is that the function is already defined for you. You can use the trace flags you specify in the WPP_CONFIG_GUIDS macro. The disadvantage of using <strong>DoTraceMessage</strong>, is that the function only takes one conditional parameter, that is, trace flags. If you want to use trace levels, to log only error or warning messages, you can use <strong>DoDebugTrace</strong> macro, or use <strong>TraceEvents</strong>, which uses both trace flags and trace levels.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>TraceEvents</strong></td>
<td align="left"><p>If you create a driver using WDF templates in Visual Studio, this is the default trace message function. The advantage of using <strong>TraceEvents</strong> is that the trace message function, the trace flags, and <a href="trace-level.md" data-raw-source="[Trace Level](trace-level.md)">Trace Level</a> are already defined for you. In addition, the templates also include instrumentation that writes messages to the log file upon function entry and exit.</p></td>
</tr>
<tr class="odd">
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff548092" data-raw-source="[&lt;strong&gt;KdPrint&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548092)"><strong>KdPrint</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548100" data-raw-source="[&lt;strong&gt;KdPrintEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548100)"><strong>KdPrintEx</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543632" data-raw-source="[&lt;strong&gt;DbgPrint&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543632)"><strong>DbgPrint</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543634" data-raw-source="[&lt;strong&gt;DbgPrintEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff543634)"><strong>DbgPrintEx</strong></a></td>
<td align="left"><p>The advantage of using the debug print functions is that you do not need to modify your existing debug print statements. You can easily switch from viewing messages in the debugger, to recording trace messages in a file. If you customized the trace message function to include one of the debug print functions, you do not need to do any more work. When you create a trace session with Logman or <a href="tracelog.md" data-raw-source="[Tracelog](tracelog.md)">Tracelog</a>, or another trace controller, you just specify the flags and levels for your provider. Any debug print statements that meet the conditions you specify are printed to the log.</p></td>
</tr>
</tbody>
</table>



<span id="using_dotracemessage"></span><span id="USING_DOTRACEMESSAGE"></span>
**Using DoTraceMessage statements**

1.  Add the [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro to your code like you would a debug print routine. The **DoTraceMessage** macro takes 3 parameters: the flag level (*TraceFlagName*), which defines the condition when the trace message is written, the *Message* string, and the optional variable list.

    ```
    DoTraceMessage(TraceFlagName, Message, [VariableList... ]
    ```

    For example, the following [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) statement writes the name of the function that contains the **DoTraceMessage** statement when the TRACE\_DRIVER flag, as defined in WPP\_CONTROL\_GUIDS, is enabled for the trace session.

    ```ManagedCPlusPlus
         DoTraceMessage( TRACE_DRIVER, "\nEntering %!FUNC!" );

    ```

    The example uses a predefined string for the of the currently executing function (%FUNC!). For more information about WPP defined format specification strings, see [What are the WPP extended format specification strings?](what-are-the-wpp-extended-format-specification-strings-.md)

2.  To generate the trace message, create a trace session for your trace provider, using Logman or [Tracelog](tracelog.md), and specify a trace flag that sets the TRACE\_DRIVER flag (bit 1, 0x2).

```ManagedCPlusPlus
//
//  DoTraceMessage examples
// 

     ...

// writes the name of the function that contains the trace statement when the flag, TRACE_DRIVER (bit 1, 0x2), 
// as defined in WPP_CONTROL_GUIDS, is enabled for the trace session.

     DoTraceMessage( TRACE_DRIVER, "\nEntering %!FUNC!" );

     ...

// writes the name of the function, the line number, and the error code 

      DoTraceMessage(
            TRACE_DRIVER,
            "[%s] Failed at %d (error code= %d)\n",
            __FUNCTION__,
            __LINE__,
            dwLastError);
```

<span id="using_traceevents"></span><span id="USING_TRACEEVENTS"></span>
If you are using the Windows driver templates in Visual Studio, the **TraceEvents** macro is defined for you in the Trace.h header file.

**Using TraceEvents statements**

1.  Add the **TraceEvents** macro to your code like you would a debug print routine. The **TraceEvents** macro takes the following parameters: the trace level (*Level*) and the trace flag (*Flags*), which define the condition when the trace message is written, the *Message* string, and the optional variable list.

    ```
    TraceEvents(Level, Flags, Message, [VariableList... ]
    ```

    For example, the following **TraceEvents** statement writes the name of the function that contains the **TraceEvents** statement when the conditions specified in the [Trace Level](trace-level.md) and Trace Flag parameters are met. The Trace Level is an integer value; anything at or below the Trace Level specified for that trace session will be traced. The TRACE\_LEVEL\_INFORMATION is defined in Evntrace.h and has the value 4. The TRACE\_DRIVER flag (bit 1, 0x2) is defined in WPP\_CONTROL\_GUIDS. If this TRACE\_DRIVER bit is set for the trace session and the Trace Level is 4 or greater, **TraceEvents** writes the trace message.

    ```ManagedCPlusPlus
            TraceEvents(TRACE_LEVEL_INFORMATION, TRACE_DRIVER, "%!FUNC! Entry");

    ```

    The example uses a predefined string for the of the currently executing function (%FUNC!). For more information about WPP defined format specification strings, see [What are the WPP extended format specification strings?](what-are-the-wpp-extended-format-specification-strings-.md)

2.  To generate the trace message, create a trace session for your trace provider, using Logman or [Tracelog](tracelog.md). Specify a trace level to TRACE\_LEVEL\_INFORMATION (4) or greater, and specify a trace level that sets the TRACE\_DRIVER bit (bit 1, 0x2).

```ManagedCPlusPlus
//
//  TraceEvents examples
// 


    TraceEvents(TRACE_LEVEL_INFORMATION, TRACE_DRIVER, "%!FUNC! Entry");

//


    TraceEvents(TRACE_LEVEL_INFORMATION, DBG_INIT,
                       "OSRUSBFX2 Driver Sample - Driver Framework Edition.\n");

    TraceEvents(TRACE_LEVEL_INFORMATION, DBG_INIT,
                "Built %s %s\n", __DATE__, __TIME__);
```

## Step 6: Modify the Visual Studio project to run the WPP preprocessor and build the solution


The WDK provides support for the [WPP Preprocessor](wpp-preprocessor.md), so that you can run the preprocessor using Visual Studio and the MSBuild environment.

**To run the WPP preprocessor**

1.  Right-click the driver project in Solutions Explorer and click **Properties.**
2.  In the project property page, click **Configuration Properties** and click **WPP Tracing**.
3.  Under **General**, set the **Run WPP** option to **Yes**.
4.  Under **Command Line**, add any additional options to customize tracing behavior. For info on what you can add, see [WPP Preprocessor](wpp-preprocessor.md).
5.  Build the project or solution for your target configuration and platform. See [Building a Driver with the WDK](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver).

For information about the build process, see [TraceWPP task](tracewpp-task.md) and [WDK and Visual Studio build environment](wdk-and-visual-studio-build-environment.md).

You can also run the preprocessor separate from the build environment by using the TraceWPP tool (TraceWPP.exe). This tool is located in the bin/x86 and bin/x64 subdirectory of the WDK.

## Step 7: Start a trace session to capture and verify your trace messages


To verify that you have set up WPP tracing correctly, you should install your driver or application on a test computer and then create a trace session to capture the trace messages. You can create a trace session for your trace provider, using any trace controller, such as Logman, [Tracelog](tracelog.md), or [TraceView](traceview.md). You can have the messages written to a log file or sent to a kernel debugger. Depending upon the trace message functions you are using, you need to be sure to specify the trace flags and trace levels that will generate the messages.

For example, if you are using the trace levels defined in Evntrace.h, and you want to capture TRACE\_LEVEL\_INFORMATION (4) or greater, you need to set the level to 4. When you set the level to 4 for the trace session, all the informational (4), warning (3), error (2), and critical (1) messages will also be captured, assuming any other conditions, such as trace flags, are also satisfied.

To verify that all your messages are generated, you might just set the trace level and trace flags to maximum values so that all messages are generated. The trace flags use a bit mask (ULONG), so you could set all bits (for example, 0xFFFFFFFF). Trace levels are represented by a byte value. For example, if you are using Logman, you could specify, 0xFF for cover all levels.

(Example) Starting a trace session using Logman

```
logman create trace "myWPP_session" -p {11C3AAE4-0D88-41b3-43BD-AC38BF747E19} 0xffffffff 0xff -o c:\DriverTest\TraceFile.etl 

logman start "myWPP_session"

logman stop "myWPP_session"
```

(Example) Starting a trace session using TraceLog

```
tracelog -start MyTrace -guid  MyProvider.guid -f d:\traces\testtrace.etl -flag 2 -level 0xFFFF
```

The [Tracelog](tracelog.md) command includes the **-f** parameter to specify the name and location of the event trace log file. It includes the **-flag** parameter to specify the flags set and the **-level** parameter to specify the level setting. You can omit these parameters, but some trace providers do not generate any trace messages unless you set the flag or the level. The [Trace Level](trace-level.md) are defined in Evntrace.h file, and the trace levels provide a convenient way of classifying the trace messages as critical, error, warning, and informational messages.









