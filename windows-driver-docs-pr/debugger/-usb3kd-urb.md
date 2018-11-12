---
title: usb3kd.urb
description: The usb3kd.urb extension displays information about a USB request block (URB).
ms.assetid: B4583F32-BBC9-4182-A403-9C43BBD9BA4F
keywords: ["usb3kd.urb Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.urb
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.urb


The [**!usb3kd.urb**](-usb3kd-device-info.md) extension displays information about a USB request block (URB).

```dbgcmd
!usb3kd.urb UrbAddress
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______UrbAddress______"></span><span id="_______urbaddress______"></span><span id="_______URBADDRESS______"></span> *UrbAddress*   
Address of the URB.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Examples
--------

The following example shows the address of a URB (0xfffffa8005a2cbe8) in the output of the [**!xhci\_deviceslots**](-usb3kd-xhci-deviceslots.md) command.

```dbgcmd
3: kd> !xhci_deviceslots 0xfffffa800520d2d0

## Dumping dt _DEVICESLOT_DATA 0xfffffa8003612e80
----------------------------------------------
DeviceContextBase: VA 0xfffffa8005a64000 LA 0x116864000 !wdfcommonbuffer 0x57ffa7ca758 Size 4096

## [1] SlotID : dt USBXHCI!_USBDEVICE_DATA 0xfffffa80059027d0 dt _SLOT_CONTEXT32 0xfffffa8005a65000
------------------------------------------------------------------------------------------------
    USB\VID_...
    SlotEnabled IsDevice NumberOfTTs 0 TTThinkTime 0
    ...
            PendingTransferList: 
                [0] dt _TRANSFER_DATA 0xfffffa80059727f0 !urb 0xfffffa8005a2cbe8 !wdfrequest 0x57ffa68d998 TransferState_Pending
    ...
```

The following example passes the address of the URB to the **!usb3kd.urb** command.

```dbgcmd
3: kd> !urb 0xfffffa8005a2cbe8

## Dumping URB 0xfffffa8005a2cbe8
------------------------------
Function:         URB_FUNCTION_BULK_OR_INTERRUPT_TRANSFER (0x9)
UsbdDeviceHandle: 
    !ucx_device 0xfffffa8005901840
    !xhci_deviceslots 0xfffffa800520d2d0 1

Status:           USBD_STATUS_PENDING (0x40000000)
UsbdFlags:        (0x0)
dt _URB_BULK_OR_INTERRUPT_TRANSFER 0xfffffa8005a2cbe8
PipeHandle:            0xfffffa800596f720
TransferFlags:         (0x1) USBD_TRANSFER_DIRECTION_IN
TransferBufferLength:  0x0
TransferBuffer:        0xfffffa8005a2cc88
TransferBufferMDL:     0xfffffa8005848930
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






