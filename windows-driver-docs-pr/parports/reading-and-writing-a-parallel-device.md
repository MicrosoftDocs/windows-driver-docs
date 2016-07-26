---
title: Reading and Writing a Parallel Device
author: windows-driver-content
description: Reading and Writing a Parallel Device
MS-HAID:
- 'vspd\_c292ce44-8328-4b86-85fe-c5a2375c500f.xml'
- 'parports.reading\_and\_writing\_a\_parallel\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f28506b1-fa87-4119-a57a-2b49573197d8
keywords: ["parallel devices WDK , reading", "parallel devices WDK , writing", "reading parallel devices", "writing parallel devices"]
---

# Reading and Writing a Parallel Device


## <a href="" id="ddk-reading-and-writing-a-parallel-device-kg"></a>


A client reads and writes a parallel device by using [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff544164) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff544175) requests. A kernel-mode driver can also use the system-supplied [**PPARALLEL\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff544537) and [**PPARALLEL\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff544771) callback routines. To obtain pointers to the system-supplied read and write callbacks, a kernel-mode driver uses an [**IOCTL\_INTERNAL\_PARCLASS\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff544040) request, which returns a [**PARCLASS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544334) structure. The **ParallelRead** and **ParallelWrite** members of the PARCLASS\_INFORMATION structure are pointers to the callbacks.

If a client uses read and write I/O requests, the parallel port bus driver queues the requests on the work queue of the parallel device. A client of a parallel device does not have to lock a parallel port before reading and writing a device because the system-supplied bus driver for parallel ports automatically locks and unlocks the port for the client.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Reading%20and%20Writing%20a%20Parallel%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


