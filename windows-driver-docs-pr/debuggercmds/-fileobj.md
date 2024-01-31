---
title: fileobj (WinDbg)
description: The fileobj extension displays detailed information about a FILE_OBJECT structure.
keywords: ["FILE_OBJECT", "fileobj Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- fileobj
api_type:
- NA
---

# !fileobj


The **!fileobj** extension displays detailed information about a FILE\_OBJECT structure.

```dbgcmd
!fileobj FileObject
```

## Parameters


<span id="_______FileObject______"></span><span id="_______fileobject______"></span><span id="_______FILEOBJECT______"></span> *FileObject*   
Specifies the address of a [FILE_OBJECT](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object) structure.

## DLL

Windows XP and later - Kdexts.dll

 

### Additional Information

For information about file objects, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

If the FILE\_OBJECT structure has an associated cache, **!fileobj** tries to parse and display cache information..

 

