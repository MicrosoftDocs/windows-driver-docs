---
title: DispatchSetInformation Routines
description: DispatchSetInformation Routines
keywords: ["dispatch routines WDK kernel , DispatchSetInformation routine", "DispatchSetInformation routine", "set information dispatch routines WDK kernel", "IRP_MJ_SET_INFORMATION I/O function code"]
ms.date: 06/16/2017
---

# DispatchSetInformation Routines





A driver's [*DispatchSetInformation*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine handles IRPs for the [**IRP\_MJ\_SET\_INFORMATION**](./irp-mj-set-information.md) I/O function code. Driver support for this I/O function code is optional, and typically appears in higher-level or file system drivers. This request is sent by the I/O manager and other operating system components, as well as other kernel-mode drivers. For example, it is sent when a user-mode application calls [**SetEndOfFile**](/windows/win32/api/fileapi/nf-fileapi-setendoffile), and when a kernel-mode component calls [**ZwSetInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile).

 

