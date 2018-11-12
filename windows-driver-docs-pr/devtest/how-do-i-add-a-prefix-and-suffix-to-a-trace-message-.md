---
title: How do I add a prefix and suffix to a trace message
description: How do I add a prefix and suffix to a trace message
ms.assetid: d8cd0a90-d020-4b1e-bec1-7d920964169e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I add a prefix and suffix to a trace message?


You can use a [WPP Preprocessor](wpp-preprocessor.md) configuration block to add data to trace messages.

The WPP configuration block is defined by the **begin\_wpp config** and **end\_wpp** statements that you place in your source code.

**//begin\_wpp config**

...

*configuration block*

...

**//end\_wpp**

If you put configuration data in a header file, specify the name of the header file in your project properties (for **WPP Tracing**). Under **File Options** on the property page, specify the **Scan Configuration file**. See [WPP Preprocessor](wpp-preprocessor.md) for more information.

### <span id="configuration_block_syntax"></span><span id="CONFIGURATION_BLOCK_SYNTAX"></span>Configuration block syntax

<span id="__USEPREFIX__Function_Name___Format_string___"></span><span id="__useprefix__function_name___format_string___"></span><span id="__USEPREFIX__FUNCTION_NAME___FORMAT_STRING___"></span>**//USEPREFIX (**<em>Function\_Name</em>**, "**<em>Format string</em>**");**  
Defines a format string prefix to use when the event is logged. The first parameter is the name of the function to which this prefix applies. The second parameter is the format string to use. To use the default value, specify %!STDPREFIX!. The default trace message prefix specifies the CPU number, process ID, thread ID, time stamp in Coordinated Universal Time (UTC) format, and the control GUID friendly name.

```
//USEPREFIX (TRACE_RETURN, "%!STDPREFIX!");
```

<span id="__FUNC_Function_Name_args__EXP__"></span><span id="__func_function_name_args__exp__"></span><span id="__FUNC_FUNCTION_NAME_ARGS__EXP__"></span>**//FUNC** *Function\_Name*{*args*}(EXP)**;**  
Defines the name and the signature of the trace function. The braces **{ }** are used to define set values for the function. In the following example, the function takes one argument and no format string, and the LEVEL is set to ERROR.

```
//FUNC TRACE_RETURN{LEVEL=ERROR}(EXP);
```

<span id="__USESUFFIX__Function_Name___Format_string___"></span><span id="__usesuffix__function_name___format_string___"></span><span id="__USESUFFIX__FUNCTION_NAME___FORMAT_STRING___"></span>**//USESUFFIX (**<em>Function\_Name</em>**, "**<em>Format string</em>**");**  
Defines the format string suffix to use when the event is logged. The first parameter is the name of the function to which this suffix applies. The second parameter is the format string to use. You can use variable names in your code.

```
//USESUFFIX (TRACE_RETURN, "Function Return=%!HRESULT!",EXP);
```

### <span id="example_configuration_block"></span><span id="EXAMPLE_CONFIGURATION_BLOCK"></span>Example configuration block

The following example defines a trace macro that uses the format string prefix and suffix. If you are defining a tracing macro, you must also define macros to select the logger and to check whether the event should be logged.

```
//MACRO: TRACE_RETURN
//
//begin_wpp config
//USEPREFIX (TRACE_RETURN, "%!STDPREFIX!");
//FUNC TRACE_RETURN{LEVEL=ERROR}(EXP);
//USESUFFIX (TRACE_RETURN, "Function Return=%!HRESULT!",EXP);
//end_wpp

//
// The next two macros are for checking if the event should be logged, and for
// choosing the logger handle to use when calling the ETW trace API
//
#define WPP_LEVEL_EXP_ENABLED(LEVEL, HR) WPP_FLAG_ENABLED(LEVEL)
#define WPP_LEVEL_EXP_LOGGER(LEVEL, HR) WPP_FLAG_LOGGER(LEVEL)
```

### <span id="example_trace_results"></span><span id="EXAMPLE_TRACE_RESULTS"></span>Example trace results

```
[0]0F78.0460::06/24/2006-15:54:54.880 [tracedrv]Function Return=0x8000000f(STATUS_DEVICE_POWERED_OFF)
```

 

 





