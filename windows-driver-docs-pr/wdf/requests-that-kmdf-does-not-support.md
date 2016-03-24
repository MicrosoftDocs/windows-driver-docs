---
title: Requests That KMDF Does Not Support
description: Requests That KMDF Does Not Support
ms.assetid: 1C23BD32-FD55-4D35-B23D-0B320E3DEDF3
---

# Requests That KMDF Does Not Support


\[Applies to KMDF only\]

Kernel-Mode Driver Framework (KMDF) does not support I/O requests that have the following major IRP codes:

IRP\_MJ\_CREATE\_MAILSLOT

IRP\_MJ\_CREATE\_NAMED\_PIPE

IRP\_MJ\_DEVICE\_CHANGE

[**IRP\_MJ\_DIRECTORY\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548658)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550751)

[**IRP\_MJ\_FLUSH\_BUFFERS**](https://msdn.microsoft.com/library/windows/hardware/ff550760)

[**IRP\_MJ\_LOCK\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff549251)

[**IRP\_MJ\_QUERY\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549279)

[**IRP\_MJ\_QUERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550788)

[**IRP\_MJ\_QUERY\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549293)

[**IRP\_MJ\_QUERY\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549298)

[**IRP\_MJ\_QUERY\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549318)

[**IRP\_MJ\_SET\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549346)

[**IRP\_MJ\_SET\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff550799)

[**IRP\_MJ\_SET\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549401)

[**IRP\_MJ\_SET\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549407)

[**IRP\_MJ\_SET\_VOLUME\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff549415)

When the framework receives such a request, its default action depends on the device object that was the target of the request. For an FDO or PDO, the framework completes the IRP with the status STATUS\_INVALID\_DEVICE\_REQUEST. For a filter DO, the framework passes the IRP to the next lower driver. Although the framework does not support these request types, a KMDF driver can still handle them. For more information, see [Handling an IRP that the Framework Does Not Support](handling-an-irp-that-the-framework-does-not-support.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Requests%20That%20KMDF%20Does%20Not%20Support%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




