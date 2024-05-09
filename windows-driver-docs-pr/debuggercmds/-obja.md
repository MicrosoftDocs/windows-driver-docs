---
title: "!obja (WinDbg)"
description: "The !obja extension displays the attributes of an object in the object manager."
keywords: ["object manager", "!obja Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- obja
api_type:
- NA
---

# !obja

The **!obja** extension displays the attributes of an object in the object manager.

```dbgcmd
!obja Address
```

## <span id="ddk__obja_dbg"></span><span id="DDK__OBJA_DBG"></span>Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the object header you want to examine.

## DLL

Ext.dll

## Additional Information

For information about objects and the object manager, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

The attributes pertaining to the specified object are listed. Valid attributes are:

```cpp
#define OBJ_INHERIT             0x00000002L
#define OBJ_PERMANENT           0x00000010L
#define OBJ_EXCLUSIVE           0x00000020L
#define OBJ_CASE_INSENSITIVE    0x00000040L
#define OBJ_OPENIF              0x00000080L
#define OBJ_OPENLINK            0x00000100L
#define OBJ_VALID_ATTRIBUTES    0x000001F2L
```

Here is an example:

```dbgcmd
kd> !obja 80967768
Obja +80967768 at 80967768:
        OBJ_INHERIT
        OBJ_PERMANENT
        OBJ_EXCLUSIVE
```
