---
title: Building EngExtCpp Extensions
description: Building EngExtCpp Extensions
ms.assetid: 63d73c4e-03b8-4bbe-9c2e-96cda3ad544c
keywords: ["EngExtCpp extensions, building"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Building EngExtCpp Extensions


## <span id="ddk_building_dbgeng_extensions_dbx"></span><span id="DDK_BUILDING_DBGENG_EXTENSIONS_DBX"></span>


The EngExtCpp extension libraries are built almost the same way as the DbgEng extension libraries. For more information, see [Building DbgEng Extensions](building-dbgeng-extensions.md).

The EngExtCpp implementation code (engextcpp.cpp) is used instead of linking with a static library.

Because the EngExtCpp extension framework is built on top of the DbgEng extension framework, an EngExtCpp extension DLL should export the same functions as a DbgEng extension DLL.

Each extension should be exported. When you use the [**EXT\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff544514) macro to define an extension function, this macro also creates a C function with the same name as the extension. This function should be exported from the DLL.

The following functions are provided by engextcpp should be exported from the EngExtCpp DLL.

-   **DebugExtensionInitialize** -- so that the [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff548226) method can be called to initialize the library.

-   **DebugExtensionUnitialize** -- so that the [**Uninitialize**](https://msdn.microsoft.com/library/windows/hardware/ff548226) method can be called to uninitialize the library.

-   **KnownStructOutputEx** -- so that the engine can call the [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) methods to format known structures for output.

-   **DebugExtensionNotify** -- so that the engine can call the [**OnSessionActive**](https://msdn.microsoft.com/library/windows/hardware/ff548226), **OnSessionInactive**, **OnSessionAccessible**, and **OnSessionInaccessible** methods to notify the extension library of changes to the debugging session's state.

-   **help** -- so that the EngExtCpp extension framework can automatically provide a **!help** extension.

These functions can be exported even if the functionality they provide is not needed. Moreover, if they are not exported, the functionality they provide will be lost.

**DebugExtensionInitialize** must be exported in order for the debugger engine to recognize the DLL as a valid DbgEng extension DLL.

 

 





