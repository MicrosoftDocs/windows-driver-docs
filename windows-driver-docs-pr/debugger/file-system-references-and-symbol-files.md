---
title: File System References and Symbol Files
description: File System References and Symbol Files
ms.assetid: c667380f-2942-453c-9ec8-70d3e1355e72
keywords: ["SymStore, short file names", "short file names and SymStore"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File System References and Symbol Files


## <span id="ddk_symbol_files_overview_dbg"></span><span id="DDK_SYMBOL_FILES_OVERVIEW_DBG"></span>


Files on disk can have both long file names and automatically generated abbreviated MS-DOS compatible 8.3 short file names. After adding a symbol file to a symbol store, it is possible that the symbols in that symbol file may not be accessible during debug if the symbol file contains any abbreviated MS-DOS 8.3 file names.

When the tools create a symbol file, the version of the file name that is recorded in the symbol file debug record depends on the tools and how they are run. If a symbol file has an abbreviated MS-DOS 8.3 file name instead of the actual file name embedded in the record, symbol loading at debug time may experience problems because the abbreviated file names vary from system to system. If this problem occurs, the contents of these symbol files may not be accessible during debug. Whenever possible, the user should refrain from using abbreviated file path names when creating symbol files. Some ways to use abbreviated file names inadvertently are to use the abbreviated file path name for a source file, an *include* directory, or an included library file.

For further information, see [Matching Symbol Names](matching-symbol-names.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20File%20System%20References%20and%20Symbol%20Files%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




