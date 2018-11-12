---
title: Extensions for Debugging Plug and Play Drivers
description: Extensions for Debugging Plug and Play Drivers
ms.assetid: 0b60c4ce-5c2d-4cce-a1e6-8275186aa147
keywords: ["Plug and Play (PnP), extensions", "extensions, plug and play"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Extensions for Debugging Plug and Play Drivers


When you debug Plug and Play drivers, you may find the following debugger extensions useful.

[**!arbiter**](-arbiter.md)  
Displays the current system resource arbiters. An arbiter is a piece of code that is exposed by the bus driver that arbitrates requests for resources, and attempts to solve the resource conflicts among the devices connected on that bus.

[**!cmreslist**](-cmreslist.md)  
Displays the CM\_RESOURCE\_LIST for the specified device object.

You must know the address of the CM Resource List.

Here is an example:

```dbgcmd
kd> !cmreslist 0xe12576e8

CmResourceList at 0xe12576e8  Version 0.0  Interface 0x1  Bus #0
  Entry 0 - Port (0x1) Device Exclusive (0x1)
    Flags (0x01) - PORT_MEMORY PORT_IO
    Range starts at 0x3f8 for 0x8 bytes
  Entry 1 - Interrupt (0x2) Shared (0x3)
    Flags (0x01) - LATCHED
    Level 0x4, Vector 0x4, Affinity 0xffffffff
```

This shows that the device with this CM resource list is using I/O Range 3F8-3FF and IRQ 4.

[**!dcs**](-dcs.md)  
This extension is obsolete -- its functionality has been subsumed by [**!pci**](-pci.md). See the !pci 100 example later in this section.

[**!devext**](-devext.md)  
Displays bus-specific device extension information for a variety of devices.

[**!devnode**](-devnode.md)  
Displays information about a node in the device tree.

Device node 0 (zero) is the root of the device tree.

Here is an example:

```dbgcmd
0: kd> !devnode 0xfffffa8003634af0
DevNode 0xfffffa8003634af0 for PDO 0xfffffa8003658590
  Parent 0xfffffa8003604010   Sibling 0xfffffa80036508e0   Child 0000000000
  InstancePath is "ROOT\SYSTEM\0000"
  ServiceName is "swenum"
  State = DeviceNodeStarted (0x308)
  Previous State = DeviceNodeEnumerateCompletion (0x30d)
  StateHistory[09] = DeviceNodeEnumerateCompletion (0x30d)
  StateHistory[08] = DeviceNodeEnumeratePending (0x30c)
  StateHistory[07] = DeviceNodeStarted (0x308)
  StateHistory[06] = DeviceNodeStartPostWork (0x307)
  StateHistory[05] = DeviceNodeStartCompletion (0x306)
  StateHistory[04] = DeviceNodeStartPending (0x305)
  ...
  Flags (0x6c000131)  DNF_MADEUP, DNF_ENUMERATED, 
                      DNF_IDS_QUERIED, DNF_NO_RESOURCE_REQUIRED, 
                      DNF_NO_LOWER_DEVICE_FILTERS, DNF_NO_LOWER_CLASS_FILTERS, 
                      DNF_NO_UPPER_DEVICE_FILTERS, DNF_NO_UPPER_CLASS_FILTERS
  UserFlags (0x00000008)  DNUF_NOT_DISABLEABLE
  DisableableDepends = 1 (including self)
```

[**!devobj**](-devobj.md)  
Displays detailed information about a DEVICE\_OBJECT.

Here is an example:

```dbgcmd
kd> !devobj 0xff0d4af0

Device object (ff0d4af0) is for:
 00252d \Driver\PnpManager DriverObject ff0d9030
Current Irp 00000000 RefCount 0 Type 00000004 Flags 00001040AttachedDev ff0b59e0

DevExt ff0d4ba8 DevNode ff0d4a08
Device queue is not busy.
```

[**!drivers**](-drivers.md)  
The [**!drivers**](-drivers.md) command is no longer supported. Please use the [**lm t n**](lm--list-loaded-modules-.md) command instead.

[**!drvobj**](-drvobj.md)  
Displays detailed information about a DRIVER\_OBJECT.

Lists all the device objects created by the specified driver.

Here is an example:

```dbgcmd
kd> !drvobj serial

Driver object (ff0ba630) is for:
 \Driver\Serial
Driver Extension List: (id , addr)

Device Object list:
ffba3040  ff0b4040  ff0b59e0  ff0b5040
```

[**!ecb, !ecd, !ecw**](-ecb---ecd---ecw.md)  
(x86 target computers only) Writes a sequence of values into the PCI configuration space.

[**ib, iw, id**](-ib---id---iw.md)  
Reads data from an I/O port.

These three commands are useful for determining whether a certain I/O range is claimed by a device other than the driver being debugged. A byte value of 0xFF at a port indicates that the port is not in use.

[**!ioreslist**](-ioreslist.md)  
Displays the specified IO\_RESOURCE\_REQUIREMENTS\_LIST.

[**!irp**](-irp.md)  
Displays information about an IRP.

[**!irpfind**](-irpfind.md)  
Displays information about all IRPs currently allocated in the target system, or information about those IRPs whose fields match the specified search criteria.

[**!pci**](-pci.md)  
(x86 target computers only) Displays the current status of the PCI buses and any devices attached to them. It can also display the PCI configuration space.

The following example displays the devices on the primary bus:

```dbgcmd
kd> !pci
PCI Bus 0
00:0  8086:1237.02  Cmd[0106:.mb..s]  Sts[2280:.....]  Device  Host bridge
0d:0  8086:7000.01  Cmd[0007:imb...]  Sts[0280:.....]  Device  ISA bridge
0d:1  8086:7010.00  Cmd[0005:i.b...]  Sts[0280:.....]  Device  IDE controller
0e:0  1011:0021.01  Cmd[0107:imb..s]  Sts[0280:.....]  PciBridge 0->1-1  PCI-PCI
 bridge
10:0  5333:8811.43  Cmd[0023:im.v..]  Sts[0200:.....]  Device  VGA compatible controller



The following example displays the devices for the secondary bus, with verbose output:

kd> !pci 1 1

PCI Bus 1
08:0  10b7:5900.00  Cmd[0107:imb..s]  Sts[0200:.....]  Device  Ethernet
      cf8:80014000  IntPin:1  IntLine:f  Rom:fa000000  cis:0  cap:0
      IO[0]:fce1

09:0  9004:8178.00  Cmd[0117:imb..s]  Sts[0280:.....]  Device  SCSI controller
      cf8:80014800  IntPin:1  IntLine:f  Rom:fa000000  cis:0  cap:0
      IO[0]:f801       MEM[1]:f9fff000

0b:0  9004:5800.10  Cmd[0116:.mb..s]  Sts[0200:.....]  Device  SubID:9004:8940
1394 host controller
      cf8:80015800  IntPin:1  IntLine:e  Rom:fa000000  cis:0  cap:0
      MEM[0]:f9ffec00
```

The following example displays the PCI configuration space for the SCSI controller (bus 1, device 9, function 0):

```dbgcmd
kd> !pci 100 1 9 0 
00: 9004    ;VendorID=9004
02: 8178    ;DeviceID=8178
04: 0117    ;Command=SERREnable,MemWriteEnable,BusInitiate,MemSpaceEnable,IOSpac
eEnable
06: 0280    ;Status=FB2BCapable,DEVSELTiming:1
08: 00      ;RevisionID=00
09: 00      ;ProgIF=00 (SCSI bus controller)
0a: 00      ;SubClass=00
0b: 01      ;BaseClass=01 (Mass storage controller)
0c: 08      ;CacheLineSize=Burst8DW
0d: 20      ;LatencyTimer=20
0e: 00      ;HeaderType=00
0f: 00      ;BIST=00
10: 0000f801;BAR0=0000f801
14: f9fff000;BAR1=f9fff000
18: 00000000;BAR2=00000000
1c: 00000000;BAR3=00000000
20: 00000000;BAR4=00000000
24: 00000000;BAR5=00000000
28: 00000000;CBCISPtr=00000000
2c: 0000    ;SubSysVenID=0000
2e: 0000    ;SubSysID=0000
30: fa000000;ROMBAR=fa000000
34: 00000000;Reserved=00000000
38: 00000000;Reserved=00000000
3c: 0f      ;IntLine=0f
3d: 01      ;IntPin=01
3e: 08      ;MinGnt=08
3f: 08      ;MaxLat=08
40: 00001580,00001580,00000000,00000000,00000000,00000000,00000000,00000000
60: 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
80: 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
a0: 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
c0: 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
e0: 00000000,00000000,00000000,00000000,00000000,00000000,00000000,00000000
```

[**!pcitree**](-pcitree.md)  
Displays information about PCI device objects, including child PCI buses and CardBus buses, as well as the devices attached to them.

[**!pnpevent**](-pnpevent.md)  
Displays the PnP device event queue.

[**!rellist**](-rellist.md)  
Displays a PnP relation list and any related CM\_RESOURCE\_LIST and IO\_RESOURCE\_LIST structures.

 

 





