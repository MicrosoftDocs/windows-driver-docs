---
title: Tape Miniclass Driver Routines
description: Tape Miniclass Driver Routines
keywords:
- tape drivers WDK storage , optional routines
- storage tape drivers WDK , optional routines
- tape drivers WDK storage , required routines
- storage tape drivers WDK , required routines
ms.date: 10/08/2019
---

# Tape Miniclass Driver Routines

A tape miniclass driver must have the following routines:

- [**DriverEntry**](driverentry-of-tape-miniclass-driver.md) provides driver-specific entry points and constants that the tape class driver uses to initialize the miniclass driver.

  The tape miniclass driver's **DriverEntry** routine allocates a TAPE_INIT_DATA_EX structure, sets driver-specific constants and entry points in the structure, and calls **TapeClassInitialize** in the tape class driver.

- Routines that implement device-specific processing for device-control requests, such as TapeMiniGetPosition and TapeMiniGetMediaTypes.

  The tape class driver calls such routines from its device-control dispatch routine. For more information, see [Processing Tape Device Control Requests](processing-tape-device-control-requests.md).

A tape miniclass driver can have the following optional routines:

- *TapeMiniExtensionInit* initializes the optional minitape extension.

  See [Storing Tape Miniclass Context in Optional Extensions](storing-tape-miniclass-context-in-optional-extensions.md) for information about minitape extensions.

- *TapeMiniTapeError* supplements the error handling of the tape class driver.

  For most devices, the tape class driver can return an appropriate status value when an error occurs without input from the tape miniclass driver. For some devices, however, the tape class driver requires device-specific information from the tape miniclass driver to return the appropriate status. For example, the miniclass driver for 4mm DAT tape drives can determine that, in certain situations, a TAPE_STATUS_BUS_RESET status is actually due to no media in the drive. The 4mm DAT miniclass driver's *TapeMiniTapeError* routine identifies these situations and changes the status that is returned to TAPE_ERROR_NO_MEDIA.

The tape miniclass driver's **DriverEntry** routine must use that name exactly in order to be loaded automatically by the operating system. *TapeMiniXxx* routines can be named as the driver writer chooses, as long as the entry points of the routines are set in the TAPE_INIT_DATA_EX structure. To aid in debugging, a miniclass driver should prefix the *TapeMiniXxx* routines with some characters to identify itself and should ensure the rest of the characters in the name reflect what the routine does.

The routines, structures, and constants required by a tape miniclass driver are declared in *minitape.h*.

For information about tape class routines, see [Tape Class Driver Routines](tape-class-driver-routines.md).
