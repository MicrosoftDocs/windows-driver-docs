---
title: usb3kd.usb_tree
description: The usb3kd.usb_tree extension displays information, in tree format, about all USB 3.0 controllers, hubs, and devices on the computer.
ms.assetid: 8E24AD44-7B32-4299-8428-D8E9B36F5848
keywords: ["usb3kd.usb_tree Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usb3kd.usb_tree
api_type:
- NA
---

# !usb3kd.usb\_tree


The [**!usb3kd.usb\_tree**](-usb3kd-device-info.md) extension displays information, in tree format, about all USB 3.0 controllers, hubs, and devices on the computer.

```
!usb3kd.usb_tree [1]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______1______"></span> **1**   
The display includes status information for hubs and ports.

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


The following screen shot shows the output of the [**!usb\_tree**](-usb3kd-device-info.md) command.

![output of the !usb\-tree command showing topology enumerated device and hub list](images/usbtree01.png)

The output shows that there is one USB 3.0 host controller, which is represented by the line that begins with [**!xhci\_info**](-usb3kd-xhci-info.md). The next line represents the root hub for the host controller. The next four lines represent ports associated with the root hub. You can see that two ports have devices connected.

The output uses [Using Debugger Markup Language (DML)](debugger-markup-language-commands.md) to provide links. The links execute commands that give detailed information about individual objects in the tree. For example, you could get information about one of the connected devices by clicking one of the [**!device\_info**](-usb3kd-device-info.md) links. As an alternative to clicking a link, you can enter a command. For example, to see information about the first connected device, you could enter the command **!device\_info 0xfffffa8004630690**.

**Note**  The DML feature is available in WinDbg, but not in Visual Studio or KD.

 

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The [**!usb\_tree**](-usb3kd-device-info.md) command is the parent command for this set of commands.

-   [**!hub\_info**](-usb3kd-hub-info.md)
-   [**!hub\_info\_from\_fdo**](-usb3kd-hub-info-from-fdo.md)
-   [**!device\_info**](-usb3kd-device-info.md)
-   [**!device\_info\_from\_pdo**](-usb3kd-device-info-from-pdo.md)
-   [**!port\_info**](-usb3kd-port-info.md)

The information displayed by the [**!usb\_tree**](-usb3kd-device-info.md) family of commands is based on data structures maintained by the USB 3.0 hub driver. For information about the USB 3.0 hub driver and other drivers in the USB 3.0 stack, see [USB Driver Stack Architecture](http://go.microsoft.com/fwlink/p?LinkID=251983). For an explanation of the data structures used by the drivers in the USB 3.0 stack, see Part 2 of the [USB Debugging Innovations in Windows 8](http://go.microsoft.com/fwlink/p/?LinkID=249153) video.

## <span id="see_also"></span>See also


[USB 3.0 Extensions](usb-3-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usb3kd.usb_tree%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





