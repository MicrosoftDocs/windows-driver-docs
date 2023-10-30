---
title: filelock (WinDbg)
description: The filelock extension displays a file lock structure.
keywords: ["filelock Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- filelock
api_type:
- NA
---

# !filelock


The **!filelock** extension displays a file lock structure.

Syntax

```dbgcmd
!filelock FileLockAddress 
!filelock ObjectAddress 
```

## <span id="ddk__filelock_dbg"></span><span id="DDK__FILELOCK_DBG"></span>Parameters


<span id="_______FileLockAddress______"></span><span id="_______filelockaddress______"></span><span id="_______FILELOCKADDRESS______"></span> *FileLockAddress*   
Specifies the hexadecimal address of the file lock structure.

<span id="_______ObjectAddress______"></span><span id="_______objectaddress______"></span><span id="_______OBJECTADDRESS______"></span> *ObjectAddress*   
Specifies the hexadecimal address of a file object that owns the file lock.

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll

### Additional Information

For information about file objects, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

 

 





