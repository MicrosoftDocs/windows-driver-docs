---
title: dma
description: The dma extension displays information about the Direct Memory Access (DMA) subsystem, and the DMA Verifier option of Driver Verifier.
ms.assetid: 4ccf679f-5804-4644-935a-18ff8711ae9a
keywords: ["DMA Verification (Driver Verifier)", "dma Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dma
api_type:
- NA
ms.localizationpriority: medium
---

# !dma


The **!dma** extension displays information about the Direct Memory Access (DMA) subsystem, and the **DMA Verifier** option of Driver Verifier.

```dbgcmd
!dma 
!dma Adapter [Flags]
```

## <span id="ddk__dma_pg"></span><span id="DDK__DMA_PG"></span>Parameters


<span id="_______Adapter______"></span><span id="_______adapter______"></span><span id="_______ADAPTER______"></span> *Adapter*   
Specifies the hexadecimal address of the DMA adapter to be displayed. If this is zero, all DMA adapters will be displayed.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the information to include in the display. This can be any combination of the following bits. The default is 0x1.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes the display to include generic adapter information.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include map register information. (Only when DMA Verification is active.)

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the display to include common buffer information. (Only when DMA Verification is active.)

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Causes the display to include scatter/gather list information. (Only when DMA Verification is active.)

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
Causes the display to include the device description for the hardware device. (Only when DMA Verification is active.)

<span id="Bit_5__0x20_"></span><span id="bit_5__0x20_"></span><span id="BIT_5__0X20_"></span>Bit 5 (0x20)  
Causes the display to include Wait context block information.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about Driver Verifier, see the Windows Driver Kit (WDK) documentation. For information about DMA, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals* by Mark Russinovich David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

Invalid arguments (for example, **!dma 1**) generate a brief help text.

When the **!dma** extension is used with no parameters, it displays a concise list of all DMA adapters and their addresses. This can be used to obtain the address of an adapter for use in the longer versions of this command.

Here is an example of how this extension can be used when the Driver Verifier's **DMA Verification** option is active:

```dbgcmd
0:kd> !dma

Dumping all DMA adapters...

Adapter: 82faebd0     Owner: SCSIPORT!ScsiPortGetUncachedExtension 
Adapter: 82f88930     Owner: SCSIPORT!ScsiPortGetUncachedExtension 
Adapter: 82f06cd0     Owner: NDIS!NdisMAllocateMapRegisters 
Master adapter: 80076800
```

From this output, you can see that there are three DMA adapters in the system. SCSIPORT owns two and NDIS owns the third. To examine the NDIS adapter in detail, use the **!dma** extension with its address:

```dbgcmd
0:kd> !dma  82f06cd0
Adapter: 82f06cd0     Owner: NDIS!NdisMAllocateMapRegisters (0x9fe24351)
 MasterAdapter:       00000000
   Adapter base Va      00000000
   Map register base:   00000000
 WCB:                 82f2b604
   Map registers: 00000000 mapped, 00000000 allocated, 00000002 max

   Dma verifier additional information:
   DeviceObject: 82f98690
   Map registers:        00000840 allocated, 00000000 freed
   Scatter-gather lists: 00000000 allocated, 00000000 freed
   Common buffers:       00000004 allocated, 00000000 freed
   Adapter channels:     00000420 allocated, 00000420 freed
   Bytes mapped since last flush: 000000f2
```

The first block of data is specific information that a HAL developer can use to debug the problem. For your purposes, the data below "Dma verifier additional information" is what is interesting. In this example, you see that NDIS has allocated 0x840 map registers. This is a huge number, especially because NDIS had indicated that it planned to use a maximum of two map registers. This adapter apparently does not use scatter/gather lists and has put away all its adapter channels. Look at the map registers in more detail:

```dbgcmd
0:kd> !dma  82f06cd0 2
Adapter: 82f06cd0     Owner: NDIS!NdisMAllocateMapRegisters 
...

  Map register file 82f06c58 (0/2 mapped)
     Double buffer mdl: 82f2c188
     Map registers:
        82f06c80: Not mapped
        82f06c8c: Not mapped

  Map register file 82f06228 (1/2 mapped)
     Double buffer mdl: 82f1b678
     Map registers:
        82f06250: 00bc bytes mapped to f83c003c
        82f0625c: Not mapped

  Map register file 82fa5ad8 (1/2 mapped)
     Double buffer mdl: 82f1b048
     Map registers:
        82fa5b00: 0036 bytes mapped to 82d17102
        82fa5b0c: Not mapped
...
```

In this example, you see that certain map registers have been mapped. Each *map register file* is an allocation of map registers by the driver. In other words, it represents a single call to **AllocateAdapterChannel**. NDIS collects a large number of these map register files, while some drivers create them one at a time and dispose of them when they are finished.

The map register files are also the addresses that are returned to the device under the name "MapRegisterBase". Note that DMA verifier only hooks the first 64 map registers for each driver. The rest are ignored for reasons of space (each map register represents three physical pages).

In this example, two map register files are in use. This means that the driver has mapped a buffer so it is visible to the hardware. In the first case, 0xBC bytes are mapped to the system virtual address 0xF83C003C.

An examination of the common buffers reveals:

```dbgcmd
0:kd> !dma  82f06cd0 4
Adapter: 82f06cd0     Owner: NDIS!NdisMAllocateMapRegisters 
...
   Common buffer allocated by NDIS!NdisMAllocateSharedMemory:
      Length:           1000
      Virtual address:  82e77000
      Physical address: 2a77000

   Common buffer allocated by NDIS!NdisMAllocateSharedMemory:
      Length:           12010
      Virtual address:  82e817f8
      Physical address: 2a817f8

   Common buffer allocated by NDIS!NdisMAllocateSharedMemory:
      Length:           4300
      Virtual address:  82e95680
      Physical address: 2a95680

   Common buffer allocated by NDIS!NdisMAllocateSharedMemory:
      Length:           4800
      Virtual address:  82e9d400
      Physical address: 2a9d400
```

This is fairly straightforward; there are four common buffers of varying lengths. The physical and virtual addresses are all given.

 

 





