---
title: usb3kd.xhci\_capability
description: The usb3kd.xhci\_capability extension displays the capabilities of a USB 3.0 host controller.
ms.assetid: 72D3919A-C111-4B16-8A52-B439429DFFCC
keywords: ["usb3kd.xhci_capability Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usb3kd.xhci_capability
api_type:
- NA
---

# !usb3kd.xhci\_capability


The [**!usb3kd.xhci\_capability**](-usb3kd-device-info.md) extension displays the capabilities of a USB 3.0 host controller.

```
!usb3kd.xhci_capability DeviceExtension
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the host controller's functional device object (FDO).

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The output the [**!xhci\_capability**](-usb3kd-device-info.md) command is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys). For more information about the USB 3.0 host controller driver and other drivers in the USB stack, see [USB Driver Stack Architecture](https://msdn.microsoft.com/library/windows/hardware/hh406256).

Examples
--------

To obtain the address of the device extension, look at the output of the [**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md) command. In the following example, the address of the device extension is 0xfffffa800536e2d0.

```
3: kd> !xhci_dumpall

## Dumping all the XHCI controllers - DrvObj 0xfffffa80053072f0
------------------------------------------------------------
1)  ... - PCI: VendorId ... DeviceId ... RevisionId ... Firmware ...

    dt USBXHCI!_CONTROLLER_DATA 0xfffffa80052f20c0
    !rcdrlogdump USBXHCI -a 0xfffffa8005068520
    !rcdrlogdump USBXHCI -a 0xfffffa8004e8b9a0 (rundown)
    !wdfdevice 0x57ffac91fd8
    !xhci_capability 0xfffffa800536e2d0
    ...
```

Now you can pass the address of the device extension to the **!xhci\_capability** command.

```
3: kd> !xhci_capability 0xfffffa800536e2d0

## Controller Capabilities
-----------------------
    dt USBXHCI!_REGISTER_DATA 0xfffffa8005362c00
    dt USBXHCI!_CAPABILITY_REGISTERS 0xfffff880046a8000
    MajorRevision.MinorRevision = 0.96
    Device Slots: 32
    Interrupters: 8
    Ports: 4
    IsochSchedulingThreshold: 1
    EventRingSegmentTableMax: 1 (2^ERST = 2)
    ScratchpadRestore: OFF
    MaxScratchpadBuffers: 0
    U1DeviceExitLatency: 0
    U2DeviceExitLatency: 0
    AddressingCapability: 64 bit
    BwNegotiationCapability: ON
    ContextSize: 32 bytes
    PortPowerControl: ON
    PortIndicators: OFF
    LightHCResetCapability: OFF
    LatencyToleranceMessagingCapability: ON
    NoSecondarySidSupport: TRUE
    MaximumPrimaryStreamArraySize = 4 ( 2^(MaxPSASize+1) = 32 )
    XhciExtendedCapabilities:
        [1] USB_LEGACY_SUPPORT: dt _USBLEGSUP 0xfffff880046a8500
        [2] Supported Protocol 0xfffff880046a8510, Version 3.0, Offset 1, Count 2, HighSpeedOnly OFF, IntegratedHub OFF, HardwareLPM OFF
        [3] Supported Protocol 0xfffff880046a8520, Version 2.0, Offset 3, Count 2, HighSpeedOnly OFF, IntegratedHub OFF, HardwareLPM OFF

## Software Supported Capabilities
-------------------------------
    DeviceSlots: 32
    Interrupters: 1
    Ports: 4
    MaxEventRingSegments: 2
    U1DeviceExitLatency: 0
    U2DeviceExitLatency: 0
    DeviceFlags:
        IgnoreBiosHandoffFailure
        SetLinkTrbChainBit
        UseSingleInterrupter
        DisableIdlePowerManagement
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usb3kd.xhci_capability%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





