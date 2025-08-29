---
title: Storport Idle Power Management Overview
description: Storport Idle Power Management Overview
keywords:
- idle power management, storage devices, Windows
ms.date: 06/27/2024
ms.topic: concept-article
---

# Storport Idle Power Management Overview

Storport provides support for [idle power management](../kernel/detecting-an-idle-device.md) to allow storage devices to enter a low power state when not in use. Storport's idle power management (IPM) support includes handling idle power management for storage devices under its management, in coordination with the Power Manager in Windows.

Storport IPM allows the *classpnp* and disk class drivers to send the **SCSI Stop Unit** command to the storage device when it's idle for some period of time. The idle period is configurable by the system administrator. The Storport miniport driver is responsible for how the command is used by the Storport miniport driver to conserve power. The following sections describe IPM in more detail.

- [Scope](ipm-scope.md)

- [Assumptions](ipm-assumptions.md)

- [Configuration and Usage](ipm-configuration-and-usage.md)

- [Hard Disk Drive Idle Timeout](ipm-hard-disk-drive-idle-timeout.md)
