---
title: .settings (Set Debug Settings)
description: The .settings command sets, modifies, displays, loads and saves settings in the Debugger.Settings namespace.
ms.assetid: DAD68FA5-21EF-4A5C-8E5E-0C763CD28C44
keywords: [".settings (Set Debug Settings) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .settings (Set Debug Settings)
api_type:
- NA
---

# .settings (Set Debug Settings)


The **.settings** command sets, modifies, displays, loads and saves settings in the Debugger.Settings namespace.

```
.settings set  namespace.setting=value
.settings set namespace.setting+=value 
.settings save [file path] 
.settings load file path
.settings list [namespace][-v]
.settings help   
```

## <span id="ddk_meta_set_symbol_path_dbg"></span><span id="DDK_META_SET_SYMBOL_PATH_DBG"></span>Parameters


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

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

On launch, the debugger will load all the settings from config.xml in the directory the debugger executable is in. Throughout your debugging session you can modify settings using the previous settings command (like .sympath or .prefer\_dml) or the new .settings commands. You can use ‘.settings save’ to save your settings to your settings configuration file. You can use the following command to enable AutoSave.

`.settings set AutoSaveSettings=true`

When auto save is enabled, the settings in the Debugger.Settings namespace will be automatically saved when exiting the debugger.

Remarks
-------

You can exchange debug xml settings files with others to duplicate their debug settings.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.settings%20%28Set%20Debug%20Settings%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




