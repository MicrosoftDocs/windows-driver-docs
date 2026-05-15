---
title: 'WinDbg: Settings, Workspaces, and Saved Debug Sessions'
description: "This article describes how to set up and configure WinDbg settings, workspaces, and saved debug sessions."
keywords: ["Settings", "Workspaces", "Debug sessions", "WinDbg", "Menu", "Windows Debugging"]
ms.date: 02/28/2026
ai-usage: ai-assisted
ms.topic: how-to
---

# WinDbg: Settings, workspaces, and saved debug sessions

:::image type="content" source="images/windbgx-preview-logo.png" alt-text="WinDbg logo with a magnifying glass inspecting bits.":::

This article describes how to set up and configure WinDbg.

WinDbg uses two types of configuration files:

- **Workspaces** store your WinDbg settings, such as theme, window layout, symbol paths, source paths, and other configuration options. Workspace files use the `.xml` extension and are stored by default in `%LOCALAPPDATA%\DBG\Workspaces`. Settings are automatically saved to the default workspace file (`%LOCALAPPDATA%\DBG\DbgX.xml`) when you close WinDbg.

- **Saved debug sessions** store target connection information (such as which dump file to open or which process to attach to) along with per-session engine options. Debug session files use the `.debugtarget` extension and are stored by default in `%LOCALAPPDATA%\DBG\Targets`. These files appear in the **Recent** targets list on the **Start debugging** page.

## Settings

Use the **Settings** menu to set items such as the source and symbol path. You can also choose the theme for WinDbg. The available theme modes are:

- **System** - Follows the Windows system theme setting (default).
- **Light** - Uses the light theme.
- **Dark** - Uses the dark theme.

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

Workspaces save your WinDbg settings, such as theme, window layout, symbol paths, source paths, and other configuration options, to a file.

### Saving and loading workspaces

You can manage workspaces through the **File** menu:

- **Save workspace** - Saves the current settings to the active workspace file.
- **Save workspace as** - Saves the current settings to a new workspace file.
- **Open workspace** - Loads settings from a previously saved workspace file.

Settings are also automatically saved when you close the debugger, unless automatic saving has been disabled with the `-Q` command-line option.

### Workspace command-line options

You can use the following command-line options to control workspace behavior:

- `-Q` - Disables automatic saving of settings. Settings changes are only persisted when you explicitly select **Save workspace** or **Save workspace as** from the **File** menu.
- `-WF SettingsFile` - Loads settings from the specified workspace file at startup.

## Saved debug sessions

Saved debug sessions store your target connection information along with per-session engine options. Debug session files use the `.debugtarget` extension and are stored by default in `%LOCALAPPDATA%\DBG\Targets`.

### Saving and loading debug sessions

You can manage debug sessions through the **File** menu and command line:

- **Save debug session** - Saves the current target connection information to a `.debugtarget` file. This option is only available when a debug target is active.
- **Recent targets** - On the **Start debugging** page, select a previously saved debug session from the **Recent** targets list to reload it.
- `-loadSession` - Loads a saved debug session configuration file from the command line.

### Debug session settings

In addition to the target connection information, the following settings are stored in the saved debug session file (`.debugtarget` file extension).

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

#### Debug session XML file

Debug session target connection information is stored in XML format with the `.debugtarget` file extension.

The following file shows an example debug session configuration file.

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
