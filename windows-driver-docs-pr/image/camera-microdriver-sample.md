---
title: Camera Microdriver Sample
description: Camera Microdriver Sample
ms.assetid: a3aa0cf1-9954-4556-8dae-512a12864dfe
ms.date: 05/29/2020
ms.localizationpriority: medium
---

# Camera Microdriver Sample

The microdrv directory in [WIA Driver Samples](https://docs.microsoft.com/samples/microsoft/windows-driver-samples/windows-image-acquisition-wia-driver-samples) for a sample WIA microdriver for a digital still camera.

This sample shows how to write a WIA user-mode microdriver for a camera. It simulates a camera by reading images from a directory on the hard disk. This sample driver can be used as a starting point for your development, but your driver should access the camera hardware through one of the kernel-mode drivers provided with Windows.
