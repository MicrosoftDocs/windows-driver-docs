---
title: Example Uses of I/O Queues
description: Example Uses of I/O Queues
ms.assetid: 13b09254-ce0a-4c7d-bdb1-d28ec094a266
keywords:
- I/O queues WDK KMDF , examples
- request handlers WDK KMDF
- default I/O queues WDK KMDF
- single I/O queues WDK KMDF
- multiple I/O queues WDK KMDF
- parallel I/O queues WDK KMDF
- sequential I/O queues WDK KMDF
- manual I/O queues WDK KMDF
- I/O queues WDK KMDF , dispatching methods
- dispatching methods WDK KMDF
- sequential dispatching WDK KMDF
- synchronous dispatching WDK KMDF
- parallel dispatching WDK KMDF
- asynchronous dispatching WDK KMDF
- manual dispatching WDK KMDF
- WdfIoQueueDispatchParallel
- WdfIoQueueDispatchSequential
- WdfIoQueueDispatchManual
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example Uses of I/O Queues





For each device that is connected to a system and supported by a particular driver, the driver can use the following combinations of I/O queues and [request handlers](request-handlers.md):

-   A single, default I/O queue and a single request handler, [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757). The framework will deliver all of the device's requests to the default queue, and it will call the driver's *EvtIoDefault* handler to deliver each request to the driver.

-   A single, default I/O queue and multiple request handlers such as [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776), [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813), and [*EvtIoDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff541758). The framework will deliver all of the device's requests to the default queue. It will call the driver's *EvtIoRead* handler to deliver read requests, the *EvtIoWrite* handler to deliver write requests, and the *EvtIoDeviceControl* handler to deliver device I/O control requests.

-   Multiple I/O queues, such as one for read requests and another for write requests. For each queue, the driver provides only one request handler because the queue receives only one type of request.

-   Multiple I/O queues, each with multiple request handlers.

Some example scenarios include:

