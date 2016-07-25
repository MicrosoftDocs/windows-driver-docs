---
title: Locking and Unlocking a Parallel Port for Use by a Parallel Device
author: windows-driver-content
description: Locking and Unlocking a Parallel Port for Use by a Parallel Device
MS-HAID:
- 'vspd\_c2ac401b-e825-4a52-81dc-35638efe8296.xml'
- 'parports.locking\_and\_unlocking\_a\_parallel\_port\_for\_use\_by\_a\_parallel\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dbfa962e-9de8-4a9c-b962-24b53c41f35d
keywords: ["parallel devices WDK , port locking/unlocking", "locking WDK parallel devices", "unlocking parallel ports", "uninterrupted operations WDK parallel devices", "freeing parallel ports"]
---

# Locking and Unlocking a Parallel Port for Use by a Parallel Device


## <a href="" id="ddk-locking-and-unlocking-a-parallel-port-for-use-by-a-parallel-device"></a>


To execute an uninterrupted sequence of operations on a parallel device, a client must allocate the parallel port and select the IEEE 1284.3 device on the port. A sequence of operations can include completing I/O requests and executing the callback routines provided by the parallel port bus driver. After completing a sequence of operations, a client must deselect the IEEE 1284.3 device and then free the parent parallel port.

The system-supplied bus driver for parallel ports supports the following internal device control requests to lock and unlock a parallel port:

[**IOCTL\_INTERNAL\_LOCK\_PORT**](https://msdn.microsoft.com/library/windows/hardware/ff544009)

[**IOCTL\_INTERNAL\_LOCK\_PORT\_NO\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff544014)

[**IOCTL\_INTERNAL\_UNLOCK\_PORT**](https://msdn.microsoft.com/library/windows/hardware/ff544056)

[**IOCTL\_INTERNAL\_UNLOCK\_PORT\_NO\_DESELECT**](https://msdn.microsoft.com/library/windows/hardware/ff544060)

Microsoft recommends that clients use the lock port and unlock port requests if the devices can be operated by only using the functionality that these requests provide. Otherwise, clients can use the lock port no select and lock port no deselect requests. This provides a client additional flexibility to operate a device that uses a selection and deselection mechanism that does not conform to the IEEE 1284.3 daisy chain specifications. A client can use the lock port no select request to allocate the port, and then operate the device by using [device control requests for parallel devices](https://msdn.microsoft.com/library/windows/hardware/ff543945) and [parallel device callback routines](https://msdn.microsoft.com/library/windows/hardware/ff544275).

Clients can send individual I/O requests to parallel devices without the need to lock and unlock a parallel port because the parallel port bus driver administers port sharing among clients. The parallel port bus driver automatically allocates the parallel port immediately before it processes an I/O request and, if there are clients waiting for the port, frees the port immediately after completing the I/O request.

If the parallel port bus driver can allocate the port to the parallel device within a set time-out period, the device's worker thread completes the request. Otherwise, the parallel port bus driver completes the pending request with a status of STATUS\_DEVICE\_BUSY.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Locking%20and%20Unlocking%20a%20Parallel%20Port%20for%20Use%20by%20a%20Parallel%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


