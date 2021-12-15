---
title: Blocking legacy file system filter drivers
description: Starting in Windows 10, version 1607, administrators and driver developers can use a registry setting to block legacy file system filter drivers.
ms.date: 04/20/2017
---

# Blocking legacy file system filter drivers

Starting in Windows 10, version 1607, administrators and driver developers can use a registry setting to block legacy file system filter drivers. *Legacy file system filter drivers* are drivers that attach to the file system stack directly and don't use Filter Manager. This topic describes the registry setting for blocking and unblocking legacy file system filter drivers. It also describes the event entered into the System event log when a legacy file system filter is blocked and how to check if the OS has legacy file system drivers running.

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

## How to block legacy drivers

Use the **IoBlockLegacyFsFilters** registry key to specify if the system blocks legacy file system filter drivers. When blocked, all legacy file system filter drivers are blocked from loading. For the registry changes to take effect, perform a system restart.

The registry key must be created under the following registry path:

``` syntax
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\I/O System
```

The valid DWORD values for the **IoBlockLegacyFsFilters** key are as follows:

| **IoBlockLegacyFsFilters** value | Description                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------------------|
| **1**                            | Legacy file system filter drivers are blocked from loading or attaching to storage volumes.       |
| **0**                            | Legacy file system filter drivers are not blocked. In this release, this is the default behavior. |

This is what the key looks like in Registry Editor:

![editing the ioblocklegacyfsfilters registry key.](images/ioblockregkey.png)

## Example: when a legacy driver is blocked from loading

An **Error** event is logged to the System event log when a legacy file system filter driver is blocked from loading, as shown here:

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
| Description    | Windows is configured to block legacy file system filters. Filter name: \Driver\sfilter |

## How to check if legacy drivers are running

If you're unsure which filters are legacy file system filter drivers or want to make sure that they're not running, you can perform the following:

1. Open an elevated Command Prompt by selecting and holding (or right-clicking) a **cmd.exe** icon and selecting **Run as administrator**.
2. Type: `fltmc filters`
3. Look for legacy drivers, they're the ones with a **Frame** value of **&lt;Legacy&gt;**.

In this example, the legacy file system filter drivers, named AVLegacy and EncryptionLegacy, are marked with the **&lt;Legacy&gt;** Frame value. The file system driver named AVMiniFilter does not have the **&lt;Legacy&gt;** Frame value because it is a minifilter driver (it does not attach to the file system stack directly and uses Filter Manager).

``` syntax
C:\Windows\system32>fltmc filters

Filter Name                     Num Instances    Altitude    Frame
------------------------------  -------------  ------------  -----
AVLegacy                                        389998.99   <Legacy>
EncryptionLegacy                                149998.99   <Legacy>
AVMiniFilter                           3        328000         0
```

If you see that legacy drivers are still running after you block legacy file system filter drivers, make sure you reboot the system after setting the **IoBlockLegacyFsFilters** registry key. The setting will not take effect until after a reboot.

If your system has legacy file system filter drivers, work with the respective ISVs to get the Minifilter version of the file system driver. For info about porting legacy file system filter drivers to minifilter drivers that use the Filter Manager model, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).
