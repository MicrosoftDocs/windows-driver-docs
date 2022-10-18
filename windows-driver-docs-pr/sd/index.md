---
title: SD Bus Driver Design Guide
description: SD Bus Driver Design Guide
ms.assetid: c082d86c-8f81-41ef-afac-bd9fd76696fd
keywords:
- SD WDK buses
- buses WDK , SD
- Secure Digital WDK buses
- memory cards WDK SD bus
ms.date: 10/17/2022
ms.topic: article
---

# SD Bus Driver Design Guide

[SD Card Driver Stack](./sd-card-driver-stack.md)

[Opening, Initializing and Closing an SD Card Bus Interface](./opening--initializing-and-closing-an-sd-card-bus-interface.md)

[Handling SD Card Interrupts](./handling-sd-card-interrupts.md)

[SD Card Requests](./sd-card-requests.md)

[SD Card I/O Requests](./sd-card-io-requests.md)

[Secure Digital Requests That Use Direct I/O](./secure-digital-requests-that-use-direct-io.md)

[Secure Digital Requests That Use Extended I/O](./secure-digital-requests-that-use-extended-io.md)

[Managing SD Cards in User-Mode Applications](./managing-sd-cards-in-user-mode-applications.md)

[Restrictions on SD Card Drivers](./restrictions-on-sd-card-drivers.md)

## SD Card Hardware Identifiers

For information about Secure Digital (SD) device identification strings, see [Identifiers for Secure Digital (SD) Devices](../install/identifiers-for-secure-digital--sd--devices.md).

## Restrictions on SD Card Drivers

Certain restrictions apply to Secure Digital (SD) card device drivers that manage a function on an SD combo or multifunction card. The driver stacks for the various card functions on a multifunction card must operate independently of one another. To ensure this independence, the bus driver rejects the following operations:

- SD commands that change the device state, such as SELECT\_CARD.

- SD I/O commands that specify function zero but are outside the range of the address specified in the function basic register (FBR).

- SD I/O commands that specify a function number of a different device stack.

SD device drivers can manage the host controller's common register set and the state of the device by calling [**SdBusSubmitRequest**](/windows-hardware/drivers/ddi/ntddsd/nf-ntddsd-sdbussubmitrequest) with function requests of type SDRF\_GET\_PROPERTY and SDRF\_SET\_PROPERTY. For a description of these function request types, see [**SD\_REQUEST\_FUNCTION**](/windows-hardware/drivers/ddi/ntddsd/ne-ntddsd-sd_request_function).

## SD Bus Sample (Windows 8.1)
This sample (no longer supported) is a functional Secure Digital (SD) IO driver. The driver is written using the Kernel Mode Driver Framework. It is a driver for a generic mars development board that implements the SDIO protocol without additional functionality.

Download the [Storage SDIO driver sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Driver%20Kit%20Sample/Windows%20Driver%20Kit%20(WDK)%208.1%20Samples/%5BC%2B%2B%5D-windows-driver-kit-81-cpp/WDK%208.1%20C%2B%2B%20Samples/Storage%20SDIO%20Driver/C%2B%2B) from GitHub.