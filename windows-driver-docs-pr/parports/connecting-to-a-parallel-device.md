---
title: Connecting to a Parallel Device
author: windows-driver-content
description: Connecting to a Parallel Device
MS-HAID:
- 'vspd\_95afbad1-a97d-4916-814c-129b107a3e0c.xml'
- 'parports.connecting\_to\_a\_parallel\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c05a1a1e-308a-4b9f-af43-761c4c14d6af
keywords: ["parallel devices WDK , connections"]
---

# Connecting to a Parallel Device


## <a href="" id="ddk-connecting-to-a-parallel-device-kg"></a>


A client uses the [**IOCTL\_INTERNAL\_PARCLASS\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff544040) request to obtain a [**PARCLASS\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff544334) structure that contains:

-   I/O resources allocated to the parallel port

-   Hardware capabilities of the parallel port

-   Pointers to callback routines that a kernel-mode driver can use to set the IEEE 1284 operating modes for a parallel device - see [Setting and Clearing a Communication Mode for a Parallel Device](setting-and-clearing-a-communication-mode-for-a-parallel-device.md)

-   Pointers to callback routines that a kernel-mode driver can use to read and write a parallel device - see [Reading and Writing a Parallel Device](reading-and-writing-a-parallel-device.md).

The callback routines provide functionality that a typical function driver needs. Using the callback routines is more efficient than using equivalent device control requests.

A client disconnects from a device by using a [**IOCTL\_INTERNAL\_PARCLASS\_DISCONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff544046) request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Connecting%20to%20a%20Parallel%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


