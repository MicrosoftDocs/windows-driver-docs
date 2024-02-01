---
title: devhandles
description: The devhandles extension displays the open handles for the specified device.
keywords: ["devhandles Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- devhandles
api_type:
- NA
---

# !devhandles


The **!devhandles** extension displays the open handles for the specified device.

```dbgcmd
!devhandles Address 
```

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the device for which to display the open handles.

## DLL

Windows XP and later - Kdexts.dll

 

## Remarks

To display complete handle information, this extension requires private symbols.

The address of a device object can be obtained using the [**!drvobj**](-drvobj.md) or [**!devnode**](-devnode.md) extensions.

Here is a truncated example:

```dbgcmd
lkd> !devhandles 0x841153d8

Checking handle table for process 0x840d3940
Handle table at 95fea000 with 578 Entries in use

Checking handle table for process 0x86951d90
Handle table at 8a8ef000 with 28 Entries in use

...

Checking handle table for process 0x87e63650
Handle table at 947bc000 with 308 Entries in use

Checking handle table for process 0x87e6f4f0
00000000: Unable to read handle table
```

 

 





