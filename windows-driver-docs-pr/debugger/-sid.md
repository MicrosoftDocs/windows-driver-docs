---
title: sid
description: The sid extension displays the security identifier (SID) at the specified address.
ms.assetid: 7b93eb0e-7c0f-4c30-851b-6f40c7df8e1b
keywords: ["sid Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- sid
api_type:
- NA
ms.localizationpriority: medium
---

# !sid


The **!sid** extension displays the security identifier (SID) at the specified address.

Syntax

```dbgcmd
!sid Address [Flags] 
```

## <span id="ddk__sid_dbg"></span><span id="DDK__SID_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the SID structure.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
If this is set to 1, the SID type, domain, and user name for the SID is displayed.

If this is set to 1, the friendly name is displayed. This includes the SID type, as well as the domain and user name for the SID.

### <span id="DLL"></span><span id="dll"></span>DLL

Exts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about SIDs, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, or *Microsoft Windows Internals* by Mark Russinovich and David Solomon. Also see [**!sd**](-sd.md) and [**!acl**](-acl.md).

Remarks
-------

Here are two examples, one without the friendly name shown, and one with:

```dbgcmd
kd> !sid 0xe1bf35b8
SID is: S-1-5-21-518066528-515770016-299552555-513

kd> !sid 0xe1bf35b8 1
SID is: S-1-5-21-518066528-515770016-299552555-513 (Group: MYGROUP\Domain Users)
```

 

 





