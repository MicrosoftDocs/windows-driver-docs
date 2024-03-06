---
title: finddata (WinDbg)
description: The finddata extension displays the cached data at a given offset within a specified file object.
keywords: ["cache manager", "finddata Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- finddata
api_type:
- NA
---

# !finddata


The **!finddata** extension displays the cached data at a given offset within a specified file object.

```dbgcmd
!finddata FileObject Offset
```

## Parameters


<span id="_______FileObject______"></span><span id="_______fileobject______"></span><span id="_______FILEOBJECT______"></span> *FileObject*   
Specifies the address of the file object.

<span id="_______Offset______"></span><span id="_______offset______"></span><span id="_______OFFSET______"></span> *Offset*   
Specifies the offset.

### DLL

Kdexts.dll

 

### Additional Information

For information about cache management, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

For information about other cache management extensions, see the [**!cchelp**](-cchelp.md) extension.

 

 





