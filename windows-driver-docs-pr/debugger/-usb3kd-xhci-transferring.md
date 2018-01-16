---
title: usb3kd.xhci_transferring
description: The usb3kd.xhci_transferring extension displays a transfer ring (used by a USB 3.0 host controller) until it detects a cycle bit change.
ms.assetid: BCF6DEF0-FB58-4FE6-88AD-BF778E00F052
keywords: ["usb3kd.xhci_transferring Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usb3kd.xhci_transferring
api_type:
- NA
---

# !usb3kd.xhci\_transferring


The [**!usb3kd.xhci\_transferring**](-usb3kd-device-info.md) extension displays a transfer ring (used by a USB 3.0 host controller) until it detects a cycle bit change.

```
!usb3kd.xhci_transferring VirtualAddress
!usb3kd.xhci_transferring PhysicalAddress 1
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______VirtualAddress______"></span><span id="_______virtualaddress______"></span><span id="_______VIRTUALADDRESS______"></span> *VirtualAddress*   
Virtual address of the transfer ring.

<span id="_______PhysicalAddress______"></span><span id="_______physicaladdress______"></span><span id="_______PHYSICALADDRESS______"></span> *PhysicalAddress*   
Physical address of the transfer ring.

<span id="_______1______"></span> 1   
Specifies that the address is a physical address.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The output of the **!xhci\_transferring** command is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys). For more information about the USB 3.0 host controller driver and other drivers in the USB stack, see [USB Driver Stack Architecture](http://go.microsoft.com/fwlink/p?LinkID=251983).

The transfer ring is a structure used by the USB 3.0 host controller driver to maintain a list of transfer request blocks (TRBs). This command takes the virtual or physical address of a transfer ring, but displays the physical address of the TRBs. This is done so the command can correctly traverse LINK TRBs.

Examples
--------

To obtain the address of the transfer ring, look at the output of the [**!xhci\_deviceslots**](-usb3kd-xhci-deviceslots.md) command. In the following example, the virtual address of the transfer ring is 0xfffffa8005b2fe00.

```
3: kd> !usb3kd.xhci_deviceslots 0xfffffa800523a2d0

## Dumping dt _DEVICESLOT_DATA 0xfffffa80051a3300
----------------------------------------------
DeviceContextBase: VA 0xfffffa8005a41000 LA 0x116841000 !wdfcommonbuffer 0x57ffa6ff9b8 Size 4096

## [1] SlotID : dt USBXHCI!_USBDEVICE_DATA 0xfffffa800598c7d0 dt _SLOT_CONTEXT32 0xfffffa8005a42000
------------------------------------------------------------------------------------------------
    USB\VID_125F&PID_312A ADATA Technology Co., Ltd.
    SlotEnabled IsDevice NumberOfTTs 0 TTThinkTime 0
    Speed: Super PortPathDepth: 1 PortPath: [ 2 ] DeviceAddress: 1
    !device_info_from_pdo 0xfffffa800597d720
    DeviceContextBuffer: VA 0xfffffa8005a42000 LA 0x116842000 !wdfcommonbuffer 0x57ffa7009b8 Size 4096
    InputDeviceContextBuffer: VA 0xfffffa8005b2d000 LA 0x11692d000 !wdfcommonbuffer 0x57ffa674958 Size 4096
    ...

    [3] DeviceContextIndex : dt USBXHCI!_ENDPOINT_DATA 0xfffffa8005b394e0 dt _ENDPOINT_CONTEXT32 0xfffffa8005a42060 ES_RUNNING
    --------------------------------------------------------------------------------------------------------------
       ...
            CurrentRingBufferData: VA 0xfffffa8005b2fe00 LA 0x11692fe00 !wdfcommonbuffer 0x57ffa67c988 Size 512
            Current:  !xhci_transferring 0xfffffa8005b2fe00
            PendingTransferList: 
                [0] dt _TRANSFER_DATA 0xfffffa8005b961b0 !urb 0xfffffa8005b52be8 !wdfrequest 0x57ffa469fd8 TransferState_Pending
```

Now you can pass the address of the transfer ring to the **!xhci\_transferring** command.

```
kd> !xhci_transferring 0xfffffa8005b2fe00

        [  0] NORMAL       0x000000011692fe00 CycleBit 1 IOC 0 BEI 0 InterrupterTarget 0 TransferLength    13 TDSize  0
        [  1] EVENT_DATA   0x000000011692fe10 CycleBit 1 IOC 1 BEI 0 InterrupterTarget 0 Data  0 0xfffffa8005986850 TotalBytes 13
        [  2] NORMAL       0x000000011692fe20 CycleBit 1 IOC 0 BEI 0 InterrupterTarget 0 TransferLength    13 TDSize  0
        [  3] EVENT_DATA   0x000000011692fe30 CycleBit 1 IOC 1 BEI 0 InterrupterTarget 0 Data  0 0xfffffa8005b96210 TotalBytes 13
        [  4] NORMAL       0x000000011692fe40 CycleBit 1 IOC 0 BEI 0 InterrupterTarget 0 TransferLength    13 TDSize  0
        [  5] EVENT_DATA   0x000000011692fe50 CycleBit 1 IOC 1 BEI 0 InterrupterTarget 0 Data  0 0xfffffa8005b96210 TotalBytes 13
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usb3kd.xhci_transferring%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





