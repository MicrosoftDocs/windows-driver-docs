---
title: Summary of changes to port a miniport driver to NDIS 6.30
description: To update an NDIS 6.x miniport driver to support NDIS 6.30, you must modify it as outlined in the following sections.
ms.assetid: 1EA926FE-367E-4A63-A197-60137D679AE6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Changes Required to Port a Miniport Driver to NDIS 6.30


To update an NDIS 6.x miniport driver to support NDIS 6.30, you must modify it as outlined in the following sections.

-   [Build Environment and Testing](#build-environment-and-testing)
-   [General Porting Requirements](#general-porting-requirements)
-   [Wi-Fi Direct Miniport Drivers](#wi-fi-direct-miniport-drivers)
-   [USB-Based WWAN (Mobile Broadband) Miniport Drivers](#usb-based-wwan-mobile-broadband-miniport-drivers)

For more information about NDIS 6.30 features, see [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md).

## Build Environment and Testing


-   Replace the preprocessor definition NDIS60\_MINIPORT or NDIS61\_MINIPORT or NDIS620\_MINIPORT with NDIS630\_MINIPORT. For more information, see [Compiling an NDIS 6.30 Driver](compiling-an-ndis-6-30-driver.md)
-   Replace the preprocessor definition NDIS60 or NDIS61 or NDIS620, if present, with NDIS630.
    **Note**  This item applies only to NDIS intermediate, protocol, and filter drivers. Most NDIS miniport drivers don't need this preprocessor definition.

     

-   In NDIS 6.30, NDIS can call [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) twice in parallel if there are two adapters plugged into the system at the same time or during system startup. Be sure to test your miniport driver under this "parallel startup" condition.

## General Porting Requirements


-   Update the major and minor NDIS version number in the NDIS\_*Xxx*\_DRIVER\_CHARACTERISTICS structure as described in [Implementing an NDIS 6.30 Driver](implementing-an-ndis-6-30-driver.md).
-   For all structures that were updated for NDIS 6.30, miniport drivers need to update the **Header** member of the structure with the correct **Revision** and **Size** values. For more information, see [Using NDIS 6.30 Data Structures](using-ndis-6-30-data-structures.md).
-   All miniport drivers should implement the no-pause-on-suspend feature. For more information, see:
    -   [Power Management Enhancements in NDIS 6.30](power-management-enhancements-in-ndis-6-30.md)
    -   [**NDIS\_MINIPORT\_ADAPTER\_REGISTRATION\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565934)
    -   [**NET\_PNP\_EVENT**](https://msdn.microsoft.com/library/windows/hardware/ff568751)
    -   [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780)

## Wi-Fi Direct Miniport Drivers


During [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389), a Wi-Fi Direct-capable miniport driver must initialize the default 802.11 MAC entity. It must also report its Wi-Fi Direct and Virtual Wi-Fi capabilities using the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

**Note**  The driver is not required to register with NDIS the NDIS port corresponding to the default MAC entity.

 

## USB-Based WWAN (Mobile Broadband) Miniport Drivers


For USB-based Mobile Broadband devices, Windows 8 provides a class driver that works with devices conforming to the MBIM specification. This model is referred to as the Mobile Broadband (MB) Class Driver. However, a class driver cannot support all of the functionality exposed by an MB device. For this reason, the MB feature provides a well-defined mechanism that you can use to extend the class driver functionality. For more information, see [MB Device Services](mb-device-services.md).

If your USB-based WWAN miniport driver cannot implement the MB class driver, it must at least implement the [NDIS Selective Suspend](ndis-selective-suspend.md) feature.

 

 





