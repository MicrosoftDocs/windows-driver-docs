---
title: SD Bus Driver Design Guide
description: SD Bus Driver Design Guide
ms.assetid: c082d86c-8f81-41ef-afac-bd9fd76696fd
keywords:
- SD WDK buses
- buses WDK , SD
- Secure Digital WDK buses
- memory cards WDK SD bus
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
author: EliotSeattle
---

# SD Bus Driver Design Guide

[SD Card Driver Stack](https://docs.microsoft.com/windows-hardware/drivers/sd/sd-card-driver-stack)

[Opening, Initializing and Closing an SD Card Bus Interface](https://docs.microsoft.com/windows-hardware/drivers/sd/opening--initializing-and-closing-an-sd-card-bus-interface)

[Handling SD Card Interrupts](https://docs.microsoft.com/windows-hardware/drivers/sd/handling-sd-card-interrupts)

[SD Card Requests](https://docs.microsoft.com/windows-hardware/drivers/sd/sd-card-requests)

## SD Card Hardware Identifiers

For information about Secure Digital (SD) device identification strings, see [Identifiers for Secure Digital (SD) Devices](https://docs.microsoft.com/windows-hardware/drivers/install/identifiers-for-secure-digital--sd--devices).

## Restrictions on SD Card Drivers

Certain restrictions apply to Secure Digital (SD) card device drivers that manage a function on an SD combo or multifunction card. The driver stacks for the various card functions on a multifunction card must operate independently of one another. To ensure this independence, the bus driver rejects the following operations:

- SD commands that change the device state, such as SELECT\_CARD.

- SD I/O commands that specify function zero but are outside the range of the address specified in the function basic register (FBR).

- SD I/O commands that specify a function number of a different device stack.

SD device drivers can manage the host controller's common register set and the state of the device by calling [**SdBusSubmitRequest**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddsd/nf-ntddsd-sdbussubmitrequest) with function requests of type SDRF\_GET\_PROPERTY and SDRF\_SET\_PROPERTY. For a description of these function request types, see [**SD\_REQUEST\_FUNCTION**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddsd/ne-ntddsd-sd_request_function).

## SD Bus Sample

This is a sample for a functional Secure Digital (SD) IO driver. The driver is written using the Kernel Mode Driver Framework. It is a driver for a generic mars development board that implements the SDIO protocol without additional functionality.

Download the [Storage SDIO driver sample](https://go.microsoft.com/fwlink/p/?LinkId=617953) from GitHub.
