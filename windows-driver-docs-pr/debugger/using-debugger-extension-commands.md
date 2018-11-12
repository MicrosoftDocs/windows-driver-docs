---
title: Using Debugger Extension Commands
description: Using Debugger Extension Commands
ms.assetid: 1db9a835-accb-41b9-9ab1-c4c9f0596aa5
keywords: ["extension commands ( commands), using", "extension commands ( commands), default search order"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Debugger Extension Commands


## <span id="ddk_using_debugger_extension_commands_dbg"></span><span id="DDK_USING_DEBUGGER_EXTENSION_COMMANDS_DBG"></span>


The use of debugger extension commands is very similar to the use of [debugger commands](using-debugger-commands.md). The command is typed in the Debugger Command window, producing either output in this window or a change in the target application or target computer.

An actual debugger extension command is an entry point in a DLL called by the debugger.

Debugger extensions are invoked by the following syntax:

**!\[**<em>module</em>**.\]**<em>extension</em> **\[**<em>arguments</em>**\]**

The module name should not be followed with the .dll file name extension. If *module* includes a full path, the default string size limit is 255 characters.

If the module has not already been loaded, it will be loaded into the debugger using a call to **LoadLibrary**(*module*). After the debugger has loaded the extension library, it calls the **GetProcAddress** function to locate the extension name in the extension module. The extension name is case-sensitive and must be entered exactly as it appears in the extension module's .def file. If the extension address is found, the extension is called.

### <span id="search_order"></span><span id="SEARCH_ORDER"></span>Search Order

If the module name is not specified, the debugger will search the loaded extension modules for this export.

The default search order is as follows:

1.  The extension modules that work with all operating systems and in both modes: Dbghelp.dll and winext\\ext.dll.

2.  The extension module that works in all modes but is operating-system-specific. For Windows XP and later versions of Windows, this is winxp\\exts.dll. There is no corresponding module for Windows 2000.

3.  The extension module that works with all operating systems but is mode-specific. For kernel mode, this is winext\\kext.dll. For user mode, this is winext\\uext.dll.

4.  The extension module that is both operating-system-specific and mode-specific. The following table specifies this module.

    <table>
    <colgroup>
    <col width="33%" />
    <col width="33%" />
    <col width="33%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Windows Build</th>
    <th align="left">User Mode</th>
    <th align="left">Kernel Mode</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>Windows 2000 (free build)</p></td>
    <td align="left"><p>w2kfre \ ntsdexts.dll</p></td>
    <td align="left"><p>w2kfre \ kdextx86.dll</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>Windows 2000 (checked build)</p></td>
    <td align="left"><p>w2kchk \ ntsdexts.dll</p></td>
    <td align="left"><p>w2kchk \ kdextx86.dll</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>Windows XP and later</p></td>
    <td align="left"><p>winxp \ ntsdexts.dll</p></td>
    <td align="left"><p>winxp \ kdexts.dll</p></td>
    </tr>
    </tbody>
    </table>

     

When an extension module is unloaded, it is removed from the search chain. When an extension module is loaded, it is added to the beginning of the search order. The [**.setdll (Set Default Extension DLL)**](-setdll--set-default-extension-dll-.md) command can be used to promote any module to the top of the search chain. By using this command repeatedly, you can completely control the search chain.

Use the [**.chain (List Debugger Extensions)**](-chain--list-debugger-extensions-.md) command to display a list of all loaded extension modules in their current search order.

If you attempt to execute an extension command that is not in any of the loaded extension modules, you will get an Export Not Found error message.

 

 





