---
title: WDDM 1.2 and Windows 8
description: This section provides details about new features and enhancements in Windows Display Driver Model (WDDM) version 1.2, which is available starting with Windows 8. It also describes hardware requirements, implementation guidelines, and usage scenarios.
ms.assetid: 8757ADDD-EDCA-4C09-BB71-2ED925DB2E41
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDDM 1.2 and Windows 8


This section provides details about new features and enhancements in Windows Display Driver Model (WDDM) version 1.2, which is available starting with Windows 8. It also describes hardware requirements, implementation guidelines, and usage scenarios.

## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="wddm-v1-2-features.md" data-raw-source="[WDDM 1.2 features](wddm-v1-2-features.md)">WDDM 1.2 features</a></p></td>
<td align="left"><p>This topic describes the WDDM Version 1.2 feature set, which includes several new enhancements that improve performance, reliability, and the overall end-user experience.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="advances-to-the-display-infrastructure.md" data-raw-source="[Advances to the display Infrastructure](advances-to-the-display-infrastructure.md)">Advances to the display Infrastructure</a></p></td>
<td align="left"><p>Windows 8 provides enhancements and optimizations to the display infrastructure to further improve the user experience.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="direct3d-features-and-requirements.md" data-raw-source="[Direct3D features and requirements in WDDM 1.2](direct3d-features-and-requirements.md)">Direct3D features and requirements in WDDM 1.2</a></p></td>
<td align="left"><p>Microsoft Direct3D offers a rich collection of 3-D graphics APIs, which are widely used by software applications for complex visualization and game development. This section describes feature improvements and Windows 8 Direct3D software and hardware requirements.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="graphics-inf-requirements.md" data-raw-source="[Graphics INF requirements in WDDM 1.2](graphics-inf-requirements.md)">Graphics INF requirements in WDDM 1.2</a></p></td>
<td align="left"><p>WDDM drivers in Windows 8 require INF changes to the graphics driver. The most notable change is in the feature score. WDDM 1.2 drivers require a higher feature score than earlier WDDM drivers. This section describes all relevant INF requirements for Windows 8 graphics drivers</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="installation-scenarios.md" data-raw-source="[WDDM 1.2 installation scenarios](installation-scenarios.md)">WDDM 1.2 installation scenarios</a></p></td>
<td align="left"><p>The Windows 8 installation graphics driver behavior is designed to ensure that, whenever possible, our customers get a graphics driver that has been tested and certified for Windows 8. This behavior is defined by the rules that are described in this section.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="wddm-v1-2-driver-enforcement-guidelines.md" data-raw-source="[WDDM 1.2 driver enforcement guidelines](wddm-v1-2-driver-enforcement-guidelines.md)">WDDM 1.2 driver enforcement guidelines</a></p></td>
<td align="left"><p>This section describes WDDM 1.2 driver enforcement guidelines.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Introduction"></span><span id="introduction"></span><span id="INTRODUCTION"></span>Introduction


The WDDM was introduced with Windows Vista as a replacement of the Windows XP or [Windows 2000 Display Driver Model (XDDM)](windows-2000-display-driver-model-design-guide.md). With its introduction in Windows Vista, the WDDM architecture offered functionality to enable new features such as Desktop Composition, enhanced fault tolerance, video memory manager, GPU scheduler, cross process sharing of Direct3D surfaces, and so on. WDDM was specifically designed for modern graphics devices that were Microsoft Direct3D 9 with pixel shader 2.0 or better, and had all the necessary hardware features to support the WDDM features. WDDM for Windows Vista was referred to as "WDDM 1.0."

