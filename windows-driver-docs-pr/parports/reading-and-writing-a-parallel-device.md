---
title: Reading and Writing a Parallel Device
description: Reading and Writing a Parallel Device
ms.assetid: f28506b1-fa87-4119-a57a-2b49573197d8
keywords:
- parallel devices WDK , reading
- parallel devices WDK , writing
- reading parallel devices
- writing parallel devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reading and Writing a Parallel Device





A client reads and writes a parallel device by using [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff544164) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff544175) requests. A kernel-mode driver can also use the system-supplied [**PPARALLEL\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff544537) and [**PPARALLEL\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff544771) callback routines. To obtain pointers to the system-supplied read and write callbacks, a kernel-mode driver uses an [**IOCTL\_INTERNAL\_PARCLASS\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff544040) request, which returns a [**PARCLASS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544334) structure. The **ParallelRead** and **ParallelWrite** members of the PARCLASS\_INFORMATION structure are pointers to the callbacks.

If a client uses read and write I/O requests, the parallel port bus driver queues the requests on the work queue of the parallel device. A client of a parallel device does not have to lock a parallel port before reading and writing a device because the system-supplied bus driver for parallel ports automatically locks and unlocks the port for the client.

 

 




