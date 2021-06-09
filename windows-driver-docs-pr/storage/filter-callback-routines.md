---
title: Filter Callback Routines
description: Filter Callback Routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Callback Routines


The crash dump driver supports the following callback routines in a crash dump filter driver. These callback routines are not mandatory, so a crash dump filter driver is free to implement only a callback routine that is required to add the desired functionality.

[**Dump\_Start**](/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_start)

[**Dump\_Write**](/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_write)

[**Dump\_Read**](/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_read)

[**Dump\_Finish**](/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_finish)

[**Dump\_Unload**](/windows-hardware/drivers/ddi/ntdddump/nc-ntdddump-dump_unload)

 

