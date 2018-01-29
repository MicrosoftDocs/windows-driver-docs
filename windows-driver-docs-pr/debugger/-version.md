---
title: version
description: The version extension displays the version information for the extension DLL.This extension command should not be confused with the version (Show Debugger Version) command.
ms.assetid: b6ca4b8c-d673-40c5-890f-3b92fbb99fae
keywords: ["version Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- version
api_type:
- NA
---

# !version


The **!version** extension displays the version information for the extension DLL.

This extension command should not be confused with the [**version (Show Debugger Version)**](version--show-debugger-version-.md) command.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!version%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




