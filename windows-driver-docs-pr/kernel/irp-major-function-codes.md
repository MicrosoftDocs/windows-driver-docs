---
title: IRP Major Function Codes
author: windows-driver-content
description: IRP Major Function Codes
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 11c5b1a9-74c0-47fb-8cce-a008ece9efae
---

# IRP Major Function Codes


## <a href="" id="ddk-irp-major-function-codes-kr"></a>


Each driver-specific I/O stack location ([**IO\_STACK\_LOCATION**](https://msdn.microsoft.com/library/windows/hardware/ff550659)) for every [**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694) contains a major function code (**IRP\_MJ\_*XXX***), which tells the driver what operation it or the underlying device driver should carry out to satisfy the I/O request. Each kernel-mode driver must provide [*dispatch routines*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-dispatch-routine) for the major function codes that it must support.

The specific operations a driver carries out for a given **IRP\_MJ\_*XXX*** code depend somewhat on the underlying device, particularly for [**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md) and [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md) requests. For example, the requests sent to a keyboard driver are necessarily somewhat different from those sent to a disk driver. However, the I/O manager defines the parameters and I/O stack location contents for each system-defined major function code.

Every higher-level driver must set up the appropriate I/O stack location in IRPs for the next-lower-level driver and call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336), either with each input IRP, or with a driver-created IRP (if the higher-level driver holds on to the input IRP). Consequently, every intermediate driver must supply a dispatch routine for each major function code that the underlying device driver handles. Otherwise, a new intermediate driver will "break the chain" whenever an application or still higher-level driver attempts to send an I/O request down to the underlying device driver.

File system drivers also handle a required subset of system-defined **IRP\_MJ\_*XXX*** function codes, some with subordinate **IRP\_MN\_*XXX*** function codes.

Drivers handle IRPs set with some or all of the following major function codes:

[**IRP\_MJ\_CLEANUP**](irp-mj-cleanup.md)

[**IRP\_MJ\_CLOSE**](irp-mj-close.md)

[**IRP\_MJ\_CREATE**](irp-mj-create.md)

[**IRP\_MJ\_DEVICE\_CONTROL**](irp-mj-device-control.md)

[**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](irp-mj-file-system-control.md)

[**IRP\_MJ\_FLUSH\_BUFFERS**](irp-mj-flush-buffers.md)

[**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](irp-mj-internal-device-control.md)

[**IRP\_MJ\_PNP**](irp-mj-pnp.md)

[**IRP\_MJ\_POWER**](irp-mj-power.md)

[**IRP\_MJ\_QUERY\_INFORMATION**](irp-mj-query-information.md)

[**IRP\_MJ\_READ**](irp-mj-read.md)

[**IRP\_MJ\_SET\_INFORMATION**](irp-mj-set-information.md)

[**IRP\_MJ\_SHUTDOWN**](irp-mj-shutdown.md)

[**IRP\_MJ\_SYSTEM\_CONTROL**](irp-mj-system-control.md)

[**IRP\_MJ\_WRITE**](irp-mj-write.md)

The input and output parameters described in this section are the function-specific parameters in the IRP.

For more information about IRPs, see [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20IRP%20Major%20Function%20Codes%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


