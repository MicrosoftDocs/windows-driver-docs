---
title: usb3kd.hub\_info\_from\_fdo
description: The usb3kd.hub\_info\_from\_fdo command displays information about a hub in the USB 3.0 tree.
ms.assetid: 07A1C3EC-76A9-49A5-8467-53FCE3667203
keywords: ["usb3kd.hub_info_from_fdo Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usb3kd.hub_info_from_fdo
api_type:
- NA
---

# !usb3kd.hub\_info\_from\_fdo


The **!usb3kd.hub\_info\_from\_fdo** command displays information about a hub in the [USB 3.0 tree](usb-3-extensions.md#usb-3-tree).

```
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

```
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

```
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

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usb3kd.hub_info_from_fdo%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





