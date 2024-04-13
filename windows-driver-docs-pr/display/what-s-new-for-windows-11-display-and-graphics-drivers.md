---
title: What's New for Windows 11 Display and Graphics Drivers
description: Describes new features in Windows 11 for display drivers
ms.date: 03/04/2022
---

# What's new for Windows 11 display and graphics drivers

This page describes what's new in display and graphics drivers for Windows 11 (WDDM 3.0).

## Direct3D 12 video encoding

Prior to Windows 11 (WDDM 3.0), DirectX 12 provided application- and driver-level interfaces (APIs and DDIs) to support GPU acceleration for several video applications, including video decoding, video processing, and motion estimation.

Starting in Windows 11, D3D12 added a [video encoding feature](video-encoding-d3d12.md) to the existing video API/DDI family. This feature provides a coherent set of encoding APIs/DDIs that are consistent with the existing D3D12 framework, and allows developers to perform video encoding using GPU-accelerated video engines.
