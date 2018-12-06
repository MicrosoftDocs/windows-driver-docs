---
title: Storing Tape Miniclass Context in Optional Extensions
description: Storing Tape Miniclass Context in Optional Extensions
ms.assetid: 9b259403-2fae-4708-8765-2d998a535620
keywords:
- tape drivers WDK storage , context storage
- storage tape drivers WDK , context storage
- context WDK storage
- context storage WDK tape
- driver-specific minitape extensions WDK tape
- command-specific command extensions WDK tape
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




