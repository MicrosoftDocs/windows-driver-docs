---
title: SymStore Compressed Files
description: SymStore Compressed Files
ms.assetid: 4ec6a7f5-ceee-46d5-9a5e-36ab9fe9db52
keywords: ["SymStore, compressed files"]
---

# SymStore Compressed Files


## <span id="ddk_symbol_files_overview_dbg"></span><span id="DDK_SYMBOL_FILES_OVERVIEW_DBG"></span>


SymStore can be used with compressed files in two different ways:

1.  Use SymStore with the **/p** option to store pointers to the symbol files. After SymStore finishes, compress the files that the pointers refer to.

2.  Use SymStore with the **/x** option to create an index file. After SymStore finishes, compress the files listed in the index file. Then, use SymStore with the **/y** option (and, if you wish, the **/p** option) to store the files or pointers to the files in the symbol store. (SymStore will not need to uncompress the files to perform this operation.)

Your symbol server will be responsible for uncompressing the files at the proper time.

If you are using SymSrv as your symbol server, any compression should be done using the compress.exe tool which is available [here](http://go.microsoft.com/fwlink/p/?linkid=239917). Compressed files should have an underscore as the last character in their file extensions (for example, module1.pd\_ or module2.db\_). For details, see [SymSrv](symsrv.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20SymStore%20Compressed%20Files%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




