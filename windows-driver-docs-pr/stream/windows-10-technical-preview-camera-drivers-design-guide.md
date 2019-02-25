---
title: Universal camera driver design guide for Windows 10
description: The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.
ms.assetid: CB5EEDF2-650D-4CD3-A5DE-DF0D6F10B394
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Universal camera driver design guide for Windows 10


The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.

The universal camera driver model also contains new DDIs, including:

* [Digital video stabilization](ksproperty-cameracontrol-extended-videostabilization.md)
* [Variable frame rate](ksproperty-cameracontrol-extended-vfr.md)
* [Face detection](ksproperty-cameracontrol-extended-facedetection.md)
* [Video high dynamic range (HDR)](ksproperty-cameracontrol-extended-videohdr.md)
* [Optical stabilization](ksproperty-cameracontrol-extended-ois.md)
* [Scene analysis: photo HDR, flash no flash, ultra low light](ksproperty-cameracontrol-extended-advancedphoto.md)
* [Capture stats: metadata framework/attributes, histograms](ksproperty-cameracontrol-extended-histogram.md)
* [Smooth zoom](ksproperty-cameracontrol-extended-zoom.md)
* [Hardware optimization hints](ksproperty-cameracontrol-extended-optimizationhint.md)
* [Camera profiles](ksproperty-cameracontrol-extended-profile.md)

## Build a universal camera driver

The universal camera driver is an AVStream minidriver built on the [Windows Driver Model](https://msdn.microsoft.com/library/windows/hardware/ff565698) (WDM).

For more information, see the following sections in the [Universal camera driver model reference for Windows 10](windows-10-technical-preview-camera-drivers-reference.md):

* [New camera driver controls](camera-driver-controls.md)
* [New camera driver enumerations](camera-driver-enumerations.md)
* [New camera driver functions](camera-driver-functions.md)
* [New camera driver structures](camera-driver-structures.md)

For more information about building AVStream minidrivers, see the following topics:

* [AVStream Overview](avstream-overview.md)
* [Writing an AVStream Minidriver](writing-an-avstream-minidriver.md)



