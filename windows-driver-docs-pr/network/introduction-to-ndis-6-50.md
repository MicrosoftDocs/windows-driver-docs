---
title: Introduction to NDIS 6.50
description: This section introduces NDIS 6.50 and describes changes from NDIS 6.40. NDIS 6.50 is included in Windows 10, version 1507 and later.
ms.assetid: 8D2EA09D-3FA3-467B-861A-AA15C790FCD3
ms.author: windowsdriverdev
ms.date: 06/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to NDIS 6.50

This topic introduces Network Driver Interface Specification (NDIS) 6.50 and describes its major design additions. NDIS 6.50 is included in Windows 10, version 1507 and later.

NDIS 6.50 is a minor version update to NDIS 6.40. For more information about porting NDIS 6.x drivers to NDIS 6.50, see [Porting NDIS 6.x drivers to NDIS 6.50](porting-ndis-6-x-drivers-to-ndis-6-50.md).

## Feature updates

NDIS 6.50 is an incremental update to NDIS 6.40 and does not contain any major new features.

## Implementing an NDIS 6.50 driver

An NDIS 6.50 driver must follow the requirements that are defined in [Implementing an NDIS 6.40 driver](implementing-an-ndis-6-40-driver.md).

In addition, an NDIS 6.50 driver must be compliant with the following requirements:

- An NDIS 6.50 driver must report the correct NDIS version when it registers with NDIS.
   
   You must update the major and minor NDIS version number in the NDIS_Xxx_DRIVER_CHARACTERISTICS structure to support NDIS 6.50. The MajorNdisVersion member must contain 6 and the MinorNdisVersion member must contain 50. This requirement applies to miniport, protocol, and filter drivers. You must also update the version information for the compiler (see [Compiling an NDIS 6.50 driver](#compiling-an-ndis-650-driver)).

- NDIS 6.50 miniport drivers for Windows 10, version 1507 and later must use the NDIS 6.50 versions of APIs. For more information, see [Using NDIS 6.50 APIs](#using-ndis-650-data-structures).

## Compiling an NDIS 6.50 driver

The WDK for Windows 10, version 1507 supports header versioning. Header versioning makes sure that NDIS 6.50 drivers use the appropriate NDIS 6.50 APIs at compile time.

Add the following compiler settings to the Visual Studio project for your driver:

- For a miniport driver, add ```NDIS650_MINIPORT=1```.
- For a filter or protocol driver, add ```NDIS650=1```.

For information on building a driver with the Windows 10, version 1507 release of the WDK, see [Building a Driver](../develop/building-a-driver.md).

## Using NDIS 6.50 APIs

### New APIs

The following APIs are new in NDIS 6.50.

- [NDIS_STATUS_PD_CURRENT_CONFIG](https://msdn.microsoft.com/library/windows/hardware/dn931850)
- [OID_WWAN_SYS_CAPS](https://msdn.microsoft.com/library/windows/hardware/mt799833)
- [OID_WWAN_DEVICE_CAPS_EX](https://msdn.microsoft.com/library/windows/hardware/mt799830)
- [OID_WWAN_SLOT_INFO_STATUS](https://msdn.microsoft.com/library/windows/hardware/mt799832)
- [OID_WWAN_NETWORK_IDLE_HINT](https://msdn.microsoft.com/library/windows/hardware/dn931089) 

### Updated APIs

The following APIs were updated for NDIS 6.50.

- [NET_PNP_EVENT_NOTIFICATION](https://msdn.microsoft.com/library/windows/hardware/ff568752)
- [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)
- [NDIS_NET_BUFFER_LIST_INFO](https://msdn.microsoft.com/library/windows/hardware/ff566569)
- [NdisMGetDeviceProperty](https://msdn.microsoft.com/library/windows/hardware/ff563592)
- [NDIS_SWITCH_OPTIONAL_HANDLERS](https://msdn.microsoft.com/library/windows/hardware/hh598219)
- [NDIS_SWITCH_NIC_SAVE_STATE](https://msdn.microsoft.com/library/windows/hardware/hh598216)

## NDIS 6.51

NDIS 6.51 is a very minor version update to NDIS 6.50. NDIS 6.51 is included in Windows 10, version 1511 and later. All information for NDIS 6.50 also applies to NDIS 6.51 with the following exceptions:

- The MinorNdisVersion changes from 50 to 51 when registering your driver with NDIS.
- The compiler settings change from ```NDIS650_MINIPORT=1``` for miniport drivers and ```NDIS650=1``` for filter or protocol drivers, to ```NDIS651_MINIPORT=1``` and ```NDIS651=1``` respectively.

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")