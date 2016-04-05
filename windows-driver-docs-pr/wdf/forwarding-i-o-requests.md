---
title: Forwarding I/O Requests
description: Forwarding I/O Requests
ms.assetid: 75e007e3-1b97-44db-ac86-56aab78222a6
keywords: ["forwarding I/O requests WDK KMDF", "I/O requests WDK KMDF , forwarding", "request processing WDK KMDF , forwarding I/O requests"]
---

# Forwarding I/O Requests


## <a href="" id="ddk-forwarding-i-o-requests-df"></a>


When a driver receives an I/O request that it cannot process, it typically does one of the following:

-   It forwards the received request to another driver.

-   It creates additional requests and sends them to another driver.

Framework-based drivers forward requests by [using I/O targets](using-i-o-targets.md), which represent other drivers on the system. Drivers can use any of the following techniques to forward a request to an I/O target:

-   A driver can forward I/O requests to the next-lower driver by calling [**WdfDeviceGetIoTarget**](https://msdn.microsoft.com/library/windows/hardware/ff546017), followed by [**WdfRequestFormatRequestUsingCurrentType**](https://msdn.microsoft.com/library/windows/hardware/ff549955), and finally [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027).

    This technique is useful only if the driver receives a request that it does not have to modify before forwarding.

-   A driver can call [**WdfFdoInitSetFilter**](https://msdn.microsoft.com/library/windows/hardware/ff547273) to register itself as a filter driver.

    If a filter driver does not provide an I/O queue for a particular type of I/O request, the framework automatically forwards requests of that type to the next-lower driver.

-   Typically, a function driver examines each I/O request's contents. If a function driver cannot process a request, it might modify the request and forward it to an I/O target. Or, it might create one or more new requests and send them to an I/O target.

    The framework's I/O target object defines several methods for sending I/O requests to other drivers. For example, a driver can call [**WdfIoTargetFormatRequestForRead**](https://msdn.microsoft.com/library/windows/hardware/ff548612), followed by [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027), to send a read request to an I/O target. For more information about I/O targets, see [Using I/O Targets](using-i-o-targets.md).

    Rarely, a driver writer might want to specify the contents of a request's underlying WDM [I/O stack location](https://msdn.microsoft.com/library/windows/hardware/ff551821) before sending a request to an I/O target. For those cases, the driver can call [**WdfRequestWdmFormatUsingStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550036) before it calls [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027).

Sometimes, a driver must send the same request to several I/O targets, typically because the driver must send a single command to all of its devices. Before sending a request to an I/O target, the driver can call [**WdfRequestChangeTarget**](https://msdn.microsoft.com/library/windows/hardware/ff549943) to verify that the I/O target is accessible.

The driver must eventually [complete](completing-i-o-requests.md) every request that it forwards to an I/O target, unless it sets the [**WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET**](https://msdn.microsoft.com/library/windows/hardware/ff552493) flag when calling [**WdfRequestSend**](https://msdn.microsoft.com/library/windows/hardware/ff550027).

Note that when a driver forwards a request, the framework does not literally transfer the framework request object from the sending driver to the receiving driver. Instead, the framework creates a new request object in the driver that receives the request. Only the request's underlying I/O request packet ([**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)) is transferred from one driver to another.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Forwarding%20I/O%20Requests%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




