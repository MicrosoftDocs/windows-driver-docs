---
title: usbkd.usb2
description: The usbkd.usb2 command displays a list of USB endpoints that have USB 2.0 scheduling information.
ms.assetid: 48DC685A-3624-4DAD-8077-FB7C4BE4BE93
keywords: ["usbkd.usb2 Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usb2
api_type:
- NA
---

# !usbkd.usb2


The **!usbkd.usb2** command displays a list of USB endpoints that have USB 2.0 scheduling information.

```
!usbkd.usb2 DeviceExtension
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the functional device object (FDO) of a USB host controller.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the device extension for the FDO of a USB host controller. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
0: kd> !usbkd.usb2tree

EHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001f48bd0
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!ehci\_info ffffe00001ca11a0**. Pass the address of the device extension to the **!usb2** command.

```
0: kd> !usbkd.usb2 ffffe00001ca11a0

Sig: HFDO
Hcd FDO Extension:
----------
----------
dt usbport!_HCD_ENDPOINT ffffe0000212d970  !usbep ffffe0000212d970
    Tt 0000000000000000 Device Address: 0x00, ep 0x81 Interrupt In
    dt _USB2LIB_ENDPOINT_CONTEXT ffffe000023b60f0    dt _USB2_EP ffffe000023b6100
    Period,offset,Ordinal(32,0,0)   smask,cmask(00,00  ........ , ........) maxpkt 1
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usb2%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





