---
title: Accessing Symbols for Debugging
description: Accessing Symbols for Debugging
ms.assetid: a0f52dc3-6903-4d63-b74c-5c16960a7cb6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accessing Symbols for Debugging


## <span id="ddk_debugging_user_mode_processes_without_symbols_dbg"></span><span id="DDK_DEBUGGING_USER_MODE_PROCESSES_WITHOUT_SYMBOLS_DBG"></span>


Setting up symbols correctly for debugging can be a challenging task, particularly for kernel debugging. It often requires that you know the names and releases of all products on your computer. The debugger must be able to locate each of the symbol files corresponding to the product releases and service packs.

This can result in an extremely long symbol path consisting of a long list of directories.

To simplify these difficulties in coordinating symbol files, the symbol files can be gathered into a *symbol store*, which is then accessed by a *symbol server*.

A symbol store is a collection of symbol files, an index, and a tool that can be used by an administrator to add and delete files. The files are indexed according to unique parameters such as the time stamp and image size. A symbol store can also hold executable image files which can be extracted using a symbol server. Debugging Tools for Windows contains a symbol store creation tool called [SymStore](symstore.md).

A symbol server enables the debuggers to automatically retrieve the correct symbol files from a symbol store without the user needing to know product names, releases, or build numbers. Debugging Tools for Windows contains a symbol server called [SymSrv](symsrv.md). The symbol server is activated by including a certain text string in the symbol path. Each time the debugger needs to load symbols for a newly loaded module, it calls the symbol server to locate the appropriate symbol files.

If you wish to use a different method for your symbol search than that provided by SymSrv, you can create your own symbol server DLL. For details on implementing such a symbol server, see [Other Symbol Servers](other-symbol-servers.md).

If you are performing user-mode debugging, you will need symbols for the target application. If you are performing kernel-mode debugging, you will need symbols for the driver you are debugging, as well as the Windows public symbols. Microsoft has created a symbol store with public symbols for Microsoft products; this symbol store is available on the internet. These symbols can be loaded using the [**.symfix (Set Symbol Store Path)**](-symfix--set-symbol-store-path-.md) command, as long as you have access to the internet while your debugger is running. For more information or to determine how to manually install these symbols, see [Installing Windows Symbol Files](installing-windows-symbol-files.md).

This section includes:

[Installing Windows Symbol Files](installing-windows-symbol-files.md)

[Symbol Stores and Symbol Servers](symbol-stores-and-symbol-servers.md)

[Deferred Symbol Loading](deferred-symbol-loading.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Accessing%20Symbols%20for%20Debugging%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




