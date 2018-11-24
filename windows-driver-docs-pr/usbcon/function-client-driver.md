---
Description: Describes the various tasks that a function controller client driver performs while interacting with USB function controller extension (UFX).
title: Write a function controller client driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Write a function controller client driver


**Summary**

-   Describes the expected behavior of the function controller client driver.

**Applies to**

-   Windows 10
-   A driver developer writing a controller driver for a USB device

**Important APIs**

-   [USB function controller client driver reference](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/_usbref/#usb-function-controller-client-driver-reference)


Describes the various tasks that a function controller client driver performs while interacting with USB function controller extension (UFX). UFX and the client driver communicate with each other by using export methods and event callback functions. Export methods (named **UfxDeviceXxx** or **UfxEndpointXxx**) are exported by UFX and invoked by the client driver. Callback functions (named *EVT\_UFX\_Xxx*)are implemented in the client driver and invoked by UFX.

UFX calls all client driver's callback functions asynchronously, and one callback at a time per object. For example, there is a USB device object and three endpoint objects. At most four callback functions (one for the device and one for each endpoint) may be called at a time. For each callback method, UFX waits until the client driver calls [**UfxDeviceEventComplete**](https://msdn.microsoft.com/library/windows/hardware/mt187952) to indicate that the driver has completed the request. The only other export method that UFX listens for while waiting for these exports is [**UfxDeviceNotifyHardwareFailure**](https://msdn.microsoft.com/library/windows/hardware/mt187957). Many client callback functions are optional. Required functions are as follows:

-   [*EVT\_UFX\_DEVICE\_DEFAULT\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187849)
-   [*EVT\_UFX\_DEVICE\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187851)
-   [*EVT\_UFX\_DEVICE\_HOST\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187852)
-   [*EVT\_UFX\_DEVICE\_HOST\_DISCONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187853)
-   [*EVT\_UFX\_DEVICE\_ADDRESSED*](https://msdn.microsoft.com/library/windows/hardware/mt187847)

## Initialization


1.  The function controller client driver starts the initialization process when Windows Driver Foundation (WDF) invokes the client driver's implementation of the [**EVT_WDF_DRIVER_DEVICE_ADD**](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback. In that implementation, the client driver is expected to call [**UfxFdoInit**](https://msdn.microsoft.com/library/windows/hardware/mt187970) and then create the device object by calling [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926).
2.  The client driver calls [**UfxDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187951) to create the USB device object and retrieve the UFXDEVICE handle.
3.  The client driver calls [**UfxDeviceNotifyHardwareReady**](https://msdn.microsoft.com/library/windows/hardware/mt187958) to indicate to UFX that it can now invoke client driver's callback functions.
4.  UFX performs initialization tasks such as:
    -   UFX calls the client driver's [*EVT\_UFX\_DEVICE\_DEFAULT\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187849) implementation to create the default endpoint.
    -   UFX creates child physical device objects (PDOs) for interfaces supported by the device.
    -   UFX waits for device class driver activation when it sends the [**IOCTL\_INTERNAL\_USBFN\_ACTIVATE\_USB\_BUS**](https://msdn.microsoft.com/library/windows/hardware/mt187891) request. It also waits for the client driver to call [**UfxDeviceNotifyAttach**](https://msdn.microsoft.com/library/windows/hardware/mt187955) that indicates the device has been attached.

## Class driver notification


In order to be notified of setup packets and the status of the bus, a class driver should send an [**IOCTL\_INTERNAL\_USBFN\_ACTIVATE\_USB\_BUS**](https://msdn.microsoft.com/library/windows/hardware/mt187891) requests. UFX queues these requests into class driver-specific notification queues. On receiving a notification about a bus event from the client driver, UFX pops from each appropriate queue and completes the request. To prevent class drivers from missing notifications, UFX keeps a fixed-size queue of notifications for the class driver.

## Device attach and detach events


UFX assumes that the device is detached until it the function controller client driver calls [**UfxDeviceNotifyAttach**](https://msdn.microsoft.com/library/windows/hardware/mt187955).

After that call, UFX sets the device state to **Powered** as defined in the USB specification. To notify the client driver about state change, UFX invokes the client driver's [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) implementation.

UFX notifies the charger driver (Cad.sys) to assist with charging the device. UFX also notifies the class drivers by completing [**IOCTL\_INTERNAL\_USBFN\_BUS\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/mt187892) requests sent previously by class drivers.

The client driver must call [**UfxDeviceNotifyDetach**](https://msdn.microsoft.com/library/windows/hardware/mt187956) when the bus is detached. The client must only call detach once after each call to [**UfxDeviceNotifyAttach**](https://msdn.microsoft.com/library/windows/hardware/mt187955). After the **UfxDeviceNotifyDetach** call, UFX calls [*EVT\_UFX\_DEVICE\_HOST\_DISCONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187853) (if this is not an interface change). UFX then proceeds with all clean up tasks such as purging all endpoint queues and starting the default endpoint queue. UFX calls [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) and notify the class drivers by completing [**IOCTL\_INTERNAL\_USBFN\_BUS\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/mt187892) requests.

**Hardware failure**

If a hardware error occurs, the client driver is expected to call [**UfxDeviceNotifyHardwareFailure**](https://msdn.microsoft.com/library/windows/hardware/mt187957). In response, UFX will tear down the device stack and might try to recover from this situation by calling client driver's [*EVT\_UFX\_DEVICE\_CONTROLLER\_RESET*](https://msdn.microsoft.com/library/windows/hardware/mt187848). The client should reset the controller to its initial state. If another hardware failure occurs, the client should call UfxDeviceNotifyHardwareFailure again. On the second call, UFX will record its state and bug-check.

## Port detection


Port detection is performed by UFX. It calls the function controller client driver's [*EVT\_UFX\_DEVICE\_PORT\_DETECT*](https://msdn.microsoft.com/library/windows/hardware/mt187855) callback function to determine the type of port to which the device is attached. The client responds by calling [**UfxDevicePortDetectComplete**](https://msdn.microsoft.com/library/windows/hardware/mt187962) or [**UfxDevicePortDetectCompleteEx**](https://msdn.microsoft.com/library/windows/hardware/mt187963) with one of the port types defined in [**USBFN\_PORT\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/mt188004).

If the client cannot determine the type of port, the client should report **UsbfnUnknownPort**. If the port is unknown or a downstream port, then UFX calls the client driver's [*EVT\_UFX\_DEVICE\_HOST\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187852) function. UFX listens to the bus for some time. If the port is unknown, but there is traffic, such as a setup packet, then UFX will assume **UsbfnStandardDownstreamPort**. Otherwise, UFX assigns the port to be **UsbfnInvalidDedicatedChargingPort**. After a port type has been determined, UFX notifies Cad.sys and calls the client driver's [*EVT\_UFX\_DEVICE\_PORT\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187854) function. In the function the client driver is expect ed to change the hardware state to match the UFX port type.

## Endpoint creation


UFX creates the default endpoint (endpoint 0) by calling the client driver's [*EVT\_UFX\_DEVICE\_DEFAULT\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187849) so that it can handle setup packets sent by the host. UFX creates other endpoints by calling [*EVT\_UFX\_DEVICE\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187851). UFX only creates endpoints after the client driver calls [**UfxDeviceNotifyHardwareReady**](https://msdn.microsoft.com/library/windows/hardware/mt187958). In these callback functions, the client driver is expected to call [**UfxEndpointCreate**](https://msdn.microsoft.com/library/windows/hardware/mt187965) to the endpoint object and obtain its UFXENDPOINT handle. UFX sets the parent to the class driver PDO associated with the interface to which the endpoint belongs. Parent of the default endpoint is the USB device object. An endpoint contains two framework queue objects: a transfer queue, and a command Queue, both of which can only be accessed when the device is in the Configured state (with the exception of Endpoint 0, which can be accessed after UFX calls [*EVT\_UFX\_DEVICE\_HOST\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187852)).

-   **Command queue requests**
-   [**IOCTL\_INTERNAL\_USBFN\_GET\_PIPE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt187898)
-   [**IOCTL\_INTERNAL\_USBFN\_SET\_PIPE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt187901)
-   [**IOCTL\_INTERNAL\_USBFN\_DESCRIPTOR\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/mt187895)
-   **Transfer queue requests**
-   [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN**](https://msdn.microsoft.com/library/windows/hardware/mt188024)
-   [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN\_APPEND\_ZERO\_PKT**](https://msdn.microsoft.com/library/windows/hardware/mt187904)
-   [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_OUT**](https://msdn.microsoft.com/library/windows/hardware/mt187905)
-   [**IOCTL\_INTERNAL\_USBFN\_CONTROL\_STATUS\_HANDSHAKE\_IN**](https://msdn.microsoft.com/library/windows/hardware/mt188023)
-   [**IOCTL\_INTERNAL\_USBFN\_CONTROL\_STATUS\_HANDSHAKE\_OUT**](https://msdn.microsoft.com/library/windows/hardware/mt187893)

## Device enumeration


The client driver should not allow connections to a host before UFX calls the driver's [*EVT\_UFX\_DEVICE\_HOST\_CONNECT*](https://msdn.microsoft.com/library/windows/hardware/mt187852). Device enumeration begins when the client driver calls [**UfxDeviceNotifyReset**](https://msdn.microsoft.com/library/windows/hardware/mt187959). In the **Default** state, UFX handles standard setup packets.

**Reset**

UFX purges all endpoint queues and sends an [**IOCTL\_INTERNAL\_USBFN\_DESCRIPTOR\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/mt187895) request to the client driver to update the **wMaxPacketSize** of endpoint 0. UFX starts the default endpoint's queue and sets the state to **Default**.

**Default**

UFX calls the client driver's [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) function. It also notifies class drivers of the state. After UFX receives the SET\_ADDRESS standard setup packet, UFX sets the state to **Addressed**.

**Addressed**

UFX calls the client driver's [*EVT\_UFX\_DEVICE\_ADDRESSED*](https://msdn.microsoft.com/library/windows/hardware/mt187847) function to indicate to the client which address it should use. - If the address is 0, UFX sets the state back to **Default** and calls [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) and notifies class drivers. On receiving the SET\_CONFIGURATION standard setup packet, UFX sets the state to **Configured**.

**Configured**

If the selected configuration is 0, UFX purges the interface endpoints and sets the state to **Addressed**. UFX sends an [**IOCTL\_INTERNAL\_USBFN\_DESCRIPTOR\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/mt187895) request to the client driver to update the **wMaxPacketSize** of the interface endpoints. UFX makes sure all interface endpoint queues have finished purging and start interface endpoint queues. If the port type is not **UsbfnStandardDownstreamPort** or **UsbfnChargingDownstreamPort**, UFX change the port type to **UsbfnStandardDownstreamPort** and informs Cad.sys; the client driver by calling [*EVT\_UFX\_DEVICE\_PORT\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187854) and [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) to update the state; the class drivers of the configured state.

## Standard control transfers


UFX can handle control transfers on the default endpoint at any time after it calls [*EVT\_UFX\_DEVICE\_DEFAULT\_ENDPOINT\_ADD*](https://msdn.microsoft.com/library/windows/hardware/mt187849), in which the client driver creates the default endpoint using. All control transfers begin with an 8-byte setup packet. To send a setup packet to the host, the client driver should call [**UfxEndpointNotifySetup**](https://msdn.microsoft.com/library/windows/hardware/mt187969). Standard control transfers are completed by UFX. If there is data associated with the control transfer, UFX reads from and writes to the default control endpoint as appropriate.

## Non-Standard control transfers


If UFX cannot handle a control transfer, the transfer is forwarded to the appropriate class driver by completing an [**IOCTL\_INTERNAL\_USBFN\_BUS\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/mt187892) request. Control transfers can occur on any endpoint which is defined as a control endpoint in the endpoint descriptor. Control transfers on endpoints other than the default control endpoint are always non-standard control transfers. If the control endpoint is the default control endpoint, UFX will notify a class drivers of setup packets which are marked as class requests for that class driver. If the control endpoint belongs to an interface, then UFX notifies the class driver associated with that interface. If necessary, class drivers are expected to read from and write to the control endpoint.

## Data transfers


Data transfers are initiated by class drivers by sending [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN**](https://msdn.microsoft.com/library/windows/hardware/mt188024), [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN\_APPEND\_ZERO\_PKT**](https://msdn.microsoft.com/library/windows/hardware/mt187904), or [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_OUT**](https://msdn.microsoft.com/library/windows/hardware/mt187905) requests. After validating each of those requests, UFX forwards it to the appropriate endpoint queue to be handled by the client driver. The client driver is expected to perform additional validation. The client driver receives transfer requests on endpoint queues. The client driver can retrieve as many requests from this queue as it needs to maximize bus utilization. The client driver should complete successful requests with STATUS\_SUCCESS. The driver should make a best-effort attempt to cancel requests, and complete cancelled requests with STATUS\_CANCELLED if cancelled. If invalid parameters are passed, the client driver completes the request with STATUS\_INVALID\_PARAMETER.

**Control transfers**

Control transfers begin with an 8-byte setup packet. To send a setup packet to the host, the client driver should call [**UfxEndpointNotifySetup**](https://msdn.microsoft.com/library/windows/hardware/mt187969). UFX notifies class drivers of non-standard control transfers by completing notification requests. Both clients and UFX use [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN**](https://msdn.microsoft.com/library/windows/hardware/mt188024), [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN\_APPEND\_ZERO\_PKT**](https://msdn.microsoft.com/library/windows/hardware/mt187904), or [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_OUT**](https://msdn.microsoft.com/library/windows/hardware/mt187905) to read from and write to the default control endpoint. However, an interface can define other control endpoints, which only the corresponding class driver can use. Control endpoints can be stalled in response to a setup packet. Class drivers send the [**IOCTL\_INTERNAL\_USBFN\_SET\_PIPE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt187901) request to stall the endpoint. The hardware or the client driver is expected to immediately resume traffic on the endpoint after the stall is sent. Control endpoints can also send and receive zero-length packets (ZLP) without any prior data. The client driver and UFX can do this by using [**IOCTL\_INTERNAL\_USBFN\_CONTROL\_STATUS\_HANDSHAKE\_IN**](https://msdn.microsoft.com/library/windows/hardware/mt188023) and [**IOCTL\_INTERNAL\_USBFN\_CONTROL\_STATUS\_HANDSHAKE\_OUT**](https://msdn.microsoft.com/library/windows/hardware/mt187893).

**Bulk and interrupt transfers**

Bulk transfers guarantee data delivery and are used to send large amounts of data. Transfers can be sent on a bulk endpoint using [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN**](https://msdn.microsoft.com/library/windows/hardware/mt188024), [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_IN\_APPEND\_ZERO\_PKT**](https://msdn.microsoft.com/library/windows/hardware/mt187904), or [**IOCTL\_INTERNAL\_USBFN\_TRANSFER\_OUT**](https://msdn.microsoft.com/library/windows/hardware/mt187905). Bulk endpoints can be stalled similarly to control endpoints using [**IOCTL\_INTERNAL\_USBFN\_SET\_PIPE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt187901). The client driver is expected to send a STALL packet in response to all host requests and hold IOCTL requests. Unlike control endpoints, a stalled bulk endpoint remains stalled until the stall state is explicitly cleared.

Interrupt Transfers Interrupt transfers are like bulk transfers, but have a guaranteed latency. Interrupt transfers have the same interface as bulk transfers, but do not have streaming capabilities.

**Isochronous transfers**

The client driver is not expected to support isochronous transfers in this version.

## Power management


The client driver owns all aspects of power management. Because callback functions are asynchronous, the client driver is expected to come back to an appropriate power state and complete the request before calling the appropriate event-complete export function, such as [**UfxDeviceEventComplete**](https://msdn.microsoft.com/library/windows/hardware/mt187952).

UFX is in a Working state if the device state (defined in [**USBFN\_DEVICE\_STATE**](https://msdn.microsoft.com/library/windows/hardware/mt187992)) is **UsbfnDeviceStateSuspended** and **UsbfnDeviceStateAttached**, and has not reported a port type. Alternately, UFX has reported the port type (defined in [**USBFN\_PORT\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/mt188004)) **UsbfnStandardDownstreamPort** or **UsbfnChargingDownstreamPort**.

UFX enters and exits a Working state by calling [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) or [*EVT\_UFX\_DEVICE\_PORT\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187854) implementations. The transition to or from a Working state is complete when the client driver calls [**UfxDeviceEventComplete**](https://msdn.microsoft.com/library/windows/hardware/mt187952).

In a Working state, UFX may call any callback. While not in the Working state, UFX only calls [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) to enter a working state; [*EVT\_UFX\_DEVICE\_REMOTE\_WAKEUP\_SIGNAL*](https://msdn.microsoft.com/library/windows/hardware/mt187859) to issue a remote-wake during suspend (if supported).

**Device suspend**

Device suspend occurs when there is no traffic on the bus for 3 milliseconds. In this case, the client driver must inform UFX when it detects suspend and resume by calling [**UfxDeviceNotifySuspend**](https://msdn.microsoft.com/library/windows/hardware/mt187961) and [**UfxDeviceNotifyResume**](https://msdn.microsoft.com/library/windows/hardware/mt187960). On receiving those calls, UFX calls [*EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE*](https://msdn.microsoft.com/library/windows/hardware/mt187863) and notifies class drivers by completing [**IOCTL\_INTERNAL\_USBFN\_BUS\_EVENT\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/mt187892) requests. If remote wake is supported by the device and enabled by the host, UFX may call calls *EVT\_UFX\_DEVICE\_USB\_STATE\_CHANGE* while suspended to issue a remote wake signal.

## Related topics
[USB device-side drivers in Windows](usb-device-side-drivers-in-windows.md)  
[Developing Windows drivers for USB function controllers](developing-windows-drivers-for-usb-function-controllers.md)  
[UFX objects and handles used by a USB function client driver](ufx-objects-and-handles-used-by-a-usb-function-controller.md)  



