---
title: ioreslist
description: The ioreslist extension displays an IO_RESOURCE_REQUIREMENTS_LIST structure.
ms.assetid: cb599656-2e0a-41ec-8358-a42047974dea
keywords: ["ioreslist Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ioreslist
api_type:
- NA
ms.localizationpriority: medium
---

# !ioreslist


The **!ioreslist** extension displays an IO\_RESOURCE\_REQUIREMENTS\_LIST structure.

```dbgcmd
!ioreslist Address 
```

## <span id="ddk__ioreslist_dbg"></span><span id="DDK__IORESLIST_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the IO\_RESOURCE\_REQUIREMENTS\_LIST structure.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For information about the IO\_RESOURCE\_REQUIREMENTS\_LIST structure, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

Here is an example of the output from this extension:

```dbgcmd
kd> !ioreslist 0xe122b768

IoResList at 0xe122b768 : Interface 0x5  Bus 0  Slot 0xe
  Alternative 0 (Version 1.1)
    Preferred Descriptor 0 - Port (0x1) Device Exclusive (0x1)
      Flags (0x01) - PORT_IO
      0x000100 byte range with alignment 0x000100
      1000 - 0x10ff
    Alternative Descriptor 1 - Port (0x1) Device Exclusive (0x1)
      Flags (0x01) - PORT_IO
      0x000100 byte range with alignment 0x000100
      0 - 0xffffffff
    Descriptor 2 - DevicePrivate (0x81) Device Exclusive (0x1)
      Flags (0000) -
      Data:              : 0x1 0x0 0x0
    Preferred Descriptor 3 - Memory (0x3) Device Exclusive (0x1)
      Flags (0000) - READ_WRITE
      0x001000 byte range with alignment 0x001000
      40080000 - 0x40080fff
    Alternative Descriptor 4 - Memory (0x3) Device Exclusive (0x1)
      Flags (0000) - READ_WRITE
      0x001000 byte range with alignment 0x001000
      0 - 0xffffffff
    Descriptor 5 - DevicePrivate (0x81) Device Exclusive (0x1)
      Flags (0000) -
      Data:              : 0x1 0x1 0x0
    Descriptor 6 - Interrupt (0x2) Shared (0x3)
      Flags (0000) - LEVEL_SENSITIVE
      0xb - 0xb
```

The IO\_RESOURCE\_REQUIREMENTS\_LIST contains information about:

-   Resource types

    There are four types of resources: I/O, Memory, IRQ, DMA.

-   Descriptors

    Each preferred setting has a "Preferred" descriptor and a number of "Alternative" descriptors.

This resource list contains the following requests:

-   I/O Ranges

    Prefers a range of 0x1000 to 0x10FF inclusive, but can use any 0x100 range between 0 and 0xFFFFFFFF, provided it is 0x100-aligned. (For example, 0x1100 to 0x11FF is acceptable.)

-   Memory

    Prefers a range of 0x40080000 to 0x40080FFF, but can use any range that is of size 0x1000, is 0x1000-aligned, and is located between 0 and 0xFFFFFFFF.

-   IRQ

    Must use IRQ 0xB.

Interrupts and DMA channels are represented as ranges with the same beginning and end.

 

 





