---
title: Forwarding I/O Requests
description: Forwarding I/O Requests
keywords:
- forwarding I/O requests WDK KMDF
- I/O requests WDK KMDF , forwarding
- request processing WDK KMDF , forwarding I/O requests
ms.date: 04/20/2017
---

# Forwarding I/O Requests





When a driver receives an I/O request that it cannot process, it typically does one of the following:

-   It forwards the received request to another driver.

-   It creates additional requests and sends them to another driver.

Framework-based drivers forward requests by [using I/O targets](/windows-hardware/drivers/wdf/introduction-to-i-o-targets), which represent other drivers on the system. Drivers can use any of the following techniques to forward a request to an I/O target:

-   A driver can forward I/O requests to the next-lower driver by calling [**WdfDeviceGetIoTarget**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetiotarget), followed by [**WdfRequestFormatRequestUsingCurrentType**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestformatrequestusingcurrenttype), and finally [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend).

    This technique is useful only if the driver receives a request that it does not have to modify before forwarding.

-   A driver can call [**WdfFdoInitSetFilter**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitsetfilter) to register itself as a filter driver.

    If a filter driver does not provide an I/O queue for a particular type of I/O request, the framework automatically forwards requests of that type to the next-lower driver.

-   Typically, a function driver examines each I/O request's contents. If a function driver cannot process a request, it might modify the request and forward it to an I/O target. Or, it might create one or more new requests and send them to an I/O target.

    The framework's I/O target object defines several methods for sending I/O requests to other drivers. For example, a driver can call [**WdfIoTargetFormatRequestForRead**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetformatrequestforread), followed by [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend), to send a read request to an I/O target. For more information about I/O targets, see [Using I/O Targets](/windows-hardware/drivers/wdf/introduction-to-i-o-targets).

    Rarely, a driver writer might want to specify the contents of a request's underlying WDM [I/O stack location](../kernel/i-o-stack-locations.md) before sending a request to an I/O target. For those cases, the driver can call [**WdfRequestWdmFormatUsingStackLocation**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestwdmformatusingstacklocation) before it calls [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend).

Sometimes, a driver must send the same request to several I/O targets, typically because the driver must send a single command to all of its devices. Before sending a request to an I/O target, the driver can call [**WdfRequestChangeTarget**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestchangetarget) to verify that the I/O target is accessible.

The driver must eventually [complete](completing-i-o-requests.md) every request that it forwards to an I/O target, unless it sets the [**WDF\_REQUEST\_SEND\_OPTION\_SEND\_AND\_FORGET**](/windows-hardware/drivers/ddi/wdfrequest/ne-wdfrequest-_wdf_request_send_options_flags) flag when calling [**WdfRequestSend**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestsend).

Note that when a driver forwards a request, the framework does not literally transfer the framework request object from the sending driver to the receiving driver. Instead, the framework creates a new request object in the driver that receives the request. Only the request's underlying I/O request packet ([**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)) is transferred from one driver to another.

