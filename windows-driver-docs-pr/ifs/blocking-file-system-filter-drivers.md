---
title: Blocking Legacy File System Filter Drivers
description: Starting in Windows 10, version 1607, administrators and driver developers can use a registry setting to block legacy file system filter drivers.
keywords:
- file system filter drivers, blocking, legacy
ms.date: 09/05/2024
---

# Blocking legacy file system filter drivers

Starting in Windows 10, version 1607, administrators and driver developers can use a registry setting to block and unblock [legacy file system filter drivers](about-file-system-legacy-filter-drivers.md). *Legacy file system filter drivers* attach to the file system stack directly and don't use Filter Manager.

This article describes the registry setting and the event entered into the System event log when a legacy file system (FS) filter is blocked. It also describes how to check if the OS has legacy FS drivers running.

## How to block legacy drivers

Use the **IoBlockLegacyFsFilters** registry key to indicate whether the system blocks legacy FS filter drivers. When blocked, all legacy FS filter drivers are blocked from loading. For the registry changes to take effect, perform a system restart.

The registry key must be created under the following registry path:

``` syntax
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\I/O System
```

The following table describes the valid DWORD values for the **IoBlockLegacyFsFilters** key.

| **IoBlockLegacyFsFilters** value | Description |
| -------------------------------- | ----------- |
| **1** | Legacy FS filter drivers are blocked from loading or attaching to storage volumes. |
| **0** | Legacy FS filter drivers aren't blocked. This behavior is the default. |

The following figure shows what the key looks like in Registry Editor.

:::image type="content" source="images/ioblockregkey.png" alt-text="Image that shows how to edit the ioblocklegacyfsfilters registry key.":::

## Example: when a legacy driver is blocked from loading

An **Error** event is logged to the System event log when a legacy FS filter driver is blocked from loading, as shown here:

| Event property | Description |
| -------------- | ----------- |
| Log Name       | System      |
| Source         | Microsoft-Windows-Kernel-IO |
| Date           | 12/29/2015 2:55:05 PM |
| Event ID       | 1205         |
| Task Category  | None         |
| Level          | Error        |
| Keywords       |              |
| User           | CONTOSO\user |
| Computer       | user.domain.corp.contoso.com |
| Description    | Windows is configured to block legacy FS filters. Filter name: \Driver\sfilter |

## How to check if legacy drivers are running

To determine which filters are legacy FS filter drivers and whether they're running, you can perform the following steps:

1. Open an elevated Command Prompt by selecting and holding (or right-clicking) a **cmd.exe** icon and selecting **Run as administrator**.
2. Type: `fltmc filters`
3. Look for legacy drivers, they're the ones with a **Frame** value of **\<Legacy>**.

In this example, three filters are running. The legacy FS filter drivers—AVLegacy and EncryptionLegacy—are marked with the **\<Legacy>** Frame value. AVMiniFilter doesn't have the **\<Legacy>** Frame value because it's a minifilter driver (it doesn't attach to the FS stack directly and uses Filter Manager).

``` syntax
C:\Windows\system32>fltmc filters

Filter Name                     Num Instances    Altitude    Frame
------------------------------  -------------  ------------  -----
AVLegacy                                        389998.99   <Legacy>
EncryptionLegacy                                149998.99   <Legacy>
AVMiniFilter                           3        328000         0
```

If you see that legacy drivers are still running after you block legacy FS filter drivers, make sure you reboot the system after setting the **IoBlockLegacyFsFilters** registry key. The setting doesn't take effect until after a reboot.

If your system has legacy FS filter drivers, work with the respective filter developers to get the minifilter version of the FS driver. For information about porting legacy FS filter drivers to minifilter drivers that use the Filter Manager model, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).
