---
title: usbkd.usbdpc
description: The usbkd.usbdpc command displays information stored in an _XDPC_CONTEXT structure.
ms.assetid: 51ED1BB0-416B-4B2B-9F4D-61F841224126
keywords: ["usbkd.usbdpc Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbdpc
api_type:
- NA
---

# !usbkd.usbdpc


The **!usbkd.usbdpc** command displays information stored in an **\_XDPC\_CONTEXT** structure.

```
!usbkd.usbdpc StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbport!\_XDPC\_CONTEXT** structure. To get the XDPC list for a USB host controller, use the [**!usbkd.usbhcdext**](-usbkd-usbhcdext.md) command.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of a **usbport!\_XDPC\_CONTEXT** structure. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
0: kd> !usbkd.usb2tree
...
UHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001e77010
...
4)!uhci_info ffffe00001c7d1a0 !devobj ffffe00001c7d050 PCI: VendorId...
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!uhci\_info ffffe00001c7d1a0**.

Either click the DML command or pass the address of the device extension to [**!usbhcdext**](https://msdn.microsoft.com/library/windows/hardware/dn367072) to get the XDPC list.

```
0: kd> !usbkd.usbhcdext ffffe00001c7d1a0
...
## XDPC List

01) dt USBPORT!_XDPC_CONTEXT ffffe00001c7df18
02) dt USBPORT!_XDPC_CONTEXT ffffe00001c7db88
03) dt USBPORT!_XDPC_CONTEXT ffffe00001c7dd50
04) dt USBPORT!_XDPC_CONTEXT ffffe00001c7e0e0
...
```

In the preceding output, `ffffe00001c7df18` is the address of an **\_XDPC\_CONTEXT** structure. Pass this address to **!usbdpc**.

```
0: kd> !usbkd.usbdpc ffffe00001c7df18

dt USBPORT!_XDPC_CONTEXT ffffe00001c7df18

## XDPC HISTORY (latest at boottom)

##      EVENT                STATE                   NEXT

[01] Ev_Xdpc_End          XDPC_Running            XDPC_Enabled            
[02] Ev_Xdpc_Signal       XDPC_Enabled            XDPC_DpcQueued          
[03] Ev_Xdpc_Signal       XDPC_DpcQueued          XDPC_DpcQueued          
[04] Ev_Xdpc_Worker       XDPC_DpcQueued          XDPC_Running            
[05] Ev_Xdpc_Signal       XDPC_Running            XDPC_Signaled           
[06] Ev_Xdpc_End          XDPC_Signaled           XDPC_DpcQueued          
[07] Ev_Xdpc_Worker       XDPC_DpcQueued          XDPC_Running            
[08] Ev_Xdpc_End          XDPC_Running            XDPC_Enabled
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbdpc%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





