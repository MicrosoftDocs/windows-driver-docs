---
title: usbkd.usb2tree
description: The usbkd.usb2tree command displays USB 2.0 tree.
ms.assetid: 6BEFE154-C8F0-466C-AB68-71C6304D0DEA
keywords: ["usbkd.usb2tree Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usb2tree
api_type:
- NA
---

# !usbkd.usb2tree


The **!usbkd.usb2tree** command displays [USB 2.0 tree](usb-2-0-extensions.md#usb-2-tree).

```
!usbkd.usb2tree
```

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


This screen shot shows and example of the output of the **!usb2tree** command.

![output of the !usbkd.usb2tree command showing uhci ehci information and an enumerated hub list](images/usb2tree01.png)

The output shows one EHCI execution unit and two UHCI execution units. The execution units shown in this example happen to be on a single USB host controller device. The output also shows the root hubs and connected devices.

The output uses [Using Debugger Markup Language (DML)](debugger-markup-language-commands.md) to provide links. The links execute commands that give detailed information related to objects in the tree. For example, you could click one of the [**!devobj**](-devobj.md) links to get information about the functional device object associated with the EHCI execution unit. As an alternative to clicking the link, you could enter the command manually: **!devobj ffffe00001ca7050**

**Note**  The DML feature is available in WinDbg, but not in Visual Studio or KD.

 

## <span id="DLL"></span><span id="dll"></span>DLL


Usb3kd.dll

Remarks
-------

The **!usb2tree** command is the parent command for many of the [USB 2.0 debugger extensions commands.](usb-2-0-extensions.md) The information displayed by these commands is based on data structures maintained by these drivers:

-   usbehci.sys (miniport driver for USB 2 host controller)
-   usbuhci.sys (miniport driver for USB 2 host controller)
-   usbport.sys (port driver for USB 2 host controller)
-   usbhub.sys (USB 2 hub driver)

For more information about these drivers, see [USB Driver Stack Architecture](http://go.microsoft.com/fwlink/p/?LinkId=251983).

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usb2tree%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





