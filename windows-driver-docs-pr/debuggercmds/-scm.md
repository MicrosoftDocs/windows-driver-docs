---
title: "!scm (WinDbg)"
description: "The !scm extension displays the specified shared cache map."
keywords: ["shared cache map", "cache manager", "!scm Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- scm
api_type:
- NA
---

# !scm

The **!scm** extension displays the specified shared cache map.

In Windows XP and later versions of Windows, use the [**dt nt!\_SHARED\_CACHE\_MAP Address**](dt--display-type-.md) command instead of **!scm**.

```dbgcmd
!scm Address
```

## Parameters
<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the shared cache map.

## DLL

Unavailable

## Additional Information

For information about cache management, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

For information about other cache management extensions, see the [**!cchelp**](-cchelp.md) extension.
