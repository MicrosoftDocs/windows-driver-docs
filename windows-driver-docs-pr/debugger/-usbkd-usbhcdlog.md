---
title: usbkd.usbhcdlog
description: The usbkd.usbhcdlog command displays a portion of the debug log for a USB host controller.
ms.assetid: 78FDC557-7791-422A-AB7B-5C9B6A1DF481
keywords: ["usbkd.usbhcdlog Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbhcdlog
api_type:
- NA
---

# !usbkd.usbhcdlog


The [**!usbkd.usbhcdlog**](https://msdn.microsoft.com/library/windows/hardware/dn367076) command displays a portion of the debug log for a USB host controller.

```
!usbkd.usbhcdlog DeviceExtension[, NumberOfEntries]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
Address of the device extension for the functional device object (FDO) of a UHCI or EHCI USB host controller.

<span id="_______NumberOfEntries______"></span><span id="_______numberofentries______"></span><span id="_______NUMBEROFENTRIES______"></span> *NumberOfEntries*   
The number of log entries to display. To display the entire log, set this parameter to -1.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of the device extension for the FDO of a USB host controller. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
0 kd> !usbkd.usb2tree

EHCI MINIPORT(s) dt usbport!_USBPORT_MINIPORT_DRIVER ffffe00001f48bd0
...

2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
...
```

In the preceding output, the address of the device extension of the FDO is displayed as the argument of the [DML](debugger-markup-language-commands.md) command **!ehci\_info ffffe00001ca11a0**.

Now pass the address of the device extension to the **!usbhcdlog** command. In this example, the second argument limits the display to four log entries.

```
0: kd> !usbkd.usbhcdlog ffffe00001ca11a0, 4

LOG@: ffffe00001ca11b8 
>LOG mask = 3ff idx = fff68e95 (295)
*LOG: ffffe000020192a0  LOGSTART: ffffe00002014000 *LOGEND: ffffe0000201bfe0 # 4 
[ 000] ffffe000020192a0 xSt0 ffffe00001ca1b88 0000000000000006 0000000000000001 
[ 001] ffffe000020192c0 xnd8 ffffe00001ca1b88 ffffe00001ca1050 0000000000000000 
[ 002] ffffe000020192e0 xnd0 ffffe00001ca1b88 ffffe00001ca1050 0000000000000000 
[ 003] ffffe00002019300 gNX0 0000000000000000 0000000000000000 ffffe00001ca1b88 
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbhcdlog%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





