---
title: mca
description: On an x86 target computer, the mca extension displays the machine check architecture (MCA) registers. On an Itanium target computer, the mca extension displays the MCA error record.
ms.assetid: 452bfbf2-fcab-4a71-bfd0-b02afe30df74
keywords: ["machine check architecture (MCA)", "MCA (machine check architecture)", "mca Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- mca
api_type:
- NA
ms.localizationpriority: medium
---

# !mca

The !mca extension displays the machine check architecture (MCA) registers. 

```dbgcmd
!mca
```


## <span id="ddk__mca_dbg"></span><span id="DDK__MCA_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
(Itanium target only) Specifies the address of the MCA error record.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
(Itanium target only) Specifies the level of output. *Flags* can be any combination of the following bits. The default value is 0xFF, which displays all sections present in the log.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays the processor section.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays the platform-specific section.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Displays the memory section.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Displays the PCI component section.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
Displays the PCI bus section.

<span id="Bit_5__0x20_"></span><span id="bit_5__0x20_"></span><span id="BIT_5__0X20_"></span>Bit 5 (0x20)  
Displays the SystemEvent Log section.

<span id="Bit_6__0x40_"></span><span id="bit_6__0x40_"></span><span id="BIT_6__0X40_"></span>Bit 6 (0x40)  
Displays the platform host controller section.

<span id="Bit_7__0x80_"></span><span id="bit_7__0x80_"></span><span id="BIT_7__0X80_"></span>Bit 7 (0x80)  
Displays to include the platform bus section.

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

 

This extension command can only be used with an x86-based or Itanium target computer.

Remarks
-------

On an Itanium target, **!mca** displays the MCA error record from the system abstraction layer (SAL). Here is an example of the output from this extension:

```dbgcmd
kd> !mca e0000165f3f58000
hal!HalpFeatureBits: 0xf [HAL_PERF_EVENTS|HAL_MCA_PRESENT|HAL_CMC_PRESENT|HAL_CPE_PRESENT]
 
MCA Error Record Header @ 0xe0000165f3f58000 0xe0000165f3f597a8
   Id               : 8
   Revision         :
      Revision         : 2
      Minor            : 0x2 '
      Major            : 0 '
   ErrorSeverity    : 0 '
   Valid            :
      Valid            : 0 '
      OemPlatformID    : 0y0
      Reserved         : 0y0000000 (0)
   Length           : 0x17a8
   TimeStamp        :
      TimeStamp        : 0x20031106`00134944
      Seconds          : 0x44 'D'
      Minutes          : 0x49 'I'
      Hours            : 0x13 '
      Reserved         : 0 '
      Day              : 0x6 '
      Month            : 0x11 '
      Year             : 0x3 '
      Century          : 0x20 ' '
   OemPlatformId    : [16]  ""
 

   Severity  : ErrorRecoverable
 
MCA Error Section Header @ 0xe0000165f3f58028 0xe0000165f3f59578   [Processor]
   Header           :
      Guid             :
         Data1            : 0xe429faf1
         Data2            : 0x3cb7
         Data3            : 0x11d4
         Data4            : [8]  "???"
      Revision         :
         Revision         : 2
         Minor            : 0x2 '
         Major            : 0 '
      RecoveryInfo     :
         RecoveryInfo     : 0 '
         Corrected        : 0y0
         NotContained     : 0y0
 Reset            : 0y0
         Reserved         : 0y0000
         Valid            : 0y0
 Reserved         : 0 '
      Length           : 0x1550
   Valid            :
 Valid            : 0x100101f
      ErrorMap         : 0y1
      StateParameter   : 0y1
      CRLid            : 0y1
      StaticStruct     : 0y1
      CacheCheckNum    : 0y0001
      TlbCheckNum      : 0y0000
      BusCheckNum      : 0y0001
      RegFileCheckNum  : 0y0000
      MsCheckNum       : 0y0000
      CpuIdInfo        : 0y1
      Reserved         : 0y000000000000000000000000000000000000000 (0)
   ErrorMap         :
      ErrorMap         : 0x1002000
      Cid              : 0y0000
      Tid              : 0y0000
      Eic              : 0y0000
      Edc              : 0y0010
      Eit              : 0y0000
      Edt              : 0y0000
      Ebh              : 0y0001
      Erf              : 0y0000
 Ems              : 0y0000000000000000 (0)
      Reserved         : 0y0000000000000000 (0)
   StateParameter   :
      StateParameter   : 0x28000000`fff21130
      reserved0        : 0y00
      rz               : 0y0
 ra               : 0y0
      me               : 0y1
      mn               : 0y1
      sy               : 0y0
      co               : 0y0
      ci               : 0y1
      us               : 0y0
      hd               : 0y0
      tl               : 0y0
      mi               : 0y1
      pi               : 0y0
      pm               : 0y0
      dy               : 0y0
      in               : 0y0
      rs               : 0y1
      cm               : 0y0
      ex               : 0y0
      cr               : 0y1
      pc               : 0y1
      dr               : 0y1
      tr               : 0y1
      rr               : 0y1
      ar               : 0y1
      br               : 0y1
      pr               : 0y1
      fp               : 0y1
      b1               : 0y1
      b0               : 0y1
      gr               : 0y1
      dsize            : 0y0000000000000000 (0)
      reserved1        : 0y00000000000 (0)
      cc               : 0y1
      tc               : 0y0
      bc               : 0y1
      rc               : 0y0
      uc               : 0y0
   CRLid            :
      LocalId          : 0
      reserved         : 0y0000000000000000 (0)
      eid              : 0y00000000 (0)
      id               : 0y00000000 (0)
      ignored          : 0y00000000000000000000000000000000 (0)
 
   CacheErrorInfo[0]:
 
   Valid            : 1
   CheckInfo        : 0y1
   RequestorIdentifier : 0y0
   ResponderIdentifier : 0y0
   TargetIdentifier : 0y0
   PreciseIP        : 0y0
 Reserved         : 0y00000000000000000000000000000000000000000000000000000000000 (0)
   CheckInfo       : 0x0
   RequestorId     : 0x0
   ResponderId     : 0x0
   TargetIp        : 0x0
   TargetId        : 0x0
   PreciseIp       : 0x0
 
   CheckInfo:
 
   CacheCheck       : 0
   Operation        : 0y0000
   Level            : 0y00
   Reserved1        : 0y00
 DataLine         : 0y0
   TagLine          : 0y0
   DataCache        : 0y0
   InstructionCache : 0y0
   MESI             : 0y000
   MESIValid        : 0y0
   Way              : 0y00000 (0)
   WayIndexValid    : 0y0
   Reserved2        : 0y0000000000 (0)
   Index            : 0y00000000000000000000 (0)
   Reserved3        : 0y00
   InstructionSet   : 0y0
   InstructionSetValid : 0y0
   PrivilegeLevel   : 0y00
   PrivilegeLevelValid : 0y0
   MachineCheckCorrected : 0y0
   TargetAddressValid : 0y0
   RequestIdValid   : 0y0
   ResponderIdValid : 0y0
   PreciseIPValid   : 0y0
 

   BusErrorInfo[0]:
 
   Valid            : 9
   CheckInfo        : 0y1
   RequestorIdentifier : 0y0
   ResponderIdentifier : 0y0
   TargetIdentifier : 0y1
   PreciseIP        : 0y0
 Reserved         : 0y00000000000000000000000000000000000000000000000000000000000 (0)
 CheckInfo       : 0x1080000003000144
   RequestorId     : 0x0
   ResponderId     : 0x0
 TargetIp        : 0x0
   TargetId        : 0xd0022004
   PreciseIp       : 0x0
 
   CheckInfo:
 
   BusCheck         : 0x10800000`03000144
   Size             : 0y00100 (0x4)
 Internal         : 0y0
   External         : 0y1
   CacheTransfer    : 0y0
 Type             : 0y00000001 (0x1)
   Severity         : 0y00000 (0)
 Hierarchy        : 0y00
   Reserved1        : 0y0
   Status           : 0y00000011 (0x3)
 Reserved2        : 0y0000000000000000000000 (0)
   InstructionSet   : 0y0
   InstructionSetValid : 0y1
 PrivilegeLevel   : 0y00
   PrivilegeLevelValid : 0y0
   MachineCheckCorrected : 0y0
   TargetAddressValid : 0y1
   RequestIdValid   : 0y0
   ResponderIdValid : 0y0
   PreciseIPValid   : 0y0
 
   StaticInfo @ 0xe0000165f3f580f0 0xe0000165f3f59578
 
   Valid @ 0xe0000165f3f580f0
 
   Valid            : 0x3f
   MinState         : 0y1
   BR               : 0y1
   CR               : 0y1
   AR               : 0y1
   RR               : 0y1
   FR               : 0y1
   Reserved         : 0y0000000000000000000000000000000000000000000000000000000000 (0)
 
 MinState @ 0xe0000165f3f580f8 0xe0000165f3f584f0
 
   IntNats          : 0
 IntGp            : 0xe0000165`f1a99b00
 IntT0            : 0
   IntT1            : 0xe0f0e0f0`e0f0e000
   IntS0            : 0
 IntS1            : 1
   IntS2            : 0xe0000000`83068300
   IntS3            : 0xe0000000`832f8780
   IntV0            : 0x4600
   IntT2            : 0x230
   IntT3            : 0x3ff
 IntT4            : 0xe0000165`f38c6000
   IntSp            : 0xe0000165`f0f97da0
   IntTeb           : 0
   IntT5            : 0
   IntT6            : 0xfffff630
   B0R16            : 0x1010`082a6018
   B0R17            : 0
   B0R18            : 0xe0000000`830067c0
   B0R19            : 0x101
   B0R20            : 0x80000000`00000308
   B0R21            : 0
   B0R22            : 0xe0000000`84bedd20
   B0R23            : 0xe0000000`84bedd20
   B0R24            : 0xe0000165`f213df5a
   B0R25            : 0xfff80000`597c84f0
   B0R26            : 0x6081
   B0R27            : 0xfffffe00`00165f20
   B0R28            : 0x8000465
   B0R29            : 0x8000465
   B0R30            : 0x60
   B0R31            : 0xa04`00000000
 IntT7            : 0x44
   IntT8            : 0x200
   IntT9            : 0xe0000165`f38c6000
   IntT10           : 0xe0000165`f3cb81bc
   IntT11           : 0xe0000165`f3cb81b8
   IntT12           : 0xe0000000`8363f7b0
   IntT13           : 0xe0000165`f1899d08
   IntT14           : 0x9804c`8a70433f
 IntT15           : 0xe0000000`832821f8
   IntT16           : 0xe0000000`836536e0
   IntT17           : 0xe0000000`8363f7b8
   IntT18           : 0xffffffff`fffffbc3
   IntT19           : 0xe0000165`f1ff6000
 IntT20           : 0x2400580
   IntT21           : 0xe0000165`f1ff6004
   IntT22           : 0xe0000165`f3cb8dc0
   Preds            : 0x2277
   BrRp             : 0xe0000165`ea212df0
   RsRSC            : 3
   StIIP            : 0xe0000165`f1895370
   StIPSR           : 0x1010`082a6018
   StIFS            : 0x80000000`00000285
   XIP              : 0xe0000165`ea212c50
   XPSR             : 0x1010`082a6018
   XFS              : 0x80000000`00000b1c
 
   BR @ 0xe0000165f3f584f8 0xe0000165f3f58530
 
e0000165`f3f584f8  e0000165`ea212df0 USBPORT!USBPORT_StopDevice+0x850
e0000165`f3f58500  00000000`00000000
e0000165`f3f58508  00000000`00000000
e0000165`f3f58510  00000000`00000000
e0000165`f3f58518  00000000`00000000
e0000165`f3f58520  00000000`00000000
e0000165`f3f58528  e0000000`832cb061 nt!NtClose+0x1
e0000165`f3f58530  e0000165`f1895320 usbohci!OHCI_StopController
 
   CR @ 0xe0000165f3f58538 0xe0000165f3f58930
 
e0000165`f3f58538  00000000`00007e05
e0000165`f3f58540  00000154`a7047201
e0000165`f3f58548  e0000000`83230000 nt!KiVhptTransVector
e0000165`f3f58550  00000000`00000000
...
e0000165`f3f585c8  00000000`00000000
e0000165`f3f585d0  e0000165`f1895370 usbohci!OHCI_StopController+0x50
e0000165`f3f585d8  e0000165`f213df5a
e0000165`f3f585e0  00000000`00000060
e0000165`f3f585e8  e0000165`f1895360 usbohci!OHCI_StopController+0x40
e0000165`f3f585f0  80000000`00000285
...
e0000165`f3f58930  00000000`00000000
 
   AR @ 0xe0000165f3f58938 0xe0000165f3f58d30
 
e0000165`f3f58938  00000000`00000000
e0000165`f3f58940  00000000`00000000
e0000165`f3f58948  00000000`00000000
e0000165`f3f58950  00000000`00000000
e0000165`f3f58958  00000000`00000000
e0000165`f3f58960  00000000`00000006
e0000165`f3f58968  e0000000`8301add0 nt!KiMemoryFault
e0000165`f3f58970  00000000`00000000
e0000165`f3f58978  00000000`00000000
e0000165`f3f58980  00000000`00000000
e0000165`f3f58988  00000000`00000000
e0000165`f3f58990  00000000`00000000
e0000165`f3f58998  00000000`00000000
e0000165`f3f589a0  00000000`00000000
e0000165`f3f589a8  00000000`00000000
e0000165`f3f589b0  00000000`00000000
e0000165`f3f589b8  e0000165`f1895370 usbohci!OHCI_StopController+0x50
e0000165`f3f589c0  e0000165`f0f988e0
...
e0000165`f3f58d30  00000000`00000000
 
   RR @ 0xe0000165f3f58d38 0xe0000165f3f58d70
 
e0000165`f3f58d38  00000000`00000535
e0000165`f3f58d40  00000000`00000535
e0000165`f3f58d48  00000000`00000535
e0000165`f3f58d50  00000000`00000535
e0000165`f3f58d58  00000000`00000535
e0000165`f3f58d60  00000000`00000535
e0000165`f3f58d68  00000000`00000535
e0000165`f3f58d70  00000000`00000535
 
   FR @ 0xe0000165f3f58d78 0xe0000165f3f59570
 
e0000165`f3f58d78  00000000`00000000
e0000165`f3f58d80  00000000`00000000
e0000165`f3f58d88  80000000`00000000
e0000165`f3f58d90  00000000`0000ffff
e0000165`f3f58d98  00000000`00000000
e0000165`f3f58da0  00000000`00000000
e0000165`f3f58da8  00000000`00000000
e0000165`f3f58db0  00000000`00000000
...
e0000165`f3f59570  00000000`00000000
 

MCA Error Section Header @ 0xe0000165f3f59578 0xe0000165f3f596a0   [PciComponent]
   Header           :
      Guid             :
         Data1            : 0xe429faf6
         Data2            : 0x3cb7
         Data3            : 0x11d4
         Data4            : [8]  "???"
 Revision         :
         Revision         : 2
         Minor            : 0x2 '
         Major            : 0 '
      RecoveryInfo     :
         RecoveryInfo     : 0x80 '
         Corrected        : 0y0
 NotContained     : 0y0
         Reset            : 0y0
         Reserved         : 0y0000
         Valid            : 0y1
 Reserved         : 0 '
      Length           : 0x128
   Valid            :
 Valid            : 0x23
      ErrorStatus      : 0y1
      Info             : 0y1
 MemoryMappedRegistersPairs : 0y0
      ProgrammedIORegistersPairs : 0y0
      RegistersDataPairs : 0y0
      OemData          : 0y1
      Reserved         : 0y0000000000000000000000000000000000000000000000000000000000 (0)
   ErrorStatus      :
      Status           : 0x121900
      Reserved0        : 0y00000000 (0)
      Type             : 0y00011001 (0x19)
      Address          : 0y0
 Control          : 0y1
      Data             : 0y0
      Responder        : 0y0
      Requestor        : 0y1
      FirstError       : 0y0
      Overflow         : 0y0
      Reserved1        : 0y00000000000000000000000000000000000000000 (0)
   Info             :
      VendorId         : 0x8086
      DeviceId         : 0x100e
 ClassCodeInterface : 0 '
 ClassCodeSubClass : 0 '
      ClassCodeBaseClass : 0x2 '
      FunctionNumber   : 0 '
      DeviceNumber     : 0x3 '
      BusNumber        : 0xa0 '
      SegmentNumber    : 0 '
      Reserved0        : 0 '
      Reserved1        : 0
   MemoryMappedRegistersPairs : 0
   ProgrammedIORegistersPairs : 0
 
   OemData @ 0xe0000165f3f595b8   0xe0000165f3f596a0
 
      Data Length = 0xe6
 Data:
e0000165`f3f595ba  00 00 00 00 00 00 91 d3-86 d3 7a 5e 7e 48 a4 0a  ..........z^~H..
e0000165`f3f595ca  2b f6 f7 a6 cc ca 00 ff-ff ff ff ff ff ff 09 00  +...............
e0000165`f3f595da  00 00 00 00 00 00 00 00-00 00 08 00 00 00 86 80  ................
e0000165`f3f595ea  0e 10 47 01 30 22 08 00-00 00 08 00 00 00 02 00  ..G.0"..........
e0000165`f3f595fa  00 02 20 80 00 00 10 00-00 00 08 00 00 00 00 00  .. .............
e0000165`f3f5960a  00 d0 00 00 00 00 18 00-00 00 08 00 00 00 81 a0  ................
e0000165`f3f5961a  00 00 00 00 00 00 20 00-00 00 08 00 00 00 00 00  ...... .........
e0000165`f3f5962a  00 00 00 00 00 00 28 00-00 00 08 00 00 00 00 00  ......(.........
e0000165`f3f5963a  00 00 3c 10 74 12 30 00-00 00 08 00 00 00 00 00  ..<.t.0.........
e0000165`f3f5964a  00 00 dc 00 00 00 38 00-00 00 08 00 00 00 00 00  ......8.........
e0000165`f3f5965a  00 00 2a 01 ff 00 e4 00-00 00 08 00 00 00 07 f0  ..*.............
e0000165`f3f5966a  1e 00 00 00 40 04 00 00-00 00 00 00 00 00 00 00  ....@...........
e0000165`f3f5967a  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00  ................
e0000165`f3f5968a  00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00  ................
e0000165`f3f5969a  00 00 00 00 00 00                                ......
 

MCA Error Section Header @ 0xe0000165f3f596a0 0xe0000165f3f597a8   [PciBus]
   Header           :
 Guid             :
         Data1            : 0xe429faf4
         Data2            : 0x3cb7
         Data3            : 0x11d4
         Data4            : [8]  "???"
 Revision         :
         Revision         : 2
         Minor            : 0x2 '
         Major            : 0 '
      RecoveryInfo     :
         RecoveryInfo     : 0x84 '
         Corrected        : 0y0
 NotContained     : 0y0
         Reset            : 0y1
         Reserved         : 0y0000
         Valid            : 0y1
 Reserved         : 0 '
      Length           : 0x108
   Valid            :
 Valid            : 0x74f
      ErrorStatus      : 0y1
      ErrorType        : 0y1
      Id               : 0y1
      Address          : 0y1
      Data             : 0y0
      CmdType          : 0y0
      RequestorId      : 0y1
      ResponderId      : 0y0
      TargetId         : 0y1
      OemId            : 0y1
 OemData          : 0y1
      Reserved         : 0y00000000000000000000000000000000000000000000000000000 (0)
   ErrorStatus      :
      Status           : 0x121900
      Reserved0        : 0y00000000 (0)
      Type             : 0y00011001 (0x19)
      Address          : 0y0
 Control          : 0y1
      Data             : 0y0
      Responder        : 0y0
      Requestor        : 0y1
      FirstError       : 0y0
      Overflow         : 0y0
 Reserved1        : 0y00000000000000000000000000000000000000000 (0)
   Type             :
      Type             : 0x4 '
      Reserved         : 0 '
   Id               :
      BusNumber        : 0xa0 '
      SegmentNumber    : 0 '
   Reserved         : [4]  ""
   Address          : 0xd0022054
   Data             : 0
   CmdType          : 0
 RequestorId      : 0xfed2a000
   ResponderId      : 0
   TargetId         : 0xd0022054
   OemId            : [16]  ".???"
   OemData          :
 Length           : 0x98
 
 
 
CP M/R/F/A Manufacturer     SerialNumber     Features         Speed
 0 1,5,31,0 GenuineIntel     0000000000000000 0000000000000001 1000 Mhz
```

On an x86 target, **!mca** displays the machine check registers supported by the active processor. It also displays basic CPU information (identical to that displayed by [**!cpuinfo**](-cpuinfo.md)). Here is an example of the output from this extension:

```dbgcmd
0: kd> !mca
MCE: Enabled, Cycle Address: 0x00000001699f7a00, Type: 0x0000000000000000

MCA: Enabled, Banks 5, Control Reg: Supported, Machine Check: None.
Bank  Error  Control Register     Status Register
  0. None   0x000000000000007f   0x0000000000000000

  1. None   0x00000000ffffffff   0x0000000000000000

  2. None   0x00000000000fffff   0x0000000000000000

  3. None   0x0000000000000007   0x0000000000000000

  4. None   0x0000000000003fff   0x0000000000000000

No register state available.

CP F/M/S Manufacturer   MHz Update Signature Features
 0 15,5,0 SomeBrandName 1394 0000000000000000 a0017fff
```

Note that this extension requires private HAL symbols. Without these symbols, the extension will display the message "HalpFeatureBits not found" along with basic CPU information. For example:

```dbgcmd
kd> !mca
HalpFeatureBits not found
CP F/M/S Manufacturer  MHz Update Signature Features
 0 6,5,1 GenuineIntel  334 0000004000000000 00001fff
```

 

 





