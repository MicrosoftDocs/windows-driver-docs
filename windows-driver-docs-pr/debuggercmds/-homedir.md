---
title: "!homedir (WinDbg)"
description: "The !homedir extension sets the default directory used by the symbol server and the source server."
keywords: ["!homedir Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- homedir
api_type:
- NA
---

# !homedir

The **!homedir** extension sets the default directory used by the symbol server and the source server.

```dbgcmd
!homedir Directory
!homedir
```

## Parameters

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies the new directory to use as the home directory.

## DLL

Dbghelp.dll

## Remarks

If the **!homedir** extension is used with no argument, the current home directory is displayed.

The cache for a source server is located in the src subdirectory of the home directory. The downstream store for a symbol server defaults to the sym subdirectory of the home directory, unless a different location is specified.

When WinDbg is started, the home directory is the directory where Debugging Tools for Windows was installed. The **!homedir** extension can be used to change this value.
