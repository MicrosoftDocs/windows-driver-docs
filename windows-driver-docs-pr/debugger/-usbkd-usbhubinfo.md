---
title: usbkd.usbhubinfo
description: The usbkd.hubinfo command displays information about a USB hub.
ms.assetid: 01FF5822-0FCF-420F-AFF7-C91448DCBB98
keywords: ["usbkd.usbhubinfo Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbhubinfo
api_type:
- NA
---

# !usbkd.usbhubinfo


The **!usbkd.hubinfo** command displays information about a USB hub.

```
!usbkd.hubinfo FDO
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______FDO______"></span><span id="_______fdo______"></span> *FDO*   
Address of the functional device object (FDO) for a USB hub.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the FDO for a USB hub. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
0: kd> !usbkd.usb2tree
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
    RootHub !hub2_info ffffe000023201a0 !devstack ffffe00002320050
```

In the preceding output, the address of the FDO for the hub appears as the argument of the suggested command **!devstack ffffe00002320050**.

Now pass the address of the FDO to the **!usbhubinfo** command.

```
0: kd> !usbkd.usbhubinfo ffffe00002320050

    !DevObj ffffe00002320050 !usbhubext ffffe000023201a0 
On Host Controller (0x8086, 0x293c) 
        Stat_AsyncResumeStartAt: 2437ee39d29bd528
        Stat_AsyncResumeCompleteAt: 24413c77d29bd528
        Stat_AsyncResume: 0x3c(60) ms
        Stat_SyncResumeStartAt: 2437ee39d29bd528
        Stat_SyncResumeCompleteAt: 2437ee39d29bd528
        Stat_SyncResume: 0x0(0) ms
Trap Regs: Event, Port, Event (ffffe000023204d0) 
    Enable: 0 Port: 0 Event 00000000
Hub Number: # 3
Number Of Ports: 4
dt usbhub!_USBHUB_FDO_FLAGS ffffe00002320ba0
>Is Root
>Power Switching: 
     No Power Switching 
>Overcurrent: 
     Global Overcurrent 
>PortIndicators: 
     No PortIndicators present
>AllowWakeOnConnect: 
     DO NOT WakeOnConnect
>CURRENT Hub Wake on Connectstate: 
     HWC_DISARM:- do not wake system on connect/disconnect event
>CURRENT Bus Wake state: 
     BUS_DISARM:- bus not armed for wake by this hub
>CURRENT Wake Detect state (WW Irp): 
     HUB_DISARM:- no ww irp pending (HUB_WAKESTATE_DISARMED)
Milliamps/Port : 500ma
Power caps (0 = not reported)
     PortPower_Registry : 0
     PortPower_DeviceStatus : 500
     PortPower_CfgDescriptor : 500
     PortPower_HubStatus : 500
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbhubinfo%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





