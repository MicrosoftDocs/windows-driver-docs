---
title: Can I customize DoTraceMessage
description: Can I customize DoTraceMessage
ms.assetid: 4c5c4990-6095-4ab8-a20b-7597b3169f52
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Can I customize DoTraceMessage?


Yes, you can write your own version of the [**DoTraceMessage**](https://msdn.microsoft.com/library/windows/hardware/ff544918) macro. DoTraceMessage generates a trace message.

The [TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726) sample driver provides an example of the methods that are described in this topic. [TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726) is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

### <span id="dotracemessage__default_version"></span><span id="DOTRACEMESSAGE__DEFAULT_VERSION"></span>DoTraceMessage: Default Version

By default, the DoTraceMessage macro has the following format:

```
DoTraceMessage(Flag,"Message",MessageVariables...);
```

In this default version, *Flag* represents the [trace flags](trace-flags.md), which are the conditions under which the message is generated. *MessageVariables* contains a comma-separated list of variables that the driver defines and that appear in the trace message. The *MessageVariables* variables are formatted by using the **printf** elements. The WPP preprocessor creates a compiler directive from the DoTraceMessage macro. This macro adds the message definition information and formatting information to the PDB file that was generated for the [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application.

The DoTraceMessage macro is expanded, logically, into the following:

```
PRE macro // If defined
If (WPP_CHECK_INIT && Flag is enabled) {
 ....Call WmiTraceMessage;
}
POST macro // If defined
```

Consider the following code example.

```
DoTraceMessage(ERROR, "IOCTL = %d", ControlCode);
```

This call generates the trace message when the ERROR flag is enabled. The message is "IOCTL=%d" and the *MessageVariables* is the value of *ControlCode*.

If the PRE-logging and POST-logging macros have been defined, they will also be expanded. The PRE macros and POST macros are supported in Microsoft Windows 2000 and later operating systems. To use the macros, you must build the driver by using the WDK. If you build a driver by using an earlier version of the Windows Driver Development Kit (DDK), the PRE and POST functionality is not available, and the macros will not be run as part of the trace statement. Building the driver by using an earlier version of the Windows DDK might not cause a build break, but the code will not work as expected.

### <span id="dotracemessage__general_format"></span><span id="DOTRACEMESSAGE__GENERAL_FORMAT"></span>DoTraceMessage: General Format

The following is a general format of a valid trace message function:

```
FunctionName(Conditions...,"Message",MessageVariables...);
```

Parameters that appear before the message are interpreted as conditions. Parameters that appear after the message are interpreted as message variables.

*Conditions* is a comma-separated list of values. The trace message is generated only if all conditions are true. You can specify any condition that is supported in the code.

### <span id="example__mytrace"></span><span id="EXAMPLE__MYTRACE"></span>Example: MyTrace

The following is a sample of a tracing function. This example adds conditions for the tracing level and the subcomponent of the provider that is generating the trace message.

```
MyDoTrace(Level, Flag, Subcomponent,"Message",MessageVariables...);
```

For example:

```
MyDoTrace(TRACE_LEVEL_ERROR, VERBOSE, Network,"IOCTL = %d", ControlCode);
```

The tracing level is the standard level that is defined in Evntrace.h, a public header file that is in the Include subdirectory of the WDK.

```
#define TRACE_LEVEL_NONE        0   // Tracing is not on
#define TRACE_LEVEL_FATAL       1   // Abnormal exit or termination
#define TRACE_LEVEL_ERROR       2   // Severe errors that need logging
#define TRACE_LEVEL_WARNING     3   // Warnings such as allocation failure
#define TRACE_LEVEL_INFORMATION 4   // Includes non-error cases(for example, Entry-Exit)
#define TRACE_LEVEL_VERBOSE     5   // Detailed traces from intermediate steps
#define TRACE_LEVEL_RESERVED6   6
#define TRACE_LEVEL_RESERVED7   7
#define TRACE_LEVEL_RESERVED8   8
#define TRACE_LEVEL_RESERVED9   9
```

### <span id="how_to_create_a_custom_tracing_function"></span><span id="HOW_TO_CREATE_A_CUSTOM_TRACING_FUNCTION"></span>How to Create a Custom Tracing Function

To create a custom tracing function, follow these steps:

-   Write alternative versions of the macros that support the DoTraceMessage macro.

-   Add the **-func** parameter to the RUN\_WPP statement that invokes the WPP preprocessor.

### <span id="write_custom_macros"></span><span id="WRITE_CUSTOM_MACROS"></span>Write Custom Macros

To create a custom tracing function that changes the conditions for a trace message (the parameters that appear before the message), you must write alternative versions of the macros that support the tracing functions, **WPP\_LEVEL\_ENABLED** and **WPP\_LEVEL\_LOGGER**.

-   **WPP\_LEVEL\_ENABLED(*Flags*)** determines whether logging is enabled with the specified flag value. It returns **TRUE** or **FALSE**.

-   **WPP\_LEVEL\_LOGGER(*Flags*)** finds the trace session to which the provider is enabled and returns a handle to the trace session.

For example, if you want to include the trace level, in addition to flags, as a condition, define a new WPP\_LEVEL\_ENABLED macro that includes the trace level. You can base the definition of the new macro on the default macro, as the following code example shows.

```
#define WPP_LEVEL_FLAGS_ENABLED(lvl, flags) (WPP_LEVEL_ENABLED(flags) && WPP_CONTROL(WPP_BIT_ ## flags).Level >=lvl
```

Typically, the WPP\_LEVEL\_LOGGER macro is not affected. In these cases, you can define the new macro to be default macro. For example:

```
#define WPP_LEVEL_FLAGS_LOGGER(lvl,flags) WPP_LEVEL_LOGGER(flags)
```

However, in some cases, you need to change the LOGGER macro. For example, you might want to write a tracing function that depends only on the trace level and not on flags.

In the following code example, the flags value in the macro is replaced by a dummy value. No flags are defined when declaring the control GUID definition.

```
#define WPP_CONTROL_GUIDS \
   WPP_DEFINE_CONTROL_GUID(CtlGuid,(a044090f,3d9d,48cf,b7ee,9fb114702dc1),  \
        WPP_DEFINE_BIT(DUMMY))
```

```
#define WPP_LEVEL_LOGGER(lvl) (WPP_CONTROL(WPP_BIT_ ## DUMMY).Logger)
```

### <span id="add_the_function_to_wpp"></span><span id="ADD_THE_FUNCTION_TO_WPP"></span>Add the Function to WPP

To add the custom tracing function to WPP, add the **-func** parameter to the RUN\_WPP statement with a declaration of the function, as the following code example shows.

```
RUN_WPP=$(SOURCES) -km -func:DoTraceLevelMessage(LEVEL,FLAGS,MSG,...)
```

**Note**  You must not specify the **-km** switch in the RUN\_WPP directive for user-mode applications or dynamic-link libraries (DLLs).



For a complete list of the optional parameters for RUN\_WPP, see [WPP Preprocessor](wpp-preprocessor.md).









