---
title: Required Changer Miniclass Routines
description: Required Changer Miniclass Routines
ms.assetid: bd706c00-5f6b-4bda-b6a1-a61046303e12
keywords: ["changer drivers WDK storage , miniclass drivers", "storage changer drivers WDK , miniclass drivers", "miniclass drivers WDK changer"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Required%20Changer%20Miniclass%20Routines%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




