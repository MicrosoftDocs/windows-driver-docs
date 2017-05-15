---
title: General Extensions
description: General Extensions
ms.assetid: 99ff4111-9f65-4e3d-beb3-0aa49f35a015
keywords: ["extension commands ( commands), general extensions", "exts.dll (general extensions)", "dbghelp.dll (general extensions)", "general extensions (exts.dll - dbghelp.dll)"]
---

# General Extensions


## <span id="ddk_general_extensions_dbg"></span><span id="DDK_GENERAL_EXTENSIONS_DBG"></span>


This section describes extension commands that are frequently used during both user-mode and kernel-mode debugging.

The debugger automatically loads the proper version of these extension commands. Unless you have manually loaded a different version, you do not have to keep track of the DLL versions that are being used. For more information about the default module search order, see [Using Debugger Extension Commands](using-debugger-extension-commands.md). For more information about how to load extension modules, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

Each extension command reference topics lists the DLLs that expose that command. Use the following rules to determine the proper directory to load this extension DLL from:

-   If your target computer is running Microsoft Windows XP or a later version of Windows, use winxp\\kdexts.dll, winxp\\ntsdexts.dll, winxp\\exts.dll, winext\\ext.dll, or dbghelp.dll.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20General%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