Windows 7 made incremental changes to the driver model for supporting Windows 7 features and capabilities and was referred to as "WDDM 1.1." WDDM 1.1 is a strict superset of WDDM 1.0. WDDM 1.1 introduced support for Microsoft Direct3D 11, Windows Graphics Device Interface (GDI) hardware acceleration, Connecting and Configuring Displays, DirectX Video Acceleration (VA) High-Definition (DXVA-HD), and many other features. For more details on these features, see the [Graphics Guide for Windows 7](http://go.microsoft.com/fwlink/p/?linkid=327733).

Windows 8 introduces an array of new features and capabilities that require graphics driver changes. These incremental changes benefit end users and developers, and improve system reliability. The WDDM driver model that enables these Windows 8 features is referred to as "WDDM 1.2." WDDM 1.2 is a superset of WDDM 1.1 and WDDM 1.0. These changes can be represented in a simplified form, as shown in this table:

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Operating system</th>
<th align="left">Driver models supported</th>
<th align="left">Direct3D versions supported</th>
<th align="left">Features enabled</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Windows Vista</td>
<td align="left">WDDM 1.0
<p>XDDM on Server and limited UMPC</p></td>
<td align="left">D3D9, D3D10</td>
<td align="left">Scheduling, Memory Management, Fault tolerance, D3D9 &amp; 10</td>
</tr>
<tr class="even">
<td align="left">Windows Vista SP1 / Windows 7 client pack</td>
<td align="left"><p>WDDM 1.05</p>
<p>XDDM on Server 2008</p></td>
<td align="left">D3D9, D3D10, D3D10.1</td>
<td align="left">+ BGRA support in D3D10, D3D 10.1</td>
</tr>
<tr class="odd">
<td align="left">Windows 7</td>
<td align="left"><p>WDDM 1.1</p>
<p>XDDM on Server 2008 R2</p></td>
<td align="left">D3D9, D3D10, D3D10.1, D3D11</td>
<td align="left">GDI Hardware acceleration, DXVA HD, D3D11</td>
</tr>
<tr class="even">
<td align="left">Windows 8</td>
<td align="left">WDDM 1.2</td>
<td align="left">D3D9, D3D10, D3D10.1, D3D11, D3D11.1</td>
<td align="left">Smooth Rotation, Stereoscopic 3-D, D3D11 Video, D3D11.1, etc.</td>
</tr>
</tbody>
</table>

 

**Note**  
With Windows 8 and WDDM 1.2, XDDM is no longer supported, and XDDM drivers do not load on Windows 8 client or server. For the scenarios that are traditionally dependent on XDDM, Windows 8 allows migration to WDDM as shown in the next table.

independent hardware vendors (IHVs) and system builders should adopt the alternative WDDM solution that works best for their customers. This means that a Windows 8 system will always have a WDDM-based driver.

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Currently using</th>
<th align="left">WDDM support for XDDM scenarios</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">XDDM VGA Driver</td>
<td align="left">Microsoft Basic Display Driver</td>
</tr>
<tr class="even">
<td align="left">XDDM IHV Driver</td>
<td align="left">System builders need to work with the IHV to get:
<ul>
<li>Display-Only WDDM Driver or</li>
<li>Full Graphics WDDM Driver</li>
</ul>
<p>Alternately Microsoft Basic Display Driver</p></td>
</tr>
<tr class="odd">
<td align="left">XDDM Virtualization Driver</td>
<td align="left">System builders need to work with the IHV to get a new Display-Only Virtualization Driver</td>
</tr>
<tr class="even">
<td align="left">CSM for Int10 support on Unified Extensible Firmware Interface (UEFI)</td>
<td align="left">No longer needed with UEFI Graphics Output Protocol (GOP) support</td>
</tr>
<tr class="odd">
<td align="left">Remote Desktop Access/Collab</td>
<td align="left">Desktop Duplication API</td>
</tr>
<tr class="even">
<td align="left">Remote Session Driver</td>
<td align="left">No change, no support for &lt;32 bpp modes</td>
</tr>
</tbody>
</table>

 

**Note**  
Microsoft provides a WDDM-based Basic Display Driver that is a replacement for the earlier in-box XDDM Standard VGA driver and provides basic display functionality and software-based 2-D and 3-D rendering.

 

WDDM 1.2 introduces new types of graphics drivers, targeting specific scenarios as described below:

-   **WDDM Full Graphics Driver:** This is the full version of the WDDM graphics driver that supports hardware accelerated 2-D and 3-D operations. This driver is fully capable of handling all the render, display, and video functions. WDDM 1.0 and WDDM 1.1 are full graphics drivers. All Windows 8 client systems must have a full graphics WDDM 1.2 device as the primary boot device.
-   **WDDM Display Only Driver**: This driver is supported only as a WDDM 1.2 driver and enables IHVs to write a WDDM based kernel-mode driver that is capable of driving display-only devices. Windows handles the 2-D or 3-D rendering by using software-simulated GPU. Display-only devices are not allowed as the primary graphics device on client systems.
-   **WDDM Render Only Driver**: This driver is supported only as a WDDM 1.2 driver and enables IHVs to write a WDDM driver that supports rendering functionality only. Render-only devices are not allowed as the primary graphics device on client systems.

This table summarizes driver model versus the supported driver categories:

| Driver model/driver category | Full graphics | Display only | Render only |
|------------------------------|---------------|--------------|-------------|
| WDDM 1.0 (Windows Vista)     | Yes           | No           | No          |
| WDDM 1.1 (Windows 7)         | Yes           | No           | No          |
| WDDM 1.2 (Windows 8)         | Yes           | Yes          | Yes         |

 

This table explains scenario usage for the new driver types:

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left"></th>
<th align="left">Client</th>
<th align="left">Server</th>
<th align="left">Client running in a virtual environment</th>
<th align="left">Server virtual</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Full Graphics</td>
<td align="left">Required as boot device</td>
<td align="left">Optional</td>
<td align="left">Optional</td>
<td align="left">Optional</td>
</tr>
<tr class="even">
<td align="left">Display-Only</td>
<td align="left">Not allowed</td>
<td align="left">Optional</td>
<td align="left">Optional</td>
<td align="left">Optional</td>
</tr>
<tr class="odd">
<td align="left">Render-Only</td>
<td align="left">Optional as non-primary adapter</td>
<td align="left">Optional</td>
<td align="left">Optional</td>
<td align="left">Optional</td>
</tr>
<tr class="even">
<td align="left">Headless</td>
<td align="left">Not allowed</td>
<td align="left">Optional</td>
<td align="left">N/A</td>
<td align="left">N/A</td>
</tr>
</tbody>
</table>

 

WDDM 1.2 is required for all systems that are shipped with Windows 8. WDDM 1.0 and WDDM 1.1 will continue to work on Windows 8. However, the best experience and Windows 8-specific features are enabled only by a WDDM 1.2 driver.

 

 





