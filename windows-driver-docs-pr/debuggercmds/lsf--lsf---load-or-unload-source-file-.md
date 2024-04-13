---
title: "lsf, lsf- (Load or Unload Source File)"
description: "The lsf and lsf- commands load or unload a source file."
keywords: ["lsf, lsf- (Load or Unload Source File) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- lsf, lsf- (Load or Unload Source File)
api_type:
- NA
---

# lsf, lsf- (Load or Unload Source File)


The **lsf** and **lsf-** commands load or unload a source file.

```dbgcmd
lsf Filename 
lsf- Filename
```

## <span id="ddk_cmd_load_or_unload_source_file_dbg"></span><span id="DDK_CMD_LOAD_OR_UNLOAD_SOURCE_FILE_DBG"></span>Parameters


<span id="_______Filename______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *Filename*   
Specifies the file to load or unload. If this file is not located in the directory where the debugger was opened from, you must include an absolute or relative path. The file name must follow Microsoft Windows file name conventions.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The **lsf** command loads a source file.

The **lsf-** command unloads a source file. You can use this command to unload files that you previously loaded with **lsf** or automatically loaded source files. You cannot use **lsf-** to unload files that were loaded through WinDbg's **File | Open Source File** command or files that a WinDbg workspace loaded.

In CDB or KD, you can view source files in the [Debugger Command window](../debugger/debugger-command-window.md). In WinDbg, source files are loaded as new [Source windows](../debugger/source-window.md).

For more information about source files, source paths, and other ways to load source files, see [Source Path](../debugger/source-path.md).

## See also


[**ls, lsa (List Source Lines)**](ls--lsa--list-source-lines-.md)

[**lsc (List Current Source)**](lsc--list-current-source-.md)


