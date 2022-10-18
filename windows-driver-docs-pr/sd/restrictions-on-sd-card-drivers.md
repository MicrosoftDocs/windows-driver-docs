---
title: Restrictions on SD Card Drivers (Windows Drivers)
description: Learn more about Restrictions on SD Card Drivers.
ms.date: 10/17/2022
---

# Restrictions on SD Card Drivers

Certain restrictions apply to Secure Digital (SD) card device drivers that manage a function on an SD combo or multifunction card. The driver stacks for the various card functions on a multifunction card must operate independently of one another. To ensure this independence, the bus driver rejects the following operations:

- SD commands that change the device state, such as SELECT\_CARD.

- SD I/O commands that specify function zero but are outside the range of the address specified in the function basic register (FBR).

- SD I/O commands that specify a function number of a different device stack.

SD device drivers can manage the host controller's common register set and the state of the device by calling [**SdBusSubmitRequest**](/windows-hardware/drivers/ddi/ntddsd/nf-ntddsd-sdbussubmitrequest) with function requests of type SDRF\_GET\_PROPERTY and SDRF\_SET\_PROPERTY. For a description of these function request types, see [**SD\_REQUEST\_FUNCTION**](/windows-hardware/drivers/ddi/ntddsd/ne-ntddsd-sd_request_function).
