---
title: DispatchQueryInformation Routines
description: DispatchQueryInformation Routines
ms.assetid: dfcb8ad0-ae95-4dd7-b4c8-a2f3ad4b12ef
keywords: ["dispatch routines WDK kernel , DispatchQueryInformation routine", "DispatchQueryInformation routine", "IRP_MJ_QUERY_INFORMATION I/O function code", "query information dispatch routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DispatchQueryInformation Routines





A driver's [*DispatchQueryInformation*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine handles IRPs for the [**IRP\_MJ\_QUERY\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-query-information) I/O function code. Driver support for this I/O function code is optional, and typically appears in higher-level or file system drivers. This request is sent by the I/O manager and other operating system components, as well as other kernel-mode drivers. For example, it is sent when a user-mode application calls [**GetFileInformationByHandle**](https://docs.microsoft.com/windows/desktop/api/fileapi/nf-fileapi-getfileinformationbyhandle), and when a kernel-mode component calls [**ZwQueryInformationFile**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationfile).

 

 




