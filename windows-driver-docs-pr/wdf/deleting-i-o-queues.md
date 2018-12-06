---
title: Deleting I/O Queues
description: Deleting I/O Queues
ms.assetid: 7eb7a24d-de39-4e3d-865c-ebfb49d43519
keywords:
- I/O queues WDK KMDF , deleting
- temporary I/O queues WDK KMDF
- deleting I/O queues WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Deleting I/O Queues


Framework-based drivers must delete only some of the I/O queues that they create. If a driver creates a [default I/O queue](creating-i-o-queues.md) or an I/O queue that it configures by calling [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920), the framework deletes the queue object for the driver.

For example, if you intend for each device's I/O queues to exist as long as each device remains plugged into the system, your driver will create its I/O queues in its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. Your driver might create a default queue that receives all requests except read requests and a separate queue that receives only read requests.

The driver cannot delete these I/O queues. Instead, the framework deletes the queue objects when it deletes the device object to which the queue belongs. For information about why your driver cannot delete these I/O queues, see the following note.

If, however, your driver creates temporary I/O queues outside of its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function, it must call [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete these queues when it has finished using them. For example, a driver that provides an [*EvtDeviceFileCreate*](https://msdn.microsoft.com/library/windows/hardware/ff540868) callback function might create an I/O queue to handle I/O requests that are associated with a particular framework file object. In this case the driver's [*EvtFileCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff541700) callback function must call [**WdfIoQueuePurge**](https://msdn.microsoft.com/library/windows/hardware/ff548442) to purge the queue and then call **WdfObjectDelete** to delete it.

**Note**   The framework does not permit a driver to delete its default I/O queue, or any I/O queue that the driver configures to receive all I/O requests of a particular type (by calling [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920)). If your driver calls [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) to delete the queue object that represents one of these queues, **WdfObjectDelete** returns without deleting the object. **WdfObjectDelete** does not provide a return status, so the framework reports an error only if you are [using the framework's verifier](using-kmdf-verifier.md).

 

 

 





