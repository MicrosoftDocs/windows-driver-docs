---
title: Support for More than 64 Processors in NDIS 6.20
description: Support for More than 64 Processors in NDIS 6.20
keywords:
- NDIS 6.20 WDK , support for more than 64 processors
ms.date: 03/02/2023
---

# Support for More than 64 Processors in NDIS 6.20





The NDIS 6.20 interface introduces support for more than 64 processors. Previous NDIS versions are limited to no more than 64 processors (32 in x86 versions of the operating system).

To remain backward compatible with older implementations, NDIS supports processor groups. Software that has not been updated to support more than 64 processors can default to processor group zero.

To support more than 64 processors, NDIS 6.20 and later provide updated versions of these interfaces:

-   [Receive Side Scaling (RSS)](./receive-side-scaling-version-2-rssv2-.md)

-   Processor information device driver interfaces (see [NDIS System Information Functions](/windows-hardware/drivers/ddi/_netvista/))

-   Resource allocation (see [NDIS Memory Management Interface](/windows-hardware/drivers/ddi/_netvista/))

-   Read and write locks (see [NDIS Read Write Lock Reference](/windows-hardware/drivers/ddi/_netvista/))

Some of the NDIS device driver interface elements are obsolete for NDIS 6.20 and later drivers. For more information about obsolete interfaces, see [Obsolete Interfaces in NDIS 6.20](obsolete-interfaces-in-ndis-6-20.md).

 

