---
title: usb3kd.xhci_trb
description: The usb3kd.xhci_trb extension displays one or more transfer request blocks (TRBs) used by a USB 3.0 host controller
ms.assetid: 6EC90908-320E-4908-BE53-1AD01A81B140
keywords: ["usb3kd.xhci_trb Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.xhci_trb
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.xhci\_trb


The [**!usb3kd.xhci\_trb**](-usb3kd-device-info.md) extension displays one or more transfer request blocks (TRBs) used by a USB 3.0 host controller

```dbgcmd
!usb3kd.xhci_trb VirtualAddress Count
!usb3kd.xhci_trb PhysicalAddress Count 1
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______VirtualAddress______"></span><span id="_______virtualaddress______"></span><span id="_______VIRTUALADDRESS______"></span> *VirtualAddress*   
Virtual address of a TRB.

<span id="_______PhysicalAddress______"></span><span id="_______physicaladdress______"></span><span id="_______PHYSICALADDRESS______"></span> *PhysicalAddress*   
Physical address of a TRB.

<span id="_______Count______"></span><span id="_______count______"></span><span id="_______COUNT______"></span> *Count*   
The number of consecutive TRBs to display, starting at *VirtualAddress* or *PhysicalAddress*.

<span id="_______1______"></span> 1   
Specifies that the address is a physical address.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The output the [**!xhci\_trb**](-usb3kd-device-info.md) command is based on the data structures maintained by the USB 3.0 host controller driver (UsbXhci.sys). For more information about the USB 3.0 host controller driver and other drivers in the USB stack, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkID=251983).

Examples
--------

In the following example, **0x844d7c00** is the virtual address of a TRB. The **1** is the count, which specifies how many consecutive TRBs to display.

```dbgcmd
0: kd> !xhci_trb 0x844d7c00 1

        [  0] ISOCH        0x844d7c00 CycleBit 1 IOC 0 CH 1 BEI 0 InterrupterTarget 1 TransferLength  2688 TDSize  0 TBC 0 TLBPC 2 Frame 0x3D2
```

In the following example, **0x0dced7c00** is the physical address of a TRB. The **4** is the count, which specifies how many consecutive TRBs to display. The **1** specifies that the address is a physical address.

```dbgcmd
0: kd> !xhci_trb 0x0dced7c00 4 1

        [  0] ISOCH        0xdced7c00 CycleBit 1 IOC 0 CH 1 BEI 0 InterrupterTarget 1 TransferLength  2688 TDSize  0 TBC 0 TLBPC 2 Frame 0x3D2
        [  1] EVENT_DATA   0xdced7c10 CycleBit 1 IOC 1 CH 0 BEI 1 InterrupterTarget 1 Data 0x194c9bcf001b0001 PacketId 27 Frame 0x194c9bcf TotalBytes 2688
        [  2] ISOCH        0xdced7c20 CycleBit 1 IOC 0 CH 1 BEI 0 InterrupterTarget 1 TransferLength  1352 TDSize  2 TBC 0 TLBPC 2 Frame 0x3D2
        [  3] NORMAL       0xdced7c30 CycleBit 1 IOC 0 CH 1 BEI 0 InterrupterTarget 1 TransferLength  1336 TDSize  0
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






