---
title: Trace Message Header File
description: Trace Message Header File
ms.assetid: 835162c0-6596-42ae-bc6d-824dd6c3f69f
keywords: ["trace message header files WDK", "TMH files WDK", "files WDK software tracing"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Message%20Header%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




