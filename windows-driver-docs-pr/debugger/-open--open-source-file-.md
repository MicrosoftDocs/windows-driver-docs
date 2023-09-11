---
title: .open (Open Source File)
description: The .open command searches the source path for a source file and opens this file.
keywords: [".open (Open Source File) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .open (Open Source File)
api_type:
- NA
---

# .open (Open Source File)


The **.open** command searches the source path for a source file and opens this file.

```dbgcmd
.open [-m Address] FileName 
.open -a Address 
```

## <span id="ddk_meta_open_source_file_dbg"></span><span id="DDK_META_OPEN_SOURCE_FILE_DBG"></span>Parameters


<span id="_______FileName______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *FileName*   
Specifies the source file name. This name can include an absolute or relative path. Unless you specify an absolute path, the path is interpreted as relative to a directory in the source path.

<span id="_______-m_______Address______"></span><span id="_______-m_______address______"></span><span id="_______-M_______ADDRESS______"></span> **-m** **** *Address*   
Specifies an address within the source file. This address must be contained in a known module. You should use the **-m** **** *Address* parameter if the file that *FileName* specifies is not unique. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

The **-m** parameter is required if you are using a [source server](using-a-source-server.md) to retrieve the source files.

<span id="_______-a_______Address______"></span><span id="_______-a_______address______"></span><span id="_______-A_______ADDRESS______"></span> **-a** *Address*   
Specifies an address within the source file. This address must be contained in a known module. If the debugger can find the source file, the debugger loads and opens the file, and the line that corresponds to the specified address is highlighted. If the debugger cannot find the source file, the address is displayed in the [Disassembly window](disassembly-window.md). For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

### Environment

You can use the **.open** command only in WinDbg, and you cannot use it in script files.

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about source files and source paths and for other ways to load source files, see [Source Path](source-path.md).

 

 





