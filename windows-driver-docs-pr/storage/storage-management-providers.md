---
title: Storage Management Providers (Windows Drivers)
description: Learn more about the Storage Management Providers.
keywords:
- storage management provider , wdk
- SMI-S provider, storage management provider
ms.date: 09/24/2024
---

# Storage Management Providers

A Windows storage management provider (SMP) is a component that enables management and configuration of storage resources through the [Windows Storage Management API](windows-storage-management-api-portal.md). An SMP acts as an intermediary between the storage management software and the underlying storage hardware or software-defined storage solutions.

Storage vendors can include Windows-based management of their storage subsystems by supporting the Windows Storage Management API. Windows management applications can use this API to provide integrated storage management services.

In order to support the [Windows Storage Management API](windows-storage-management-api-portal.md), storage vendors can choose to either:

* Develop an SMP.
* Develop an [SMI-S provider](/previous-versions/windows/desktop/smi-s/dn265461(v=vs.85)). This provider is accessed through the built-in Windows Storage Management Service, which is implemented as an SMP.

Both mechanisms equally enable ease-of-management of the storage subsystem through the storage management API. Further, both mechanisms enable easy extensibility through a well-defined pass-through interface.

As previously stated, the [Windows Storage Management API](windows-storage-management-api-portal.md) aims to deliver on comprehensive storage provisioning and administration capabilities. The API is designed to evolve as needed with successive Windows versions.

The pass-through interface enables storage management applications to perform operations on compatible storage subsystems that, for various reasons, aren't yet enabled directly through the API. While the pass-through mechanism is important for easy extensibility, it's to be used solely for capabilities that aren't exposed through the API. To that end, it must not be used for capabilities that can be administered through the API.

## Architecture

The SMP architectural model has the following features:

* Windows management applications, including built-in PowerShell commandlets, use the [Windows Storage Management API](windows-storage-management-api-portal.md). For the small subset of capabilities not yet exposed through the API, Windows storage management applications can use a pass-through mechanism. This capability allows, for example, the full suite of SMI-S classes and methods to be used if needed and also enables proprietary communication between the application and the storage provider.

* Storage subsystems can ensure they're manageable by Windows management applications by committing to responding to the new API through their SMP or SMI-S provider implementation. If the storage vendor chooses to develop an SMP, communication between the vendor SMP and the associated storage subsystem can be proprietary. If the storage vendor chooses to utilize the SMI-S Service, it must respond to the SMI-S command issued by Windows Storage Management Service.

* The SMP interfaces use WMI.

There are API sets with similar methods and properties:

* [Storage Management API Classes](storage-management-api-classes.md) are the set of classes that applications such as File Server Manager and System Center Virtual Machine Manager use. It includes more host-side-only classes such as Partition, Volume, and InitiatorPort. Certain methods in Storage Management API Classes contain an extra *RunAsJob* input parameter. For more information, see [Asynchronous Operations](smp-behavior-interaction.md).

* SMP Interfaces, which don't have host-side-only classes and use InitiatorId as opposed to InitiatorPort.

Despite certain differences, most of the class definitions from the Storage Management API Classes and the SMP Interface are the same.
