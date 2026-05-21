---
title: DxgKrnl Configuration
description: This page hosts miscellaneous configuration interfaces for the accelerator stack that don't have another page
ms.author: maiah
ms.date: 5/26/2026
ms.topic: reference
---

# DxgKrnl Configuration

This page hosts miscellaneous configuration interfaces for the accelerator stack that don't have another page.  

> [!IMPORTANT]
> This page exposes behaviors that might change as systems evolve. These behaviors might not be supported on all releases.

## Registry

If they're defined, DxgKrnl uses the following values under the key `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers` to override default behavior. DxgKrnl uses safe and appropriate default values when no override is specified in the registry.

> [!CAUTION]
> Adjusting these values can cause system instability.

| Name | Type | Description |
| --- | --- | --- |
| MemoryManager\SystemPartitionCommitLimitPercentage | DWORD | Minimum limit for the percentage of system memory that accelerators are allowed to access, if available at runtime. |
| MemoryManager\SystemPartitionCommitLimitPercentageMax | DWORD | Maximum limit for the percentage of system memory that accelerators are allowed to access, if available at runtime. |
