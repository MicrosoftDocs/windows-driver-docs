---
title: pci
description: The pci extension displays the current status of the peripheral component interconnect (PCI) buses, as well as any devices attached to those buses.
ms.assetid: 37b767db-18c9-4fd3-8910-4be03f41e764
keywords: ["PCI bus", "PCI device", "PCI configuration space", "pci Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- pci
api_type:
- NA
ms.localizationpriority: medium
---

# !pci


The **!pci** extension displays the current status of the peripheral component interconnect (PCI) buses, as well as any devices attached to those buses.

```dbgcmd
!pci [Flags [Segment] [Bus [Device [Function [MinAddress MaxAddress]]]]]
```

## <span id="ddk__pci_dbg"></span><span id="DDK__PCI_DBG"></span>Parameters


<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Specifies the level of output. Can be any combination of the following bits:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Causes a verbose display.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Causes the display to include all buses in the range from bus 0 (zero) to the specified *Bus*.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Causes the display to include information in raw byte format. If *MinAddress*, *MaxAddress*, or flag bit 0x8 is set, this bit is automatically set as well.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Causes the display to include information in raw DWORD format.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
Causes the display to include invalid device numbers. If *Device* is specified, this flag is ignored.

<span id="Bit_5__0x20_"></span><span id="bit_5__0x20_"></span><span id="BIT_5__0X20_"></span>Bit 5 (0x20)  
Causes the display to include invalid function numbers.

<span id="Bit_6__0x40_"></span><span id="bit_6__0x40_"></span><span id="BIT_6__0X40_"></span>Bit 6 (0x40)  
Causes the display to include capabilities.

<span id="Bit_7__0x80_"></span><span id="bit_7__0x80_"></span><span id="BIT_7__0X80_"></span>Bit 7 (0x80)  
Causes the display to include Intel 8086 device-specific information.

<span id="Bit_8__0x100_"></span><span id="bit_8__0x100_"></span><span id="BIT_8__0X100_"></span>Bit 8 (0x100)  
Causes the display to include the PCI configuration space.

<span id="Bit_9__0x200_"></span><span id="bit_9__0x200_"></span><span id="BIT_9__0X200_"></span>Bit 9 (0x200)  
Causes the display to include segment information. When this bit is included, the *Segment* parameter must be included.

<span id="Bit_10__0x400_"></span><span id="bit_10__0x400_"></span><span id="BIT_10__0X400_"></span>Bit 10 (0x400)  
Causes the display to include all valid segments in the range from segment 0 to the specified segment. When this bit is included, the *Segment* parameter must be included.

<span id="_______Segment______"></span><span id="_______segment______"></span><span id="_______SEGMENT______"></span> *Segment*   
Specifies the number of the segment to be displayed. Segment numbers range from 0 to 0xFFFF. If *Segment* is omitted, information about the primary segment (segment 0) is displayed. If *Flags* includes bit 10 (0x400), *Segment* specifies the highest valid segment to be displayed.

<span id="_______Bus______"></span><span id="_______bus______"></span><span id="_______BUS______"></span> *Bus*   
Specifies the bus to be displayed. *Bus* can range from 0 to 0xFF. If it is omitted, information about the primary bus (bus 0) is displayed. If *Flags* includes bit 1 (0x2), *Bus* specifies the highest bus number to be displayed.

<span id="_______Device______"></span><span id="_______device______"></span><span id="_______DEVICE______"></span> *Device*   
Specifies the slot device number for the device. If this is omitted, information about all devices is printed.

<span id="_______Function______"></span><span id="_______function______"></span><span id="_______FUNCTION______"></span> *Function*   
Specifies the slot function number for the device. If this is omitted, all information about all device functions is printed.

<span id="_______MinAddress______"></span><span id="_______minaddress______"></span><span id="_______MINADDRESS______"></span> *MinAddress*   
Specifies the first address from which raw bytes or DWORDs are to be displayed. This must be between 0 and 0xFF.

<span id="_______MaxAddress______"></span><span id="_______maxaddress______"></span><span id="_______MAXADDRESS______"></span> *MaxAddress*   
Specifies the last address from which raw bytes or DWORDs are to be displayed. This must be between 0 and 0xFF, and not less than *MinAddress*.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p></p>
Kext.dll
Kdextx86.dll</td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kext.dll</p></td>
</tr>
</tbody>
</table>



This extension command can only be used with an x86-based target computer.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command and additional examples. For information about PCI buses, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

To edit the PCI configuration space, use [**!ecb**](-ecb---ecd---ecw.md), **!ecd**, or **!ecw**.

The following example displays a list of all buses and their devices. This command will take a long time to execute. You will see a moving counter at the bottom of the display while the debugger scans the target system for PCI buses:

```dbgcmd
kd> !pci 2 ff
PCI Bus 0
00:0  8086:1237.02  Cmd[0106:.mb..s]  Sts[2280:.....]  Device  Host bridge
0d:0  8086:7000.01  Cmd[0007:imb...]  Sts[0280:.....]  Device  ISA bridge
0d:1  8086:7010.00  Cmd[0005:i.b...]  Sts[0280:.....]  Device  IDE controller
0e:0  1011:0021.02  Cmd[0107:imb..s]  Sts[0280:.....]  PciBridge 0->1-1  PCI-PCI bridge
10:0  102b:0519.01  Cmd[0083:im....]  Sts[0280:.....]  Device  VGA compatible controller
PCI Bus 1
08:0  10b7:9050.00  Cmd[0107:imb..s]  Sts[0200:.....]  Device  Ethernet
09:0  9004:8178.00  Cmd[0117:imb..s]  Sts[0280:.....]  Device  SCSI controller
```

This example displays verbose information about the devices on the primary bus. The two-digit number at the beginning of each line is the device number; the one-digit number following it is the function number:

```dbgcmd
kd> !pci 1 0
PCI Bus 0
00:0  8086:1237.02  Cmd[0106:.mb..s]  Sts[2280:.....]  Device  Host bridge
      cf8:80000000  IntPin:0  IntLine:0  Rom:0  cis:0  cap:0

0d:0  8086:7000.01  Cmd[0007:imb...]  Sts[0280:.....]  Device  ISA bridge
      cf8:80006800  IntPin:0  IntLine:0  Rom:0  cis:0  cap:0

0d:1  8086:7010.00  Cmd[0005:i.b...]  Sts[0280:.....]  Device  IDE controller
      cf8:80006900  IntPin:0  IntLine:0  Rom:0  cis:0  cap:0
      IO[4]:fff1       

0e:0  1011:0021.02  Cmd[0107:imb..s]  Sts[0280:.....]  PciBridge 0->1-1  PCI-PCI bridge
      cf8:80007000  IntPin:0  IntLine:0  Rom:0  cap:0  2sts:2280  BCtrl:6 ISA
      IO:f000-ffff  Mem:fc000000-fdffffff  PMem:fff00000-fffff

10:0  102b:0519.01  Cmd[0083:im....]  Sts[0280:.....]  Device  VGA compatible controller
      cf8:80008000  IntPin:1  IntLine:9  Rom:80000000  cis:0  cap:0
      MEM[0]:fe800000  MPF[1]:fe000008  
```

This example shows even more detailed information about bus 0 (zero), device 0x0D, and function 0x1, including the raw DWORDS from addresses between 0x00 and 0x3F:

```dbgcmd
kd> !pci f 0 d 1 0 3f
PCI Bus 0
0d:1  8086:7010.00  Cmd[0005:i.b...]  Sts[0280:.....]  Device  IDE controller
      cf8:80006900  IntPin:0  IntLine:0  Rom:0  cis:0  cap:0
      IO[4]:fff1       
      00000000:  70108086 02800005 01018000 00002000
      00000010:  00000000 00000000 00000000 00000000
      00000020:  0000fff1 00000000 00000000 00000000
      00000030:  00000000 00000000 00000000 00000000
```

This example displays the configuration space for segment 1, bus 0, device 1:

```dbgcmd
0: kd> !pci 301 1 0 1

PCI Configuration Space (Segment:0001 Bus:00 Device:01 Function:00)
Common Header:
    00: VendorID       14e4 Broadcom Corporation
    02: DeviceID       16c7
    04: Command        0146 MemSpaceEn BusInitiate PERREn SERREn
    06: Status         02b0 CapList 66MHzCapable FB2BCapable DEVSELTiming:1
.
.
.
    5a: MsgCtrl        64BitCapable MultipleMsgEnable:0 (0x1) MultipleMsgCapable:3 (0x8)
    5c: MsgAddr        2d4bff00
    60: MsgAddrHi      1ae09097
    64: MsData         9891
```

To display all devices and buses on valid segments, issue the command **!pci 602 ffff ff**:

```dbgcmd
0: kd> !pci 602 ffff ff
Scanning the following PCI segments: 0 0x1
PCI Segment 0 Bus 0
01:0  14e4:16c7.10  Cmd[0146:.mb.ps]  Sts[02b0:c6...]  Ethernet Controller  SubID:103c:1321
02:0  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
02:1  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
03:0  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
03:1  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
PCI Segment 0 Bus 0x38
01:0  14e4:1644.12  Cmd[0146:.mb.ps]  Sts[02b0:c6...]  Ethernet Controller  SubID:10b7:1000
PCI Segment 0 Bus 0x54
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0x54->0x55-0x55
PCI Segment 0 Bus 0x70
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0x70->0x71-0x71
PCI Segment 0 Bus 0xa9
01:0  8086:b154.00  Cmd[0147:imb.ps]  Sts[0ab0:c6.A.]  Intel PCI-PCI Bridge 0xa9->0xaa-0xaa
PCI Segment 0 Bus 0xaa
04:0  1033:0035.41  Cmd[0146:.mb.ps]  Sts[0210:c....]  NEC USB Controller  SubID:103c:1293
04:1  1033:0035.41  Cmd[0146:.mb.ps]  Sts[0210:c....]  NEC USB Controller  SubID:103c:aa55
04:2  1033:00e0.02  Cmd[0146:.mb.ps]  Sts[0210:c....]  NEC USB2 Controller  SubID:103c:aa55
05:0  1002:5159.00  Cmd[0187:imb..s]  Sts[0290:c....]  ATI VGA Compatible Controller  SubID:103c:1292
PCI Segment 0 Bus 0xc6
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0xc6->0xc7-0xc7
PCI Segment 0 Bus 0xe3
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0xe3->0xe4-0xe4
PCI Segment 0x1 Bus 0
01:0  14e4:16c7.10  Cmd[0146:.mb.ps]  Sts[02b0:c6...]  Ethernet Controller  SubID:103c:1321
02:0  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
02:1  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
03:0  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
03:1  1000:0030.08  Cmd[0147:imb.ps]  Sts[0230:c6...]  LSI SCSI Controller  SubID:103c:1323
PCI Segment 0x1 Bus 0x54
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0x54->0x55-0x55
PCI Segment 0x1 Bus 0x55
00:0  8086:10b9.06  Cmd[0147:imb.ps]  Sts[0010:c....]  Intel Ethernet Controller  SubID:8086:1083
PCI Segment 0x1 Bus 0x70
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0x70->0x71-0x71
PCI Segment 0x1 Bus 0xc6
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0xc6->0xc7-0xc7
PCI Segment 0x1 Bus 0xe3
00:0  103c:403b.00  Cmd[0547:imb.ps]  Sts[0010:c....]  HP PCI-PCI Bridge 0xe3->0xe4-0xe4
```









