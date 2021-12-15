---
title: Universal camera driver design guide for Windows 10
description: The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.
ms.date: 03/23/2021
---

# Universal camera driver design guide for Windows 10

The camera driver interface for Windows 10 is converged for all devices and uses a universal camera driver model.

The universal camera driver model contains the following controls:

- [Digital video stabilization](ksproperty-cameracontrol-extended-videostabilization.md)

- [Variable frame rate](ksproperty-cameracontrol-extended-vfr.md)

- [Face detection](ksproperty-cameracontrol-extended-facedetection.md)

- [Video high dynamic range (HDR)](ksproperty-cameracontrol-extended-videohdr.md)

- [Optical stabilization](ksproperty-cameracontrol-extended-ois.md)

- [Scene analysis: photo HDR, flash no flash, ultra low light](ksproperty-cameracontrol-extended-advancedphoto.md)

- [Capture stats: metadata framework/attributes, histograms](ksproperty-cameracontrol-extended-histogram.md)

- [Smooth zoom](ksproperty-cameracontrol-extended-zoom.md)

- [Hardware optimization hints](ksproperty-cameracontrol-extended-optimizationhint.md)

- [Camera profiles](ksproperty-cameracontrol-extended-profile.md)

## Build a universal camera driver

The universal camera driver is an AVStream minidriver built on the [Windows Driver Model](../kernel/introduction-to-wdm.md) (WDM).

For more information, see the following sections in the [Universal camera driver reference for Windows 10](windows-10-technical-preview-camera-drivers-reference.md):

- [Universal camera driver controls for Windows 10](camera-driver-controls.md)

- [Universal camera driver enumerations for Windows 10](camera-driver-enumerations.md)

- [Universal camera driver functions for Windows 10](camera-driver-functions.md)

- [Universal camera driver structures for Windows 10](camera-driver-structures.md)

For more information about building AVStream minidrivers, see the following topics:

- [AVStream Overview](avstream-overview.md)

- [Writing an AVStream Minidriver](writing-an-avstream-minidriver.md)

## See also

[Streaming media device driver reference](/windows-hardware/drivers/ddi/_stream/index)
