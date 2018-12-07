---
title: Required and Optional Tape Miniclass Routines
description: Required and Optional Tape Miniclass Routines
ms.assetid: 7a641199-2607-4980-bd8b-ec3856b311ef
keywords:
- tape drivers WDK storage , optional routines
- storage tape drivers WDK , optional routines
- tape drivers WDK storage , required routines
- storage tape drivers WDK , required routines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required and Optional Tape Miniclass Routines


## <span id="ddk_required_and_optional_tape_miniclass_routines_kg"></span><span id="DDK_REQUIRED_AND_OPTIONAL_TAPE_MINICLASS_ROUTINES_KG"></span>


A tape miniclass driver must have the following routines:

-   **DriverEntry** provides driver-specific entry points and constants that the tape class driver uses to initialize the miniclass driver.

    The tape miniclass driver's **DriverEntry** routine allocates a TAPE\_INIT\_DATA\_EX structure, sets driver-specific constants and entry points in the structure, and calls **TapeClassInitialize** in the tape class driver.

-   Routines that implement device-specific processing for device-control requests, such as TapeMiniGetPosition and TapeMiniGetMediaTypes.

    The tape class driver calls such routines from its device-control dispatch routine. For more information, see [Processing Tape Device Control Requests](processing-tape-device-control-requests.md).

A tape miniclass driver can have the following optional routines:

-   TapeMiniExtensionInit initializes the optional minitape extension.

    See [Storing Tape Miniclass Context in Optional Extensions](storing-tape-miniclass-context-in-optional-extensions.md) For information about minitape extensions.

-   TapeMiniTapeError supplements the error handling of the tape class driver.

    For most devices, the tape class driver can return an appropriate status value when an error occurs without input from the tape miniclass driver. For some devices, however, the tape class driver requires device-specific information from the tape miniclass driver to return the appropriate status. For example, the miniclass driver for 4mm DAT tape drives can determine that, in certain situations, a TAPE\_STATUS\_BUS\_RESET status is actually due to no media in the drive. The 4mm DAT miniclass driver's TapeMiniTapeError routine identifies these situations and changes the status that is returned to TAPE\_ERROR\_NO\_MEDIA.

The tape miniclass driver's **DriverEntry** routine must use that name exactly in order to be loaded automatically by the operating system. TapeMini*Xxx* routines can be named as the driver writer chooses, as long as the entry points of the routines are set in the TAPE\_INIT\_DATA\_EX structure. To aid in debugging, a miniclass driver should prefix the TapeMini*Xxx* routines with some characters to identify itself and should ensure the rest of the characters in the name reflect what the routine does.

See also the description of tape miniclass routines in [Tape Miniclass Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff567970).

 

 




