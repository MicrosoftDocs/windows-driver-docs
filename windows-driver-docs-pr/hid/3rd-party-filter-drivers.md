---
title: 3rd party filter drivers
ms.assetid: 2EAFE726-2266-4E40-AC51-0025BF6069B6
description: Sample filter drivers in the Microsoft Windows Driver Kit (WDK).
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 3rd party filter drivers


This topic describes the features of the following sample filter drivers in the Microsoft Windows Driver Kit (WDK):

-   **Kbfiltr**, an optional upper-level filter driver for a Plug and Play PS/2-style keyboard device

-   **Moufiltr**, an optional upper-level filter driver for a Plug and Play PS/2-style mouse device

Kbfiltr and Moufiltr demonstrate how to filter I/O requests and add callback routines that modify the operation of the class service and the operation of I8042prt.

**Note**   The design of the Terminal Server for Windows 2000 and later does not support using the sample keyboard and mouse filter drivers to filter input from devices physically installed on a remote client. A filter driver installed on a Terminal Server can only be used to filter the input from the devices physically installed on a Terminal Server. This is a consequence of the way the TermDD.sys driver for the Terminal Server handles input from remote clients.

 

Kbfiltr and Moufiltr support Plug and Play and power management.

Kbfiltr provides the following callback routines:

