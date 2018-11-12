---
title: version
description: The version extension displays the version information for the extension DLL.This extension command should not be confused with the version (Show Debugger Version) command.
ms.assetid: b6ca4b8c-d673-40c5-890f-3b92fbb99fae
keywords: ["version Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- version
api_type:
- NA
ms.localizationpriority: medium
---

# !version


The **!version** extension displays the version information for the extension DLL.

This extension command should not be confused with the [**version (Show Debugger Version)**](version--show-debugger-version-.md) command.

```dbgcmd
![ExtensionDLL.]version
```

## <span id="ddk__version_dbg"></span><span id="DDK__VERSION_DBG"></span>Parameters


<span id="_______ExtensionDLL______"></span><span id="_______extensiondll______"></span><span id="_______EXTENSIONDLL______"></span> *ExtensionDLL*   
Specifies the extension DLL whose version number is to be displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension is available in most extension DLLs.

Remarks
-------

If the extension DLL version does not match the debugger version, error messages will be displayed.

This extension command will not work on Windows XP and later versions of Windows. To display version information, use the [**version (Show Debugger Version)**](version--show-debugger-version-.md) command.

The original purpose of this extension was to ensure that the DLL version matched the target version, since a mismatch would result in inaccurate results for many extensions. Newer DLLs are no longer restricted to working with only one version of Windows, so this extension is obsolete.

 

 





