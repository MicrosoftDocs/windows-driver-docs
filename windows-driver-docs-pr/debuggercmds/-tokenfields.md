---
title: "!tokenfields"
description: "The **!tokenfields** extension is obsolete. Instead, use the dt (Display Type) command."
keywords: ["token", "!tokenfields Windows Debugging"]
ms.date: 04/01/2024
topic_type:
- apiref
ms.topic: reference
api_name:
- tokenfields
api_type:
- NA
---

# !tokenfields

The **!tokenfields** extension is obsolete. Instead, use the dt (Display Type) command.

```dbgcmd
!tokenfields
```

## DLL

Unavailable (see the Remarks section)

## Additional Information

For information about the TOKEN structure, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. This book may not be available in some languages and countries.(The user-mode token structures described in the Microsoft Windows SDK documentation are slightly different.)

## Remarks

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

