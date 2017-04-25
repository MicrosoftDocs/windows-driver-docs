---
title: WdbgExts Extension API Overview
description: WdbgExts Extension API Overview
ms.assetid: e54d330f-ab48-407f-a9f2-e4a521f5e27b
keywords: ["WdbgExts extensions, overview"]
---

# WdbgExts Extension API Overview


## <span id="ddk_wdbgexts_extension_api_overview_dbwx"></span><span id="DDK_WDBGEXTS_EXTENSION_API_OVERVIEW_DBWX"></span>


Each WdbgExts extension DLL exports one or more functions that are used to implement *extension commands*. These functions are named according to the standard C convention, except that upper-case letters are not permitted.

The function name and the extension command name are identical, except that the extension command begins with an exclamation point ( **!** ). For example, when you load Myextension.dll into the debugger and then type **!stack** into the Debugger Command window, the debugger looks for an exported function named **stack** in Myextension.dll.

If Myextension.dll is not already loaded, or if there are other extension commands with the same name in other extension DLLs, you can type **!myextension.stack** into the Debugger Command window to indicate the extension DLL and the extension command in that DLL.

Each WdbgExts extension DLL also exports a number of *callback functions*. These functions are called by the debugger when the DLL is loaded and when extension commands are used.

The debugger engine will place a **try / except** block around a call to an extension DLL. This protects the engine from some types of bugs in the extension code. However, since the extension calls are executed in the same thread as the engine, they can still cause the engine to crash.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20WdbgExts%20Extension%20API%20Overview%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




