---
title: usb3kd-xhci_findowner
description: The usb3kd.xhci_findowner command finds the owner a common buffer.
ms.assetid: 6AA3E41C-5838-4425-B1CE-37A13E8F755E
keywords: ["usb3kd.xhci_findowner Windows Debugging"]
ms.author: domars
ms.date: 10/18/2018
topic_type:
- apiref
api_name:
- usb3kd.xhci_findowner
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.xhci\_findowner


The **!usb3kd.xhci\_findowner** command finds the owner a common buffer.

```dbgcmd
!usb3kd.xhci_findowner Address
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Virtual or physical address of a common buffer.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

A common buffer is a block of physically contiguous memory that’s addressable by hardware. The USB 3.0 driver stack uses common buffers to communicate with USB 3.0 host controllers. Suppose the system crashes, and you come across an address that you suspect might be common buffer memory. If the address is common buffer memory, this command tells you which USB 3.0 host controller the memory belongs to (in case you that you have more than one USB 3.0 controller) and what the memory is used for.

Examples
--------

The following example calls [**!xhci\_resourceusage**](-usb3kd-xhci-resourceusage.md) to list the addresses of some common buffers.

```dbgcmd
0: kd> !usb3kd.xhci_resourceusage 0x867fbff0

## Dumping CommonBuffer Resources
------------------------------
    dt USBXHCI!_COMMON_BUFFER_DATA 0x868d61c0
    DmaEnabler:!wdfdmaenabler 0x79729fe8

    CommonBuffers Large: Total 8 Available 2 Used 6 TotalBytes 32768
        [ 1] dt _TRACKING_DATA 0x868d73a4 VA 0x868e0000 LA 0xdb2e0000 -- Owner 0x86801690 Tag: Int2 Size 4096
        [ 2] dt _TRACKING_DATA 0x868d6d1c VA 0x868e1000 LA 0xdb2e1000 -- Owner 0x86801690 Tag: Int2 Size 4096
        [ 3] dt _TRACKING_DATA 0x868d6c54 VA 0x868e2000 LA 0xdb2e2000 -- Owner 0x86801690 Tag: Int2 Size 4096
        [ 4] dt _TRACKING_DATA 0x868d6b8c VA 0x868e3000 LA 0xdb2e3000 -- Owner 0x86801690 Tag: Int2 Size 4096
        [ 5] dt _TRACKING_DATA 0x868d67b4 VA 0x868e5000 LA 0xdb2e5000 -- Owner 0x86801548 Tag: Slt1 Size 4096
        [ 6] dt _TRACKING_DATA 0x868d50b4 VA 0x868e6000 LA 0xdb2e6000 -- Owner 0x86801548 Tag: Slt3 Size 4096

    CommonBuffers Small: Total 16 Available 13 Used 3 TotalBytes 8192
        [ 1] dt _TRACKING_DATA 0x868d6974 VA 0x868e4000 LA 0xdb2e4000 -- Owner 0x86801690 Tag: Int1 Size 512
        [ 2] dt _TRACKING_DATA 0x868d69a4 VA 0x868e4200 LA 0xdb2e4200 -- Owner 0x86801548 Tag: Slt2 Size 512
        [ 3] dt _TRACKING_DATA 0x868d69d4 VA 0x868e4400 LA 0xdb2e4400 -- Owner 0x86801488 Tag: Cmd1 Size 512
```

One of the virtual addresses listed in the preceding output is 0x868e2000. The following example passes that address to **!xhci\_findowner**. One of the physical addresses listed in the preceding output is 0xdb2e4400. The following example passes 0xdb2e4440 (offset 0x40 bytes from 0xdb2e4400) to **!xhci\_findowner**.

```dbgcmd
0: kd> !xhci_findowner 0x868e2000 

!xhci_info 0x867fbff0  Texas Instruments - PCI: VendorId 0x104c DeviceId 0x8241 RevisionId 0x02

    dt _TRACKING_DATA 0x868d6c54 VA 0x868e2000 LA 0xdb2e2000 -- Owner 0x86801690 Tag: Int2 Size 4096

    dt _INTERRUPTER_DATA 0x86801690 
    !xhci_eventring 0x867fbff0  <-- This memory is used for event ring.


0: kd> !xhci_findowner 0xdb2e4440  <-- Note the offset difference.

!xhci_info 0x867fbff0  Texas Instruments - PCI: VendorId 0x104c DeviceId 0x8241 RevisionId 0x02

    dt _TRACKING_DATA 0x868d69d4 VA 0x868e4400 LA 0xdb2e4400 -- Owner 0x86801488 Tag: Cmd1 Size 512

    dt _COMMAND_DATA 0x86801488 
    !xhci_commandring 0x867fbff0  <-- This memory is used for command ring.
```

The **!xhci\_findowner** command is especially useful when you have an address in a transfer request block (TRB), and you want to track it back to the device slot that it belongs to. In the following example, one of the addresses listed in the output of [**!xhci\_transferring**](-usb3kd-xhci-transferring.md) is 0xda452230, which is the physical address of a TRB. The example passes that address to **!xhci\_findowner**. The output shows that the TRB belongs to device slot 8 (**!xhci\_deviceslots 0x8551d370 8**).

```dbgcmd
0: kd> !usb3kd.xhci_transferring 0x87652200

        [  0] NORMAL       0xda452200 CycleBit 1 IOC 0 BEI 0 InterrupterTarget 2 TransferLength     6 TDSize  0
        [  1] EVENT_DATA   0xda452210 CycleBit 1 IOC 1 BEI 0 InterrupterTarget 2 Data 0x8511375c TotalBytes 6
        [  2] NORMAL       0xda452220 CycleBit 1 IOC 0 BEI 0 InterrupterTarget 2 TransferLength     6 TDSize  0
        [  3] EVENT_DATA   0xda452230 CycleBit 1 IOC 1 BEI 0 InterrupterTarget 2 Data 0x857d076c TotalBytes 6

0: kd> !xhci_findowner 0xda452230 

!xhci_info 0x8551d370  Renesas - PCI: VendorId 0x1912 DeviceId 0x0015 RevisionId 0x02 Firmware 0x0020.0006

    dt _TRACKING_DATA 0x8585fd5c VA 0x87652200 LA 0xda452200 -- Owner 0x85894548 Tag: Rng1 Size 512

    !xhci_deviceslots 0x8551d370 8

    [0] dt _TRANSFERRING_DATA 0x85894548 Events: 0x0 TransferRingState_Idle
    ------------------------------------------------------------------------------
        WdfQueue: !wdfqueue 0x7a76bcb0 (0 waiting)
        CurrentRingBufferData: VA 0x87652200 LA 0xda452200 !wdfcommonbuffer 0x7a7a0370 Size 512
        Current:  !xhci_transferring 0x87652200
        PendingTransferList: 
            [0] dt _TRANSFER_DATA 0x851136f0 !urb 0x84e55468 !wdfrequest 0x7aeec9e8 TransferState_Pending
            [1] dt _TRANSFER_DATA 0x857d0700 !urb 0x85733be8 !wdfrequest 0x7a82f9d8 TransferState_Pending
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!xhci\_dumpall**](-usb3kd-xhci-dumpall.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






