---
title: Filter Callback Routines
description: Filter Callback Routines
ms.assetid: 3d9f874c-f026-40fc-a97d-0d4cefa3d1f9
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Callback Routines


The crash dump driver supports the following callback routines in a crash dump filter driver. These callback routines are not mandatory, so a crash dump filter driver is free to implement only a callback routine that is required to add the desired functionality.

[**Dump\_Start**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_start)

[**Dump\_Write**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_write)

[**Dump\_Read**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_read)

[**Dump\_Finish**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_finish)

[**Dump\_Unload**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_unload)

 

 




