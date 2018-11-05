---
title: USB 2.0 Extensions
description: This section describes the USB 2.0 debugger extension commands. These commands display information from data structures maintained by drivers in the USB 2.0 driver stack.
ms.assetid: 42A78738-CE0D-42EA-9E3D-04CDC2060266
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# USB 2.0 Extensions


This section describes the USB 2.0 debugger extension commands. These commands display information from data structures maintained by drivers in the USB 2.0 driver stack. For more information about these three drivers, see [USB Driver Stack Architecture](https://go.microsoft.com/fwlink/p?LinkId=251983).

The USB 2.0 debugger extension commands are implemented in Usbkd.dll. To load the Usbkd commands, enter **.load usbkd.dll** in the debugger.

## <span id="usb-2-tree"></span><span id="USB_2_TREE"></span>USB 2.0 Tree


The USB 2.0 tree contains the device nodes that represent execution units on EHCI host controller devices along with the child nodes that represent hubs and connected devices. This diagram shows an example of a USB 2.0 tree.

![diagram that shows usb 2tree](images/usbkd01.png)

The diagram shows one physical host controller device that has two execution units. Each execution unit appears as a device node in the Plug and Play device tree. One execution unit appears as a UHCI USB host controller node, and the other execution unit shows as an EHCI USB host controller node. Each of those nodes has a child node that represents a USB root hub. Each root hub has a single child node that represents a connected USB device.

Notice that the diagram is not a tree in the sense that not all nodes descend from a single parent node. However, when we use the term *USB 2.0 tree*, we are referring to the set of device nodes that represent execution units on EHCI host controller devices along with the nodes for hubs and connected devices.

## <span id="getting_started_with_usb_2.0_debugging"></span><span id="GETTING_STARTED_WITH_USB_2.0_DEBUGGING"></span>Getting started with USB 2.0 debugging


To start debugging a USB 2.0 issue, enter the [**!usb2tree**](-usbkd-usb2tree.md) command. The **!usb2tree** command displays a list of commands and addresses that you can use to investigate host controllers, hubs, ports, devices, endpoints, and other elements of the USB 2.0 tree.

## <span id="in_this_section"></span>In this section


-   [**!usbkd.usbhelp**](-usbkd-usbhelp.md)
-   [**!usbkd.\_ehcidd**](-usbkd--ehcidd.md)
-   [**!usbkd.\_ehciep**](-usbkd--ehciep.md)
-   [**!usbkd.\_ehciframe**](-usbkd--ehciframe.md)
-   [**!usbkd.\_ehciqh**](-usbkd--ehciqh.md)
-   [**!usbkd.\_ehciregs**](-usbkd--ehciregs.md)
-   [**!usbkd.\_ehcisitd**](-usbkd--ehcisitd.md)
-   [**!usbkd.\_ehcistq**](-usbkd--ehcistq.md)
-   [**!usbkd.\_ehcitd**](-usbkd--ehcitd.md)
-   [**!usbkd.\_ehcitfer**](-usbkd--ehcitfer.md)
-   [**!usbkd.\_ehciitd**](-usbkd--ehciitd.md)
-   [**!usbkd.doesdumphaveusbdata**](-usbkd-doesdumphaveusbdata.md)
-   [**!usbkd.isthisdumpasyncissue**](-usbkd-isthisdumpasyncissue.md)
-   [**!usbkd.urbfunc**](-usbkd-urbfunc.md)
-   [**!usbkd.usb2**](-usbkd-usb2.md)
-   [**!usbkd.usb2tree**](-usbkd-usb2tree.md)
-   [**!usbkd.usbchain**](-usbkd-usbchain.md)
-   [**!usbkd.usbdevobj**](-usbkd-usbdevobj.md)
-   [**!usbkd.usbdpc**](-usbkd-usbdpc.md)
-   [**!usbkd.ehci\_info\_from\_fdo**](-usbkd-ehci-info-from-fdo.md)
-   [**!usbkd.usbdevh**](-usbkd-usbdevh.md)
-   [**!usbkd.usbep**](-usbkd-usbep.md)
-   [**!usbkd.usbfaildata**](-usbkd-usbfaildata.md)
-   [**!usbkd.usbhcdext**](-usbkd-usbhcdext.md)
-   [**!usbkd.usbdstatus**](-usbkd-usbdstatus.md)
-   [**!usbkd.usbhcdhccontext**](-usbkd-usbhcdhccontext.md)
-   [**!usbkd.usbhcdlist**](-usbkd-usbhcdlist.md)
-   [**!usbkd.usbhcdlistlogs**](-usbkd-usbhcdlistlogs.md)
-   [**!usbkd.usbhcdlog**](-usbkd-usbhcdlog.md)
-   [**!usbkd.usbhcdlogex**](-usbkd-usbhcdlogex.md)
-   [**!usbkd.usbhcdpnp**](-usbkd-usbhcdpnp.md)
-   [**!usbkd.usbhcdpow**](-usbkd-usbhcdpow.md)
-   [**!usbkd.hub2\_info\_from\_fdo**](-usbkd-hub2-info-from-fdo.md)
-   [**!usbkd.usbhuberr**](-usbkd-usbhuberr.md)
-   [**!usbkd.usbhubext**](-usbkd-usbhubext.md)
-   [**!usbkd.usbhubinfo**](-usbkd-usbhubinfo.md)
-   [**!usbkd.usbhublog**](-usbkd-usbhublog.md)
-   [**!usbkd.usbhubmddevext**](-usbkd-usbhubmddevext.md)
-   [**!usbkd.usbhubmdpd**](-usbkd-usbhubmdpd.md)
-   [**!usbkd.usbhubpd**](-usbkd-usbhubpd.md)
-   [**!usbkd.usbhubs**](-usbkd-usbhubs.md)
-   [**!usbkd.usblist**](-usbkd-usblist.md)
-   [**!usbkd.usbpo**](-usbkd-usbpo.md)
-   [**!usbkd.usbpdos**](-usbkd-usbpdos.md)
-   [**!usbkd.usbpdoxls**](-usbkd-usbpdoxls.md)
-   [**!usbkd.usbpnp**](-usbkd-usbpnp.md)
-   [**!usbkd.usbportisasyncadv**](-usbkd-usbportisasyncadv.md)
-   [**!usbkd.usbportmdportlog**](-usbkd-usbportmdportlog.md)
-   [**!usbkd.usbportmddcontext**](-usbkd-usbportmddcontext.md)
-   [**!usbkd.usbportmddevext**](-usbkd-usbportmddevext.md)
-   [**!usbkd.usbtriage**](-usbkd-usbtriage.md)
-   [**!usbkd.usbtt**](-usbkd-usbtt.md)
-   [**!usbkd.usbtx**](-usbkd-usbtx.md)
-   [**!usbkd.usbusb2ep**](-usbkd-usbusb2ep.md)
-   [**!usbkd.usbusb2tt**](-usbkd-usbusb2tt.md)
-   [**!usbkd.usbver**](-usbkd-usbver.md)

## <span id="related_topics"></span>Related topics


[USB 3.0 Extensions](usb-3-extensions.md)

[RCDRKD Extensions](rcdrkd-extensions.md)

 

 






