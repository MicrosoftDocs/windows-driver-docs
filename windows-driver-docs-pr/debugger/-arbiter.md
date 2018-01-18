---
title: arbiter
description: The arbiter extension displays the current system resource arbiters and arbitrated ranges.
ms.assetid: 95149538-6fcd-4638-b35f-4e1a562e5231
keywords: ["arbiter Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- arbiter
api_type:
- NA
---

# !arbiter


The **!arbiter** extension displays the current system resource arbiters and arbitrated ranges.

```
!arbiter [Flags] 
```

## <span id="ddk__arbiter_dbg"></span><span id="DDK__ARBITER_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies which classes of arbiters are displayed. If omitted, all arbiters are displayed. These bits can be combined freely.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Display I/O arbiters.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Display memory arbiters.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Display IRQ arbiters.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Display DMA arbiters.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
Display bus number arbiters.

<span id="Bit_8__0x100_"></span><span id="bit_8__0x100_"></span><span id="BIT_8__0X100_"></span>Bit 8 (0x100)  
Do not display aliases.

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

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command.

Remarks
-------

For each arbiter, **!arbiter** displays each allocated range of system resources, some optional flags, the PDO attached to that range (in other words, the range's owner), and the service name of this owner (if known).

The flags have the following meanings:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>S</p></td>
<td align="left"><p>Range is shared</p></td>
</tr>
<tr class="even">
<td align="left"><p>C</p></td>
<td align="left"><p>Range in conflict</p></td>
</tr>
<tr class="odd">
<td align="left"><p>B</p></td>
<td align="left"><p>Range is boot-allocated</p></td>
</tr>
<tr class="even">
<td align="left"><p>D</p></td>
<td align="left"><p>Range is driver-exclusive</p></td>
</tr>
<tr class="odd">
<td align="left"><p>A</p></td>
<td align="left"><p>Range alias</p></td>
</tr>
<tr class="even">
<td align="left"><p>P</p></td>
<td align="left"><p>Range positive decode</p></td>
</tr>
</tbody>
</table>

 

Here is an example:

```
kd> !arbiter 4

DEVNODE 80e203b8 (HTREE\ROOT\0)
  Interrupt Arbiter "" at 80167140
    Allocated ranges:
      0000000000000000 - 0000000000000000   B   80e1d3d8 
      0000000000000001 - 0000000000000001   B   80e1d3d8 
 .....
      00000000000001a2 - 00000000000001a2    
        00000000000001a2 - 00000000000001a2  CB   80e1d3d8 
        00000000000001a2 - 00000000000001a2  CB   80e52538  (Serial)
      00000000000001a3 - 00000000000001a3       80e52778  (i8042prt)
      00000000000001b3 - 00000000000001b3       80e1b618  (i8042prt)
 Possible allocation:
      < none >
```

In this example, the next-to-last line shows the resource range (which consists of 0x1A3 alone), the PDO of 0x80E52778, and the service of i8042prt.sys. No flags are listed on this line.

You can now use [**!devobj**](-devobj.md) with this PDO address to find the device extension and device node addresses:

```
kd> !devobj 80e52778
Device object (80e52778) is for:
 00000034 \Driver\PnpManager DriverObject 80e20610
Current Irp 00000000 RefCount 1 Type 00000004 Flags 00001040
DevExt 80e52830 DevObjExt 80e52838 DevNode 80e52628 
ExtensionFlags (0000000000)  
AttachedDevice (Upper) 80d78b28 \Driver\i8042prt
Device queue is not busy.
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!arbiter%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




