---
title: How do I trace function entry and exit
description: How do I trace function entry and exit
ms.assetid: 08b0cf86-0f19-4972-8ae1-44ffdc968c16
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How do I trace function entry and exit?


The following sample code shows how to trace function entry and exit calls. This code works in Windows 2000 and later versions of Windows.

First, add the definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro to a source or header file. When defining the [trace flags](trace-flags.md), define a flag for function tracing, as shown in the following example:

```
#define WPP_CONTROL_GUIDS \
    WPP_DEFINE_CONTROL_GUID(CtlGuid,(a044090f,3d9d,48cf,b7ee,9fb114702dc1),  \
        WPP_DEFINE_BIT(ERROR)                \
        WPP_DEFINE_BIT(Unusual)              \
        WPP_DEFINE_BIT(Noise)                \
 WPP_DEFINE_BIT(FuncTrace) )
```

Then, in the same file, add the configuration data for the trace messages. Start the configuration data with a **begin\_wpp config** statement, and end it with an **end\_wpp** statement. Then add the definitions for the macros that support FuncTrace.

```
// begin_wpp config
// FUNC FuncEntry();
// FUNC FuncExit();
// USESUFFIX(FuncEntry, " Entry to %!FUNC!");
// USESUFFIX(FuncExit, " Exit from %!FUNC!");
// end_wpp

// Map the null flags used by Entry/Exit to a function called FuncTrace
#define WPP__ENABLED() WPP_LEVEL_ENABLED(FuncTrace)
#define WPP__LOGGER() WPP_LEVEL_LOGGER(FuncTrace)
```

In the source file, surround the function code with **FuncEntry()** and **FuncExit()** calls.

```
#include "mytrace.h"
#include "entryexit.tmh"
void examplesub(int x)
{
    FuncEntry();
    // function code
    FuncExit();
}
```

For example:

```
#include "mytrace.h"
#include "entryexit.tmh"
void examplesub(int x)
{
    FuncEntry();
       DoTraceMessage(Noise, "Value is %d",x);
    FuncExit();
}
```

If you put configuration data in a header file, use the **-scan** parameter to direct WPP to look for configuration data in the specified file. In this example, the configuration data is in the mytrace.h file.

```
RUN_WPP=$(SOURCES) -km -scan:mytrace.h
```

**Note**  You must not specify the **-km** switch in the RUN\_WPP directive for user-mode applications or dynamic-link libraries (DLLs).



For a complete list of the optional parameters for RUN\_WPP, see [WPP Preprocessor](wpp-preprocessor.md).









