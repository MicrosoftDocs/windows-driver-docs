---
title: EngExtCpp Extension Libraries
description: EngExtCpp Extension Libraries
keywords: ["EngExtCpp extensions, libraries"]
ms.date: 05/23/2017
---

# EngExtCpp Extension Libraries


## <span id="ddk_anatomy_of_a_dbgeng_extension_dll_dbx"></span><span id="DDK_ANATOMY_OF_A_DBGENG_EXTENSION_DLL_DBX"></span>


An EngExtCpp extension library is a DLL that uses the EngExtCpp extension framework found in EngExtCpp.h. When this library is loaded by the debugger engine, its methods and functions can provide extra functionality or automation of tasks while performing user-mode or kernel-mode debugging on Microsoft Windows.

The EngExtCpp extension framework is built on top of the [DbgEng extension framework](writing-dbgeng-extension-code.md). It offers the same debugger engine API for interaction with the debugger engine. but it also provides additional features to make common tasks simpler.

If you performed a full install of Debugging Tools for Windows, a sample EngExtCpp extension called "extcpp" can be found in the sdk\\samples\\extcpp subdirectory of the installation directory.

### <span id="ext_class_and_extextension"></span><span id="EXT_CLASS_AND_EXTEXTENSION"></span>EXT\_CLASS and ExtExtension

At the core of an EngExtCpp extension library is a single instance of the [**EXT\_CLASS**](/previous-versions/ff544508(v=vs.85)) class. An EngExtCpp extension library will provide the implementation of this class, which contains all the extension commands and methods for formatting structures that are exported by the library.

EXT\_CLASS is a subclass of [**ExtExtension**](/previous-versions/ff543981(v=vs.85)). The single instance of this class is created using the [**EXT\_DECLARE\_GLOBALS**](/previous-versions/ff544527(v=vs.85)) macro which must appear exactly once in the source files for the extension library.

When the extension library is loaded, the [**Initialize**](/previous-versions/windows/hardware/previsioning-framework/ff550945(v=vs.85)) method of the class is called by the engine, and the [**Uninitialize**](/previous-versions/windows/hardware/previsioning-framework/ff558961(v=vs.85)) method is called before unloading the class. Additionally, the methods [**OnSessionActive**](/previous-versions/windows/hardware/previsioning-framework/ff552312(v=vs.85)), [**OnSessionInactive**](/previous-versions/windows/hardware/previsioning-framework/ff552318(v=vs.85)), [**OnSessionAccessible**](/previous-versions/windows/hardware/previsioning-framework/ff552310(v=vs.85)), and [**OnSessionInaccessible**](/previous-versions/windows/hardware/previsioning-framework/ff552315(v=vs.85)) are called by the engine to notify the extension library of the state of the debugging session.

### <span id="extension_commands"></span><span id="EXTENSION_COMMANDS"></span>Extension Commands

The [**EXT\_CLASS**](/previous-versions/ff544508(v=vs.85)) class can contain a number of methods that are used to execute extension commands. Each extension command is declared in the EXT\_CLASS class by using the [**EXT\_COMMAND\_METHOD**](/windows-hardware/drivers/ddi/engextcpp/nf-engextcpp-ext_command_method) macro. The implementation of a command is defined by using the [**EXT\_COMMAND**](/windows-hardware/drivers/ddi/engextcpp/nf-engextcpp-ext_command) macro.

### <span id="known_structures"></span><span id="KNOWN_STRUCTURES"></span>Known Structures

The [**EXT\_CLASS**](/previous-versions/ff544508(v=vs.85)) class can contain a number of methods that use the [*ExtKnownStructMethod*](/previous-versions/windows/hardware/previsioning-framework/ff543989(v=vs.85)) prototype. The methods can be used by the engine to format instances of certain structure types for output.

### <span id="provided_values"></span><span id="PROVIDED_VALUES"></span>Provided Values

The [**EXT\_CLASS**](/previous-versions/ff544508(v=vs.85)) class can contain a number of methods that use the **ExtProvideValueMethod** prototype. The methods can be used by the engine to evaluate some pseudo-registers provided by the extension.

 

