---
title: SerCx I/O Control Requests
description: A list of the serial I/O control requests that SerCx supports.
ms.assetid: 2697096f-73a2-4474-9040-e1cadbb10b1e
keywords:
-    SerCx IOCTLs
ms.date: 11/30/2017
ms.localizationpriority: medium
---

# SerCx I/O Control Requests

With a few exceptions, version 1 of the serial framework extension (SerCx) supports I/O control requests that use the IOCTL_SERIAL_XXX I/O control codes (IOCTLs) that are defined in the Ntddser.h header file. SerCx handles some of these requests, but SerCx must rely on the serial controller driver to handle many other requests that require hardware-specific processing. Some of the requests that are handled by SerCx also require hardware-specific processing. Although SerCx is responsible for completing these requests, SerCx offloads much of the processing of these requests to the serial controller driver.

Most of these IOCTLs are also supported by the system-supplied Serial.sys driver, which manages the named serial ports on PCs. Serial.sys is available in all supported versions of Windows. For detailed descriptions of the serial IOCTLs, see [Serial Device Control Requests](serial-device-control-requests2.md).

SerCx does not support all of the IOCTLs that are defined in the Ntddser.h header file. SerCx does not support the obsolete IOCTL_SERIAL_CONFIG_SIZE IOCTL, which should not be used by client peripheral drivers. Also not supported is the IOCTL_SERIAL_RESET_DEVICE IOCTL, which SerCx always completes with the STATUS_NOT_IMPLEMENTED error status code. In addition, SerCx supports none of the IOCTL_SERIAL_INTERNAL_XXX IOCTLs that are defined in Ntddser.h.

Many of the IOCTLs that SerCx supports are used to configure the hardware settings on a serial port. Immediately after opening a serial port, the client should assume that the serial port is in an unknown or undefined state, and not in a known default state. The client is responsible for configuring the serial port so that it is ready to use.

Most of the IOCTLs that SerCx supports are handled by the EvtSerCxControl callback function, which is implemented by the serial controller driver. SerCx handles eight of the serial IOCTLs without calling the EvtSerCxControl function. However, to process some of these IOCTLs, SerCx requires assistance from callback functions in the serial controller driver other than EvtSerCxControl. For more information, see IOCTLs handled by SerCx.

## IOCTLs handled by the EvtSerCxControl function

If SerCx receives an I/O control request that has an IOCTL that SerCx does not support, SerCx calls the serial controller driver's EvtSerCxControl callback function to handle the request. In response, this function must complete the request. However, this function might not handle all the I/O control requests that it receives. If the EvtSerCxControl function receives an IOCTL that it does not recognize or support, it should complete the request with a STATUS_NOT_IMPLEMENTED error status code.
Some of the I/O control requests processed by the EvtSerCxControl function might change the configuration or behavior of the serial controller in some way. To avoid errors, a peripheral device driver should avoid sending I/O control requests to reconfigure the controller while the controller is still processing a pending transmit or receive operation. Additionally, this peripheral device driver should avoid initiating a new transmit or receive operation until the serial controller driver has completed any pending I/O control requests that might change the controller's configuration.

Typically, many of the requests that SerCx sends to the EvtSerCxControl function can be completed by this function before it returns. If a request requires deferred processing, the function can schedule a DPC routine or worker thread to complete the request. For performance reasons, the function should avoid unnecessarily scheduling a DPC routine or worker thread for an operation that does not require deferred processing.

SerCx does not try to serialize calls to the EvtSerCxControl function. These calls might occur concurrently from different threads, and two or more invocations of the EvtSerCxControl function might be running at the same time.

## IOCTLs handled by SerCx

SerCx handles and completes IOCTL_SERIAL_GET_TIMEOUTS and IOCTL_SERIAL_SET_TIMEOUTS requests without assistance from the serial controller driver, but SerCx does apply the current time-out parameters to the transmit and receive operations that the driver performs. The serial controller driver can get the current read-interval time-out value by calling the SerCxGetReadIntervalTimeout method. For more information about time-outs, see SERIAL_TIMEOUTS.

SerCx handles and completes IOCTL_SERIAL_APPLY_DEFAULT_CONFIGURATION requests. During the processing of this request, SerCx calls the driver's EvtSerCxApplyConfig callback function to configure the serial controller to use the default connection settings in the request. These settings are copied from the ACPI firmware for the hardware platform.

SerCx handles and completes IOCTL_SERIAL_PURGE requests. During the processing of such a request, SerCx can, if necessary, call the driver's EvtSerCxPurge callback function for assistance in purging a receive or transmit operation that the serial controller driver might have pending. As currently implemented, SerCx handles all supported purge operations without assistance from the EvtSerCxPurge function. However, future implementations of SerCx might call the EvtSerCxPurge function to perform new types of purge operations.

SerCx handles and completes IOCTL_SERIAL_GET_WAIT_MASK, IOCTL_SERIAL_SET_WAIT_MASK, and IOCTL_SERIAL_WAIT_ON_MASK requests. During the processing of an IOCTL_SERIAL_SET_WAIT_MASK request, SerCx calls the driver's EvtSerCxWaitmask callback function to notify the serial controller driver that the wait mask has changed. This function calls the SerCxGetWaitMask method to get the new wait mask. Later, when a hardware event occurs that is specified in this wait mask, the serial controller driver calls the SerCxCompleteWait method to notify SerCx, and SerCx completes any pending IOCTL_SERIAL_WAIT_ON_MASK request that might be waiting for the event. If no such request is pending, SerCx stores the event in its internal event history in anticipation of a future IOCTL_SERIAL_WAIT_ON_MASK request.

SerCx can call the EvtSerCxWaitmask function while a wait operation is pending. To determine whether to start a new wait operation, the function calls SerCxGetWaitMask. If SerCxGetWaitMask returns a nonzero wait mask, this wait mask replaces the old wait mask, and a new wait operation starts with the updated wait mask. If SerCxGetWaitMask returns a wait mask of zero, the function ends the wait operation. In neither case does the function call SerCxCompleteWait.
