---
title: drivers
description: In Windows XP and later versions of Windows, the drivers extension is obsolete. Instead use the lm command.
ms.assetid: 48b69af3-bf00-43d3-ac1a-e9513ead8647
keywords: ["drivers Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- drivers
api_type:
- NA
ms.localizationpriority: medium
---

# !drivers

In Windows XP and later versions of Windows, the **!drivers** extension is obsolete. To display information about loaded drivers and other modules, use the [**lm**](lm--list-loaded-modules-.md) command. The command lm t n displays information in a format very similar to the old **!drivers** extension. However, this command will not display the memory usage of the drivers as the **!drivers** extension did. It will only display the drivers' start and end addresses, image names, and timestamps. The [**!vm**](-vm.md) and [**!memusage**](-memusage.md) extensions can be used to display memory usage statistics.

```dbgcmd
!drivers [Flags]
```

## <span id="ddk__drivers_dbg"></span><span id="DDK__DRIVERS_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Can be any combination of the following values. (The default is 0x0.)

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the display to include information about resident and standby memory.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
If this bit is set and bit 2 (0x4) is not set, the display will include information about resident, standby, and locked memory, as well as the loader entry address. If bit 2 is set, this causes the display to be a much longer and more detailed list of the driver image. Information about the headers is included, as is section information.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the display to be a much longer and more detailed list of the driver image. Information about each section is included. If bit 1 (0x2) is set, this will also include header information.

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
<td align="left"><p>Unavailable</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For information about drivers and their memory use, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

An explanation of this command's display is given in the following table:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Column</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Base</p></td>
<td align="left"><p>The starting address of the device driver code, in hexadecimal. When the memory address used by the code that causes a stop falls between the base address for a driver and the base address for the next driver in the list, that driver is frequently the cause of the fault. For instance, the base for Ncrc810.sys is 0x80654000. Any address between that and 0x8065a000 belongs to this driver.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code Size</p></td>
<td align="left"><p>The size, in kilobytes, of the driver code, in both hexadecimal and decimal.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Data Size</p></td>
<td align="left"><p>The amount of space, in kilobytes, allocated to the driver for data, in both hexadecimal and decimal.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Locked</p></td>
<td align="left"><p>(Only when Flag 0x2 is used) The amount of memory locked by the driver.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Resident</p></td>
<td align="left"><p>(Only when Flag 0x1 or 0x2 is used) The amount of the driver&#39;s memory that actually resides in physical memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Standby</p></td>
<td align="left"><p>(Only when Flag 0x1 or 0x2 is used) The amount of the driver&#39;s memory that is on standby.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Loader Entry</p></td>
<td align="left"><p>(Only when Flag 0x2 is used) The loader entry address.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Driver Name</p></td>
<td align="left"><p>The driver file name.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Creation Time</p></td>
<td align="left"><p>The link date of the driver. Do not confuse this with the file date of the driver, which can be set by external tools. The link date is set by the compiler when a driver or executable file is compiled. It should be close to the file date, but it is not always the same.</p></td>
</tr>
</tbody>
</table>

 

The following is a truncated example of this command:

```dbgcmd
kd> !drivers
Loaded System Driver Summary
Base     Code Size      Data Size      Driver Name  Creation Time
80080000 f76c0 (989 kb) 1f100 (124 kb) ntoskrnl.exe Fri May 26 15:13:00
80400000 d980  ( 54 kb) 4040  ( 16 kb) hal.dll      Tue May 16 16:50:34
80654000 3f00  ( 15 kb) 1060   ( 4 kb) ncrc810.sys  Fri May 05 20:07:04
8065a000 a460  ( 41 kb) 1e80   ( 7 kb) SCSIPORT.SYS Fri May 05 20:08:05
```

 

 





