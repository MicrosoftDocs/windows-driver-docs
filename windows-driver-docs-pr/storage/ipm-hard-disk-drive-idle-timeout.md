---
title: Idle Power Management Hard Disk Drive Idle Timeout
description: Idle Power Management Hard Disk Drive Idle Timeout
ms.date: 04/20/2017
---

# Idle Power Management Hard Disk Drive Idle Timeout

Although the hard disk drive (HDD) is not the primary power consumer in the typical mobile PC, power savings can be realized by spinning down the HDD media. The HDD idle timeout allows Windows to automatically spin down the HDD media after a period of disk read and write inactivity.

The power savings that are realized when the HDD media is spun down varies by the make and model of the HDD. We encourage system manufacturers to work with HDD vendors to determine the optimal HDD idle timeout value for specific devices.

By default, Windows Vista specifies moderately long HDD idle timeout values. System manufacturers should consider specifying shorter values when trying to achieve aggressive battery conservation on mobile PCs. The following table summarizes details of the HDD idle settings.

| Detail | Description |
| ------ | ----------- |
| Friendly name     | Turn off hard disk after |
| Description       | Specifies how long the hard drive is inactive before the disk turns off |
| PowerCfg Alias    | DISKIDLE |
| Group policy path | Administrative Templates\System\Power Management\Hard Disk Settings\Turn Off the Hard Disk |
| GUID              | 6738e2c4-e8a5-4a42-b16a-e040e769756e |
| Defined in        | Ntpoapi.h |
| Balanced defaults | 60 minutes (AC) 30 minutes (DC) |

For more information see [Mobile Battery Life Solutions - A Guide for Mobile Platform Professionals.](https://go.microsoft.com/fwlink/p/?linkid=144534)
