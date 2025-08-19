---
title: Windows Storage Management Provider
description: Introduces the Windows Storage Management Provider API.
ms.date: 11/21/2024
ms.topic: concept-article
---

# Windows Storage Management Provider API

A Windows [Storage Management Provider](storage-management-providers.md) (SMP) provides an interface for management applications to interact with storage configurations, including disks, partitions, volumes, and storage spaces. As a bridge between management applications and the underlying storage subsystems, it enables the creation, modification, and monitoring of storage resources through a standardized set of Windows Management Instrumentation (WMI) classes.  

Storage subsystem manufacturers can support Windows-based storage management for their products by implementing an SMP.

* [Storage Management API Classes](storage-management-api-classes.md)

* [Storage Management API Common Return Codes](storage-management-api-common-return-codes.md)

## Developer audience

The Windows Storage Management API is designed for WMI developers who use C/C++, the Microsoft Visual Basic application, or a scripting language that has an engine on Windows and handles Microsoft ActiveX objects. Familiarity with COM programming is helpful but not required. For more information about WMI, see [Windows Management Instrumentation](/windows/win32/wmisdk/wmi-start-page).

## Run-time requirements

The Windows Storage Management API is included starting in Windows 8 and Windows Server 2012.

The Windows Storage Management API supersedes the [Virtual Disk Service](/windows/win32/vds/virtual-disk-service-portal) (VDS) API beginning with the Windows 8 and Windows Server 2012 operating systems.
