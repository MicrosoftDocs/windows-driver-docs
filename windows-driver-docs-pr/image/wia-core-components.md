---
title: WIA Core Components
description: WIA Core Components
ms.assetid: 59c02fa2-9116-4b57-a8fa-b977a4d6c714
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# WIA Core Components

The WIA components are shown in the following figure.

![diagram illustrating wia core components](images/stiwhist.png)

The WIA Service (*wiaservc.dll*) is hosted by a generic host called *svchost.exe*. *Wiaservc.dll* communicates with one or more user-mode still image drivers (labeled USD1, USD2, and USD3 in the figure), each of which communicates with a particular type of kernel-mode driver. Windows provides three types of bus abstraction: USB, SCSI, and serial ( *usbscan.sys*, *scsiscan.sys*, and *serscan.sys*).

On the client side, an application can be either a TWAIN-compatible application (see [Support for TWAIN-Compatible Applications](support-for-twain-compatible-applications.md)) or a WIA application. A TWAIN application calls into the data source manager, which in turn calls into *wiadss.dll*, a translation component that communicates with an instance of *sti.dll*. *Sti.dll* is a stub that communicates with the WIA service. In contrast, a WIA application makes calls directly to *sti.dll*.
