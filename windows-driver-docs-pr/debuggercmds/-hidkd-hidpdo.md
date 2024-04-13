---
title: "!hidkd.hidpdo"
description: "The !hidkd.hidpdo extension command displays HID information associated with a physical device object (PDO)."
keywords: ["!hidkd.hidpdo Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- hidkd.hidpdo
api_type:
- NA
---

# !hidkd.hidpdo

The **!hidkd.hidpdo** extension command displays HID information associated with a physical device object (PDO).

```dbgcmd
!hidkd.hidpdo pdo
```

## Parameters


<span id="_______pdo______"></span><span id="_______PDO______"></span> *pdo*   
Address of a PDO. To get the addresses of PDOs that are associated with HID drivers, use the [**!usbhid.hidtree**](-hidkd-hidtree.md) command.

## DLL


Hidkd.dll

## Examples

Here is an example of the output of the **!hidpdo** command. The example first calls [**!hidtree**](-hidkd-hidtree.md) to get the address of a PDO.

```dbgcmd
0: kd> !hidkd.hidtree
HID Device Tree
...
FDO  VendorID:0x045E(Microsoft Corporation) ProductID:0x0745 Version:0x0634
...
    PDO  Generic Desktop Controls (0x01) | Mouse (0x02)
    !hidpdo 0xffffe000056281e0
    ...

0: kd> !hidpdo 0xffffe000056281e0
# PDO 0xffffe000056281e0  (!devobj/!devstack)

  Collection Num  : 1
  Name            : \Device\_HID00000002#COLLECTION00000001
  FDO             : !hidfdo 0xffffe00004f466e0
  Per-FDO IFR Log : !rcdrlogdump HIDCLASS -a 0xFFFFE0000594D000

  Usage Page      : Generic Desktop Controls (0x01)
  Usage           : Mouse (0x02)
  Report Length   : 0xa(Input) 0x0(Output) 0x2(Feature)
  Pre-parsed Data : 0xffffe00003742840
  Position in HID tree

  dt PDO_EXTENSION 0xffffe00005628350

## Power States

  Power States  : S0/D0
  Wait Wake IRP : !irp 0xffffe00004fc57d0 (pending on \Driver\HidUsb)
```

## See also


[HID Extensions](hid-extensions.md)


