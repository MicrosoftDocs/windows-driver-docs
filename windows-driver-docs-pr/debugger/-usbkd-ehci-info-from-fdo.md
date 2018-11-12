---
title: usbkd.ehci_info_from_fdo
description: The usbkd.ehci_info_from_fdo command displays information about a USB host controller.
ms.assetid: C7026EF3-F58D-45EB-83D5-8B4A3E661759
keywords: ["usbkd.ehci_info_from_fdo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd.ehci_info_from_fdo
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.ehci\_info\_from\_fdo


The [**!usbkd.ehci\_info\_from\_fdo**](https://msdn.microsoft.com/library/windows/hardware/dn367058) command displays information about a USB host controller.

```dbgcmd
!usbkd.ehci_info_from_fdo fdo
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______fdo______"></span><span id="_______FDO______"></span> *fdo*   
Address of the functional device object (FDO) of a UHCI or EHCI USB host controller. You can get the address of the FDO from the output of the [**!usb2tree**](-usbkd-usb2tree.md) command.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

First use the [**!usb2tree**](-usbkd-usb2tree.md) command to get the address of the FDO.

```dbgcmd
0: kd> !usbkd.usb2tree

EHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001f48bd0

1)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
...
```

In the preceding output, you can see that the address of the FDO of the USB host controller is `ffffe00001ca1050`. Pass the address of the FDO to [**!ehci\_info\_from\_fdo**](https://msdn.microsoft.com/library/windows/hardware/dn367058).

```dbgcmd
0: kd> !usbkd.ehci_info_from_fdo ffffe00001ca1050

HC Flavor 1000  FDO ffffe00001ca1050
Root Hub: FDO ffffe00002320050 !hub2_info ffffe000023201a0
Operational Registers ffffd000228bf020
Device Data ffffe00001ca2da0
dt USBPORT!_FDO_EXTENSION ffffe00001ca15a0
DM Timer Flags ffffe00001ca16d4
FDO Flags ffffe00001ca16d0
HCD Log ffffe00001ca11a0

DeviceHandleList: !usblist ffffe00001ca23b8, DL 
DeviceHandleDeletedList: !usblist ffffe00001ca23c8, DL [Empty]
GlobalEndpointList: !usblist ffffe00001ca2388, EP 
EpNeoStateChangeList: !usblist ffffe00001ca2370, SC [Empty]
GlobalTtListHead: !usblist ffffe00001ca23a8, TT [Empty]
BusContextHead: !usblist ffffe00001ca16b0, BC 

## Pending Requests

[001] dt USBPORT!_USB_IOREQUEST_CONTEXT ffffe00001ca1450 Tag: AddD Obj: ffffe00001ca11a0
...

## XDPC List

01) dt USBPORT!_XDPC_CONTEXT ffffe00001ca1f18
...

## PnP FUNC HISTORY (latest at bottom)

[01] IRP_MN_QUERY_CAPABILITIES
...
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






