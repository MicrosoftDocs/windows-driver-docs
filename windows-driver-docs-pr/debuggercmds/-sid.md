---
title: "!sid (WinDbg)"
description: "The !sid extension displays the security identifier (SID) at the specified address."
keywords: ["!sid Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- sid
api_type:
- NA
---

# !sid

The **!sid** extension displays the security identifier (SID) at the specified address.

Syntax

```dbgcmd
!sid Address [Flags] 
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the SID structure.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
If this is set to 1, the SID type, domain, and user name for the SID is displayed.

If this is set to 1, the friendly name is displayed. This includes the SID type, as well as the domain and user name for the SID.

## DLL

Exts.dll

## Additional Information

For information about SIDs, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, or *Microsoft Windows Internals* by Mark Russinovich and David Solomon. Also see [**!sd**](-sd.md) and [**!acl**](-acl.md).

## Remarks

Here are two examples, one without the friendly name shown, and one with:

```dbgcmd
kd> !sid 0xe1bf35b8
SID is: S-1-5-21-518066528-515770016-299552555-513

kd> !sid 0xe1bf35b8 1
SID is: S-1-5-21-518066528-515770016-299552555-513 (Group: MYGROUP\Domain Users)
```
