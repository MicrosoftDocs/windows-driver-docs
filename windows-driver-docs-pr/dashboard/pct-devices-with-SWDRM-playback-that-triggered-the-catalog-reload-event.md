---
title: Percentage of devices with SWDRM playback that triggered the Catalog reload event
description: Devices that experience a Code Integrity catalog reload event when loading binaries into mfpmp.exe, may receive a timeout from Netflix and other applications. This "device based" measure is used to capture this scenario.
ms.topic: article
ms.date: 01/19/2023
---

#  Percentage of devices with SWDRM playback that triggered the Catalog reload event

## Description

Devices that experience a Code Integrity catalog reload event when loading binaries into mfpmp.exe, may receive a timeout from Netflix and other applications. This "device based" measure is used to capture this scenario.

DRM (Digital Rights Management) techniques (Software or Hardware) are used during Video Playback on windows devices. We use the set of all devices with SWDRM playback as our sample space to compute the percentage. More information about DRM can be found at [Digital Rights Management - Windows drivers | Microsoft Docs](/windows-hardware/drivers/audio/digital-rights-management).

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | This device-based Catalog Reload Driver measure is used to capture the percentage of SWDRM devices that encounter an unsigned dll, which may cause a timeout in applications during video playback. |
| **Time period** | Daily |
| **Measurement criteria** | Percent of machines hitting the catalog reload event |
| **Minimum population** | 200 machines |
| **Passing criteria** | >=99% of devices do not have a catalog reload event during playback|
| **Measure ID** | 41328752 (Legacy), 43952484 |

## Calculation

1. The measure is computed daily. Each row corresponds to a device and the metric value is 1 or 0 respectively, if the device did or did not hit a catalog reload event.
2. This information is then directly input to Mission control after leveraging the graphics BYOD modules which adds additional GPU related columns.
3. One additional check is we only associate IHVs with their missing dlls (such as only nv*.dll, amd*.dll and ig*.dll files are associated with Nvidia, AMD and Intel respectively) so that third party dlls with missing page hashes and unsigned OS dlls don't corrupt this measure