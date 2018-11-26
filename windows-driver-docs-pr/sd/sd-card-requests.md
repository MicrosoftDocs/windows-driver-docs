---
title: SD Card Requests
description: SD Card Requests
ms.assetid: 3c04573a-5fe7-4332-b899-5aff3234f1ad
keywords:
- SD WDK buses , request processing
- I/O WDK SD bus
- request processing WDK SD bus
- synchronous requests WDK SD bus
- asynchronous requests WDK SD bus
- SdBusSubmitRequest
- SdBusSubmitRequestAsync
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SD Card Requests


After a Secure Digital (SD) card device driver has opened and initialized an interface to the SD bus driver, it can submit requests. There are two ways to submit requests: synchronously by means of the [**SdBusSubmitRequest**](https://msdn.microsoft.com/library/windows/hardware/ff537909) routine, and asynchronously by means of the [**SdBusSubmitRequestAsync**](https://msdn.microsoft.com/library/windows/hardware/ff537914) routine. Both of these routines are exported by the SD bus library (*sdbus.lib*).

The synchronous request routine takes two parameters: an interface context and a request packet.

<a href="" id="interface-context"></a>**Interface context**  
The device driver retrieves the interface context from the **Context** member of the [**SDBUS\_INTERFACE\_STANDARD**](https://msdn.microsoft.com/library/windows/hardware/ff537923) structure after opening an SD interface with [**SdBusOpenInterface**](https://msdn.microsoft.com/library/windows/hardware/ff537906). The driver must pass this context information in whenever it calls a method in the interface.

<a href="" id="request-packet"></a>**Request packet**  
The device driver must allocate and initialize an [**SDBUS\_REQUEST\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff537931) structure. This structure specifies the request function and other characteristics of the request.

Because **SdBusSubmitRequest** is synchronous, it does not return STATUS\_PENDING. The device driver must be running at IRQL &lt; DISPATCH\_LEVEL when it calls this routine.

The asynchronous request routine takes the following five parameters: an interface context, a request packet, an IRP, a pointer to a completion routine, and a completion context.

<a href="" id="interface-context"></a>**Interface context**  
This parameter is the same as the parameter by the same name used with the synchronous case.

<a href="" id="request-packet"></a>**Request packet**  
This parameter is the same as the parameter by the same name used with the synchronous case.

<a href="" id="irp"></a>**IRP**  
This parameter holds an IRP that the device driver has allocated, or an IRP that the driver received from the driver located above it in the driver stack. The IRP is used as a carrier for the request.

<a href="" id="completion-routine"></a>**Completion routine**  
This parameter holds an [**IoCompletion**](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for the IRP supplied in the IRP parameter.

<a href="" id="user-context"></a>**User context**  
This parameter holds a pointer to user context data that the system passes to the completion routine specified in the completion routine parameter.

The device driver must be running at IRQL &lt;= DISPATCH\_LEVEL when it calls the **SdBusSubmitRequestAsync** routine. **SdBusSubmitRequest** is a wrapper that allocates its own IRP and calls **SdBusSubmitRequestAsync**. It is provided for convenience of the driver writer.

The following sections provide code examples that illustrate how a device driver submits each of the two principal categories of SD requests: For a description the different requests, see [**SD\_REQUEST\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff538012).

## Secure Digital (SD) Property Requests


Secure Digital (SD) card drivers use property requests to read or set card properties. For example, an SD card driver might read a property to determine whether the write-protect switch on the SD card is in the locked position, or a driver for a particular function on a multifunction SDIO card might request the number that the bus driver assigns to the function it manages.

The following code example illustrates how a driver for a function on a multifunction card might request its function number from the bus driver:

```cpp
 sdrp = ExAllocatePool(NonPagedPool, 
 sizeof(SDBUS_REQUEST_PACKET));
 if (!sdrp) {
 return STATUS_INSUFFICIENT_RESOURCES;
 }
 RtlZeroMemory(sdrp, sizeof(SDBUS_REQUEST_PACKET));
 sdrp->RequestFunction = SDRF_GET_PROPERTY;
 sdrp->Parameters.GetSetProperty.Property = 
 SDP_FUNCTION_NUMBER;
 sdrp->Parameters.GetSetProperty.Buffer = 
 &pDevExt->FunctionNumber;
 sdrp->Parameters.GetSetProperty.Length = 
 sizeof(pDevExt->FunctionNumber);
 status = SdBusSubmitRequest (pDevExt->BusInterface.Context,sdrp);
 ExFreePool(sdrp);
 if (!NT_SUCCESS(status)) {
 return status;
 }
```

In this code example, a device driver initializes an SD bus request packet, [**SDBUS\_REQUEST\_PACKET**](https://msdn.microsoft.com/library/windows/hardware/ff537931), and passes it to [**SdBusSubmitRequest**](https://msdn.microsoft.com/library/windows/hardware/ff537909). The fully initialized request packet has the following characteristics:

<a href="" id="type-of-the-request"></a>**Type of the request**  
The code example specifies an SDRF\_GET\_PROPERTY request in the **RequestFunction** member of the request packet, which instructs the bus driver to retrieve a property from the card. For a description of the SDRF\_GET\_PROPERTY request, see [**SD\_REQUEST\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff538012).

<a href="" id="property-to-retrieve"></a>**Property to retrieve**  
The code example specifies the SDP\_FUNCTION\_NUMBER property in the **Parameters.GetSetProperty.Property** member of the request packet, which instructs the bus driver to retrieve the contents of the function number property. For a description of the SDP\_FUNCTION\_NUMBER property, see [**SDBUS\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537927).

<a href="" id="property-contents-and-length"></a>**Property Contents and Length**  
The code example puts a pointer to a buffer in the device extension in the

**Parameters.GetSetProperty.Buffer** member of the request packet. The bus driver will store the function number in this location. The example code also stores the size of this buffer in the **Parameters.GetSetProperty.Length** member of the request packet.

## Secure Digital (SD) Device Command Requests


Drivers use Secure Digital (SD) card command requests to send commands to an SD device. The protocol for SD commands is defined in the *Secure Digital Card* specification. Drivers can send command requests at any time after the [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) IRP that starts the device completes successfully.

This section contains two code examples: a command request that reads a byte of data from a register of an SD card using direct I/O, and a device command request that writes a larger quantity of data to an SD card using extended I/O. The explanation in the second section depends on the first, therefore, readers should study the first section before studying the second:

[Secure Digital Requests That Do Use](https://msdn.microsoft.com/library/windows/hardware/ff538051)

[Secure Digital Requests That Do Use Extended I/O](https://msdn.microsoft.com/library/windows/hardware/ff538055)

 

 




