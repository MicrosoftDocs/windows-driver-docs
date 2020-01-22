---
title: DispatchFlushBuffers Routines
description: DispatchFlushBuffers Routines
ms.assetid: 091ce55c-e867-4ba4-aa25-5c20af45d9c2
keywords: ["dispatch routines WDK kernel , DispatchFlushBuffers routine", "DispatchFlushBuffers routine", "IRP_MJ_FLUSH_BUFFERS I/O function code", "flush buffers dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchFlushBuffers Routines





A driver's [*DispatchFlushBuffers*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine handles IRPs for the [**IRP\_MJ\_FLUSH\_BUFFERS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-flush-buffers) I/O function code. Driver support for this I/O function code is optional, but all file system and filter drivers that maintain internal data buffers must handle it to preserve changes to file data or metadata across system shutdowns. This request is sent by the I/O manager and other operating system components, as well as other kernel-mode drivers, when buffered data needs to be flushed to disk. For example, it is sent when a user-mode application calls [**FlushFileBuffers**](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-flushfilebuffers).

 

 




