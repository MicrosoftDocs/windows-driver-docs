---
title: .writemem (Write Memory to File)
description: The .writemem command writes a section of memory to a file.
keywords: [".writemem (Write Memory to File) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .writemem (Write Memory to File)
api_type:
- NA
---

# .writemem (Write Memory to File)


The **.writemem** command writes a section of memory to a file.

```dbgcmd
.writemem FileName Range 
```

## <span id="ddk_meta_write_memory_to_file_dbg"></span><span id="DDK_META_WRITE_MEMORY_TO_FILE_DBG"></span>Parameters


<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the name of the file to be created. You can specify a full path and file name, or just the file name. If the file name contains spaces, *FileName* should be enclosed in quotation marks. If no path is specified, the current directory is used.

<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory range to be written to the file. For syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The memory is copied literally to the file. It is not parsed in any way.

The **.writemem** command is the opposite of the [**.readmem (Read Memory from File)**](-readmem--read-memory-from-file-.md) command.

 

 





