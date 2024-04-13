---
title: ".settings (Set Debug Settings)"
description: "The .settings command sets, modifies, displays, loads and saves settings in the Debugger.Settings namespace."
keywords: [".settings (Set Debug Settings) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .settings (Set Debug Settings)
api_type:
- NA
---

# .settings (Set Debug Settings)

The **.settings** command sets, modifies, displays, loads and saves settings in the Debugger.Settings namespace.

```dbgcmd
.settings set  namespace.setting=value
.settings set namespace.setting+=value 
.settings save [file path] 
.settings load file path
.settings list [namespace][-v]
.settings help   
```

## Parameters

**.settings set parameters**

<span id="_______NAMESPACE.SETTING_VALUE______"></span> **namespace.setting=value**   
Sets or modifies a setting. When specifying file paths use slash escaping, for example C:\\\\Symbols\\\\.

Examples:

`.settings set Display.PreferDMLOutput=false`

`.settings set Sources.DisplaySourceLines=true`

`.settings set Symbols.Sympath="C:\\Symbols\\"`

<span id="_______NAMESPACE.SETTING__VALUE______"></span> **namespace.setting+=value**   
Specifies that the new value will be appended to (rather than replace) the previous value.

Example:

`.settings set Extensions.ExtensionSearchPath+=";C:\\MyExtension\\"`

**.setting save parameters**

<span id="_______file_path______"></span><span id="_______FILE_PATH______"></span> **file path**   
Saves all of the values in the Debugger.Settings namespace to the specified XML file.

<span id="_______none______"></span><span id="_______NONE______"></span> **none**   
If a file path is not provided, the settings will be saved to the last file that was loaded or saved to. If a previous file does not exist, a file named config.xml will be created in the directory that the debugger executable was loaded from.

**.setting load parameters**

<span id="_______file_path______"></span><span id="_______FILE_PATH______"></span> **file path**   
Loads all the settings from an XML settings file. Loading settings will change only the settings that are defined in that file. Any previously loaded or changed settings that do not appear in that file will not be modified. This file will be treated as your default save path until the next save or load operation.

**.setting list parameters**

<span id="_______namespace______"></span><span id="_______NAMESPACE______"></span> **namespace**   
List all settings in the given namespace and their values.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
The –v flag causes a description of the setting to be displayed.

**.setting help parameters**

<span id="_______None______"></span><span id="_______none______"></span><span id="_______NONE______"></span> **None**   
Lists all of the settings in the Debugger namespace and their description.

<span id="_______Namespace______"></span><span id="_______namespace______"></span><span id="_______NAMESPACE______"></span> **Namespace**   
Lists all settings in the given namespace and their description.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

On launch, the debugger will load all the settings from config.xml in the directory the debugger executable is in. Throughout your debugging session you can modify settings using the previous settings command (like .sympath or .prefer\_dml) or the new .settings commands. You can use ‘.settings save’ to save your settings to your settings configuration file. You can use the following command to enable AutoSave.

`.settings set AutoSaveSettings=true`

When auto save is enabled, the settings in the Debugger.Settings namespace will be automatically saved when exiting the debugger.

## Remarks

You can exchange debug xml settings files with others to duplicate their debug settings.
