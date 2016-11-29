---
title: How do I include a trace statement in a C/C++ macro
description: How do I include a trace statement in a C/C++ macro
ms.assetid: 1ab7f87e-7dbc-49a1-b3a2-24e4d525dc8b
---

# How do I include a trace statement in a C/C++ macro?


Strictly speaking, you cannot have a trace statement within a macro, because the WPP preprocessor runs before the C preprocessor. One solution is to run the C preprocessor twice, but there is an even simpler solution: define optional PRE and POST steps to the trace macros.

For example, you might want an "exit on failed" macro, such as

```
If (FAILED(HR)) {
     DoTraceMessage(ERROR,"We failed!");
     Goto done ;
} 
```

In this case, using PRE and POST forms of the macro makes this possible.

### <span id="define_the_function"></span><span id="DEFINE_THE_FUNCTION"></span>Define the function

In the source file, define the function, for example:

```
FUNC:_EXIT_IF_EXP_FAILED{LEVEL=WSM_ERROR}(_EXIT_IF_EXP_FAILED_EXP,MSG,...)
```

### <span id="define_the_macros"></span><span id="DEFINE_THE_MACROS"></span>Define the macros

In a header file, add the following definition directives. Put them after the WPP\_CONTROL\_GUIDS definition and before the **\#include** statement for the [trace message header file](trace-message-header-file.md).

```
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_PRE(LEVEL, HR) {HRESULT hr=S_OK ; if(FAILED(hr = HR)) {
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_POST(LEVEL, HR) ; goto done; } }
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_ENABLED(LEVEL, HR) WPP_LEVEL_ENABLED(LEVEL)
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_LOGGER(LEVEL, HR) WPP_LEVEL_LOGGER(WSM_ERROR)
```

### <span id="add_formatting"></span><span id="ADD_FORMATTING"></span>Add formatting

You can make the trace messages easier to read by including formatting data in the header file. This step is optional.

```
// MACRO: _EXIT_IF_EXP_FAILED
//
// begin_wpp config
// USEPREFIX (_EXIT_IF_EXP_FAILED,"%!STDPREFIX!");
// FUNC _EXIT_IF_EXP_FAILED{LEVEL=WSM_ERROR}(_EXIT_IF_EXP_FAILED_EXP,MSG,...);
// USESUFFIX (_EXIT_IF_EXP_FAILED," hr= %!HRESULT!", hr);
// end_wpp
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_PRE(LEVEL, HR) {HRESULT hr=S_OK ; if(FAILED(hr = HR)) {
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_POST(LEVEL, HR) ; goto done; } }
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_ENABLED(TRACELEVEL, HR) WPP_LEVEL_ENABLED(TRACELEVEL)
#define WPP_LEVEL__EXIT_IF_EXP_FAILED_EXP_LOGGER(LEVEL, HR) WPP_LEVEL_LOGGER(WSM_ERROR)
```

In this example, the **begin\_wpp config** and **end\_wpp** statements identify the configuration data in the header file for WPP.

Also, to notify WPP that there is configuration data in the header file, add the **-scan** parameter to the RUN\_WPP macro that invokes the WPP preprocessor. For example:

```
RUN_WPP -scan:trace.h
```

For a complete list of the optional parameters for RUN\_WPP, see [WPP Preprocessor](wpp-preprocessor.md).

### <span id="use_the_macros"></span><span id="USE_THE_MACROS"></span>Use the macros

In the source code, use the macros, such as in the following call:

```
_EXIT_IF_EXP_FAILED(hr,"it failed");
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20How%20do%20I%20include%20a%20trace%20statement%20in%20a%20C/C++%20macro?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




