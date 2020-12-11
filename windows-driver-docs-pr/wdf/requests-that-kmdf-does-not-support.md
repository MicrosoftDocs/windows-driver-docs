---
title: Requests That KMDF Does Not Support
description: Requests That KMDF Does Not Support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requests That KMDF Does Not Support


\[Applies to KMDF only\]

Kernel-Mode Driver Framework (KMDF) does not support I/O requests that have the following major IRP codes:

-   IRP\_MJ\_CREATE\_MAILSLOT

-   IRP\_MJ\_CREATE\_NAMED\_PIPE

-   IRP\_MJ\_DEVICE\_CHANGE

-   [**IRP\_MJ\_DIRECTORY\_CONTROL**](../ifs/irp-mj-directory-control.md)

-   [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](../kernel/irp-mj-file-system-control.md)

-   [**IRP\_MJ\_FLUSH\_BUFFERS**](../kernel/irp-mj-flush-buffers.md)

-   [**IRP\_MJ\_LOCK\_CONTROL**](../ifs/irp-mj-lock-control.md)

-   [**IRP\_MJ\_QUERY\_EA**](../ifs/irp-mj-query-ea.md)

-   [**IRP\_MJ\_QUERY\_INFORMATION**](../kernel/irp-mj-query-information.md)

-   [**IRP\_MJ\_QUERY\_QUOTA**](../ifs/irp-mj-query-quota.md)

-   [**IRP\_MJ\_QUERY\_SECURITY**](../ifs/irp-mj-query-security.md)

-   [**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](../ifs/irp-mj-query-volume-information.md)

-   [**IRP\_MJ\_SET\_EA**](../ifs/irp-mj-set-ea.md)

-   [**IRP\_MJ\_SET\_INFORMATION**](../kernel/irp-mj-set-information.md)

-   [**IRP\_MJ\_SET\_QUOTA**](../ifs/irp-mj-set-quota.md)

-   [**IRP\_MJ\_SET\_SECURITY**](../ifs/irp-mj-set-security.md)

-   [**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](../ifs/irp-mj-set-volume-information.md)

When the framework receives such a request, its default action depends on the device object that was the target of the request. For an FDO or PDO, the framework completes the IRP with the status STATUS\_INVALID\_DEVICE\_REQUEST. For a filter DO, the framework passes the IRP to the next lower driver. Although the framework does not support these request types, a KMDF driver can still handle them. For more information, see [Handling an IRP that the Framework Does Not Support](handling-an-irp-that-the-framework-does-not-support.md).

 

