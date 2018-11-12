---
title: acl
description: The acl extension formats and displays the contents of an access control list (ACL).
ms.assetid: 591f56b6-5a70-4037-a285-a1bffd5bd387
keywords: ["acl Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- acl
api_type:
- NA
ms.localizationpriority: medium
---

# !acl


The **!acl** extension formats and displays the contents of an access control list (ACL).

Syntax

```dbgcmd
    !acl Address [Flags] 
```

## <span id="ddk__acl_dbg"></span><span id="DDK__ACL_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the ACL.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Displays the friendly name of the ACL, if the value of *Flags* is 1. This friendly name includes the security identifier (SID) type and the domain and user name for the SID.

### <span id="DLL"></span><span id="dll"></span>DLL

Exts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about access control lists, see [**!sid**](-sid.md), [**!sd**](-sd.md), and [Determining the ACL of an Object](determining-the-acl-of-an-object.md). Also, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

Remarks
-------

The following example shows the **!acl** extension.

```console
kd> !acl e1bf35d4 1
ACL is:
ACL is: ->AclRevision: 0x2
ACL is: ->Sbz1       : 0x0
ACL is: ->AclSize    : 0x40
ACL is: ->AceCount   : 0x2
ACL is: ->Sbz2       : 0x0
ACL is: ->Ace[0]: ->AceType: ACCESS_ALLOWED_ACE_TYPE
ACL is: ->Ace[0]: ->AceFlags: 0x0
ACL is: ->Ace[0]: ->AceSize: 0x24
ACL is: ->Ace[0]: ->Mask : 0x10000000
ACL is: ->Ace[0]: ->SID: S-1-5-21-518066528-515770016-299552555-2981724 (User: MYDOMAIN\myuser)

ACL is: ->Ace[1]: ->AceType: ACCESS_ALLOWED_ACE_TYPE
ACL is: ->Ace[1]: ->AceFlags: 0x0
ACL is: ->Ace[1]: ->AceSize: 0x14
ACL is: ->Ace[1]: ->Mask : 0x10000000
ACL is: ->Ace[1]: ->SID: S-1-5-18 (Well Known Group: NT AUTHORITY\SYSTEM)
```

 

 





