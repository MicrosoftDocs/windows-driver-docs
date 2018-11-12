---
title: Debugger Engine and Extension APIs
description: Debugger Engine and Extension APIs
ms.assetid: 2d651c4b-e123-4285-b69c-d7fd5e1f9a81
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Debugger Engine and Extension APIs


This section includes:

[Debugger Engine Overview](debugger-engine-overview.md)

[Using the Debugger Engine API](using-the-debugger-engine-api.md)

[Writing DbgEng Extensions](writing-dbgeng-extensions.md)

[EngExtCpp Extensions](engextcpp-extensions.md)

[Writing WdbgExts Extensions](writing-wdbgexts-extensions.md)

[Customizing Debugger Output Using DML](#dml)

[Using JavaScript to Extend the Capabilities of the Debugger](#javascript)

## <span id="ddk_introduction_dbx"></span><span id="DDK_INTRODUCTION_DBX"></span>


This documentation describes how to use the debugger engine and how to write extensions that will run in WinDbg, KD, CDB, and NTSD. These debugger extensions can be used when performing user-mode or kernel-mode debugging on Microsoft Windows.

### <span id="debugger_engine"></span><span id="DEBUGGER_ENGINE"></span>Debugger Engine

The debugger engine provides an interface for examining and manipulating debugging targets in user-mode and kernel-mode on Microsoft Windows.

The debugger engine can acquire targets, set breakpoints, monitor events, query symbols, read and write memory, and control threads and processes in a target.

You can use the debugger engine to write both debugger extension libraries and stand-alone applications. Such applications are *debugger engine applications*. A debugger engine application that uses the full functionality of the debugger engine is a *debugger*. For example, WinDbg, CDB, NTSD, and KD are debuggers; the debugger engine provides the core of their functionality.

The debugger engine API is specified by the prototypes in the header file dbgeng.h.

For more information, see [Debugger Engine Overview](debugger-engine-overview.md) and [Using the Debugger Engine API](using-the-debugger-engine-api.md).

.

### <span id="extensions"></span><span id="EXTENSIONS"></span>Extensions

You can create your own debugging commands by writing and building an extension DLL. For example, you might want to write an extension command to display a complex data structure.

There are three different types of debugger extension DLLs:

-   *DbgEng extension DLLs*. These are based on the prototypes in the dbgeng.h header file. Each DLL of this type may export DbgEng extension commands. These extension commands use the Debugger Engine API and may also use the WdbgExts API.

    For more information, see [Writing DbgEng Extensions](writing-dbgeng-extensions.md).

-   *EngExtCpp extension DLLs*. These are based on the prototypes in the engextcpp.h and dbgeng.h header files. Each DLL of this type may export DbgEng extension commands. These extension commands use both the Debugger Engine API and the EngExtCpp extension framework, and may also use the WdbgExts API.

-   *WdbgExts extension DLLs*. These are based on the prototypes in the wdbgexts.h header file. Each DLL of this type exports one or more WdbgExts extension commands. These extension commands use the WdbgExts API exclusively. For more information see [Writing WdbgExts Extensions](writing-wdbgexts-extensions.md).

The DbgEng API can be used to create extensions or stand-alone applications. The WdbgExts API contains a subset of the functionality of the debugger engine API and can be used only by extensions.

All debugger extensions should be compiled and built using Visual Studio.

Extension code samples are installed as part of the Debugging Tools for Windows package if you perform a custom installation and select the **SDK** component and all its subcomponents. They can be found in the sdk\\samples subdirectory of the Debugging Tools for Windows installation directory.

The easiest way to write new debugger extensions is to study the sample extensions. Each sample extension includes makefile and sources files for use with the Build utility. Both types of extensions are represented in the samples.

## <span id="Analysis"></span><span id="analysis"></span><span id="ANALYSIS"></span>Writing Custom Analysis Debugger Extensions


You can extend the capabilities of the [**!analyze**](-analyze.md) debugger command by writing an analysis extension plugin. By providing an analysis extension plugin, you can participate in the analysis of a bug check or an exception in a way that is specific to your own component or application. When you write an analysis extension plugin, you also write a metadata file that describes the situations for which you want your plugin to be called. When **!analyze** runs, it locates, loads, and runs the appropriate analysis extension plugins. For more information, see [Writing Custom Analysis Debugger Extensions](writing-custom-analysis-debugger-extensions.md)

## <span id="DML"></span><span id="dml"></span>Customizing Debugger Output Using DML


You can customize debugger output using DML. For more information see [Customizing Debugger Output Using DML](customizing-debugger-output-using-dml.md).

## <span id="JavaScript"></span><span id="javascript"></span><span id="JAVASCRIPT"></span>Using JavaScript to Extend the Capabilities of the Debugger


Use JavaScript to create scripts that understand debugger objects and extend and customize the capabilities of the debugger. JavaScript providers bridge a scripting language to the debugger's internal object model. The JavaScript debugger scripting provider, allows the for use of JavaScript with the debugger. For more information, see [JavaScript Debugger Scripting](javascript-debugger-scripting.md).

 

 





