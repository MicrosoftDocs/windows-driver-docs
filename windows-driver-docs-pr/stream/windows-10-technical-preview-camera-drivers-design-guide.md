---
title: Universal camera driver design guide for Windows 10
author: windows-driver-content
description: The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.
ms.assetid: CB5EEDF2-650D-4CD3-A5DE-DF0D6F10B394
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Universal camera driver design guide for Windows 10


The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.

The universal camera driver model also contains new DDIs, including:

* [Digital video stabilization](https://msdn.microsoft.com/library/windows/hardware/dn936754)
* [Variable frame rate](https://msdn.microsoft.com/library/windows/hardware/dn917971)
* [Face detection](https://msdn.microsoft.com/library/windows/hardware/dn917937)
* [Video high dynamic range (HDR)](https://msdn.microsoft.com/library/windows/hardware/dn936752)
* [Optical stabilization](https://msdn.microsoft.com/library/windows/hardware/dn917954)
* [Scene analysis: photo HDR, flash no flash, ultra low light](https://msdn.microsoft.com/library/windows/hardware/dn917934)
* [Capture stats: metadata framework/attributes, histograms](https://msdn.microsoft.com/library/windows/hardware/dn917945)
* [Smooth zoom](https://msdn.microsoft.com/library/windows/hardware/dn936756)
* [Hardware optimization hints](https://msdn.microsoft.com/library/windows/hardware/dn917956)
* [Camera profiles](camera-driver-functions.md)

## Build a universal camera driver

The universal camera driver is an AVStream minidriver built on the [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM).

For more information, see the following sections in the [Universal camera driver model reference for Windows 10](windows-10-technical-preview-camera-drivers-reference.md):

* [New camera driver controls](camera-driver-controls.md)
* [New camera driver enumerations](camera-driver-enumerations.md)
* [New camera driver functions](camera-driver-functions.md)
* [New camera driver structures](camera-driver-structures.md)

For more information about building AVStream minidrivers, see the following topics:

* [Roadmap for Developing Streaming Minidrivers](https://msdn.microsoft.com/library/windows/hardware/ff568130)
* [AVStream Overview](avstream-overview.md)
* [Writing an AVStream Minidriver](writing-an-avstream-minidriver.md)



