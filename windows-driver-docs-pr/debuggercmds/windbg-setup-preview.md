---
title: 'WinDbg: Settings and Workspaces'
description: "This article describes how to set up the WinDbg debugger."
keywords: ["Settings and workspaces", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 01/16/2020
ms.topic: how-to
---

# WinDbg: Settings and workspaces

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to set up and configure WinDbg.

## Settings

Use the **Settings** menu to set items such as the source and symbol path. You can also choose the light or dark theme for WinDbg.

:::image type="content" source="images/windbgx-settings-menu.png" alt-text="Screenshot of the WinDbg Settings menu displaying the General tab.":::

There are currently six **Settings** dialogs:

- **General**
- **Command window**
- **Debugging settings**
- **Disassembly windows**
- **Events & exceptions**
- **Source window**

For more information on setting the paths, see [Symbol path for Windows debugger](../debugger/symbol-path.md) and [Source code debugging in WinDbg (Classic)](../debugger/source-window.md).

## Workspaces

With workspaces, you can save configuration information in the target connection information file.

The options in workspaces are saved when you close the debugger. To save them manually, select **File** > **Save Workspace**.

Workspaces are automatically loaded if you open them from the recent targets list. You can also load them manually on the **File** menu.

In addition to the target connection information, the following settings are stored in the workspace file.

#### General settings

> [!NOTE]
> This list and format isn't final and is subject to change.

Setting | Default | Description
--- | --- | ---
`FinalBreak` |`true` | If `true`, ignores the final breakpoint (`-g` command-line option).
`SourceDebugging` |`true`  | Toggles between source or assembly mode.
`DebugChildProcesses` | `false`| (User mode only.) If `true`, debugs child processes started by the target application (`-o` command-line option).
`Noninvasive` | `false`  |  Specifies noninvasive attach (`-pv` command-line option).
`NoDebugHeap` | `false`  |  Specifies the debug heap shouldn't be used (`-hd` command-line option).
`Verbose` | `false`  | When verbose mode is turned on, produces more detailed output (`-v` command-line option) for some display commands (such as register dumping).
`Elevate` | - |  Used internally by WinDbg. Do not modify.
`Restartable` | - |  Used internally by WinDbg. Do not modify.
`UseImplicitCommandLine` | `false` | Uses implicit command line (`-cimp` command-line option). This setting starts the debugger with an implicit command line instead of an explicit process to run.

For more information about the command-line options, see [WinDbg command-line options](../debugger/windbg-command-line-options.md).

#### Symbol settings

Setting | Default | Description
--- | --- | ---
`SymbolOptionsOverride` | `0` | This explicit symbol option mask is in the form of a single hex number.
`ShouldOverrideSymbolOptions` | `false` | If set to `true`, overrides all the symbol options listed in this table with the provided symbol option mask, which is described in the preceding table.
`SymOptExactSymbols` | `false` | This option causes the debugger to perform a strict evaluation of all symbol files.
`SymOptFailCriticalErrors` | `false` | This symbol option causes file access error dialog boxes to be suppressed.
`SymOptIgnoreCvRec` | `false` | This option causes the symbol handler to ignore the CV record in the loaded image header when searching for symbols.
`SymOptIgnoreNtSympath` | `false` | This option causes the debugger to ignore the environment variable settings for the symbol path and the executable image path.
`SymOptNoCpp` | `false` | This symbol option turns off C++ translation. When this symbol option is set, `__` replaces `::` in all symbols.
`SymOptNoUnqualifiedLoads` | `false` | This symbol option disables the symbol handler's automatic loading of modules. When this option is set, the debugger attempts to match a symbol. It searches only modules that were already loaded.
`SymOptAutoPublics` | `false` | This symbol option causes DbgHelp to search the public symbol table in a .pdb file only as a last resort. If any matches are found when searching the private symbol data, the public symbols aren't searched. This setting improves symbol search speed.
`SymOptDebug` | `false` | This symbol option turns on noisy symbol loading. This setting instructs the debugger to display information about its search for symbols.

For more information on symbol options, see [Symbol options](../debugger/symbol-options.md).

#### Window layout settings

 Window layout settings are saved globally and aren't saved in the workspace file.

#### Workspace XML file

The workspace and target connection information is stored in XML format.

The following file shows an example workspace configuration file.

```xml
<?xml version="1.0" encoding="utf-8"?>
<TargetConfig Name="C:\paint.dmp" LastUsed="2017-08-03T21:34:20.1013837Z">
  <EngineConfig />
  <EngineOptions>
    <Property name="FinalBreak" value="true" />
    <Property name="SourceDebugging" value="true" />
    <Property name="DebugChildProcesses" value="false" />
    <Property name="Noninvasive" value="false" />
    <Property name="NoDebugHeap" value="false" />
    <Property name="Verbose" value="false" />
    <Property name="SymbolOptionsOverride" value="0" />
    <Property name="ShouldOverrideSymbolOptions" value="false" />
    <Property name="SymOptExactSymbols" value="false" />
    <Property name="SymOptFailCriticalErrors" value="false" />
    <Property name="SymOptIgnoreCvRec" value="false" />
    <Property name="SymOptIgnoreNtSympath" value="false" />
    <Property name="SymOptNoCpp" value="false" />
    <Property name="SymOptNoUnqualifiedLoads" value="false" />
    <Property name="SymOptAutoPublics" value="false" />
    <Property name="SymOptDebug" value="false" />
    <Property name="Elevate" value="false" />
    <Property name="Restartable" value="true" />
    <Property name="UseImplicitCommandLine" value="false" />
  </EngineOptions>
  <TargetOptions>
    <Option name="OpenDump">
      <Property name="DumpPath" value="C:\paint.dmp" />
    </Option>
  </TargetOptions>
</TargetConfig>
```

This file format continues to evolve as more features are added to WinDbg.

---

## Related content

- [WinDbg features](../debugger/debugging-using-windbg-preview.md)
