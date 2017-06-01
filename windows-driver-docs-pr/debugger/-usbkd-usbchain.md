---
title: usbkd.usbchain
description: The usbkd.usbchain command displays a USB device chain starting at a specified PDO, and going back to the root hub.
ms.assetid: 0D69E29E-3886-436F-B5EE-E4F297D9CE36
keywords: ["usbkd.usbchain Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbchain
api_type:
- NA
---

# !usbkd.usbchain


The **!usbkd.usbchain** command displays a USB device chain starting at a specified PDO, and going back to the root hub.

```
!usbkd.usbchain PDO
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______PDO______"></span><span id="_______pdo______"></span> *PDO*   
Address of the physical device object (PDO) of a device that is connected to a USB hub.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the PDO of a USB device. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
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

```
0: kd> !usbkd.usbchain ffffe00007c882a0

usbchain
*****************************************************************************
HUB PDO ffffe00007c882a0 on port 3 !usbhubext ffffe00007c883f0 ArmedForWake = 0
VID Xxxx PID Xxxx REV 0100  Xxxx Corporation
    HUB #3 FDO ffffe00002320050 , !usbhubext ffffe000023201a0  HWC_ARM=0
    ROOT HUB PDO(ext) @ffffe0000213c1a0
        ROOT HUB FDO @ffffe00001ca1050, !usbhcdext ffffe00001ca11a0 PCI Vendor:Device:...
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbchain%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





