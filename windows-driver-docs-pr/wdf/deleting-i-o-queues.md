---
title: Deleting I/O Queues
author: windows-driver-content
description: Deleting I/O Queues
ms.assetid: 7eb7a24d-de39-4e3d-865c-ebfb49d43519
keywords: ["I/O queues WDK KMDF , deleting", "temporary I/O queues WDK KMDF", "deleting I/O queues WDK KMDF"]
---

# Deleting I/O Queues


Framework-based drivers must delete only some of the I/O queues that they create. If a driver creates a [default I/O queue](creating-i-o-queues.md) or an I/O queue that it configures by calling [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920), the framework deletes the queue object for the driver.

For example, if you intend for each device's I/O queues to exist as long as each device remains plugged into the system, your driver will create its I/O queues in its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. Your driver might create a default queue that receives all requests except read requests and a separate queue that receives only read requests.

The driver cannot delete these I/O queues. Instead, the framework deletes the queue objects when it deletes the device object to which the queue belongs. For information about why your driver cannot delete these I/O queues, see the following note.

If, however, your driver creates temporary I/O queues outside of its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, it must call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete these queues when it has finished using them. For example, a driver that provides an [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function might create an I/O queue to handle I/O requests that are associated with a particular framework file object. In this case the driver's [*EvtFileCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff541700) callback function must call [**WdfIoQueuePurge**](https://msdn.microsoft.com/library/windows/hardware/ff548442) to purge the queue and then call **WdfObjectDelete** to delete it.

**Note**   The framework does not permit a driver to delete its default I/O queue, or any I/O queue that the driver configures to receive all I/O requests of a particular type (by calling [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920)). If your driver calls [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the queue object that represents one of these queues, **WdfObjectDelete** returns without deleting the object. **WdfObjectDelete** does not provide a return status, so the framework reports an error only if you are [using the framework's verifier](using-kmdf-verifier.md).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Deleting%20I/O%20Queues%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




