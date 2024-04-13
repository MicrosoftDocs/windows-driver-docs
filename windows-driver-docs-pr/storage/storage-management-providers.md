---
title: Storage Management Providers (Windows Drivers)
description: Learn more about the Storage Management Providers.
ms.date: 01/20/2023
---

# Storage Management Providers

Storage vendors can include Windows-based management of their storage subsystems by supporting the [Windows Storage Management API](windows-storage-management-api-portal.md). Windows management applications can use this API and provide integrated storage management services.

Starting with Windows 8, [Windows Storage Management API](windows-storage-management-api-portal.md) supersedes the Virtual Disk Service (VDS), its APIs, and associated utilities. Additionally, none of the storage management utilities in introduced in Windows 8 use VDS. Storage vendors are therefore encouraged to adopt the Windows Storage Management API and develop an appropriate provider to support this API.

In order to support the [Windows Storage Management API](windows-storage-management-api-portal.md), storage vendors can choose to either:

* Develop a Storage Management Provider (SMP).
* Develop an [SMI-S provider](/previous-versions/windows/desktop/smi-s/dn265461(v=vs.85)). This provider is accessed through the built-in Windows Storage Management Service. The Storage Management Service is implemented as an SMP.

Both mechanisms equally enable ease-of-management of the storage subsystem through the new API. Further, both mechanisms enable easy extensibility through a well-defined pass-through interface.

As previously stated, the [Windows Storage Management API](windows-storage-management-api-portal.md) aims to deliver on comprehensive storage provisioning and administration capabilities. Further, this API is designed to evolve, as needed, with successive Windows versions. The pass-through interface enables storage management applications to perform operations on compatible storage subsystems, which have for various reasons not yet been enabled directly through the well-defined API. While this is an important mechanism for easy extensibility, the pass-through mechanism is intended to be used solely for capabilities not exposed through the API and must not be used for capabilities that can be administered through the API.

## Architecture

The SMP architectural model is composed of the following features:

* Windows management applications, including in-built PowerShell commandlets, use the [Windows Storage Management API](windows-storage-management-api-portal.md). For the (expected) small subset of capabilities not yet exposed through the API, Windows storage management applications can use a pass-through mechanism. This capability allows, for example, the full suite of SMI-S classes and methods to be used if needed and also enables proprietary communication between the application and the storage provider.

* Storage subsystems can ensure they're manageable by Windows management applications by committing to responding to the new API. This is done either by delivering an SMP or by delivering an SMI-S provider, which in turn will be invoked through Windows Storage Management Service. If the storage vendor chooses to develop an SMP, communication between the vendor SMP and the associated storage subsystem can be proprietary. If the storage vendor chooses to utilize the SMI-S Service, it must respond to the SMI-S command issued by Windows Storage Management Service.

* The SMP interfaces use WMI.

There are API sets with similar methods and properties: [Storage Management API Classes](storage-management-api-classes.md) and SMP Interfaces. The Storage Management API Classes are the set of classes that applications such as File Server Manager and System Center Virtual Machine Manager use. It includes more host-side-only classes such as Partition, Volume and InitiatorPort. Certain methods in Storage Management API Classes contain an extra input parameter “RunAsJob” (refer to “Asynchronous Operations” section for more information). Meanwhile, SMP Interfaces don't have host-side-only classes and it uses InitiatorId as opposed to InitiatorPort. Despite certain differences, most of the class definitions from the Storage Management API Classes and the SMP Interface are the same.
