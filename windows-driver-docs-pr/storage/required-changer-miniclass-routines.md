---
title: Required Changer Miniclass Routines
description: Required Changer Miniclass Routines
ms.assetid: bd706c00-5f6b-4bda-b6a1-a61046303e12
keywords:
- changer drivers WDK storage , miniclass drivers
- storage changer drivers WDK , miniclass drivers
- miniclass drivers WDK changer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Required Changer Miniclass Routines


## <span id="ddk_required_changer_miniclass_routines_kg"></span><span id="DDK_REQUIRED_CHANGER_MINICLASS_ROUTINES_KG"></span>


A changer miniclass driver must have the following routines, which are called by the changer class driver:

-   **DriverEntry** -- In Windows XP and later operating systems, the changer miniclass driver's **DriverEntry** routine calls the changer class driver's [**ChangerClassInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff551413) routine to initialize the driver. See [Differences in Changer Class Driver Versions](differences-in-changer-class-driver-versions.md) for more information. Changer miniclass drivers do not have a **DriverEntry** routine in Windows 2000.

-   [**ChangerAdditionalExtensionSize**](https://msdn.microsoft.com/library/windows/hardware/ff551400) indicates the number of bytes of additional space the miniclass driver requires in the changer's device extension for device-specific information.

-   [**ChangerInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff551431) prepares the changer to receive other requests.

-   [**ChangerError**](https://msdn.microsoft.com/library/windows/hardware/ff551418) performs device-specific error processing after the changer class driver has performed any device-independent error processing.

-   [**ChangerExchangeMedium**](https://msdn.microsoft.com/library/windows/hardware/ff551421) and [**ChangerMoveMedium**](https://msdn.microsoft.com/library/windows/hardware/ff551436) move media between elements in a changer.

-   [**ChangerReinitializeUnit**](https://msdn.microsoft.com/library/windows/hardware/ff551443), [**ChangerSetAccess**](https://msdn.microsoft.com/library/windows/hardware/ff551447), and [**ChangerSetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff551449) position elements and control access to them.

-   [**ChangerGetElementStatus**](https://msdn.microsoft.com/library/windows/hardware/ff551424), [**ChangerGetParameters**](https://msdn.microsoft.com/library/windows/hardware/ff551425), [**ChangerGetProductData**](https://msdn.microsoft.com/library/windows/hardware/ff551427), [**ChangerGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff551429), [**ChangerInitializeElementStatus**](https://msdn.microsoft.com/library/windows/hardware/ff551433), and [**ChangerQueryVolumeTags**](https://msdn.microsoft.com/library/windows/hardware/ff551440) get and, in the case of **ChangerQueryVolumeTags**, set various kinds of changer information.

Changer miniclass driver routines typically build SCSI request blocks (SRB) with command descriptor blocks (CDB) for the appropriate command, and send the SRBs to the system port driver.

If a changer does not support the functionality implied by a given routine, its driver must implement the routine so that it returns STATUS\_INVALID\_DEVICE\_REQUEST.

For more information about the required **Changer***Xxx* routines for changer miniclass drivers, see [Changer Miniclass Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff551472). For more information about the changer-specific I/O control codes for device control requests, see [Changer I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff551469).

 

 