<a href="" id="kbfilter-servicecallback"></a>[**KbFilter\_ServiceCallback**](https://msdn.microsoft.com/library/windows/hardware/ff542297)  
The keyboard filter service callback is added to the keyboard class service callback. The filter service callback can be configured to modify the keyboard input data that is saved in the class driver's data queue.

<a href="" id="kbfilter-isrhook"></a>[**KbFilter\_IsrHook**](https://msdn.microsoft.com/library/windows/hardware/ff542294)  
The keyboard filter ISR hook routine is a template for the **IsrRoutine** callback that I8042prt supports for a keyboard device. The callback can be configured to customize the operation of an ISR of a keyboard.

<a href="" id="kbfilter-initializationroutine"></a>[**KbFilter\_InitializationRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff542293)  
The keyboard filter initialization routine is a template for the **InitializationRoutine** callback that I8042prt supports for a keyboard device. This callback can be configured to customize the initialization of a keyboard device.

Moufiltr provides the following callback routines:

<a href="" id="moufilter-servicecallback"></a>[**MouFilter\_ServiceCallback**](https://msdn.microsoft.com/library/windows/hardware/ff542380)  
The mouse filter service callback is added to the mouse class service callback. The filter service callback can be configured to modify the mouse input data that is saved in the class driver's data queue.

<a href="" id="moufilter-isrhook"></a>[**MouFilter\_IsrHook**](https://msdn.microsoft.com/library/windows/hardware/ff542379)  
The mouse filter ISR hook routine is a template for the **IsrRoutine** callback that I8042prt supports for a mouse device. The callback can be configured to customize the operation of that mouse's ISR.

## Customize the initialization and ISR of a device


Vendors can supply optional upper-level device filter drivers that can add the following optional callbacks to the operation of I8042prt:

<a href="" id="pi8042-keyboard-isr"></a>[**PI8042\_KEYBOARD\_ISR**](https://msdn.microsoft.com/library/windows/hardware/ff543248)  
The keyboard interrupt service routine (ISR) customizes the operation of the I8042prt keyboard ISR. A keyboard ISR callback is not needed if the default operation of I8042prt is sufficient. After the I8042prt keyboard ISR validates a keyboard interrupt, it calls the keyboard ISR callback.

<a href="" id="pi8042-mouse-isr"></a>[**PI8042\_MOUSE\_ISR**](https://msdn.microsoft.com/library/windows/hardware/ff543252)  
The mouse ISR customizes the operation of the I8042prt mouse ISR. A mouse ISR callback is not needed if the default operation of I8042prt is sufficient. After the I8042prt mouse ISR validates a mouse interrupt, it calls the mouse ISR callback.

<a href="" id="pi8042-keyboard-initialization-routine"></a>[**PI8042\_KEYBOARD\_INITIALIZATION\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff543243)  
The keyboard initialization callback supplements the default initialization of a keyboard device by I8042prt. I8042prt calls this routine when it initializes a keyboard device.

I8042prt adds the callbacks provided by an upper-level device filter driver by using an [**IOCTL\_INTERNAL\_I8042\_HOOK\_KEYBOARD**](https://msdn.microsoft.com/library/windows/hardware/ff541233) request for a keyboard device and an [**IOCTL\_INTERNAL\_I8042\_HOOK\_MOUSE**](https://msdn.microsoft.com/library/windows/hardware/ff541242) request for a mouse device. After I8042prt receives a connect request from a device class driver, I8042prt synchronously sends the device-specific hook request to the top of the device stack.

After a filter driver receives a hook request, it does the following:

-   Saves the upper-level driver hook information, if any, that is passed to the filter driver.

    The hook information includes a pointer to a context, a pointer to an ISR callback, and a pointer to an initialization callback (initialization callback for a keyboard only).

-   Replaces the upper-level driver hook information with the filter driver's hook information.

-   Saves the context of I8042prt and the pointers to callbacks that the filter driver callbacks can use.

The sample filter drivers, Kbfiltr and Moufiltr, provide the following callback routines:

-   [**KbFilter\_IsrHook**](https://msdn.microsoft.com/library/windows/hardware/ff542294) is a template for the PI8042\_KEYBOARD\_ISR callback.

-   [**KbFilter\_InitializationRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff542293) is a template for the PI8042\_KEYBOARD\_INITIALIZATION\_ROUTINE callback.

-   [**MouFilter\_IsrHook**](https://msdn.microsoft.com/library/windows/hardware/ff542379) is a template for the PI8042\_MOUSE\_ISR callback.

## Synchronize the operation of a filter driver with a device's ISR


I8042prt uses a start information request to pass a pointer to a device's interrupt object to the upper-level drivers in its device stack. After a device is started, the filter driver can use the interrupt object to synchronize its operation with the interrupt service routine. Filter drivers should only use the interrupt object in calls to [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302).

I8042prt passes the interrupt object pointer to the top of the device stack by using an [**IOCTL\_INTERNAL\_I8042\_KEYBOARD\_START\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff541257) request for a keyboard device and an [**IOCTL\_INTERNAL\_I8042\_MOUSE\_START\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff541265) request for a mouse device. I8042prt synchronously sends a start information request to the top of the device stack after the hardware initialization of a device. After a filter driver receives a start information request, it saves the start information and passes the request down the device stack. I8042prt completes the request.

## Synchronize writes by a filter driver to a device


To customize the operation of a device, a filter driver needs to write control data to the device. The filter driver must synchronize writes to a device with the device's interrupt service routine and other asynchronous reads or writes on the device (for example, writes that are initiated by a set typematic request or a set keyboard indicator request).

I8042prt supports an [**IOCTL\_INTERNAL\_I8042\_KEYBOARD\_WRITE\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff541263) request and an [**IOCTL\_INTERNAL\_I8042\_MOUSE\_WRITE\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff541270) request for this purpose. A write buffer request is synchronized with the device's ISR and other requests that read or write the device.

## I8042prt callbacks that filter drivers can use


I8042prt supports the following callbacks that an upper-level device filter driver can use in its ISR callback:

<a href="" id="pi8042-isr-write-port"></a>[**PI8042\_ISR\_WRITE\_PORT**](https://msdn.microsoft.com/library/windows/hardware/ff543231)  
A write port callback for a device writes to the i8042 port at the IRQL of the device's ISR.

<a href="" id="pi8042-queue-packet"></a>[**PI8042\_QUEUE\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff543263)  
A queue packet callback for a device queues an input data packet for processing by the device's ISR [*DPC*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-deferred-procedure-call--dpc-).

<a href="" id="pi8042-synch-read-port"></a>[**PI8042\_SYNCH\_READ\_PORT**](https://msdn.microsoft.com/library/windows/hardware/ff543272)  
This callback can be used in a [**PI8042\_KEYBOARD\_INITIALIZATION\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff543243) callback. I8042prt specifies the read port callback in the *ReadPort* parameter that I8042prt inputs to a keyboard initialization routine.

<a href="" id="pi8042-synch-write-port"></a>[**PI8042\_SYNCH\_WRITE\_PORT**](https://msdn.microsoft.com/library/windows/hardware/ff543276)  
This callback can be used in a [**PI8042\_KEYBOARD\_INITIALIZATION\_ROUTINE**](https://msdn.microsoft.com/library/windows/hardware/ff543243) callback. I8042prt specifies the write port callback in the *WritePort* parameter that I8042prt inputs to a keyboard initialization routine.

I8042prt passes pointers to the keyboard device callbacks in a [**INTERNAL\_I8042\_HOOK\_KEYBOARD**](https://msdn.microsoft.com/library/windows/hardware/ff541039) structure that I8042prt uses to input information with an [**IOCTL\_INTERNAL\_I8042\_HOOK\_KEYBOARD**](https://msdn.microsoft.com/library/windows/hardware/ff541233) request.

I8042prt passes pointers to the mouse device callbacks in a [**INTERNAL\_I8042\_HOOK\_MOUSE**](https://msdn.microsoft.com/library/windows/hardware/ff541044) structure that I8042prt uses to input information with an [**IOCTL\_INTERNAL\_I8042\_HOOK\_KEYBOARD**](https://msdn.microsoft.com/library/windows/hardware/ff541233) request.

After a filter driver receives a hook device request, it saves the I8042prt callback pointers for use in the filter driver's ISR callback.

 

 




