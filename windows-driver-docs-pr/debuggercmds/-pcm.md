---
title: "!pcm (WinDbg)"
description: "The !pcm extension displays the specified private cache map. This extension is only available in Windows 2000."
keywords: ["private cache map", "cache manager", "!pcm Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- pcm
api_type:
- NA
---

# !pcm

The **!pcm** extension displays the specified private cache map. This extension is only available in Windows 2000.

```dbgcmd
!pcm Address
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the private cache map.

## DLL

Windows XP - Kdexts.dll

Windows Vista and later - Unavailable

## Additional Information

For information about cache management, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

For information about other cache management extensions, see the [**!cchelp**](-cchelp.md) extension reference.

## Remarks

This extension is supported only in Windows 2000. In Windows XP and later versions of Windows, use the [**dt nt!\_PRIVATE\_CACHE\_MAP Address**](dt--display-type-.md) command.
