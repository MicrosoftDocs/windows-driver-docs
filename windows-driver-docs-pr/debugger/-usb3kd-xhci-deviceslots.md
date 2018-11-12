---
title: usb3kd.xhci_deviceslots
description: The usb3kd.xhci_deviceslots extension displays information about the devices connected to a USB 3.0 host controller.
ms.assetid: 471167EA-F7F8-470D-B09C-8627C5BE9566
keywords: ["usb3kd.xhci_deviceslots Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.xhci_deviceslots
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.xhci\_deviceslots


The [**!usb3kd.xhci\_deviceslots**](-usb3kd-device-info.md) extension displays information about the devices connected to a USB 3.0 host controller.

```dbgcmd
!usb3kd.xhci_deviceslots DeviceExtension [SlotNumber] [verbose]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the host controller's functional device object (FDO).

<span id="_______SlotNumber______"></span><span id="_______slotnumber______"></span><span id="_______SLOTNUMBER______"></span> *SlotNumber*   
Slot number of the device to be displayed. If this parameter is omitted, all devices are displayed.

<span id="_______verbose______"></span><span id="_______VERBOSE______"></span> **verbose**   
The display is verbose.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The output the **!xhci\_deviceslots** command is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys). For more information about the USB 3.0 host controller driver and other drivers in the USB stack, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkID=251983).

The USB 3.0 host controller driver maintains a list of data structures that represent the devices connected to the controller. Each of these data structures is identified by a slot number.

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
    ...
```

Now you can pass the address of the device extension to the **!usb3kd.xhci\_deviceslots** command.

```dbgcmd
3: kd> !xhci_deviceslots 0xfffffa800536e2d0

## Dumping dt _DEVICESLOT_DATA 0xfffffa8005226220
----------------------------------------------
DeviceContextBase: VA 0xfffffa8005ab9000 LA 0x1168b9000 !wdfcommonbuffer 0x57ffa65c9b8 Size 4096

## [1] SlotID : dt USBXHCI!_USBDEVICE_DATA 0xfffffa8005a427d0 dt _SLOT_CONTEXT32 0xfffffa8005aba000
------------------------------------------------------------------------------------------------
    USB\VID_125F&PID_312A ADATA Technology Co., Ltd.
    SlotEnabled IsDevice NumberOfTTs 0 TTThinkTime 0
    Speed: Super PortPathDepth: 1 PortPath: [ 2 ] DeviceAddress: 1
    !device_info_from_pdo 0xfffffa8005a36800
    DeviceContextBuffer: VA 0xfffffa8005aba000 LA 0x1168ba000 !wdfcommonbuffer 0x57ffa656948 Size 4096
    InputDeviceContextBuffer: VA 0xfffffa8005b65000 LA 0x116965000 !wdfcommonbuffer 0x57ffa5be958 Size 4096

    [1] DeviceContextIndex : dt USBXHCI!_ENDPOINT_DATA 0xfffffa8005a126f0 dt _ENDPOINT_CONTEXT32 0xfffffa8005aba020 ES_RUNNING
    --------------------------------------------------------------------------------------------------------------
        EndpointType_Control Address: 0x0 PacketSize: 512 Interval: 0
        !ucx_endpoint 0xfffffa8005a3f710
        RecorderLog: !rcdrlogdump USBXHCI -a 0xfffffa8005b60010

        [0] dt _TRANSFERRING_DATA 0xfffffa8005b64ec0 Events: 0x0 TransferRingState_Idle
     ...

## [2] SlotID : dt USBXHCI!_USBDEVICE_DATA 0xfffffa80052de320 dt _SLOT_CONTEXT32 0xfffffa8005b8b000
------------------------------------------------------------------------------------------------
    USB\VID_18A5&PID_0304 Verbatim Americas LLC
    SlotEnabled IsDevice NumberOfTTs 0 TTThinkTime 0
    Speed: High PortPathDepth: 1 PortPath: [ 3 ] DeviceAddress: 2
    !device_info_from_pdo 0xfffffa80058fb800
    DeviceContextBuffer: VA 0xfffffa8005b8b000 LA 0x11698b000 !wdfcommonbuffer 0x57ffa426b18 Size 4096
    InputDeviceContextBuffer: VA 0xfffffa8005b8c000 LA 0x11698c000 !wdfcommonbuffer 0x57ffadbe3c8 Size 4096

    [1] DeviceContextIndex : dt USBXHCI!_ENDPOINT_DATA 0xfffffa800714b050 dt _ENDPOINT_CONTEXT32 0xfffffa8005b8b020 ES_RUNNING
    --------------------------------------------------------------------------------------------------------------
        EndpointType_Control Address: 0x0 PacketSize: 64 Interval: 0
        !ucx_endpoint 0xfffffa80036a20c0
        RecorderLog: !rcdrlogdump USBXHCI -a 0xfffffa8005bd0b60

        [0] dt _TRANSFERRING_DATA 0xfffffa8004ed8df0 Events: 0x0 TransferRingState_Idle
        ------------------------------------------------------------------------------
    ...
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






