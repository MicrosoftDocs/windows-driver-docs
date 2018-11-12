---
title: usb3kd.xhci_resourceusage
description: The usb3kd.xhci_resourceusage extension displays the resources used by a USB 3.0 host controller.
ms.assetid: 6AAB64D6-3CDA-4BA2-BBA8-F2F5AD1DBB6F
keywords: ["usb3kd.xhci_resourceusage Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.xhci_resourceusage
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.xhci\_resourceusage


The [**!usb3kd.xhci\_resourceusage**](-usb3kd-device-info.md) extension displays the resources used by a USB 3.0 host controller.

```dbgcmd
!usb3kd.xhci_resourceusage DeviceExtension
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the host controller's functional device object (FDO).

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The output the **!xhci\_resourceusage** command is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys). For more information about the USB 3.0 host controller driver and other drivers in the USB stack, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkID=251983).

Examples
--------

To obtain the address of the device extension, look at the output of the [**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md) command. In the following example, the address of the device extension is 0xfffffa800536e2d0.

```dbgcmd
3: kd> !xhci_dumpall

## Dumping all the XHCI controllers - DrvObj 0xfffffa80053072f0
------------------------------------------------------------
1)  ... - PCI: VendorId ... DeviceId ... RevisionId ... Firmware ...

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
    ...
```

Now you can pass the address of the device extension to the **!xhci\_resourceusage** command.

```dbgcmd
 3: kd> !xhci_resourceusage 0xfffffa800536e2d0

## Dumping CommonBuffer Resources
------------------------------
    dt USBXHCI!_COMMON_BUFFER_DATA 0xfffffa80059a5920
    DmaEnabler:!wdfdmaenabler 0x57ffa65a9c8

    CommonBuffers Large: Total 9 Available 2 Used 7 TotalBytes 36864
        [ 1] dt _TRACKING_DATA 0xfffffa80059a6768 VA 0xfffffa8005370000 LA 0x117170000 ...
        [ 2] dt _TRACKING_DATA 0xfffffa80059a4768 VA 0xfffffa8005373000 LA 0x117173000 ...
        ...
    CommonBuffers Small: Total 32 Available 8 Used 24 TotalBytes 16384
        [ 1] dt _TRACKING_DATA 0xfffffa80059a2798 VA 0xfffffa8005aeb000 LA 0x1168eb000 ...
        [ 2] dt _TRACKING_DATA 0xfffffa80059a27e8 VA 0xfffffa8005aeb200 LA 0x1168eb200 ...
        ...
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






