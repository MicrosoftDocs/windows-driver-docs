---
title: Dispatch Routine IRQL and Thread Context
description: Dispatch Routine IRQL and Thread Context
keywords:
- IRP dispatch routines WDK file system , IRQL
- IRP dispatch routines WDK file system , thread context
- nonarbitrary thread context WDK file system
- thread context WDK file system
- arbitrary thread context WDK file system
- IRQLs WDK file system
ms.date: 02/23/2023
---

# Dispatch Routine IRQL and Thread Context

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

The following table summarizes the IRQL and thread context requirements for legacy file system filter driver dispatch routines.

| Dispatch routine | Caller's Maximum IRQL | Caller's thread context |
| ---------------- | --------------------- | ----------------------- |
| Cleanup                           | PASSIVE_LEVEL | Nonarbitrary |
| Close                             | APC_LEVEL | Arbitrary |
| Create                            | PASSIVE_LEVEL | Nonarbitrary |
| DeviceControl (except paging I/O) | PASSIVE_LEVEL | Nonarbitrary |
| DeviceControl (paging I/O path)   | APC_LEVEL | Arbitrary |
| DirectoryControl                  | APC_LEVEL | Arbitrary |
| FlushBuffers                      | PASSIVE_LEVEL | Nonarbitrary |
| FsControl (except paging I/O)     | PASSIVE_LEVEL | Nonarbitrary |
| FsControl (paging I/O path)       | APC_LEVEL | Arbitrary |
| LockControl                       | PASSIVE_LEVEL | Nonarbitrary |
| PnP                               | PASSIVE_LEVEL | Arbitrary |
| QueryEa                           | PASSIVE_LEVEL | Nonarbitrary |
| QueryInformation                  | PASSIVE_LEVEL | Nonarbitrary |
| QueryQuota                        | PASSIVE_LEVEL | Nonarbitrary |
| QuerySecurity                     | PASSIVE_LEVEL | Nonarbitrary |
| QueryVolumeInfo                   | PASSIVE_LEVEL | Nonarbitrary |
| Read (except paging I/O)          | PASSIVE_LEVEL | Nonarbitrary |
| Read (paging I/O path)            | APC_LEVEL | Arbitrary |
| SetEa                             | PASSIVE_LEVEL | Nonarbitrary |
| SetInformation                    | PASSIVE_LEVEL | Nonarbitrary |
| SetQuota                          | PASSIVE_LEVEL | Nonarbitrary |
| SetSecurity                       | PASSIVE_LEVEL | Nonarbitrary |
| SetVolumeInfo                     | PASSIVE_LEVEL | Nonarbitrary |
| Shutdown                          | PASSIVE_LEVEL | Arbitrary |
| Write (except paging I/O)         | PASSIVE_LEVEL | Nonarbitrary |
| Write (paging I/O path)           | APC_LEVEL | Arbitrary |
