---
title: usb3kd.device\_info
description: The usb3kd.device\_info command displays information about a USB device in the USB 3.0 tree.
ms.assetid: BD6D1562-2606-42C1-9EE6-D38D93D685DE
keywords: ["usb3kd.device_info Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usb3kd.device_info
api_type:
- NA
---

# !usb3kd.device\_info


The **!usb3kd.device\_info** command displays information about a USB device in the [USB 3.0 tree](usb-3-extensions.md#usb-3-tree).

``` syntax
!usb3kd.device_info DeviceContext
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceContext______"></span><span id="_______devicecontext______"></span><span id="_______DEVICECONTEXT______"></span> *DeviceContext*   
Address of the \_DEVICE\_CONTEXT structure that represents the device.

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

**!device\_info** and [**!ucx\_device**](-usb3kd-ucx-device.md) both display information about a device, but the information displayed is different. The output of **!device\_info** is from the point of view of the USB 3.0 hub driver, and the output of **!ucx\_device** is from the point of view of the USB host controller extension driver. For example, the **!device\_info** output includes information about configuration and interface descriptors, and **!ucx\_device** output includes information about endpoints.

Examples
--------

You can obtain the address of the device context structure by looking at the output of the [**!usb\_tree**](-usb3kd-usb-tree.md) command. In the following example, the address of the device context structure is 0xfffffa8005abd0c0.

```cmd
3: kd> !usb_tree

## Dumping HUB Tree - !drvObj 0xfffffa800597f770
--------------------------------------------

Topology
--------
1)  !xhci_info 0xfffffa80051d1940  ... - PCI: VendorId ...
    !hub_info 0xfffffa8005ad92d0 (ROOT)
    ...
## Enumerated Device List
----------------------
...

2) !device_info 0xfffffa8005abd0c0, !devstack fffffa80059c3800
    Current Device State: ConfiguredInD0
    Desc: ... USB Flash Drive
    ...
```

Now you can pass the address of the device context to the **!device\_info** command.

```cmd
3: kd> !device_info 0xfffffa8005abd0c0

## Dumping Device Information fffffa8005abd0c0
-------------------------------------------
dt USBHUB3!_DEVICE_CONTEXT 0xfffffa8005abd0c0
dt USBHUB3!_HUB_PDO_CONTEXT 0xfffffa8005b118d0
!idle_info 0xfffffa8005b11920 (dt USBHUB3!_ISM_CONTEXT 0xfffffa8005b11920)
Parent !hub_info 0xfffffa8005ad92d0 (dt USBHUB3!_HUB_FDO_CONTEXT 0xfffffa8005ad92d0)
!port_info 0xfffffa8005abe0c0 (dt USBHUB3!_PORT_CONTEXT 0xfffffa8005abe0c0)
!ucx_device 0xfffffa8005992840 !xhci_deviceslots 0xfffffa80051d1940 1

LPMState: U1IsEnabledForUpStreamPort U2IsEnabledForUpStreamPort U1Timeout: 38, U2Timeout: 3
DeviceFlags: HasContainerId NoBOSContainerId Removable HasSerialNumber MsOsDescriptorNotSupported NoWakeUpSupport DeviceIsSuperSpeedCapable 
DeviceHackFlags: WillDisableOnSoftRemove SkipSetIsochDelay WillResetOnResumeS0 DisableOnSoftRemove 

Descriptors:
dt _USB_CONFIGURATION_DESCRIPTOR 0xfffffa80053f9250
dt _USB_INTERFACE_DESCRIPTOR 0xfffffa80053f9259
ProductId: ... Flash Drive
DeviceDescriptor: VID ... PID ... REV 0a00,  Class: (0)(0) BcdUsb: 0300

UcxRequest: !wdfrequest 0x57ffa662948, 
ControlRequest: !wdfrequest 0x57ffa667798, !irp 0xfffffa8005997650 !urb 0xfffffa8005abd1c0, NumberOfBytes 0
Device working at SuperSpeed
Current Device State: ConfiguredInD0

Device State History: <Event> NewState (<Operation>(),..) :

    [16] <Yes> ConfiguredInD0
    ...
Device Event History:
    [10] TransferSuccess
    ...
```

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[**!usb3kd.device\_info\_from\_pdo**](-usb3kd-device-info-from-pdo.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usb3kd.device_info%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





