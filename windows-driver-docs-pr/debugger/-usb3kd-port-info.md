---
title: usb3kd.port_info
description: The usb3kd.port_info command displays information about a USB port in the USB 3.0 tree.
ms.assetid: 78233FE5-981E-42C4-A100-198CAAA840A0
keywords: ["usb3kd.port_info Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.port_info
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.port\_info


The [**!usb3kd.port\_info**](-usb3kd-device-info.md) command displays information about a USB port in the [USB 3.0 tree](usb-3-extensions.md#usb-3-tree).

```dbgcmd
!usb3kd.port_info PortContext
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______PortContext______"></span><span id="_______portcontext______"></span><span id="_______PORTCONTEXT______"></span> *PortContext*   
Address of a \_PORT\_CONTEXT structure.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Examples
--------

To obtain the address of the port context, look at the output of the [**!usb\_tree**](-usb3kd-usb-tree.md) command. In the following example, the address of a port context is 0xfffffa8005abe0c0.

```dbgcmd
3: kd> !usb_tree

## Dumping HUB Tree - !drvObj 0xfffffa800597f770
--------------------------------------------

Topology
--------
1)  !xhci_info 0xfffffa80051d1940  ... - PCI: VendorId ...
    !hub_info 0xfffffa8005ad92d0 (ROOT)
        ...
        !port_info 0xfffffa8005abe0c0 !device_info 0xfffffa8005abd0c0 Desc: ... USB Flash Drive Speed: Super
```

Now you can pass the address of the port context to the **!port\_info** command.

```dbgcmd
3: kd> !port_info 0xfffffa8005abe0c0

## Dumping Port Context 0xfffffa8005abe0c0
---------------------------------------
dt USBHUB3!_PORT_CONTEXT 0xfffffa8005abe0c0
!hub_info 0xfffffa8005ad92d0 (dt _HUB_FDO_CONTEXT 0xfffffa8005ad92d0)
!device_info 0xfffffa8005abd0c0 (dt _DEVICE_CONTEXT 0xfffffa8005abd0c0)
!rcdrlogdump usbhub3 -a 0xfffffa8005abf6b0

PortNumber: 2
Last Port Status(3.0): Connected Enabled Powered
Last Port Change: <none>

CurrentPortEvent: PsmEventPortConnectChange
Current Port(3.0) State: ConnectedEnabled.WaitingForPortChangeEvent

Port(3.0) State History: <Event> NewState (<Operation>(),..) :

    [34] <Push> WaitingForPortChangeEvent 
    ...
Port Event History:
    [ 8] TransferSuccess
    ...  
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






