---
title: NetAdapterCx version overview
description: This topic lists versions of the Network Adapter WDF Class Extension (NetAdapterCx).
keywords:
- Version overview Network Adapter Class Extension, version overview NetAdapterCx, version overview NetCx
ms.date: 12/09/2021
ms.custom: Vib
---

# NetAdapterCx version overview

This section highlights new features for the Network Adapter WDF Class Extension (NetAdapterCx) driver model. Use the following topics to learn more about the changes in each version of NetAdapterCx.

The current version of NetAdapterCx is **2.2**.

Windows OS support for NetAdapterCx versions are described in the following table.

| Operating system | KMDF version | Supported NetAdapterCx version | Version notes |
| --- | --- | --- | --- |
| Windows 10, version 2004 | 1.31 | 2.0 | Initial release. Supports [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband) only. |
| Windows 11 | 1.33 | 2.2 | Supports [NetAdapterCx](index.md) (Ethernet), [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband), and [WiFiCx](wifi-wdf-class-extension-wificx.md) (Wi-Fi). |

> [!IMPORTANT]
> NetAdapterCx client drivers written in previous versions will not work in the latest version of Windows until they are retargeted to the current version.

