---
title: Extensions for Debugging SCSI Miniport Drivers
description: Extensions for Debugging SCSI Miniport Drivers
ms.assetid: 6e6c35e5-d9dd-430a-8fc4-86f24344c24d
keywords: ["SCSI Miniport Debugging, useful extensions"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Extensions for Debugging SCSI Miniport Drivers


When you debug SCSI miniport drivers, you may find the following debugger extensions useful. General debugger extensions are listed first, followed by those specific to SCSI miniport debugging.

[**!devobj**](-devobj.md)  
The **!devobj** extension displays detailed information about a DEVICE\_OBJECT. If the **Current Irp** field is nonnull, this could be caused by the SCSI driver waiting for map registers.

Here is an example:

```dbgcmd
0: kd> !devobj 8633da70
Device object (8633da70) is for:
 adpu160m1 \Driver\adpu160m DriverObject 8633eeb8
Current Irp 860ef008 RefCount 0 Type 00000004 Flags 00000050
Dacl e129871c DevExt 8633db28 DevObjExt 8633dfd0
ExtensionFlags (0000000000)
AttachedTo (Lower) 863b2978 \Driver\PCI
Device queue is not busy. 
```

[**!errlog**](-errlog.md)  
The **!errlog** extension displays the contents of any pending entries in the I/O system's error log.

[**!object**](-object.md)  
The **!object** extension displays information about a system object. This extension displays all SCSI devices.

For example:

```dbgcmd
0: kd> !object \device\scsi
Object: e12a2520  Type: (863d12c8) Directory
    ObjectHeader: e12a2508
    HandleCount: 0  PointerCount: 9
    Directory Object: e1001100  Name: Scsi

    Hash Address  Type          Name
    ---- -------  ----          ----
     04  86352040 Device        adpu160m1Port3Path0Target6Lun0
     11  86353040 Device        adpu160m1Port3Path0Target1Lun0
     13  86334a70 Device        lp6nds351
     22  862e6040 Device        adpu160m1Port3Path0Target0Lun0
     24  8633da70 Device        adpu160m1
     25  86376040 Device        adpu160m2
     34  862e5040 Device        adpu160m1Port3Path0Target2Lun0 
```

[**!pcr**](-pcr.md)  
The **!pcr** extension displays detailed information about the Processor Control Region (PCR) on a processor. The information includes the items in the DPC queue, which can be useful. when you are debugging a stalled driver or a time-out.

[**!minipkd.help**](-minipkd-help.md)  
The **!minipkd.help** extension displays a list of all of the Minipkd.dll extension commands.

If an error message similar to the following appears, it indicates that the symbol path is incorrect and does not point to the correct version of the Scsiport.sys symbols.

```dbgcmd
minipkd error (0) <path> ... \minipkd\minipkd.c @ line 435
```

The [**.sympath (Set Symbol Path)**](-sympath--set-symbol-path-.md) command can be used to display the current path and to change the path. The [**.reload (Reload Module)**](-reload--reload-module-.md) command will reload symbols from the current path.

[**!minipkd.adapter Adapter**](-minipkd-adapter.md)  
The **!minipkd.adapter** extension displays detailed information about a specified adapter. The **Adapter** can be found by looking at the **DevExt** field in the **!minipkd.adapters** display.

[**!minipkd.adapters**](-minipkd-adapters.md)  
The **!minipkd.adapters** extension displays all the adapters that work with the SCSI Port driver that have been identified by Windows, and the individual devices associated with each adapter.

Here is an example:

```dbgcmd
0: kd> !minipkd.adapters
Adapter \Driver\lp6nds35     DO 86334a70         DevExt 86334b28
Adapter \Driver\adpu160m     DO 8633da70         DevExt 8633db28
 LUN 862e60f8 @(0,0,0) c ev     pnp(00/ff) pow(0,0) DevObj 862e6040
 LUN 863530f8 @(0,1,0) c ev p d pnp(00/ff) pow(0,0) DevObj 86353040
 LUN 862e50f8 @(0,2,0) c ev     pnp(00/ff) pow(0,0) DevObj 862e5040
 LUN 863520f8 @(0,6,0)   ev     pnp(00/ff) pow(0,0) DevObj 86352040
Adapter \Driver\adpu160m     DO 86376040         DevExt 863760f8 
```

An error message similar to the following indicates that either the symbol path is incorrect and does not point to the correct version of the Scsiport.sys symbols, or that Windows has not identified any adapters that work with the SCSI Port driver:

```dbgcmd
minipkd error (0) <path> ... \minipkd\minipkd.c @ line 435
```

If the [**!minipkd.help**](-minipkd-help.md) extension command returns help information successfully, the SCSI Port symbols are correct.

[**!minipkd.exports Adapter**](-minipkd-exports.md)  
The **!minipkd.exports** extension displays the addresses of the miniport exports for the specified adapter.

[**!minipkd.lun {LUN | Device}**](-minipkd-lun.md)  
The **!minipkd.lun** extension displays detailed information about a specified Logical Unit Extension (LUN). The LUN can be specified either by its address (which can be found by looking at the **LUN** field in the **!minipkd.adapters** display) or by its physical device object (which can be found in the **DevObj** field of the **!minipkd.adapters** display).

[**!minipkd.portconfig PortConfig**](-minipkd-portconfig.md)  
The **!minipkd.portconfig** extension displays detailed information about a specified PORT\_CONFIGURATION\_DATA. The **PortConfig** can be found in the **Port Config Info** field of the **!minipkd.adapter** display.

[**!minipkd.req {Adapter | Device}**](-minipkd-req.md)  
The **!minipkd.req** extension displays information about all of the currently active requests on the specified adapter or LUN device.

[**!minipkd.srb SRB**](-minipkd-srb.md)  
The **!minipkd.srb** extension displays detailed information about a specified SCSI request block (SRB). The SRB is specified by address. The addresses of all currently active requests can be found in the **SRB** fields of the output from the **!minipkd.req** command.

[**!scsikd.classext \[Device \[Level\]\]**](-scsikd-classext.md)  
The **!scsikd.classext** extension displays detailed information about a specified class Plug and Play (PnP) device or a list of all such devices. The *Device* is the device object or device extension of the class PnP device. If *Device* is omitted, a list of all class PnP extensions is displayed.

Here is an example:

```dbgcmd
0: kd> !scsikd.classext 

 ' !scsikd.classext 8633e3f0 '   (             ) "IBM     " / "DDYS-T09170M    " / "S93E" / "        XBY45906"
 ' !scsikd.classext 86347b48 '   (paging device) "IBM     " / "DDYS-T09170M    " / "S80D" / "        VDA60491"
  ' !scsikd.classext 86347360 '   (             ) "UNISYS  " / "003451ST34573WC " / "5786" / "HN0220750000181300L6"
  ' !scsikd.classext 861d1898 '   (             ) "" / "MATSHITA CD-ROM CR-177" / "7T03" / ""

 usage: !classext <class fdo> <level [0-2]> 
```

[**!scsikd.scsiext Device**](-scsikd-scsiext.md)  
The **!scsikd.scsiext** extension displays detailed information about a specified SCSI port extension. The *Device* can be the device object or device extension of either the adapter or the LUN.

Here are some examples:

```dbgcmd
0: kd> !scsikd.scsiext 86353040
Common Extension:
   < ..omitted.. >
Logical Unit Extension:
  Address (3, 0, 1, 0) Claimed  Enumerated Visible
  LuFlags (0x00000000):
  Retry 0x00          Key 0x008889ff
  Lock 0x00000000  Pause 0x00000000   CurrentLock: 0x00000000
  HwLuExt 0x862e6f00  Adapter 0x8633db28  Timeout 0x0000000a
  NextLun 0x00000000  ReadyLun 0x00000000
  Pending 0x00000000  Busy 0x00000000     Untagged 0x00000000
  < ..omitted.. >
Request list @0x86353200:
      Tick count is 2526
      SrbData 8615d700  Srb 8611f4fc  Irp 8611f2b8   Key 60197  <1s
      SrbData 85e72868  Srb 86100c3c Irp 861009f8   Key e29dc7  <1s

0: kd> !scsikd.scsiext 8633da70 
Common Extension:
   < ..omitted.. >
Adapter Extension:
  Port 3     IsPnp VirtualSlot HasInterrupt
  LowerPdo 0x84f9fb68   HwDevExt 0x84634004   Active Requests 0x00000000
  MaxBus 0x03   MaxTarget 0x40   MaxLun 0x08
  Port Flags (0x00001000): PD_DISCONNECT_RUNNING
  NonCacheExt 0x850d4000  IoBase 0xd80f0000   Int 0x23  < ..omitted.. > 
```

[**!scsikd.srbdata Address**](-scsikd-srbdata.md)  
The **!scsikd.srbdata** extension displays detailed information about a specified SRB\_DATA tracking block.

 

 





