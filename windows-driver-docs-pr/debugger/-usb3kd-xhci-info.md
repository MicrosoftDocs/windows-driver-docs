---
title: usb3kd.xhci_info
description: The usb3kd.xhci_info extension displays all the XHCI commands for an individual USB 3.0 host controller.
ms.assetid: C3C3B379-4871-4293-9C35-B64F3A5E1348
keywords: ["usb3kd.xhci_info Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.xhci_info
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.xhci\_info


The [**!usb3kd.xhci\_info**](-usb3kd-device-info.md) extension displays all the XHCI commands for an individual USB 3.0 host controller.

```dbgcmd
!usb3kd.xhci_info DeviceExtension
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the host controller's functional device object (FDO).

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The output the **!usb3kd.xhci\_info** command is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys). For more information about the USB 3.0 host controller driver and other drivers in the USB stack, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkID=251983).

Examples
--------

You can get address of the device extension from the [**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md) command or from a variety of other debugger commands. For example, the [**!devstack**](-devstack.md) command displays the address of the device extension. In the following example, the address of the device extension for the host controller's FDO is fffffa800536e2d0.

```dbgcmd
3: kd> !devnode 0 1 usbxhci
Dumping IopRootDeviceNode (= 0xfffffa8003609cc0)
DevNode 0xfffffa8003df3010 for PDO 0xfffffa8003dd5870
  InstancePath is "PCI\VEN_...
  ServiceName is "USBXHCI"
  ...

3: kd> !devstack 0xfffffa8003dd5870
  !DevObj   !DrvObj            !DevExt   ObjectName
  fffffa800534b060  \Driver\USBXHCI    fffffa800536e2d0  USBFDO-3
  fffffa8003db5790  \Driver\ACPI       fffffa8003701cb0  
> fffffa8003dd5870  \Driver\pci        fffffa8003dd59c0  NTPNP_PCI0020
...
```

Now you can pass the address of the device extension to the **!xhci\_info** command.

```dbgcmd
3: kd> !xhci_info 0xfffffa80`0536e2d0

## Dumping XHCI controller commands - DeviceExtension 0xfffffa800536e2d0
------------------------------------------------------------
 ... - PCI: VendorId ... DeviceId ... RevisionId ... Firmware ...

    dt USBXHCI!_CONTROLLER_DATA 0xfffffa80052f20c0
    !rcdrlogdump USBXHCI -a 0xfffffa8005068520
    !rcdrlogdump USBXHCI -a 0xfffffa8004e8b9a0 (rundown)
    !wdfdevice 0x57ffac91fd8
    !xhci_capability 0xfffffa800536e2d0
    !xhci_registers 0xfffffa800536e2d0
    !xhci_commandring 0xfffffa800536e2d0 (No commands are pending)
    !xhci_deviceslots 0xfffffa800536e2d0
    !xhci_eventring 0xfffffa800536e2d0
    !xhci_resourceusage 0xfffffa800536e2d0
    !pci 100 0x30 0x0 0x0
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






