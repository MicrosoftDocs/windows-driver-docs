---
title: Using Debugger Extensions
description: Using Debugger Extensions
ms.assetid: 55de0cbd-c6ba-40af-a932-2f9e57f1e8ec
keywords: ["extension commands ( commands)", "extension commands ( commands), overview", "commands", "commands, See "extension commands"", "debugger extensions, See "extension commands"", "extensions", "extensions, commands"]
---

# Using Debugger Extensions


## <span id="ddk_debugger_extensions_dbg"></span><span id="DDK_DEBUGGER_EXTENSIONS_DBG"></span>


Visual Studio, WinDbg, KD, and CDB all allow the use of debugger extension commands. These extensions give these three Microsoft debuggers a great degree of power and flexibility.

Debugger extension commands are used much like the standard debugger commands. However, while the built-in debugger commands are part of the debugger binaries themselves, debugger extension commands are exposed by DLLs distinct from the debugger.

This allows you to write new debugger commands which are tailored to your specific need. In addition, a number of debugger extension DLLs are shipped with the debugging tools themselves.

This section includes:

[Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md)

[Using Debugger Extension Commands](using-debugger-extension-commands.md)

[Writing New Debugger Extensions](writing-new-debugger-extensions.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Debugger%20Extensions%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




