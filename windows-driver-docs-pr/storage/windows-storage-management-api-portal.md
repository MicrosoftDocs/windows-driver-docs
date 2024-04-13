---
title: Windows Storage Management Provider
description: The Windows Storage Management provider can be used to manage a wide range of storage configurations, from single-disk desktops to external storage arrays.
ms.assetid: ff5e492d-5e62-4c9b-8f55-07859c9fee83
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Storage Management Provider

## Purpose

The Windows Storage Management provider can be used to manage a wide range of storage configurations, from single-disk desktops to external storage arrays.

Storage subsystem manufacturers can support Windows-based storage management for their products by implementing a Storage Management Provider (SMP). For more information, see [How to Implement a Storage Management Provider](/previous-versions/windows/hardware/drivers/dn342891(v=vs.85)).

The Windows Storage Management API supersedes the [Virtual Disk Service](/windows/win32/vds/virtual-disk-service-portal) API beginning with the Windows 8 and Windows Server 2012 operating systems.

## In this section

-   [Storage Management API Classes](storage-management-api-classes.md)
-   [Storage Management API Common Return Codes](storage-management-api-common-return-codes.md)

## Developer audience

The Windows Storage Management API is designed for WMI developers who use C/C++, the Microsoft Visual Basic application, or a scripting language that has an engine on Windows and handles Microsoft ActiveX objects. Familiarity with COM programming is helpful but not required. For more information about WMI, see [Windows Management Instrumentation](/windows/win32/wmisdk/wmi-start-page).

## Run-time requirements

The Windows Storage Management API is included in Windows 8 and Windows Server 2012.

 

 