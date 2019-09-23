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

-   **DriverEntry** -- In Windows XP and later operating systems, the changer miniclass driver's **DriverEntry** routine calls the changer class driver's [**ChangerClassInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changerclassinitialize) routine to initialize the driver. See [Differences in Changer Class Driver Versions](differences-in-changer-class-driver-versions.md) for more information. Changer miniclass drivers do not have a **DriverEntry** routine in Windows 2000.

-   [**ChangerAdditionalExtensionSize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changeradditionalextensionsize) indicates the number of bytes of additional space the miniclass driver requires in the changer's device extension for device-specific information.

-   [**ChangerInitialize**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changerinitialize) prepares the changer to receive other requests.

-   [**ChangerError**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changererror) performs device-specific error processing after the changer class driver has performed any device-independent error processing.

-   [**ChangerExchangeMedium**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changerexchangemedium) and [**ChangerMoveMedium**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changermovemedium) move media between elements in a changer.

-   [**ChangerReinitializeUnit**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changerreinitializeunit), [**ChangerSetAccess**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changersetaccess), and [**ChangerSetPosition**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changersetposition) position elements and control access to them.

-   [**ChangerGetElementStatus**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changergetelementstatus), [**ChangerGetParameters**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changergetparameters), [**ChangerGetProductData**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changergetproductdata), [**ChangerGetStatus**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changergetstatus), [**ChangerInitializeElementStatus**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changerinitializeelementstatus), and [**ChangerQueryVolumeTags**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/mcd/nf-mcd-changerqueryvolumetags) get and, in the case of **ChangerQueryVolumeTags**, set various kinds of changer information.

Changer miniclass driver routines typically build SCSI request blocks (SRB) with command descriptor blocks (CDB) for the appropriate command, and send the SRBs to the system port driver.

If a changer does not support the functionality implied by a given routine, its driver must implement the routine so that it returns STATUS\_INVALID\_DEVICE\_REQUEST.

For more information about the required **Changer***Xxx* routines for changer miniclass drivers, see [Changer Miniclass Driver Routines](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index). For more information about the changer-specific I/O control codes for device control requests, see [Changer I/O Control Codes](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/index).

 

 




