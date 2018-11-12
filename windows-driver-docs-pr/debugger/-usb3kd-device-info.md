---
title: usb3kd.device_info
description: The usb3kd.device_info command displays information about a USB device in the USB 3.0 tree.
ms.assetid: BD6D1562-2606-42C1-9EE6-D38D93D685DE
keywords: ["usb3kd.device_info Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usb3kd.device_info
api_type:
- NA
ms.localizationpriority: medium
---

# !usb3kd.device\_info


The **!usb3kd.device\_info** command displays information about a USB device in the [USB 3.0 tree](usb-3-extensions.md#usb-3-tree).

```dbgcmd
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

```dbgcmd
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

```dbgcmd
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

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






