---
title: "!arbinst (WinDbg)"
description: "The !arbinst extension displays information about a specified arbiter."
keywords: ["arbiter", "!arbinst Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- arbinst
api_type:
- NA
---

# !arbinst


The **!arbinst** extension displays information about a specified arbiter.

```dbgcmd
    !arbinst Address [Flags]
```

## Parameters


<span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>*Address*  
Specifies the hexadecimal address of the arbiter to be displayed.

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>*Flags*  
Specifies how much information to display for each arbiter. At present, the only flag is 0x100. If this flag is set, then the aliases are displayed.

## DLL


Kdexts.dll

 

## Additional Information


See also the [**!arbiter**](-arbiter.md) extension.

## Remarks

For the arbiter specified, **!arbinst** displays each allocated range of system resources, some optional flags, the PDO attached to that range (in other words, the range's owner), and the service name of this owner (if known).

Here is an example:

```console
kd> !arbinst e0000106002ee8e8
Port Arbiter "PCI I/O Port (b=02)" at e0000106002ee8e8
  Allocated ranges:
    0000000000000000 - 0000000000001fff       00000000 <Not on bus>
    0000000000002000 - 00000000000020ff     P e0000000858bea20  (ql1280)
    0000000000003000 - ffffffffffffffff       00000000 <Not on bus>
  Possible allocation:
    < none >
kd> !arbinst e0000106002ec458
Memory Arbiter "PCI Memory (b=02)" at e0000106002ec458
  Allocated ranges:
    0000000000000000 - 00000000ebffffff       00000000 <Not on bus>
    00000000effdef00 - 00000000effdefff   B   e0000000858be560 
    00000000effdf000 - 00000000effdffff       e0000000858bea20  (ql1280)
    00000000f0000000 - ffffffffffffffff       00000000 <Not on bus>
  Possible allocation:
    < none >
```

