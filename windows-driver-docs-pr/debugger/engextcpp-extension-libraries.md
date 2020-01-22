---
title: EngExtCpp Extension Libraries
description: EngExtCpp Extension Libraries
ms.assetid: 8c7ce3f8-46c4-408c-aab5-00d654bddfcd
keywords: ["EngExtCpp extensions, libraries"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# EngExtCpp Extension Libraries


## <span id="ddk_anatomy_of_a_dbgeng_extension_dll_dbx"></span><span id="DDK_ANATOMY_OF_A_DBGENG_EXTENSION_DLL_DBX"></span>


An EngExtCpp extension library is a DLL that uses the EngExtCpp extension framework found in EngExtCpp.h. When this library is loaded by the debugger engine, its methods and functions can provide extra functionality or automation of tasks while performing user-mode or kernel-mode debugging on Microsoft Windows.

The EngExtCpp extension framework is built on top of the [DbgEng extension framework](writing-dbgeng-extension-code.md). It offers the same debugger engine API for interaction with the debugger engine. but it also provides additional features to make common tasks simpler.

If you performed a full install of Debugging Tools for Windows, a sample EngExtCpp extension called "extcpp" can be found in the sdk\\samples\\extcpp subdirectory of the installation directory.

### <span id="ext_class_and_extextension"></span><span id="EXT_CLASS_AND_EXTEXTENSION"></span>EXT\_CLASS and ExtExtension

At the core of an EngExtCpp extension library is a single instance of the [**EXT\_CLASS**](https://docs.microsoft.com/previous-versions/ff544508(v=vs.85)) class. An EngExtCpp extension library will provide the implementation of this class, which contains all the extension commands and methods for formatting structures that are exported by the library.

EXT\_CLASS is a subclass of [**ExtExtension**](https://msdn.microsoft.com/library/windows/hardware/ff543981). The single instance of this class is created using the [**EXT\_DECLARE\_GLOBALS**](https://docs.microsoft.com/previous-versions/ff544527(v=vs.85)) macro which must appear exactly once in the source files for the extension library.

When the extension library is loaded, the [**Initialize**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff550945(v=vs.85)) method of the class is called by the engine, and the [**Uninitialize**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff558961(v=vs.85)) method is called before unloading the class. Additionally, the methods [**OnSessionActive**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff552312(v=vs.85)), [**OnSessionInactive**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff552318(v=vs.85)), [**OnSessionAccessible**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff552310(v=vs.85)), and [**OnSessionInaccessible**](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff552315(v=vs.85)) are called by the engine to notify the extension library of the state of the debugging session.

### <span id="extension_commands"></span><span id="EXTENSION_COMMANDS"></span>Extension Commands

The [**EXT\_CLASS**](https://docs.microsoft.com/previous-versions/ff544508(v=vs.85)) class can contain a number of methods that are used to execute extension commands. Each extension command is declared in the EXT\_CLASS class by using the [**EXT\_COMMAND\_METHOD**](https://docs.microsoft.com/windows-hardware/drivers/ddi/engextcpp/nf-engextcpp-ext_command_method) macro. The implementation of a command is defined by using the [**EXT\_COMMAND**](https://docs.microsoft.com/windows-hardware/drivers/ddi/engextcpp/nf-engextcpp-ext_command) macro.

### <span id="known_structures"></span><span id="KNOWN_STRUCTURES"></span>Known Structures

The [**EXT\_CLASS**](https://docs.microsoft.com/previous-versions/ff544508(v=vs.85)) class can contain a number of methods that use the [*ExtKnownStructMethod*](https://docs.microsoft.com/previous-versions/windows/hardware/previsioning-framework/ff543989(v=vs.85)) prototype. The methods can be used by the engine to format instances of certain structure types for output.

### <span id="provided_values"></span><span id="PROVIDED_VALUES"></span>Provided Values

The [**EXT\_CLASS**](https://docs.microsoft.com/previous-versions/ff544508(v=vs.85)) class can contain a number of methods that use the **ExtProvideValueMethod** prototype. The methods can be used by the engine to evaluate some pseudo-registers provided by the extension.

 

 





