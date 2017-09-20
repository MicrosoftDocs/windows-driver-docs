---
title: Source Line Syntax
description: Source Line Syntax
ms.assetid: a4622a89-6419-4547-9650-eb10c3803462
keywords: ["expressions, source line numbers", "source files and paths, line number syntax", "line number syntax", "source files and paths, file name syntax", "file name syntax", "syntax rules for commands, source line numbers"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Source Line Syntax


## <span id="ddk_source_line_syntax_dbg"></span><span id="DDK_SOURCE_LINE_SYNTAX_DBG"></span>


You can specify source file line numbers as all or part of an MASM expression. These numbers evaluate to the offset of the executable code that corresponds to this source line.

**Note**   You cannot use source line numbers as part of a C++ expression. For more information about when MASM and C++ expression syntax is used, see [Evaluating Expressions](evaluating-expressions.md).

 

You must enclose source file and line number expressions by grave accents ( **\`** ). The following example shows the full format for source file line numbers.

```
`[[Module!]Filename][:LineNumber]`
```

If you have multiple files that have identical file names, *Filename* should include the whole directory path and file name. This directory path should be the one that is used at compilation time. If you supply only the file name or only part of the path and if there are multiple matches, the debugger uses the first match that it finds.

If you omit *Filename*, the debugger uses the source file that corresponds to the current program counter.

*LineNumber* is read as a decimal number unless you precede it with **0x**, regardless of the current default radix. If you omit *LineNumber*, the expression evaluates to the initial address of the executable that corresponds to the source file.

Source line expressions are not evaluated in CDB unless you issue a [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command or you include the [**-lines command-line option**](cdb-command-line-options.md) when you start WinDbg..

For more information about source debugging, see [Debugging in Source Mode](debugging-in-source-mode.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Source%20Line%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




