---
title: sysptes
description: The sysptes extension displays a formatted view of the system page table entries (PTEs).
ms.assetid: cfb40732-6658-43aa-8b83-0ad4b55194ba
keywords: ["sysptes Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- sysptes
api_type:
- NA
---

# !sysptes


The **!sysptes** extension displays a formatted view of the system page table entries (PTEs).

```
!sysptes [Flags]
```

## <span id="ddk__sysptes_dbg"></span><span id="DDK__SYSPTES_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the level of detail to display. *Flags* can be any combination of the following bits. The default is zero:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays information about free PTEs.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
(Windows 2000 only) Displays unused pages in the page usage statistics.

(Windows XP and later) Displays information about free PTEs in the global special pool.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Displays detailed information about any system PTEs that are allocated to mapping locked pages.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
(Windows 2000 and Windows XP only) Displays nonpaged pool expansion free PTE information. If this bit is set, the other lists are not displayed. If both 0x1 and 0x8 are set, all nonpaged pool expansion free PTEs are displayed. If only 0x8 is set, only the total is displayed.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
(Windows Vista and later) Displays special pool free PTE information for the session.

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

For information about page tables and PTEs, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon. (This book may not be available in some languages and countries.)

Remarks
-------

To examine a specific PTE, use the [**!pte**](-pte.md) extension.

Here is an example from a Windows 2000 system:

```
kd> !sysptes 1

System PTE Information
  Total System Ptes 50962
     SysPtes list of size   1 has 389 free
     SysPtes list of size   2 has  95 free
     SysPtes list of size   4 has  55 free
     SysPtes list of size   8 has  35 free
     SysPtes list of size  16 has  27 free
 
    starting PTE: c03c7000
    ending PTE:   c03f8c44

loading (99% complete)

      free ptes: c03c8d60   number free: 45134.

  free blocks: 1   total free: 45134    largest free block: 45134

     Page    Count
       a0        2.
       a1        2.
       a2        2.
       a3        2.
......
```

In Windows XP and later versions of Windows, the display is similar, except that the page count statistics at the end are not included. Here is an example from a Windows XP system:

```
kd> !sysptes 1

System PTE Information
  Total System Ptes 571224
     SysPtes list of size 1 has 361 free
     SysPtes list of size 2 has 91 free
     SysPtes list of size 4 has 48 free
     SysPtes list of size 8 has 36 free
     SysPtes list of size 9 has 29 free
     SysPtes list of size 23 has 29 free
 
    starting PTE: fffffe0059388000
    ending PTE:   fffffe00597e3ab8

      free ptes: fffffe0059388000   number free: 551557.
      free ptes: fffffe00597be558   number free: 104.
      free ptes: fffffe00597d2828   number free: 676.

  free blocks: 3   total free: 552337    largest free block: 551557
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!sysptes%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




