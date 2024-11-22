---
title: Introduction to Storage Management for Driver Developers
description: Introduces storage management
keywords:
- storage management , Windows , WDK
- SMI-S , Windows , storage management , WDK
- storage management provider , WDK
- WMI , Windows , storage management , WDK
ms.date: 11/21/2024
---

# Introduction to storage management for driver developers

As storage infrastructure gets increasingly complex, it's important to be able to manage storage ecosystems efficiently. This article introduces:

* The storage industry's Storage Management Initiative Specification (SMI-S).

* The Windows Storage Management Provider (SMP) framework.

* The Windows Management Instrumentation (WMI) classes available in the Windows storage management architecture.  

## Storage Management Initiative Specification (SMI-S)  

SMI-S is an ANSI standard developed by the Storage Networking Industry Association (SNIA). It defines an interoperable framework for the management of storage devices and services in a storage area network (SAN) of *heterogenous* storage vendor devices. SMI-S aims to help the management of storage environments by providing a standardized method for the discovery, configuration, monitoring, and management of storage resources, regardless of the vendor or technology. This standard enables a wide range of storage operations, including provisioning, capacity management, and SAN configuration, through a common set of interfaces.

For driver developers, adhering to SMI-S standards ensures that storage solutions can be managed consistently in multi-vendor environments, enhancing compatibility and integration capabilities.  

## Storage Management Provider (SMP)  

Windows [SMP](storage-management-providers.md)  is a powerful and flexible framework for managing storage resources within Windows environments. By abstracting the complexities of the underlying storage technologies into a consistent set of management interfaces, SMP simplifies the tasks of configuration, optimization, and monitoring of storage resources.

SMP uses a set of Windows Management Instrumentation (WMI) classes to offer a standardized interface for managing storage configurations such as disks, partitions, volumes, and Storage Spaces. SMP facilitates a wide array of storage management tasks including the creation and management of virtual disks, monitoring disk health, and configuring resilient storage spaces.  

## Windows Management Instrumentation (WMI) Classes  

WMI provides a standardized method for accessing management information in an enterprise environment. It includes a rich set of classes for managing both hardware and software components, including storage. WMI classes relevant to storage management allow for querying disk information, monitoring health status, and performing various configuration tasks programmatically.  

## Relationship between SMI-S, SMP, and WMI  

While SMI-S, SMP, and WMI serve distinct functions, they collectively contribute to a comprehensive storage management framework in Windows environments. SMI-S allows for interoperability and standardized management across nonheterogeneous storage technologies and vendors. SMP uses WMI classes to provide the specific mechanisms for managing storage within the Windows ecosystem.  

* SMI-S ensures that storage devices from various vendors can be managed in a standardized way, facilitating broad compatibility.

* SMP acts as the bridge between Windows' management infrastructure and the underlying storage hardware, standardizing the management interface within Windows itself.

* WMI Classes provide the foundational access to storage management capabilities, enabling both SMP and custom management solutions to interact with storage hardware and configurations.  
