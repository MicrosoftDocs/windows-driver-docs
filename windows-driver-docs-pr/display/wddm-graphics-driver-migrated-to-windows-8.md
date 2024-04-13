---
title: WDDM Graphics Driver Migrated to Windows 8
description: When there is no Window 8 in-box coverage for the graphics hardware in a Windows 8 upgrade installation, a WDDM 1.1 or WDDM 1.0 graphics driver that was used by the previous version of Windows will be migrated to Windows 8.
ms.date: 04/20/2017
---

# WDDM graphics driver migrated to Windows 8

When there is no Window 8 in-box coverage for the graphics hardware in a Windows 8 upgrade installation, a WDDM 1.1 or WDDM 1.0 graphics driver that was used by the previous version of Windows will be migrated to Windows 8.

The Windows 8 installer can block certain problem drivers. Such drivers are not migrated to Windows 8. Drivers are identified for such blocks based on issues that are reported by using Windows telemetry. In such cases, Windows 8 uses the MSBDD until a newer driver is installed by Windows Update or by the user from an OEM/IHV support site.
