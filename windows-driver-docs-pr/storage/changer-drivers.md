---
title: Changer Drivers
description: Changer Drivers
ms.assetid: 47310de7-e69d-4f06-9995-3d95783d607a
keywords:
- changer drivers WDK storage
- storage changer drivers WDK
- storage drivers WDK , changer drivers
- changer drivers WDK storage , about changer drivers
- storage changer drivers WDK , about changer drivers
- autoloaders WDK storage
- autochangers WDK storage
- jukebox WDK storage
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changer Drivers


## <span id="ddk_changer_drivers_kg"></span><span id="DDK_CHANGER_DRIVERS_KG"></span>


This section contains the following information:

[System-Supplied Changer Drivers](system-supplied-changer-drivers.md)

[Vendor-Supplied Changer Drivers](vendor-supplied-changer-drivers.md)

[Storing Device-Specific Information in the Changer's Device Extension](storing-device-specific-information-in-the-changer-s-device-extension.md)

[Processing Changer Device-Control Requests](processing-changer-device-control-requests.md)

A changer driver controls the elements of a media library, or *changer* (sometimes called an *autoloader*, *autochanger*, or *jukebox*). In NT-based operating systems, a driver for a changer consists of the following:

-   A system-supplied changer class driver provided as a library, *mcd.lib*, that provides functionality common to all changer drivers

-   A device-specific miniclass driver, statically linked to *mcd.lib*, that provides routines called by the changer class driver to support a particular type of changer

This section contains guidelines for writing a new changer miniclass driver.

 

 




