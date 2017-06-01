---
title: usbkd.usbpdos
description: The usbkd.usbpdos command displays information about all physical device objects (PDOs) created by the USB hub driver.
ms.assetid: 2EFAC774-C400-4218-BF48-2D5DC557A83B
keywords: ["usbkd.usbpdos Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbpdos
api_type:
- NA
---

# !usbkd.usbpdos


The **!usbkd.usbpdos** command displays information about all physical device objects (PDOs) created by the USB hub driver.

```
!usbkd.usbpdos
```

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here's an example of the output of the **!usbpdos** command.

```
0: kd> !usbkd.usbpdos

ext ffffe00006c513f0
VID 0a12 PID 0001 REV 0309 
 dt USBHUB!_USB_DEVICE_DESCRIPTOR ffffe00006c51960
Vendor: Xxxx
 Xxxx Corporation
 dd Class: (224)(e0)
 (224)(e0)
HubFdo: ffffe00000d94050, port: 2
<null>
SystemWake 5 SystemHibernate(S4)
wake_irp_list_head = ffffe00006c51cb0
wake_irp = ffffe00006c51cb0
PDO Times:
    Stat_PdoCreatedAt: 0d29bbd58
    Stat_PdoEnumeratedAt: b65ace75d29bbd58
    Stat: Enumeration Time: 0xa7d3842a(-1479310294) ms
    Stat_Pdo_SetD0_StartAt: 0d29bbd58
    Stat_Pdo_SetD0_CompleteAt: 0d29bbd58
    Stat: PDO Set_D0 time: 0x0(0) ms

## 

ext ffffe00007c883f0
VID 0781 PID 5530 REV 0100 
 dt USBHUB!_USB_DEVICE_DESCRIPTOR ffffe00007c88960
Vendor: Xxxx
 Xxxx Corporation
 dd Class: (0)(0)
 (8)Class_UsbStorage
HubFdo: ffffe00002320050, port: 3
:Xxxx  
SystemWake 5 SystemHibernate(S4)
wake_irp_list_head = ffffe00007c88cb0
wake_irp = ffffe00007c88cb0
PDO Times:
    Stat_PdoCreatedAt: 0d29bbd58
    Stat_PdoEnumeratedAt: 2380af52d29bbd58
    Stat: Enumeration Time: 0x9a24226c(-1708907924) ms
    Stat_Pdo_SetD0_StartAt: 0d29bbd58
    Stat_Pdo_SetD0_CompleteAt: 0d29bbd58
##     Stat: PDO Set_D0 time: 0x0(0) ms

```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbpdos%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





