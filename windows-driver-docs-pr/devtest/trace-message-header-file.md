---
title: Trace Message Header File
description: Trace Message Header File
ms.assetid: 835162c0-6596-42ae-bc6d-824dd6c3f69f
keywords:
- trace message header files WDK
- TMH files WDK
- files WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Message Header File


A *trace message header* (TMH) file is a text file that contains declarations of functions and variables used by the tracing code that WPP generates. The header file also includes macros that add trace message formatting instructions to a PDB file of a [trace provider](trace-provider.md), such as a kernel-mode driver or user-mode application.

WPP generates the TMH file automatically when you compile a [trace provider](trace-provider.md) that includes WPP macros. The TMH file has the same name as the source file, but with a .tmh file name extension. WPP saves the file in the same directory as the source file.

When you add the WPP macros to source code, you must also add an **\#include** directive for the TMH file that WPP will generate. The include statement has the form:

```
#include SourceFileName.tmh
```

This include statement must appear after the definition of the [WPP\_CONTROL\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186) macro, but before any calls to the WPP macros.

For more information, see [Adding WPP Macros to a Trace Producer](adding-wpp-macros-to-a-trace-provider.md) and see [TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726), a sample driver that was designed for software tracing. The TraceDrv sample is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

 

 