-   [A Single Sequential I/O Queue](#a-single-sequential-io-queue)

-   [Multiple Sequential I/O Queues and a Manual Queue](#multiple-sequential-io-queues-and-a-manual-queue)

-   [A Single Parallel I/O Queue](#a-single-parallel-io-queue)

-   [Multiple Parallel I/O Queues](#multiple-parallel-io-queues)

## A Single Sequential I/O Queue

If you are writing a function driver for a disk drive that can only service read and write requests one at a time, the function driver needs only one I/O queue per device.

The driver can use the default I/O queue that the framework creates when the driver calls [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) and sets **DefaultQueue** to **TRUE** in the queue's [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure. In the WDF\_IO\_QUEUE\_CONFIG structure, the driver should also specify:

-   **WdfIoQueueDispatchSequential** as the dispatching method, so the default I/O queue will deliver I/O requests to the driver synchronously.

-   A single event callback function, [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757), that will receive all I/O requests.

Each time an I/O request is available in the driver's default I/O queue, the framework will deliver the request to the driver by calling the driver's [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) request handler. If another request becomes available in the queue, the framework will not deliver it until the driver calls [**WdfRequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549945) for the previously delivered request.

## Multiple Sequential I/O Queues and a Manual Queue

Consider a serial port device that has the following characteristics:

-   It can simultaneously perform one read operation and one write operation.

-   It cannot perform multiple read or write operations asynchronously.

-   It can receive device I/O control requests for status information. The device's driver might take a long time to complete some of these requests (such as a request to wait for a status change).

A function driver for this device could use multiple, sequential I/O queues per device. The driver would call [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) three times: once to create a default queue and twice to create two additional I/O queues. In the [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure for each of these queues, the driver should specify:

-   **WdfIoQueueDispatchSequential** as the dispatching method for each queue, so that the framework will deliver I/O requests to the driver synchronously.

-   A different [request handler](request-handlers.md) for each queue ([*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757), [*EvtIoRead*](https://msdn.microsoft.com/library/windows/hardware/ff541776), and [*EvtIoWrite*](https://msdn.microsoft.com/library/windows/hardware/ff541813)), which will receive the queue's I/O requests.

After calling [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401), the driver could call [**WdfDeviceConfigureRequestDispatching**](https://msdn.microsoft.com/library/windows/hardware/ff545920) twice - to forward all read requests to one of the additional queues and all write requests to the other.

With this configuration, the device's default I/O queue [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) callback function will receive only the device I/O control requests for status information.

If the driver has to hold a status request for a long time, it can create a fourth queue and specify **WdfIoQueueDispatchManual** as the dispatching method. When the driver receives a request for information that it must wait for, it can place the request in this extra queue until the status information becomes available. Then the driver can retrieve the request from the queue and complete it. In the meantime, the default queue can deliver another request to the driver.

## A Single Parallel I/O Queue

IDE disk controllers can overlap some I/O operations, but not others. For example, while a controller is processing a read or write operation on one disk, it can send a seek command to another disk. On the other hand, multiple, simultaneous read and write commands are not supported.

A function driver for this controller must examine each I/O request. If the driver receives a seek command, it must determine if the seek command can be processed. The seek command cannot be processed if:

-   The specified disk drive is already busy.

-   A disk drive is being formatted and, therefore, no other drives can be active.

For each device that is connected to the controller, the driver could call [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create a default I/O queue. In the [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure for each of these queues, the driver should specify:

-   **WdfIoQueueDispatchParallel** as the dispatching method for each queue, so that the framework will deliver I/O requests to the driver asynchronously.

-   An [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) event callback function for each queue, which will receive the queue's I/O requests.

With this configuration, a single, parallel I/O queue is assigned to each device. The driver must examine each I/O request that the framework delivers from each I/O queue. If the driver can process the request immediately, it does so. Otherwise, the driver calls [**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482), which causes the framework to stop delivering requests until the driver calls [**WdfIoQueueStart**](https://msdn.microsoft.com/library/windows/hardware/ff548478).

## Multiple Parallel I/O Queues

A SCSI host adapter is an example of a device that supports asynchronous, overlapped I/O operations. Up to 32 devices can be connected to the adapter. Consider a system with the following configuration:

-   Some of the devices connected to the SCSI adapter support "reselection", and some do not. If a SCSI device supports reselection, then during an I/O operation the device can temporarily release the adapter so the adapter can service another device. The first device later reselects itself to finish its operation.

-   The SCSI adapter uses hardware mailboxes to pass requests and responses between the driver and the devices. If a device is ready for a request but there are no available mailboxes, the device must wait.

For best performance, the function driver for this SCSI host adapter should receive I/O requests from the framework as soon as they are available. The driver must examine each request and determine if it can be started immediately or must be postponed until the device and resources (such as mailbox memory) are available.

The driver should probably use multiple, parallel I/O queues. For each device that is connected to the adapter, the driver would call [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create a default I/O queue. In the [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure for each of these queues, the driver should specify:

-   **WdfIoQueueDispatchParallel** as the dispatching method for each queue, so that the framework will deliver I/O requests to the driver asynchronously.

-   An [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) event callback function for each queue, which will receive the queue's I/O requests.

Each I/O queue's [*EvtIoDefault*](https://msdn.microsoft.com/library/windows/hardware/ff541757) callback function must examine the queue's I/O requests, as they are delivered, and determine whether each one can be serviced immediately. If the device and system resources are available, the driver starts the I/O operation. If the device or resources are not available, the driver must call [**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482) to stop delivery of additional requests until the current one can be processed.

Optionally, the driver can call [**WdfIoQueueCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547401) to create additional queues for each device. Then the driver can call [**WdfRequestForwardToIoQueue**](https://msdn.microsoft.com/library/windows/hardware/ff549958) to requeue some types of requests to the additional queues. When the framework delivers requests from an additional queue, the driver can call [**WdfIoQueueStop**](https://msdn.microsoft.com/library/windows/hardware/ff548482), if necessary, on that queue instead of the default queue, thereby minimizing the number or type of requests for which delivery is postponed.

 

 





