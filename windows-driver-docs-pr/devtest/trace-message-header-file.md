---
title: Trace Message Header File
description: Trace Message Header File
keywords:
- trace message header files WDK
- TMH files WDK
- files WDK software tracing
ms.date: 04/20/2017
---

# Trace Message Header File


A *trace message header* (TMH) file is a text file that contains declarations of functions and variables used by the tracing code that WPP generates. The header file also includes macros that add trace message formatting instructions to a PDB file of a [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application.

WPP generates the TMH file automatically when you compile a [trace provider](trace-provider.md) that includes WPP macros. The TMH file has the same name as the source file, but with a .tmh file name extension. WPP saves the file in the same directory as the source file.

When you add the WPP macros to source code, you must also add an **\#include** directive for the TMH file that WPP will generate. The include statement has the form:

```
#include SourceFileName.tmh
```

This include statement must appear after the definition of the [WPP\_CONTROL\_GUIDS](/previous-versions/windows/hardware/previsioning-framework/ff556186(v=vs.85)) macro, but before any calls to the WPP macros.

For more information, see [Adding WPP Macros to a Trace Producer](adding-wpp-macros-to-a-trace-provider.md) and see [TraceDrv](https://github.com/Microsoft/Windows-driver-samples/tree/master/general/tracing/tracedriver), a sample driver that was designed for software tracing. The TraceDrv sample is available in the [Windows driver samples](https://github.com/Microsoft/Windows-driver-samples) repository on GitHub.

 

