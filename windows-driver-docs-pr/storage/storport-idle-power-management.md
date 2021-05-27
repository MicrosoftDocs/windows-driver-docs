---
title: Storport Idle Power Management Overview
description: Storport Idle Power Management Overview
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport Idle Power Management Overview

Storport Idle Power Management (IPM) allows the classpnp and disk class drivers to send the SCSI Stop Unit command to the disk device when it has been idle for some period of time. The idle period is configurable by the system administrator. The Storport miniport driver is responsible for how the command is used by the Storport miniport driver to conserve power. The following sections describe IPM in more detail.

- [Scope](ipm-scope.md)

- [Assumptions](ipm-assumptions.md)

- [Configuration and Usage](ipm-configuration-and-usage.md)

- [Hard Disk Drive Idle Timeout](ipm-hard-disk-drive-idle-timeout.md)
