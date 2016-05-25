---
title: Required and Optional Tape Miniclass Routines
author: windows-driver-content
description: Required and Optional Tape Miniclass Routines
ms.assetid: 7a641199-2607-4980-bd8b-ec3856b311ef
keywords: ["tape drivers WDK storage , optional routines", "storage tape drivers WDK , optional routines", "tape drivers WDK storage , required routines", "storage tape drivers WDK , required routines"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Required%20and%20Optional%20Tape%20Miniclass%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


