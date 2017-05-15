---
title: EngExtCpp Extension Libraries
description: EngExtCpp Extension Libraries
ms.assetid: 8c7ce3f8-46c4-408c-aab5-00d654bddfcd
keywords: ["EngExtCpp extensions, libraries"]
---

# EngExtCpp Extension Libraries


## <span id="ddk_anatomy_of_a_dbgeng_extension_dll_dbx"></span><span id="DDK_ANATOMY_OF_A_DBGENG_EXTENSION_DLL_DBX"></span>


An EngExtCpp extension library is a DLL that uses the EngExtCpp extension framework found in EngExtCpp.h. When this library is loaded by the debugger engine, its methods and functions can provide extra functionality or automation of tasks while performing user-mode or kernel-mode debugging on Microsoft Windows.

The EngExtCpp extension framework is built on top of the [DbgEng extension framework](writing-dbgeng-extension-code.md). It offers the same debugger engine API for interaction with the debugger engine. but it also provides additional features to make common tasks simpler.

If you performed a full install of Debugging Tools for Windows, a sample EngExtCpp extension called "extcpp" can be found in the sdk\\samples\\extcpp subdirectory of the installation directory.

### <span id="ext_class_and_extextension"></span><span id="EXT_CLASS_AND_EXTEXTENSION"></span>EXT\_CLASS and ExtExtension

At the core of an EngExtCpp extension library is a single instance of the [**EXT\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff544508) class. An EngExtCpp extension library will provide the implementation of this class, which contains all the extension commands and methods for formatting structures that are exported by the library.

EXT\_CLASS is a subclass of [**ExtExtension**](https://msdn.microsoft.com/library/windows/hardware/ff543981). The single instance of this class is created using the [**EXT\_DECLARE\_GLOBALS**](https://msdn.microsoft.com/library/windows/hardware/ff544527) macro which must appear exactly once in the source files for the extension library.

When the extension library is loaded, the [**Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff550945) method of the class is called by the engine, and the [**Uninitialize**](https://msdn.microsoft.com/library/windows/hardware/ff558961) method is called before unloading the class. Additionally, the methods [**OnSessionActive**](https://msdn.microsoft.com/library/windows/hardware/ff552312), [**OnSessionInactive**](https://msdn.microsoft.com/library/windows/hardware/ff552318), [**OnSessionAccessible**](https://msdn.microsoft.com/library/windows/hardware/ff552310), and [**OnSessionInaccessible**](https://msdn.microsoft.com/library/windows/hardware/ff552315) are called by the engine to notify the extension library of the state of the debugging session.

### <span id="extension_commands"></span><span id="EXTENSION_COMMANDS"></span>Extension Commands

The [**EXT\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff544508) class can contain a number of methods that are used to execute extension commands. Each extension command is declared in the EXT\_CLASS class by using the [**EXT\_COMMAND\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff544517) macro. The implementation of a command is defined by using the [**EXT\_COMMAND**](https://msdn.microsoft.com/library/windows/hardware/ff544514) macro.

### <span id="known_structures"></span><span id="KNOWN_STRUCTURES"></span>Known Structures

The [**EXT\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff544508) class can contain a number of methods that use the [*ExtKnownStructMethod*](https://msdn.microsoft.com/library/windows/hardware/ff543989) prototype. The methods can be used by the engine to format instances of certain structure types for output.

### <span id="provided_values"></span><span id="PROVIDED_VALUES"></span>Provided Values

The [**EXT\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff544508) class can contain a number of methods that use the **ExtProvideValueMethod** prototype. The methods can be used by the engine to evaluate some pseudo-registers provided by the extension.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20EngExtCpp%20Extension%20Libraries%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




