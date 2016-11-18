---
title: How do I add a prefix and suffix to a trace message
description: How do I add a prefix and suffix to a trace message
ms.assetid: d8cd0a90-d020-4b1e-bec1-7d920964169e
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

<span id="__USEPREFIX__Function_Name___Format_string___"></span><span id="__useprefix__function_name___format_string___"></span><span id="__USEPREFIX__FUNCTION_NAME___FORMAT_STRING___"></span>**//USEPREFIX (***Function\_Name***, "***Format string***");**  
Defines a format string prefix to use when the event is logged. The first parameter is the name of the function to which this prefix applies. The second parameter is the format string to use. To use the default value, specify %!STDPREFIX!. The default trace message prefix specifies the CPU number, process ID, thread ID, time stamp in Coordinated Universal Time (UTC) format, and the control GUID friendly name.

```
//USEPREFIX (TRACE_RETURN, "%!STDPREFIX!");
```

<span id="__FUNC_Function_Name_args__EXP__"></span><span id="__func_function_name_args__exp__"></span><span id="__FUNC_FUNCTION_NAME_ARGS__EXP__"></span>**//FUNC** *Function\_Name*{*args*}(EXP)**;**  
Defines the name and the signature of the trace function. The braces **{ }** are used to define set values for the function. In the following example, the function takes one argument and no format string, and the LEVEL is set to ERROR.

```
//FUNC TRACE_RETURN{LEVEL=ERROR}(EXP);
```

<span id="__USESUFFIX__Function_Name___Format_string___"></span><span id="__usesuffix__function_name___format_string___"></span><span id="__USESUFFIX__FUNCTION_NAME___FORMAT_STRING___"></span>**//USESUFFIX (***Function\_Name***, "***Format string***");**  
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20add%20a%20prefix%20and%20suffix%20to%20a%20trace%20message?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




