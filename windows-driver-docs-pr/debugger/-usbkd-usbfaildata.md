---
title: usbkd.usbfaildata
description: The usbkd.usbfaildata command displays the failure data (if any) stored for a USB device.
ms.assetid: 08FD3F82-73E3-4616-92EB-D562ECAB8A96
keywords: ["usbkd.usbfaildata Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.usbfaildata
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.usbfaildata


The **!usbkd.usbfaildata** command displays the failure data (if any) stored for a USB device.

```dbgcmd
!usbkd.usbfaildata PDO
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______PDO______"></span><span id="_______pdo______"></span> *PDO*   
Address of the physical device object (PDO) of a device that is connected to a USB hub.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the PDO of a USB device. Enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

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

In the preceding output, the address of the PDO appears as the argument of the suggested command **!devstack ffffe00007c882a0**.

Now pass the address of the PDO to **!usbkd.usbfaildata**.

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






