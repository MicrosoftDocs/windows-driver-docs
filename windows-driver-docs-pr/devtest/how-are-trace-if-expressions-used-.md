---
title: How are Trace-If expressions used
description: How are Trace-If expressions used
ms.assetid: 05fc8225-ba4e-4718-a5e1-c9e49ec931b7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How are Trace-If expressions used?


To help you understand how Trace-If expressions are used, we provide an example of such expressions that demonstrates the usage and syntax of "begin\_wpp config" statements. This example refers to a function TRACE\_RETURN, which logs an event if the expression FAILED(HR) is true.

If FAILED(HR) is true, assume that there is a source file that has status ULONG and an event will be logged by calling TRACE\_RETURN(Status).
```
//MACRO: TRACE_RETURN
//
//begin_wpp config
//USEPREFIX (TRACE_RETURN, "%!STDPREFIX!");
//FUNC TRACE_RETURN{LEVEL=ERROR}(EXP);
//USESUFFIX (TRACE_RETURN, "Function Return=%!HRESULT!",EXP);
//end_wpp

#define WPP_LEVEL_EXP_PRE(LEVEL, HR) {if (FAILED(HR)) {
#define WPP_LEVEL_EXP_POST(LEVEL, HR) ;}}
#define WPP_LEVEL_EXP_ENABLED(LEVEL, HR) WPP_LEVEL_ENABLED(LEVEL)
#define WPP_LEVEL_EXP_LOGGER(LEVEL, HR) WPP_LEVEL_LOGGER(ERROR)
```

In the previous example, notice that, TRACE\_RETURN is defined between the begin\_wpp config and end\_wpp lines. This definition is then followed by the PRE / POST macro and the ENABLED and LOGGER definitions.

The begin\_wpp config and end\_wpp delimiters define a configuration block that is parsed by the preprocessor. The file that contains the configuration block definition must be scanned by WPP. This file is specified with the -scan:file.extension parameter.

**Note**   For information about **-scan** and other **RUN\_WPP** options, see [WPP Preprocessor](wpp-preprocessor.md).



The following list provides more information about each statement in the example configuration block:

<span id="USEPREFIX"></span><span id="useprefix"></span>**USEPREFIX**  
Defines a prefix format string to be used when the event is logged. In the example, STDPREFIX is used. For values available with STDPREFIX, see [How do I change the prefix output on every trace line?](how-do-i-change-the-prefix-output-on-every-trace-line-.md)

<span id="USESUFFIX"></span><span id="usesuffix"></span>**USESUFFIX**  
Defines a suffix format string to be used when the event is logged.

<span id="FUNC"></span><span id="func"></span>**FUNC**  
Defines the name and signature of the trace function. In the example, the function takes one parameter and no format string.

For another example of Trace-If expressions, see the [How do I include a trace statement in a C/C++ macro?](how-do-i-include-a-trace-statement-in-a-c-c---macro-.md) section.









