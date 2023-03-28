---
title: Camera Microdriver Sample
description: Camera Microdriver Sample
ms.date: 03/28/2023
---

# Camera Microdriver Sample

The microdrv directory in [WIA Driver Samples](/samples/microsoft/windows-driver-samples/windows-image-acquisition-wia-driver-samples) contains a sample WIA microdriver for a digital still camera.

This sample shows how to write a WIA user-mode microdriver for a camera. It simulates a camera by reading images from a directory on the hard disk. This sample driver can be used as a starting point for your development, but your driver should access the camera hardware through one of the kernel-mode drivers provided with Windows.
