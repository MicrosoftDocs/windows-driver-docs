---
title: Source Line Syntax
description: Source Line Syntax
ms.assetid: a4622a89-6419-4547-9650-eb10c3803462
keywords: ["expressions, source line numbers", "source files and paths, line number syntax", "line number syntax", "source files and paths, file name syntax", "file name syntax", "syntax rules for commands, source line numbers"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Source Line Syntax


## <span id="ddk_source_line_syntax_dbg"></span><span id="DDK_SOURCE_LINE_SYNTAX_DBG"></span>


You can specify source file line numbers as all or part of an MASM expression. These numbers evaluate to the offset of the executable code that corresponds to this source line.

**Note**   You cannot use source line numbers as part of a C++ expression. For more information about when MASM and C++ expression syntax is used, see [Evaluating Expressions](evaluating-expressions.md).

 

You must enclose source file and line number expressions by grave accents ( **\`** ). The following example shows the full format for source file line numbers.

```text
`[[Module!]Filename][:LineNumber]`
```

If you have multiple files that have identical file names, *Filename* should include the whole directory path and file name. This directory path should be the one that is used at compilation time. If you supply only the file name or only part of the path and if there are multiple matches, the debugger uses the first match that it finds.

If you omit *Filename*, the debugger uses the source file that corresponds to the current program counter.

*LineNumber* is read as a decimal number unless you precede it with **0x**, regardless of the current default radix. If you omit *LineNumber*, the expression evaluates to the initial address of the executable that corresponds to the source file.

Source line expressions are not evaluated in CDB unless you issue a [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command or you include the [**-lines command-line option**](cdb-command-line-options.md) when you start WinDbg..

For more information about source debugging, see [Debugging in Source Mode](debugging-in-source-mode.md).

 

 





