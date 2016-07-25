---
title: Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port
author: windows-driver-content
description: Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port
MS-HAID:
- 'vspd\_4b957dca-54da-4129-8726-a43b64136753.xml'
- 'parports.selecting\_and\_deselecting\_an\_ieee\_1284\_device\_attached\_to\_a\_parallel\_p'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1a3ac1b1-9180-4b71-8740-70c6fbe9a885
keywords: ["IEEE 1284 WDK", "parallel ports WDK , IEEE 1284 devices"]
---

# Selecting and Deselecting an IEEE 1284 Device Attached to a Parallel Port


## <a href="" id="ddk-selecting-and-deselecting-an-ieee-1284-device-attached-to-a-parall"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Selecting%20and%20Deselecting%20an%20IEEE%201284%20Device%20Attached%20to%20a%20Parallel%20Port%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


