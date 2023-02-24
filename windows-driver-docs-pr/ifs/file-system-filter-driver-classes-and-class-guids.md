---
title: File System Filter Driver Classes and Class GUIDs
description: File System Filter Driver Classes and Class GUIDs
keywords:
- GUIDs WDK file system
- class GUIDs WDK file system
- classes WDK file system
- filter drivers WDK file system , classes
- file system filter drivers WDK , classes
ms.date: 02/23/2023
---

# File System Filter Driver Classes and Class GUIDs

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

Microsoft Windows XP and later operating systems provide setup classes for legacy file system filter drivers. These classes provide a subset of the functionality that system-supplied [device setup classes](../install/overview-of-device-setup-classes.md) provide for hardware devices.

Each setup class is associated with a class GUID. The system-defined class GUIDs are defined in *devguid.h*.

This article lists the setup classes for file system filter drivers. In the definition for each class, the **Class** and **ClassGuid** entries contain the values that you should specify in the [**INF Version section**](../install/inf-version-section.md) of a filter's INF file. Your filter driver should use the class and GUID that match the [load order group](load-order-groups-for-file-system-filter-drivers.md) that is specified in your driver's INF file.

When your filter driver supplies the appropriate **ClassGuid** value in the INF file for a device, rather than or in addition to the **Class** = *class-name* entry, it significantly improves the performance of searching system INF files.

The following list includes system-defined classes and class GUIDs for file system filter drivers. The entries in this list correspond to the load order groups that were created for file system filter drivers in Windows XP and later operating systems.

> [!NOTE]
> Three load order groups do not appear in the list, because they are not considered setup classes and thus do not have class GUIDs assigned to them: Filter, FSFilter Top, and FSFilter Bottom.

FSFilter Activity Monitor

* Class = ActivityMonitor
* ClassGuid = {b86dff51-a31e-4bac-b3cf-e8cfe75c9fc2}

FSFilter Undelete

* Class = Undelete
* ClassGuid = {fe8f1572-c67a-48c0-bbac-0b5c6d66cafb}

FSFilter Anti-Virus

* Class = AntiVirus
* ClassGuid = {b1d1a169-c54f-4379-81db-bee7d88d7454}

FSFilter Replication

* Class = Replication
* ClassGuid = {48d3ebc4-4cf8-48ff-b869-9c68ad42eb9f}

FSFilter Continuous Backup

* Class = ContinuousBackup
* ClassGuid = {71aa14f8-6fad-4622-ad77-92bb9d7e6947}

FSFilter Content Screener

* Class = ContentScreener
* ClassGuid = {3e3f0674-c83c-4558-bb26-9820e1eba5c5}

FSFilter Quota Management

* Class = QuotaManagement
* ClassGuid = {8503c911-a6c7-4919-8f79-5028f5866b0c}

FSFilter System Recovery

* Class = SystemRecovery
* ClassGuid = {2db15374-706e-4131-a0c7-d7c78eb0289a}

FSFilter Cluster File System

* Class = CFSMetaDataServer
* ClassGuid = {cdcf0939-b75b-4630-bf76-80f7ba655884}

FSFilter HSM

* Class = HSM
* ClassGuid = {d546500a-2aeb-45f6-9482-f4b1799c3177}

FSFilter Imaging

* No load order group defined; use FSFilter Compression

FSFilter Compression

* Class = Compression
* ClassGuid = {f3586baf-b5aa-49b5-8d6c-0569284c639f}

FSFilter Encryption

* Class = Encryption
* ClassGuid = {a0a701c0-a511-42ff-aa6c-06dc0395576f}

FSFilter Virtualization

* Class = Virtualization
* ClassGuid = {f75a86c0-10d8-4c3a-b233-ed60e4cdfaac} |

FSFilter Physical Quota Management

* Class = PhysicalQuotaManagement
* ClassGuid = {6a0a8e78-bba6-4fc4-a709-1e33cd09d67e}

FSFilter Open File

* Class = OpenFileBackup
* ClassGuid = {f8ecafa6-66d1-41a5-899b-66585d7216b7}

FSFilter Security Enhancer

* Class = SecurityEnhancer
* ClassGuid = {d02bc3da-0c8e-4945-9bd5-f1883c226c8c}

FSFilter Copy Protection

* Class = CopyProtection
* ClassGuid = {89786ff1-9c12-402f-9c9e-17753c7f4375}

FSFilter System

* Class = FSFilterSystem
* ClassGuid = {5d1b9aaa-01e2-46af-849f-272b3f324c46}

FSFilter Infrastructure

* Class = Infrastructure
* ClassGuid = {e55fa6f9-128c-4d04-abab-630c74b1453a}
