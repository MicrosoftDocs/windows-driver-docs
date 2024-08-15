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

## KMDF NetAdapaterCx

The following table describes Windows OS support for KMDF NetAdapterCx versions.

| Operating system | KMDF version | Supported NetAdapterCx version | Version notes |
| --- | --- | --- | --- |
| Windows 11, version 24H2 | 1.33 | 2.5 | Supports [NetAdapterCx](index.md) (Ethernet), [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband), and [WiFiCx](wifi-wdf-class-extension-wificx.md) (Wi-Fi). |
| Windows Server 2022 23H2 | 1.33 | 2.4 | Supports [NetAdapterCx](index.md) (Ethernet), [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband), and [WiFiCx](wifi-wdf-class-extension-wificx.md) (Wi-Fi). |
| Windows 11, version 22H2 | 1.33 | 2.3 | Supports [NetAdapterCx](index.md) (Ethernet), [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband), and [WiFiCx](wifi-wdf-class-extension-wificx.md) (Wi-Fi). |
| Windows 11, version 21H2 | 1.33 | 2.2 | Supports [NetAdapterCx](index.md) (Ethernet), [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband), and [WiFiCx](wifi-wdf-class-extension-wificx.md) (Wi-Fi). |
| Windows 10, version 2004 | 1.31 | 2.0 | Initial release. Supports [MBBCx](mobile-broadband-mbb-wdf-class-extension-mbbcx.md) (Mobile Broadband) only. |

## UMDF NetAdapaterCx

The following table describes Windows OS support for UMDF NetAdapterCx versions.

| Operating system | UMDF version | Supported NetAdapterCx version | Version notes |
| --- | --- | --- | --- |
| Windows 11, version 24H2 | 2.33 | 2.5 | Supports [User-mode NetAdapterCx](user-mode-netcx.md) (Ethernet). |

> [!IMPORTANT]
> NetAdapterCx client drivers written in previous versions will not work in the latest version of Windows until they are retargeted to the current version.

