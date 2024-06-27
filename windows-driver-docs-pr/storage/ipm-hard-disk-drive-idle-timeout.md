---
title: Idle Power Management Policy
description: Idle Power Management Timeout
ms.date: 06/27/2024
---

# Idle Power Management

This article describes the idle power management (IPM) policy for all storage devices. This policy isn't used on a Modern Standby Windows client.

Although the storage media isn't the primary power consumer on a typical mobile PC, power savings can be realized by idling the storage media. The idle timeout allows Windows to automatically spin down the storage media after a period of disk read and write inactivity for all storage devices.

The power savings that are realized when the storage media is spun down varies by the device's make and model. System manufacturers are encouraged to work with storage vendors to determine the optimal idle timeout value for specific devices.

By default, Windows specifies moderately long idle timeout values. System manufacturers should consider specifying shorter values when trying to achieve aggressive battery conservation on mobile PCs.

The following table summarizes details of idle settings for a hard disk drive (HDD) as an example.

| Detail | Description |
| ------ | ----------- |
| Friendly name     | Turn off hard disk after |
| Description       | Specifies how long the hard drive is inactive before the disk turns off |
| PowerCfg Alias    | DISKIDLE |
| Group policy path | Administrative Templates\System\Power Management\Hard Disk Settings\Turn Off the Hard Disk |
| GUID              | 6738e2c4-e8a5-4a42-b16a-e040e769756e |
| Defined in        | Ntpoapi.h |
| Balanced defaults | 60 minutes (AC) 30 minutes (DC) |

For more information, see [Mobile Battery Life Solutions - A Guide for Mobile Platform Professionals.](https://go.microsoft.com/fwlink/p/?linkid=144534)
