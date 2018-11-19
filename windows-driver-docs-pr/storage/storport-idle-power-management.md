---
title: Storport Idle Power Management
description: Storport Idle Power Management
ms.assetid: 1ad47775-4d7a-47c4-83eb-774e58c863d3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport Idle Power Management


Storport Idle Power Management (IPM) allows the classpnp and disk class drivers to send the SCSI Stop Unit command to the disk device when it has been idle for some period of time. The idle period is configurable by the system administrator. The Storport miniport driver is responsible for how the command is used by the Storport miniport driver to conserve power. The following sections describe IPM in more detail.

[IPM Scope](ipm-scope.md)

[IPM Assumptions](ipm-assumptions.md)

[IPM Configuration and Usage](ipm-configuration-and-usage.md)

[IPM Hard Disk Drive Idle Timeout](ipm-hard-disk-drive-idle-timeout.md)

 

 




