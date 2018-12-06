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

-   [**IRP\_MJ\_DIRECTORY\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548658)

-   [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550751)

-   [**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760)

-   [**IRP\_MJ\_LOCK\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff549251)

-   [**IRP\_MJ\_QUERY\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549279)

-   [**IRP\_MJ\_QUERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550788)

-   [**IRP\_MJ\_QUERY\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549293)

-   [**IRP\_MJ\_QUERY\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549298)

-   [**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549318)

-   [**IRP\_MJ\_SET\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549346)

-   [**IRP\_MJ\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550799)

-   [**IRP\_MJ\_SET\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549401)

-   [**IRP\_MJ\_SET\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549407)

-   [**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549415)

When the framework receives such a request, its default action depends on the device object that was the target of the request. For an FDO or PDO, the framework completes the IRP with the status STATUS\_INVALID\_DEVICE\_REQUEST. For a filter DO, the framework passes the IRP to the next lower driver. Although the framework does not support these request types, a KMDF driver can still handle them. For more information, see [Handling an IRP that the Framework Does Not Support](handling-an-irp-that-the-framework-does-not-support.md).

 

 





