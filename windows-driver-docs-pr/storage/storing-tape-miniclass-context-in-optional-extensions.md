---
title: Storing Tape Miniclass Context in Optional Extensions
description: Storing Tape Miniclass Context in Optional Extensions
ms.assetid: 9b259403-2fae-4708-8765-2d998a535620
keywords: ["tape drivers WDK storage , context storage", "storage tape drivers WDK , context storage", "context WDK storage", "context storage WDK tape", "driver-specific minitape extensions WDK tape", "command-specific command extensions WDK tape"]
---

# Storing Tape Miniclass Context in Optional Extensions


## <span id="ddk_storing_tape_miniclass_context_in_optional_extensions_kg"></span><span id="DDK_STORING_TAPE_MINICLASS_CONTEXT_IN_OPTIONAL_EXTENSIONS_KG"></span>


A tape miniclass driver can store context in two optional extensions:

1.  A driver-specific minitape extension

    When used, this extension typically stores information about device capabilities (SCSI inquiry data or equivalent). A driver that supports several devices can store details about each device, rather than repeatedly querying the devices.

    A miniclass driver specifies the size of the minitape extension in the **MinitapeExtensionSize** member of the TAPE\_INIT\_DATA\_EX structure it passes to **TapeClassInitialize** from its **DriverEntry** routine. The tape class driver allocates the requested storage on behalf of the miniclass driver. The miniclass driver initializes the optional extension with a TapeMiniExtensionInit routine. The minitape extension remains valid until the driver is unloaded.

2.  A command-specific command extension

    When used, this extension stores command-specific context between calls to a tape miniclass routine that might be called more than once to process a single request. For example, a tape miniclass driver's TapeMiniGetStatus routine might store the status from a TEST\_UNIT\_READY command in the command extension while it determines whether the tape drive also requires cleaning.

    A miniclass driver specifies the size of the command extension in the **CommandExtensionSize** member of the TAPE\_INIT\_DATA\_EX structure it passes to **TapeClassInitialize** from its **DriverEntry** routine.

    All tape miniclass routines that handle device-specific aspects of device-control requests are given a pointer to the command extension when they are called. The tape class driver allocates storage for the command extension before calling such a miniclass routine. The miniclass routine initializes the command extension on the first call to process a given request; that is, when the *CallNumber* parameter to the routine equals zero. The command extension remains valid until the tape miniclass routine returns either TAPE\_STATUS\_SUCCESS or an error status.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storing%20Tape%20Miniclass%20Context%20in%20Optional%20Extensions%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




