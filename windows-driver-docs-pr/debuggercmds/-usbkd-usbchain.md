---
title: "!usbkd.usbchain"
description: "The !usbkd.usbchain command displays a USB device chain starting at a specified PDO, and going back to the root hub."
keywords: ["!usbkd.usbchain Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- usbkd.usbchain
api_type:
- NA
---

# !usbkd.usbchain

The **!usbkd.usbchain** command displays a USB device chain starting at a specified PDO, and going back to the root hub.

```dbgcmd
!usbkd.usbchain PDO
```

## Parameters

<span id="_______PDO______"></span><span id="_______pdo______"></span> *PDO*   
Address of the physical device object (PDO) of a device that is connected to a USB hub.

## DLL

Usbkd.dll

## Examples

Here is one way to find the address of the PDO of a USB device. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```dbgcmd
 kd> !usbkd.usb2tree
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
    RootHub !hub2_info ffffe000023201a0 !devstack ffffe00002320050
        Port 1: !port2_info ffffe000021bf000 
        Port 2: !port2_info ffffe000021bfb40 
        Port 3: !port2_info ffffe000021c0680 !devstack ffffe00007c882a0
...
```

In the preceding output, the address of the PDO is the argument of the suggested command **!devstack ffffe00007c882a0**. Pass the address of the PDO to **!usbkd.usbchain**.

```dbgcmd
0: kd> !usbkd.usbchain ffffe00007c882a0

usbchain
*****************************************************************************
HUB PDO ffffe00007c882a0 on port 3 !usbhubext ffffe00007c883f0 ArmedForWake = 0
VID Xxxx PID Xxxx REV 0100  Xxxx Corporation
    HUB #3 FDO ffffe00002320050 , !usbhubext ffffe000023201a0  HWC_ARM=0
    ROOT HUB PDO(ext) @ffffe0000213c1a0
        ROOT HUB FDO @ffffe00001ca1050, !usbhcdext ffffe00001ca11a0 PCI Vendor:Device:...
```

## See also

[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](../usbcon/index.md)
