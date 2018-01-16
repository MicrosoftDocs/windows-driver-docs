---
title: ptov
description: The ptov extension displays the entire physical-to-virtual map for a given process.
ms.assetid: 82352d12-4e81-4746-9333-b2cc98eb7a9d
keywords: ["ptov Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ptov
api_type:
- NA
---

# !ptov


The **!ptov** extension displays the entire physical-to-virtual map for a given process.

```
!ptov DirBase
```

## <span id="ddk__ptov_dbg"></span><span id="DDK__PTOV_DBG"></span>Parameters


<span id="_______DirBase______"></span><span id="_______dirbase______"></span><span id="_______DIRBASE______"></span> *DirBase*   
Specifies the directory base for the process. To determine the directory base, use the [**!process**](-process.md) command, and look at the value displayed for DirBase.

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
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Here is an example. First, use [**.process**](-process--set-process-context-.md) and [**!process**](-process.md) to determine the directory base of the current process:

```
1: kd> .process
Implicit process is now 852b4040
1: kd> !process 852b4040 1
PROCESS 852b4040  SessionId: none  Cid: 0004    Peb: 00000000  ParentCid: 0000
    DirBase: 00185000  ObjectTable: 83203000  HandleCount: 663.
    Image: System
    ...
```

In this case, the directory base is 0x00185000. Pass this address to **!ptov**:

```
1: kd> !ptov 185000
X86PtoV: pagedir 185000, PAE enabled.
15e11000 10000
549e6000 20000
...
60a000 210000
40b000 211000
...
54ad3000 25f000
548d3000 260000
...
d71000 77510000
...
```

The numbers in the left column are the physical addresses of each memory page that has a mapping for this process. The numbers in the right column are the virtual addresses to which they are mapped.

The total display is very long.

Here is a 64-bit example.

```
3: kd> .process
Implicit process is now fffffa80`0361eb30
3: kd> !process fffffa80`0361eb30 1
PROCESS fffffa800361eb30
    SessionId: none  Cid: 0004    Peb: 00000000  ParentCid: 0000
    DirBase: 00187000  ObjectTable: fffff8a000002870  HandleCount: 919.
    Image: System
    ...
3: kd> !ptov 187000
Amd64PtoV: pagedir 187000
00000001`034fb000 1d0000
a757c000 1d1000
00000001`0103d000 1d2000
c041e000 1d3000
...
2ed6f000 fffff680`00001000
00000001`13939000 fffff680`00003000
ceefb000 fffff680`00008000
...
```

The directory base is the physical address of the first table that is used in virtual address translation. This table has different names depending on the bitness of the target operating system and whether Physical Address Extension (PAE) is enabled for the target operating system.

For 64-bit Windows, the directory base is the physical address of the Page Map Level 4 (PML4) table. For 32-bit Windows with PAE enabled, the directory base is the physical address of the Page Directory Pointers (PDP) table. For 32-bit Windows with PAE disabled, the directory bas is the physical address of the Page Directory (PD) table.

For related topics, see [**!vtop**](-vtop.md) and [Converting Virtual Addresses to Physical Addresses](converting-virtual-addresses-to-physical-addresses.md). For information about virtual address translation, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ptov%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




