---
title: SD Bus Driver Design Guide
description: SD Bus Driver Design Guide
ms.assetid: c082d86c-8f81-41ef-afac-bd9fd76696fd
keywords:
- SD WDK buses
- buses WDK , SD
- Secure Digital WDK buses
- memory cards WDK SD bus
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SD Bus Driver Design Guide


## In this section
[SD Card Driver Stack](https://msdn.microsoft.com/library/windows/hardware/ff537964)

[Opening, Initializing and Closing an SD Card Bus Interface](https://msdn.microsoft.com/library/windows/hardware/ff537442)

[Handling SD Card Interrupts](https://msdn.microsoft.com/library/windows/hardware/ff537177)

[SD Card Requests](https://msdn.microsoft.com/library/windows/hardware/ff537983)
 

## SD Card Hardware Identifiers


For information about Secure Digital (SD) device identification strings, see [Identifiers for Secure Digital (SD) Devices](https://msdn.microsoft.com/library/windows/hardware/ff546279).

## Restrictions on SD Card Drivers


Certain restrictions apply to Secure Digital (SD) card device drivers that manage a function on an SD combo or multifunction card. The driver stacks for the various card functions on a multifunction card must operate independently of one another. To ensure this independence, the bus driver rejects the following operations:

-   SD commands that change the device state, such as SELECT\_CARD.

-   SD I/O commands that specify function zero but are outside the range of the address specified in the function basic register (FBR).

-   SD I/O commands that specify a function number of a different device stack.

SD device drivers can manage the host controller's common register set and the state of the device by calling [**SdBusSubmitRequest**](https://msdn.microsoft.com/library/windows/hardware/ff537909) with function requests of type SDRF\_GET\_PROPERTY and SDRF\_SET\_PROPERTY. For a description of these function request types, see [**SD\_REQUEST\_FUNCTION**](https://msdn.microsoft.com/library/windows/hardware/ff538012).

## SD Bus Sample


This is a sample for a functional Secure Digital (SD) IO driver. The driver is written using the Kernel Mode Driver Framework. It is a driver for a generic mars development board that implements the SDIO protocol without additional functionality.

Download the [Storage SDIO driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617953) from GitHub.

 

 




