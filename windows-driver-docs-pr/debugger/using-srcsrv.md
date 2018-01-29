---
title: Using SrcSrv
description: Using SrcSrv
ms.assetid: 2696e5e9-343f-49a2-bdab-23a54f8c9e5c
keywords: ["source servers, SrcSrv (srcsrv.dll)", "SrcSrv, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using SrcSrv


To use [SrcSrv](srcsrv.md) with WinDbg, KD, NTSD, or CDB, verify that you have installed a recent version of the [Debugging Tools for Windows](https://docs.microsoft.com/windows-hardware/drivers/debugger/) package (version 6.3 or later). Then, include the text `srv*` in the source path, separated by semicolons from any directories that are also in the source path.

For example:

```
.srcpath srv*;c:\someSourceCode
```

If the source path is set as shown in the preceding example, the debugger first uses [SrcSrv](srcsrv.md) to retrieve source files from locations specified in the target modules' symbol files. If SrcSrv is unable to retrieve a source file, the debugger attempts to retrieve it from c:\\someSourceCode. Regardless of whether srv\* is the first element in the path or appears later, the debugger always uses SymSrv before it searches any other directories listed in the path.

If a source file is retrieved by [SrcSrv](srcsrv.md), it remains on your hard drive after the debugging session is over. Source files are stored locally in the src subdirectory of the home directory (unlike the symbol server, the source server does not specify a local cache in the `srv*` syntax itself). The home directory defaults to the Debugging Tools for Windows installation directory; it can be changed by using the [**!homedir**](-homedir.md) extension or by setting the DBGHELP\_HOMEDIR environment variable. If the src subdirectory of the home directory does not already exist, it is created.

### <span id="debugging_srcsrv"></span><span id="DEBUGGING_SRCSRV"></span>Debugging SrcSrv

If you experience any trouble extracting the source files from the debugger, start the debugger with the -n command-line parameter to view the actual source extraction commands along with the output of those commands. The !sym noisy command does the same thing, but you may have already missed important information from previous extraction attempts. This is because the debugger gives up trying to access source from version control repositories that appear to be unreachable.

### <span id="retrieving_source_files"></span><span id="RETRIEVING_SOURCE_FILES"></span>Retrieving Source Files

If you use the [**.open (Open Source File)**](-open--open-source-file-.md) command to open a new source file through [SrcSrv](srcsrv.md), you must include the -m Address parameter.

To facilitate the use of [SrcSrv](srcsrv.md) from tools other than the debuggers listed previously, the DbgHelp API provides access to SrcSrv functionality through the **SymGetSourceFile** function. To retrieve the name of the source file to be retrieved, call the **SymEnumSourceFiles** or **SymGetLineFromAddr64** function. For more details on the DbgHelp API, see the dbghelp.chm documentation, which can be found in the sdk/help subdirectory of the Debugging Tools for Windows installation directory, or see [Debug Help Library](http://go.microsoft.com/fwlink/p/?linkid=125231) on MSDN.

### <span id="using_agestore_to_reduce_the_cache_size"></span><span id="USING_AGESTORE_TO_REDUCE_THE_CACHE_SIZE"></span>Using AgeStore to Reduce the Cache Size

Any source files downloaded by [SrcSrv](srcsrv.md) remain on your hard drive after the debugging session is over. To control the size of the source cache, the AgeStore tool can be used to delete cached files that are older than a specified date or to reduce the contents of the cache below a specified size. For details, see [AgeStore](agestore.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20SrcSrv%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




