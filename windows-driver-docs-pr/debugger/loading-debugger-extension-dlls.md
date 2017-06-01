---
title: Loading Debugger Extension DLLs
description: Loading Debugger Extension DLLs
ms.assetid: 6ca70732-cbf6-44fd-a020-c297b40d41f6
keywords: ["extension commands ( commands), loading", "loading extension commands", "nt4fre directory", "nt4chk directory", "w2kfre directory", "w2kchk directory", "winxp directory", "winext directory"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Loading Debugger Extension DLLs


## <span id="ddk_loading_debugger_extension_dlls_dbg"></span><span id="DDK_LOADING_DEBUGGER_EXTENSION_DLLS_DBG"></span>


There are several methods of loading debugger extension DLLs, as well as controlling the default debugger extension DLL and the default debugger extension path:

-   (Before starting the debugger) Use the \_NT\_DEBUGGER\_EXTENSION\_PATH [environment variable](environment-variables.md) to set the default path for extension DLLs. This can be a number of directory paths, separated by semicolons.

-   Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load a new DLL.

-   Use the [**.unload (Unload Extension DLL)**](-unload--unload-extension-dll-.md) command to unload a DLL.

-   Use the [**.unloadall (Unload All Extension DLLs)**](-unloadall--unload-all-extension-dlls-.md) command to unload all debugger extensions.

-   (Before starting the debugger; CDB only) Use the [tools.ini](configuring-tools-ini.md) file to set the default extension DLL.

-   (Before starting the debugger) Use the **-a** [command-line option](command-line-options.md) to set the default extension DLL.

-   Use the [**.extpath (Set Extension Path)**](-extpath--set-extension-path-.md) command to set the extension DLL search path.

-   Use the [**.setdll (Set Default Extension DLL)**](-setdll--set-default-extension-dll-.md) command to set the default extension DLL.

-   Use the [**.chain (List Debugger Extensions)**](-chain--list-debugger-extensions-.md) command to display all loaded debugger extension modules, in their default search order.

You can also load an extension DLL simply by using the full **!***module***.***extension* syntax the first time you issue a command from that module. See [Using Debugger Extension Commands](using-debugger-extension-commands.md) for details.

The extension DLLs that you are using must match the operating system of the target computer. The extension DLLs that ship with the Debugging Tools for Windows package are each placed in a different subdirectory of the installation directory:

-   The winxp directory contains extensions that can be used with Windows XP and later versions of Windows.

-   The winext directory contains extensions that can be used with any version of Windows. The dbghelp.dll module, located in the base directory of Debugging Tools for Windows, also contains extensions of this type.

If you write your own debugger extensions, you can place them in any directory. However, it is advised that you place them in a new directory and add that directory to the debugger extension path.

There can be as many as 32 extension DLLs loaded.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Loading%20Debugger%20Extension%20DLLs%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




