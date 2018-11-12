---
title: File System References and Symbol Files
description: File System References and Symbol Files
ms.assetid: c667380f-2942-453c-9ec8-70d3e1355e72
keywords: ["SymStore, short file names", "short file names and SymStore"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File System References and Symbol Files


## <span id="ddk_symbol_files_overview_dbg"></span><span id="DDK_SYMBOL_FILES_OVERVIEW_DBG"></span>


Files on disk can have both long file names and automatically generated abbreviated MS-DOS compatible 8.3 short file names. After adding a symbol file to a symbol store, it is possible that the symbols in that symbol file may not be accessible during debug if the symbol file contains any abbreviated MS-DOS 8.3 file names.

When the tools create a symbol file, the version of the file name that is recorded in the symbol file debug record depends on the tools and how they are run. If a symbol file has an abbreviated MS-DOS 8.3 file name instead of the actual file name embedded in the record, symbol loading at debug time may experience problems because the abbreviated file names vary from system to system. If this problem occurs, the contents of these symbol files may not be accessible during debug. Whenever possible, the user should refrain from using abbreviated file path names when creating symbol files. Some ways to use abbreviated file names inadvertently are to use the abbreviated file path name for a source file, an *include* directory, or an included library file.

For further information, see [Matching Symbol Names](matching-symbol-names.md).

 

 





