---
title: Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port
description: Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port
ms.assetid: 1a3ac1b1-9180-4b71-8740-70c6fbe9a885
keywords:
- IEEE 1284 WDK
- parallel ports WDK , IEEE 1284 devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port





A client can select and deselect an IEEE 1284.3 device attached to a parallel port by using the following internal device control requests:

[**IOCTL\_INTERNAL\_SELECT\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff544052)

[**IOCTL\_INTERNAL\_DESELECT\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543987)

A kernel-mode driver can also use the system-supplied [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275) that are obtained by using an [**IOCTL\_INTERNAL\_GET\_PARALLEL\_PNP\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff543997) request. This request returns a [**PARALLEL\_PNP\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544299) structure that includes the following pointers to system-supplied callbacks:

-   The **TrySelectDevice** member is a pointer to a [*PPARALLEL\_TRY\_SELECT\_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff544767) callback, which deselects an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port.

-   The **DeselectDevice** member is a pointer to a [*PPARALLEL\_DESELECT\_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff544504) callback, which selects an IEEE 1284.3 daisy chain device or an IEEE 1284 end-of-chain device that is attached to a parallel port.

The select requests require the least handling by the client because the system-supplied function driver for parallel ports queues the select request for the client if the parallel port is allocated by another client. After the parallel port function driver dequeues the select request, it attempts to allocate the port and to select the IEEE 1284.3 device. The client can cancel a select request at any time because of an acceptable time-out delay or some other device-specific condition.

**Note**   If a client uses only the [**PPARALLEL\_TRY\_SELECT\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff544767) callback to attempt to select a parallel device, and other clients are contending for the parallel port, the system-supplied function driver for parallel ports might never allocate the port to the client. To ensure success, a client must use an [**IOCTL\_INTERNAL\_SELECT\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff544052) request. (The parallel port function driver queues, and subsequently processes, port allocate requests and device select requests in the order in which select device requests are received.)

 

After the parallel port function driver selects an IEEE 1284.3 device for a client, the client has exclusive access to the port and the selected IEEE 1284.3 device. The client must call the [**PPARALLEL\_DESELECT\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff544504) callback to free the port and deselect the IEEE 1284.3 device. After a client frees the port, the parallel port function driver dequeues a pending request, if any, and processes the request.

Microsoft Windows 2000 supports four daisy chain devices per port; however, Microsoft recommends using at most two daisy chain devices per port. Windows XP supports at most two daisy chain devices per port.

 

 




