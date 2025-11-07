---
title: What's New for Windows 11 Graphics Display Drivers
description: Lists features added for graphics display drivers starting in Windows 11
ms.date: 11/05/2025
ms.topic: whats-new
---

# What's new for Windows 11 graphics display drivers

This page describes what's new in graphics display drivers for Windows 11 (version 21H2) and later releases of Windows 11.

## Windows 11, version 24H2 (WDDM 3.2)

For a list of features that WDDM 3.2 and later drivers can support, see [What's new in driver development for Windows 11, version 24H2](..//what-s-new-in-driver-development.md).

## Windows 11, version 23H2

[Version 1.10 of the Indirect Display Driver (IDD) model](iddcx1.10-updates.md) was shipped. This IddCx version adds HDR10 (high dynamic range) and SDR (standard dynamic range) Wide Color Gamut (WCG) support for indirect displays.

The WDDM version didn't change.

## Windows 11, version 22H2 (WDDM 3.1)

WDDM 3.1 and later drivers can support the following features that were added in WDDM 3.1.

* [Sharing the backing store with KMD](sharing-backing-store-with-kmd.md)

## Windows 11, version 21H2 (WDDM 3.0)

WDDM 3.0 and later drivers can support the following features that were added in WDDM 3.0.

* [D3D12 enhanced barriers](enhanced-barriers.md)

* [Direct3D 12 video encoding](video-encoding-d3d12.md)

  Before Windows 11, DirectX 12 provided application- and driver-level interfaces to support GPU acceleration for several video applications, including:

  * Video decoding
  * Video processing
  * Motion estimation

  Starting in Windows 11, D3D12 added a [video encoding feature](video-encoding-d3d12.md) to the existing video API/DDI family. This feature provides a coherent set of encoding APIs/DDIs that are consistent with the existing D3D12 framework, and allows developers to perform video encoding using GPU-accelerated video engines.

* [DisplayPort monitors connected over USB4](supporting-usb4.md)

* [Hardware flip queue](hardware-flip-queue.md)

* [IOMMU DMA remapping](iommu-dma-remapping.md)

* [Signaling a CPU event from KMD](signaling-cpu-event-from-kmd.md)
