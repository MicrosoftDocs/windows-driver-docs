---
title: tokenfields
description: The tokenfields extension displays the names and offsets of the fields within the access token object (the TOKEN structure).
ms.assetid: dfadfdb0-1ed8-4c21-9207-dc02d7435475
keywords: ["token", "tokenfields Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- tokenfields
api_type:
- NA
ms.localizationpriority: medium
---

# !tokenfields


The **!tokenfields** extension displays the names and offsets of the fields within the access token object (the TOKEN structure).

```dbgcmd
!tokenfields
```

## <span id="ddk__tokenfields_dbg"></span><span id="DDK__TOKENFIELDS_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Unavailable (see the Remarks section)</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about the TOKEN structure, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. This book may not be available in some languages and countries.(The user-mode token structures described in the Microsoft Windows SDK documentation are slightly different.)

Remarks
-------

This extension command is not available in Windows XP or later versions of Windows. Instead, use the [**dt (Display Type)**](dt--display-type-.md) command to show the TOKEN structure directly:

```dbgcmd
kd> dt nt!_TOKEN 
```

To see a specific instance of the TOKEN structure, use the [**!token**](-token.md) extension.

Here is an example of **!tokenfields** from a Windows 2000 system:

```dbgcmd
kd> !tokenfields
 TOKEN structure offsets:
    TokenSource:           0x0
    AuthenticationId:      0x18
    ExpirationTime:        0x28
    ModifiedId:            0x30
    UserAndGroupCount:     0x3c
    PrivilegeCount:        0x44
    VariableLength:        0x48
    DynamicCharged:        0x4c
    DynamicAvailable:      0x50
    DefaultOwnerIndex:     0x54
    DefaultDacl:           0x6c
    TokenType:             0x70
    ImpersonationLevel:    0x74
    TokenFlags:            0x78
    TokenInUse:            0x79
 ProxyData:             0x7c
    AuditData:             0x80
    VariablePart:          0x84
```

 

 





