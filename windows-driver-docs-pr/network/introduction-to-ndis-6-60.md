---
title: Introduction to NDIS 6.60
description: This section introduces NDIS 6.60 and describes changes from NDIS 6.50. NDIS 6.60 is included in Windows 10, version 1607 and Windows Server 2016 and later.
ms.assetid: AFDFD1CD-2E07-4A4F-82E2-5E6C5AABD5A3
ms.author: windowsdriverdev
ms.date: 06/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to NDIS 6.60

This topic introduces Network Driver Interface Specification (NDIS) 6.60 and describes its major design additions. NDIS 6.60 is included in Windows 10, version 1607 and Windows Server 2016 and later.

NDIS 6.60 is a minor version update to NDIS 6.50. For more information about porting NDIS 6.x drivers to NDIS 6.60, see [Porting NDIS 6.x drivers to NDIS 6.60](porting-ndis-6-x-drivers-to-ndis-6-60.md).

## Feature updates

NDIS 6.60 is an incremental update to NDIS 6.50 and does not contain any major new features.

## Implementing an NDIS 6.60 driver

An NDIS 6.60 driver must follow the requirements that are defined in [Implementing an NDIS 6.50 driver](introduction-to-ndis-6-50.md#implementing-an-ndis-650-driver).

In addition, an NDIS 6.60 driver must be compliant with the following requirements:

- An NDIS 6.60 driver must report the correct NDIS version when it registers with NDIS.
   
   You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.60. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 60. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.60 driver](#compiling-an-ndis-660-driver)).

- NDIS 6.60 miniport drivers for Windows 10, version 1607 and Windows Server 2016 and later must use the NDIS 6.60 versions of APIs. For more information, see [Using NDIS 6.60 APIs](#using-ndis-660-apis).

## Compiling an NDIS 6.60 driver

The WDK for Windows 10, version 1607 supports header versioning. Header versioning makes sure that NDIS 6.60 drivers use the appropriate NDIS 6.60 APIs at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add ```NDIS660_MINIPORT=1```.
- For a filter or protocol driver, add ```NDIS660=1```.

For information on building a driver with the Windows 10, version 1607 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

## Using NDIS 6.60 APIs

### New APIs

The following APIs are new in NDIS 6.60.

- [OID_WWAN_PRESHUTDOWN](https://msdn.microsoft.com/library/windows/hardware/mt593239)

### Updated APIs

The following APIs were updated in NDIS 6.60.

- [NDIS_NIC_SWITCH_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff566583)
- [NDIS_RECEIVE_SCALE_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff567228)

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")