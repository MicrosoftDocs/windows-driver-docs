---
title: WDDM 1.2 and Windows 8
description: This section provides details about features and enhancements added in Windows Display Driver Model (WDDM) version 1.2, which is available starting with Windows 8. It also describes hardware requirements, implementation guidelines, and usage scenarios.
ms.date: 07/18/2022
---

# WDDM 1.2 and Windows 8

This section provides details about features and enhancements that were added in WDDM version 1.2, which is available starting with Windows 8. It also describes hardware requirements, implementation guidelines, and usage scenarios.

## In this section

| Topic | Description |
| ----- | ----------- |
| [WDDM 1.2 features](wddm-v1-2-features.md)  | Describes the WDDM Version 1.2 feature set, which includes several enhancements that improve performance, reliability, and the overall end-user experience. |
| [Advances to the display infrastructure](advances-to-the-display-infrastructure.md) | Windows 8 provides enhancements and optimizations to the display infrastructure to further improve the user experience. |
| [Direct3D features and requirements in WDDM 1.2](direct3d-features-and-requirements.md) | Microsoft Direct3D offers a rich collection of 3-D graphics APIs, which are widely used by software applications for complex visualization and game development. This section describes feature improvements and Windows 8 Direct3D software and hardware requirements. |
| [Graphics INF requirements in WDDM 1.2](graphics-inf-requirements.md) | WDDM drivers in Windows 8 require INF changes to the graphics driver. The most notable change is in the feature score. WDDM 1.2 drivers require a higher feature score than earlier WDDM drivers. This section describes all relevant INF requirements for Windows 8 graphics drivers |
| [WDDM 1.2 installation scenarios](installation-scenarios.md) | The Windows 8 installation graphics driver behavior is designed to ensure that, whenever possible, our customers get a graphics driver that has been tested and certified for Windows 8. This behavior is defined by the rules that are described in this section. |
| [WDDM 1.2 driver enforcement guidelines](wddm-v1-2-driver-enforcement-guidelines.md) | This section describes WDDM 1.2 driver enforcement guidelines. |

## Introduction

The WDDM was introduced with Windows Vista as a replacement of the Windows XP or [Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md). With its introduction in Windows Vista, the WDDM architecture offered functionality to enable new features such as Desktop Composition, enhanced fault tolerance, video memory manager, GPU scheduler, cross process sharing of Direct3D surfaces, and so on. WDDM was specifically designed for modern graphics devices that were Microsoft Direct3D 9 with pixel shader 2.0 or better, and had all the necessary hardware features to support the WDDM features. WDDM for Windows Vista was referred to as "WDDM 1.0."

Windows 7 made incremental changes to the driver model for supporting Windows 7 features and capabilities and was referred to as "WDDM 1.1." WDDM 1.1 is a strict superset of WDDM 1.0. WDDM 1.1 introduced support for Microsoft Direct3D 11, Windows Graphics Device Interface (GDI) hardware acceleration, Connecting and Configuring Displays, DirectX Video Acceleration (VA) High-Definition (DXVA-HD), and many other features. For more details on these features, see the [Graphics Guide for Windows 7](/previous-versions/windows/hardware/download/dn550976(v=vs.85)).

Windows 8 introduced an array of features and capabilities that required graphics driver changes. These incremental changes benefit end users and developers, and improve system reliability. The WDDM driver model that enables these Windows 8 features is referred to as "WDDM 1.2." WDDM 1.2 is a superset of WDDM 1.1 and WDDM 1.0. These changes can be represented in a simplified form, as shown in the following table.

