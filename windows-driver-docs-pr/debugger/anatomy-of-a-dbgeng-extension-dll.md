---
title: Anatomy of a DbgEng Extension DLL
description: Anatomy of a DbgEng Extension DLL
ms.assetid: 5131115b-b9a0-479b-9391-7ab384633d92
keywords: ["DbgEng Extensions, DLL anatomy"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Anatomy of a DbgEng Extension DLL


## <span id="ddk_anatomy_of_a_dbgeng_extension_dll_dbx"></span><span id="DDK_ANATOMY_OF_A_DBGENG_EXTENSION_DLL_DBX"></span>


A DbgEng extension DLL exports a number of callback functions, some of which may be implementations of extension commands.

These extension DLLs are loaded by the [debugger engine](introduction.md#debugger-engine) and can provide extra functionality or automation of tasks while performing user-mode or kernel-mode debugging on Microsoft Windows.

If you performed a full install of Debugging Tools for Windows, a sample DbgEng extension called "exts" can be found in the sdk\\samples\\exts subdirectory of the installation directory.

### <span id="extension_commands"></span><span id="EXTENSION_COMMANDS"></span>Extension Commands

An extension DLL may export any number of functions that are used to execute extension commands. Each function is explicitly declared as an export in the .def file, and its name must consist entirely of lowercase letters.

Functions used to implement extension commands must match the prototype [**PDEBUG\_EXTENSION\_CALL**](https://msdn.microsoft.com/library/windows/hardware/ff553378).

These functions are named according to the standard C++ convention, except that uppercase letters are not permitted. The exported function name and the extension command name are identical, except that the extension command begins with an exclamation point (!). For example, when you load myextension.dll into the debugger and then type **!stack** into the Debugger Command window, the debugger looks for an exported function named **stack** in myextension.dll.

If myextension.dll is not already loaded, or if there may be other extension commands with the same name in other extension DLLs, you can type **!myextension.stack** into the Debugger Command window to indicate the extension DLL and the extension command in that DLL.

### <span id="other_exported_functions"></span><span id="OTHER_EXPORTED_FUNCTIONS"></span>Other Exported Functions

A DbgEng extension DLL must export [*DebugExtensionInitialize*](https://msdn.microsoft.com/library/windows/hardware/ff540476). This will be called when the DLL is loaded, to initialize the DLL. It may be used by the DLL to initialize global variables.

An extension DLL may export [*DebugExtensionUninitialize*](https://msdn.microsoft.com/library/windows/hardware/ff540495). If this is exported, it will be called before the extension DLL is unloaded. It may be used by the DLL to clean up before it is unloaded.

An extension DLL may export [*DebugExtensionNotify*](https://msdn.microsoft.com/library/windows/hardware/ff540478). If this is exported, it will be called when a session begins or ends, and when a target starts or stops executing. These notifications are also provided to [IDebugEventCallbacks](https://msdn.microsoft.com/library/windows/hardware/ff550550) objects registered with a client.

An extension DLL may export [*KnownStructOutput*](https://msdn.microsoft.com/library/windows/hardware/ff551934). If this is exported, it will be called when the DLL is loaded. This function returns a list of structures that the DLL knows how to print on a single line. It may be called later to format instances of these structures for printing.

### <span id="engine_procedure_for_loading_a_dbgeng_extension_dll"></span><span id="ENGINE_PROCEDURE_FOR_LOADING_A_DBGENG_EXTENSION_DLL"></span>Engine Procedure for Loading a DbgEng Extension DLL

When an extension DLL is loaded, the callback functions are called by the engine in the following order:

1.  **DebugExtensionInitialize** is called so the extension DLL can initialize.

2.  If exported, **DebugExtensionNotify** is called if the engine has an active session, and called again if the session is suspended and accessible.

3.  If exported, **KnownStructOutput** is called to request a list of structures the DLL knows how to print on a single line.

See [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md) for information about how to use the debugger to load and unload an extension DLL, and see [Using Debugger Extension Commands](using-debugger-extension-commands.md) for information about executing an extension command.

The debugger engine will place a **try / except** block around a call to an extension DLL. This protects the engine from some types of bugs in the extension code; but, since the extension calls are executed in the same thread as the engine, they can still cause it to crash.

 

 





