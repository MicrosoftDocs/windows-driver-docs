---
title: SymStore Compressed Files
description: SymStore Compressed Files
ms.assetid: 4ec6a7f5-ceee-46d5-9a5e-36ab9fe9db52
keywords: ["SymStore, compressed files"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# SymStore Compressed Files


## <span id="ddk_symbol_files_overview_dbg"></span><span id="DDK_SYMBOL_FILES_OVERVIEW_DBG"></span>


SymStore can be used with compressed files in two different ways:

1.  Use SymStore with the **/p** option to store pointers to the symbol files. After SymStore finishes, compress the files that the pointers refer to.

2.  Use SymStore with the **/x** option to create an index file. After SymStore finishes, compress the files listed in the index file. Then, use SymStore with the **/y** option (and, if you wish, the **/p** option) to store the files or pointers to the files in the symbol store. (SymStore will not need to uncompress the files to perform this operation.)

Your symbol server will be responsible for uncompressing the files at the proper time.

If you are using SymSrv as your symbol server, any compression should be done using the compress.exe tool which is available [here](https://go.microsoft.com/fwlink/p/?linkid=239917). Compressed files should have an underscore as the last character in their file extensions (for example, module1.pd\_ or module2.db\_). For details, see [SymSrv](symsrv.md).

 

 





