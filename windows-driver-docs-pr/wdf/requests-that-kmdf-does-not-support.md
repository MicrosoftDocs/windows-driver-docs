---
title: Requests That KMDF Does Not Support
description: Requests That KMDF Does Not Support
ms.assetid: 1C23BD32-FD55-4D35-B23D-0B320E3DEDF3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requests That KMDF Does Not Support


\[Applies to KMDF only\]

Kernel-Mode Driver Framework (KMDF) does not support I/O requests that have the following major IRP codes:

-   IRP\_MJ\_CREATE\_MAILSLOT

-   IRP\_MJ\_CREATE\_NAMED\_PIPE

-   IRP\_MJ\_DEVICE\_CHANGE

-   [**IRP\_MJ\_DIRECTORY\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-directory-control)

-   [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-file-system-control)

-   [**IRP\_MJ\_FLUSH\_BUFFERS**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-flush-buffers)

-   [**IRP\_MJ\_LOCK\_CONTROL**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-lock-control)

-   [**IRP\_MJ\_QUERY\_EA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-ea)

-   [**IRP\_MJ\_QUERY\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-query-information)

-   [**IRP\_MJ\_QUERY\_QUOTA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-quota)

-   [**IRP\_MJ\_QUERY\_SECURITY**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-security)

-   [**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-query-volume-information)

-   [**IRP\_MJ\_SET\_EA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-ea)

-   [**IRP\_MJ\_SET\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/kernel/irp-mj-set-information)

-   [**IRP\_MJ\_SET\_QUOTA**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-quota)

-   [**IRP\_MJ\_SET\_SECURITY**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-security)

-   [**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](https://docs.microsoft.com/windows-hardware/drivers/ifs/irp-mj-set-volume-information)

When the framework receives such a request, its default action depends on the device object that was the target of the request. For an FDO or PDO, the framework completes the IRP with the status STATUS\_INVALID\_DEVICE\_REQUEST. For a filter DO, the framework passes the IRP to the next lower driver. Although the framework does not support these request types, a KMDF driver can still handle them. For more information, see [Handling an IRP that the Framework Does Not Support](handling-an-irp-that-the-framework-does-not-support.md).

 

 





