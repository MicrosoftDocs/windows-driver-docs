---
title: usb3kd.xhci_registers
description: The usb3kd.xhci_registers extension displays the registers of a USB 3.0 host controller.
ms.assetid: C695C23D-B617-4D1E-87F8-62CF99426CA3
keywords: ["usb3kd.xhci_registers Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.xhci_registers
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.xhci\_registers


The [**!usb3kd.xhci\_registers**](-usb3kd-device-info.md) extension displays the registers of a USB 3.0 host controller.

```dbgcmd
!usb3kd.xhci_registers DeviceExtension
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the host controller's functional device object (FDO).

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The output the **!xhci\_registers** command is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys). For more information about the USB 3.0 host controller driver and other drivers in the USB stack, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkID=251983).

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
    ...
```

Now you can pass the address of the device extension to the **!xhci\_registers** command.

```dbgcmd
3: kd> !xhci_registers 0xfffffa800536e2d0

## Dumping controller registers
----------------------------

    dt USBXHCI!_OPERATIONAL_REGISTERS 0xfffff880046a8020

    DeviceContextBaseAddressArrayPointer: 00000001168b9000

    Command Registers
    -----------------
        RunStopBit: 1
        HostControllerReset: 0
        ...

    Status Registers
    ----------------
        HcHalted: 0
        HostSystemError: 0
        ...

    commandRingControl Registers
    ----------------------------
        RingCycleState: 0
        CommandStop: 0
        ...
    Runtime Registers
    -----------------
        dt USBXHCI!_RUNTIME_REGISTERS 0xfffff880046a8600
        MicroFrameIndex: 0x3f7a

        dt -ba8 USBXHCI!_INTERRUPTER_REGISTER_SET 0xfffff880046a8620

    RootPort Registers
    ------------------
        dt -a4 -r2 USBXHCI!_PORT_REGISTER_SET 0xfffff880046a8420
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






