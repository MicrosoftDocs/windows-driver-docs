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

The current version of NetAdapterCx is **2.5**.

Windows OS support for NetAdapterCx versions are described in the following table.

| Operating system | KMDF version | UMDF version | Supported NetAdapterCx version | Version notes |
| --- | --- | --- | --- | --- |
| WIN11_NEXT | 1.33 | 2.33 | 2.5 | Supports KMDF and UMDF [NetAdapterCx](index.md) (Ethernet), [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband), and [WiFiCx](wifi-wdf-class-extension-wificx.md) (Wi-Fi). |
| Windows 11 | 1.33 | N/A | 2.2 | Supports KMDF [NetAdapterCx](index.md) (Ethernet), [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband), and [WiFiCx](wifi-wdf-class-extension-wificx.md) (Wi-Fi). |
| Windows 10, version 2004 | 1.31 | N/A | 2.0 | Initial release. Supports KMDF [NetAdapterCx](index.md) (Ethernet) and [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband). |

> [!IMPORTANT]
> NetAdapterCx client drivers written in previous versions will not work in the latest version of Windows until they are retargeted to the current version.

