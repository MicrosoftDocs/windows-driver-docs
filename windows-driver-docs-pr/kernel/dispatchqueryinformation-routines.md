---
title: DispatchQueryInformation Routines
description: DispatchQueryInformation Routines
keywords: ["dispatch routines WDK kernel , DispatchQueryInformation routine", "DispatchQueryInformation routine", "IRP_MJ_QUERY_INFORMATION I/O function code", "query information dispatch routines WDK kernel"]
ms.date: 06/16/2017
---

# DispatchQueryInformation Routines





A driver's [*DispatchQueryInformation*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine handles IRPs for the [**IRP\_MJ\_QUERY\_INFORMATION**](./irp-mj-query-information.md) I/O function code. Driver support for this I/O function code is optional, and typically appears in higher-level or file system drivers. This request is sent by the I/O manager and other operating system components, as well as other kernel-mode drivers. For example, it is sent when a user-mode application calls [**GetFileInformationByHandle**](/windows/win32/api/fileapi/nf-fileapi-getfileinformationbyhandle), and when a kernel-mode component calls [**ZwQueryInformationFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile).

 

