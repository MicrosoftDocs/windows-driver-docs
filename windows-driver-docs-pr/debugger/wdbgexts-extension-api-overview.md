---
title: WdbgExts Extension API Overview
description: WdbgExts Extension API Overview
ms.assetid: e54d330f-ab48-407f-a9f2-e4a521f5e27b
keywords: ["WdbgExts extensions, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# WdbgExts Extension API Overview


## <span id="ddk_wdbgexts_extension_api_overview_dbwx"></span><span id="DDK_WDBGEXTS_EXTENSION_API_OVERVIEW_DBWX"></span>


Each WdbgExts extension DLL exports one or more functions that are used to implement *extension commands*. These functions are named according to the standard C convention, except that upper-case letters are not permitted.

The function name and the extension command name are identical, except that the extension command begins with an exclamation point ( **!** ). For example, when you load Myextension.dll into the debugger and then type **!stack** into the Debugger Command window, the debugger looks for an exported function named **stack** in Myextension.dll.

If Myextension.dll is not already loaded, or if there are other extension commands with the same name in other extension DLLs, you can type **!myextension.stack** into the Debugger Command window to indicate the extension DLL and the extension command in that DLL.

Each WdbgExts extension DLL also exports a number of *callback functions*. These functions are called by the debugger when the DLL is loaded and when extension commands are used.

The debugger engine will place a **try / except** block around a call to an extension DLL. This protects the engine from some types of bugs in the extension code. However, since the extension calls are executed in the same thread as the engine, they can still cause the engine to crash.

 

 





