---
title: Building EngExtCpp Extensions
description: Building EngExtCpp Extensions
ms.assetid: 63d73c4e-03b8-4bbe-9c2e-96cda3ad544c
keywords: ["EngExtCpp extensions, building"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Building%20EngExtCpp%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




