---
title: usb3kd.hub_info_from_fdo
description: The usb3kd.hub_info_from_fdo command displays information about a hub in the USB 3.0 tree.
ms.assetid: 07A1C3EC-76A9-49A5-8467-53FCE3667203
keywords: ["usb3kd.hub_info_from_fdo Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.hub_info_from_fdo
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.hub\_info\_from\_fdo


The **!usb3kd.hub\_info\_from\_fdo** command displays information about a hub in the [USB 3.0 tree](usb-3-extensions.md#usb-3-tree).

```dbgcmd
!usb3kd.hub_info_from_fdo DeviceObject
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceObject______"></span><span id="_______deviceobject______"></span><span id="_______DEVICEOBJECT______"></span> *DeviceObject*   
Address of the functional device object (FDO) that represents the hub.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Examples
--------

You can get the address of the FDO from the output of [**!usb\_tree**](-usb3kd-usb-tree.md) or from a variety of other debugger commands. For example, the [**!devstack**](-devstack.md) command displays the address of the FDO. In the following example, the address of the FDO is fffffa800597a660.

```dbgcmd
3: kd> !devnode 0 1 usbhub3
Dumping IopRootDeviceNode (= 0xfffffa8003609cc0)
DevNode 0xfffffa8005981730 for PDO 0xfffffa8004ffc550
...
3: kd> !devstack 0xfffffa8004ffc550
  !DevObj   !DrvObj            !DevExt   ObjectName
  fffffa800597a660  \Driver\USBHUB3    fffffa8005ad92d0  
> fffffa8004ffc550  \Driver\USBXHCI    fffffa8005251d00  USBPDO-0
...
```

Now you can pass the address of the FDO to the **!usb3kd.hub\_info\_from\_fdo** command.

```dbgcmd
 3: kd> !hub_info_from_fdo fffffa800597a660

## Dumping HUB Information fffffa800597a660
----------------------------------------
dt USBHUB3!_HUB_FDO_CONTEXT 0xfffffa8005ad92d0
!rcdrlogdump usbhub3 -a 0xfffffa8005ad8010
Capabilities: Initialized, Configured, HasOverCurrentProtection, SelectiveSuspendSupportedByParentStack, CannotWakeOnConnect, NotArmedForWake

Total number of ports: 4, HUB depth is 0
Number of 3.0 ports: 2 (Range 1 - 2)
Number of 2.0 ports: 2 (Range 3 - 4)

Descriptors:
    dt _USB_HUB_DESCRIPTOR 0xfffffa8005ad9728
    dt _USB_30_HUB_DESCRIPTOR 0xfffffa8005ad9728
    dt _USB_DEVICE_DESCRIPTOR 0xfffffa8005ad92d0
    dt _USB_CONFIGURATION_DESCRIPTOR 0xfffffa8005ad9770

List of PortContext: 4
    [1] !port_info 0xfffffa8005a5ca80    !device_info 0xfffffa8005b410c0
            Last Port Status(2.0): Connected Enabled Powered HighSpeedDeviceAttached
            Last Port Change: <none>
            Current Port(2.0) State: ConnectedEnabled.WaitingForPortChangeEvent
            Current Device State: ConfiguredInD0
         ...

Current Hub State: ConfiguredWithIntTransfer

Hub State History: <Event> NewState (<Operation>(),..) :

    [43] <OperationSuccess> ConfiguredWithIntTransfer 
    ...

Hub Event History:
    [ 0] PortEnableInterruptTransfer
    ...
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!usb3kd.hub\_info**](-usb3kd-hub-info.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






