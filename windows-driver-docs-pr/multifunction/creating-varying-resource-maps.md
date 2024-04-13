---
title: Creating Varying Resource Maps
description: Varying resource maps let you subdivide a parent resource among children enumerated by mf.sys.
keywords:
- varying resource maps WDK multifunction devices
ms.date: 05/08/2023
---

# Creating Varying Resource Maps

While standard resource maps can only assign an entire parent resource to a child of a multifunction device, varying resource maps let you subdivide a parent resource among children enumerated by mf.sys. Varying resource maps are supported on Windows XP and later versions of the NT-based operating system.

For example, consider a multiport serial card on the PCI bus. Assume each of the card's 16550 UART functions requires a set of eight I/O ports and a single, shared interrupt. Also assume that the card is implemented as a single PCI function. In this scenario, it is typical to request a single block of I/O ports and to then split this block into eight segments, one for each 16550 UART function.

In addition to the I/O port and interrupt resources required by the card's 16550 UART functions, assume that the device also requires memory ranges and device-private resources.

Based on these assumptions, mf.sys will return a resource requirements list for this device, constructed as follows:

| Resourcenumber | Resource |
|--|--|
| 00 | *Memory Range* Base Register Address (BAR) 0 |
| 01 | *Private Data* |
| 02 | *Memory Range* BAR 1 |
| 03 | *Private Data* |
| 04 | *I/O Port Range* BAR 2 |
| 05 | *Private Data* |
| 06 | *Interrupt* |

Vendors use INF file directives to specify the sharing of these resources among the card's 16550 UART functions. For each function that requires a segment of the device's resources, you must use a **VaryingResourceMap** entry in the INF to create a registry entry. Following is an excerpt from the INF file for this device:

```inf
[DDInstall.RegHW]
; for each "child" function list hardware ID and resource map
; and/or varying resource map
HKR,Child0002,HardwareID,, child0002-hardware ID
HKR,Child0002,VaryingResourceMap,1,04, 10,00,00,00, 08,00,00,00
HKR,Child0002,ResourceMap,1,06
```

The line containing **VaryingResourceMap** is interpreted as follows:

- The "1" following the **VaryingResourceMap** parameter specifies that the registry entry's data type is REG\_BINARY.

- The numbers following the "1" are the varying resource map values. The '04' indicates the parent resource, a segment of which we are assigning to this child. In this case, we're assigning a segment of resource 04 (BAR 2) to the child (that is, a piece of the resource representing the eight I/O port ranges for each serial port).

- The next two DWORDs indicate, first, the offset into the resource and, second, the length of the range that should be allocated to this child. In this case, eight I/O ports are being allocated to this child, starting at offset 0x10 into the parent resource.

- If this child required another parent resource, the resource's number, length, and offset would be included on the same line of the INF, following the first resource.

The **ResourceMap** parameter is described in [Creating Standard Resource Maps](creating-standard-resource-maps.md) and indicates that this child should get a share of resource 06, which in this case is the PCI device's interrupt.

Following is a more complete example for this device, specifying four child functions:

```inf
[Version]
Signature="$Windows NT$"
Class=MultiFunction
ClassGUID={4d36e971-e325-11ce-bfc1-08002be10318}
Provider=%MYCOMPANY%
DriverVer=1/20/2000
CatalogFile=ExampleCatalog.cat
PnpLockdown=1

[ControlFlags]
ExcludeFromSelect=*

[Manufacturer]
%MYCOMPANY%=MYCOMPANY,NTamd64

[MYCOMPANY.NTamd64]
%MYCOMPANY_4PORT%=MYCOMPANY4PORT_inst, PCI\VEN_10B5&DEV_9050&SUBSYS_003112E0

[MYCOMPANY4PORT_inst]
Include = mf.inf
Needs = MFINSTALL.mf

[MYCOMPANY4PORT_inst.HW]
AddReg=MYCOMPANY4PORT_inst.RegHW

[MYCOMPANY4PORT_inst.Services]
Include = mf.inf
Needs = MFINSTALL.mf.Services

[MYCOMPANY4PORT_inst.RegHW]
HKR,Child0000,HardwareID,,*PNP0501
HKR,Child0000,VaryingResourceMap,1,04, 00,00,00,00, 08,00,00,00
HKR,Child0000,ResourceMap,1,06
HKR,Child0001,HardwareID,,*PNP0501
HKR,Child0001,VaryingResourceMap,1,04, 08,00,00,00, 08,00,00,00
HKR,Child0001,ResourceMap,1,06
HKR,Child0002,HardwareID,,*PNP0501
HKR,Child0002,VaryingResourceMap,1,04, 10,00,00,00, 08,00,00,00
HKR,Child0002,ResourceMap,1,06
HKR,Child0003,HardwareID,,*PNP0501
HKR,Child0003,VaryingResourceMap,1,04, 18,00,00,00, 08,00,00,00
HKR,Child0003,ResourceMap,1,06

[Strings]
MYCOMPANY= "MYCOMPANY Inc."
MYCOMPANY_4PORT="MYCOMPANY 4PORT"
```
