---
title: "!vad_reload"
description: "The !vad_reload extension reloads the user-mode modules for a specified process by using the virtual address descriptors (VADs) of that process."
keywords: ["!vad_reload Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- vad_reload
api_location:
- Kdextx86.dll
- Kdexts.dll
api_type:
- DllExport
---

# !vad\_reload

The **!vad\_reload** extension reloads the user-mode modules for a specified process by using the virtual address descriptors (VADs) of that process.

```dbgcmd
!vad_reload Process
```

## Parameters

<span id="_______Process______"></span><span id="_______process______"></span><span id="_______PROCESS______"></span> *Process*   
Specifies the hexadecimal address of the process for which the modules will be loaded.

## Additional Information

For information about VADs, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. 

## Remarks

You can use the [**!process**](-process.md) extension to find the address of a process.

Here is an example of how to find an address and use it in the **!vad\_reload** command.

```dbgcmd
3: kd> !process 0 0
. . .
PROCESS fffffa8007d54450
    SessionId: 1  Cid: 115c    Peb: 7ffffef6000  ParentCid: 0c58
    DirBase: 111bc3000  ObjectTable: fffff8a006ae0960  HandleCount: 229.
    Image: SearchProtocolHost.exe
. . .
3: kd> !vad_reload fffffa8007d54450
fffffa80`04f5e8b0: VAD maps 00000000`6c230000 - 00000000`6c26bfff, file cscobj.dll
fffffa80`04e8f890: VAD maps 00000000`6ef90000 - 00000000`6f04afff, file mssvp.dll
fffffa80`07cbb010: VAD maps 00000000`6f910000 - 00000000`6faf5fff, file tquery.dll
fffffa80`08c1f2a0: VAD maps 00000000`6fb80000 - 00000000`6fb9bfff, file mssprxy.dll
fffffa80`07dce8b0: VAD maps 00000000`6fba0000 - 00000000`6fba7fff, file msshooks.dll
fffffa80`04fd2e70: VAD maps 00000000`72a50000 - 00000000`72a6cfff, file userenv.dll
. . .
```

## DLL

Kdexts.dll

## See also

[**!process**](-process.md)

[**!vad**](-vad.md)
