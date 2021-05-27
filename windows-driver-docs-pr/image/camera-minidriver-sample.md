---
title: Camera Minidriver Sample
description: Camera Minidriver Sample
ms.date: 05/29/2020
ms.localizationpriority: medium
---

# Camera Minidriver Sample

The wiadriverex directory in [WIA Driver Samples](/samples/microsoft/windows-driver-samples/windows-image-acquisition-wia-driver-samples) contains a sample WIA minidriver for a digital still camera.

This sample shows how to write a WIA user-mode minidriver for a camera. It simulates a camera by reading images from a directory on the hard disk. This sample driver can be used as a starting point for your development, but your driver should access the camera hardware through one of the kernel-mode drivers provided with Windows.
