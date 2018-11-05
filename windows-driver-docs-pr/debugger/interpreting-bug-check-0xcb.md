---
title: Interpreting Bug Check 0xCB
description: Interpreting Bug Check 0xCB
ms.assetid: 82951e2b-cbb2-45d2-a6b8-4fddece035ce
keywords: ["kernel streaming debugging, video stream stall, bug check 0xcb"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Interpreting Bug Check 0xCB


The most common bug check code associated with debugging a video stream stall is Bug Check 0xCB (DRIVER\_LEFT\_LOCKED\_PAGES\_IN\_PROCESS). For a detailed list of its parameters, see [**Bug Check 0xCB**](bug-check-0xcb--driver-left-locked-pages-in-process.md).

The message displayed when the bug check occurs will point to Ks.sys as the cause.

```dbgcmd
Use !analyze -v to get detailed debugging information.
BugCheck CB, {f90c6ae0, f9949215, 81861788, 26}
Probably caused by : ks.sys ( ks!KsProbeStreamIrp+333 )
```

As suggested, use [**!analyze -v**](-analyze.md) to get more detailed information.

```dbgcmd
kd> !analyze -v
DRIVER_LEFT_LOCKED_PAGES_IN_PROCESS (cb)
Caused by a driver not cleaning up completely after an I/O.
When possible, the guilty driver's name (Unicode string) is printed on
the bugcheck screen and saved in KiBugCheckDriver.
Arguments:
Arg3: 81861788, A pointer to the MDL containing the locked pages.
```

Now, use the [**!search**](-search.md) extension to find the virtual addresses that are associated with the MDL pointer.

```dbgcmd
kd> !search 81861788
Searching PFNs in range 00000001 - 0000FF76 for [FFFFFFFF81861788 - FFFFFFFF81861788]

Pfn      Offset   Hit      Va       Pte
- - - - - - - - - - - - - - - - - - - - - - - - - - -
000008A7 00000B0C 81861788 808A7B0C C020229C
00000A04 00000224 16000001 80A04224 C0202810
...
00001732 000009B4 81861788 817329B4 C0205CC8
```

For each virtual address (VA) found, look for an IRP signature. Do this by using the [**dd**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command with the VA minus one DWORD.

```dbgcmd
kd> dd 808A7B0C-4 l4
808a7b08  f9949215 81861788 00000026 00000000
kd> $ Not an Irp
kd> dd 80A04224-4 l4
80a04220  00000000 00000000 00000000 00000000
kd> $ Not an Irp
kd> dd 817329B4-4 l4
817329b0  01900006 81861788 00000070 ffa59220
kd> $ Matches signature
```

After a VA with an IRP signature has been found, use the [**!irp**](-irp.md) extension to find out what driver is pending on this IRP.

```dbgcmd
kd> !irp 817329b0 7
Irp is active with 2 stacks 2 is current (= 0x81732a44)
 Mdl = 81861788 System buffer = ffa59220 Thread 00000000:  Irp stack trace.
>[  e, 0]   1  1 81a883c8 81ae6158 00000000-00000000    pending
 \Driver\TESTCAP
                        Args: 00000070 00000000 002f4017 00000000
```

In this case, \\Driver\\TESTCAP is the likely cause of the bug check.

 

 