| Operating system | Driver models supported | Direct3D versions supported | Features enabled |
| ---------------- | ----------------------- | --------------------------- | ---------------- |
| Windows Vista    | WDDM 1.0; XDDM on Server and limited UMPC | D3D9, D3D10 | Scheduling, Memory Management, Fault tolerance, D3D9 & 10 |
| Windows Vista SP1 / Windows 7 client pack | WDDM 1.05; XDDM on Server 2008 | D3D9, D3D10, D3D10.1 | + BGRA support in D3D10, D3D 10.1 |
| Windows 7        | WDDM 1.1; XDDM on Server 2008 R2 | D3D9, D3D10, D3D10.1, D3D11 | GDI Hardware acceleration, DXVA HD, D3D11 |
| Windows 8        | WDDM 1.2 | D3D9, D3D10, D3D10.1, D3D11, D3D11.1 | Smooth Rotation, Stereoscopic 3-D, D3D11 Video, D3D11.1, etc. |

> [!NOTE]
> With Windows 8 and WDDM 1.2, XDDM is no longer supported, and XDDM drivers do not load on Windows 8 client or server. For the scenarios that are traditionally dependent on XDDM, Windows 8 allows migration to WDDM as shown in the next table.

Independent hardware vendors (IHVs) and system builders should adopt the alternative WDDM solution that works best for their customers. This means that a Windows 8 system will always have a WDDM-based driver.

| Currently using | WDDM support for XDDM scenarios |
| --------------- | ------------------------------- |
| XDDM VGA Driver | Microsoft Basic Display Driver |
| XDDM IHV Driver | System builders need to work with the IHV to get a Display-Only WDDM Driver or Full Graphics WDDM Driver. Alternately Microsoft Basic Display Driver |
| XDDM Virtualization Driver | System builders need to work with the IHV to get a new Display-Only Virtualization Driver |
| CSM for Int10 support on Unified Extensible Firmware Interface (UEFI) | No longer needed with UEFI Graphics Output Protocol (GOP) support |
| Remote Desktop Access/Collab | Desktop Duplication API |
| Remote Session Driver | No change; no support for <32 bpp modes |

> [!NOTE]
> Microsoft provides a WDDM-based Basic Display Driver that is a replacement for the earlier in-box XDDM Standard VGA driver and provides basic display functionality and software-based 2-D and 3-D rendering.

WDDM 1.2 introduced new types of graphics drivers, targeting specific scenarios as described below:

* **WDDM Full Graphics Driver:** This is the full version of the WDDM graphics driver that supports hardware accelerated 2-D and 3-D operations. This driver is fully capable of handling all the render, display, and video functions. WDDM 1.0 and WDDM 1.1 are full graphics drivers. All Windows 8 client systems must have a full graphics WDDM 1.2 device as the primary boot device.
* **WDDM Display Only Driver**: This driver is supported only as a WDDM 1.2 driver and enables IHVs to write a WDDM based kernel-mode driver that is capable of driving display-only devices. Windows handles the 2-D or 3-D rendering by using software-simulated GPU. Display-only devices are not allowed as the primary graphics device on client systems.
* **WDDM Render Only Driver**: This driver is supported only as a WDDM 1.2 driver and enables IHVs to write a WDDM driver that supports rendering functionality only. Render-only devices are not allowed as the primary graphics device on client systems.

The following table summarizes driver model versus the supported driver categories.

| Driver model/driver category | Full graphics | Display only | Render only |
|------------------------------|---------------|--------------|-------------|
| WDDM 1.0 (Windows Vista)     | Yes           | No           | No          |
| WDDM 1.1 (Windows 7)         | Yes           | No           | No          |
| WDDM 1.2 (Windows 8)         | Yes           | Yes          | Yes         |

The following table explains scenario usage for the new driver types:

| Driver category | Client | Server | Client running in a virtual environment | Server virtual |
| --------------- | ------ | ------ | --------------------------------------- | -------------- |
| Full Graphics   | Required as boot device | Optional | Optional | Optional |
| Display-Only    |  Not allowed            | Optional | Optional | Optional |
| Render-Only     | Optional as non-primary adapter | Optional | Optional | Optional |
| Headless | Not allowed | Optional | N/A | N/A |

WDDM 1.2 is required for all systems that are shipped with Windows 8. WDDM 1.0 and WDDM 1.1 will continue to work on Windows 8. However, the best experience and Windows 8-specific features are enabled only by a WDDM 1.2 driver.
