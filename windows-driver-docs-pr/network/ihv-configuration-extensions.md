---
title: IHV Configuration Extensions
description: IHV Configuration Extensions
ms.assetid: f6a05241-4064-426e-a5f5-be3232e38118
keywords:
- configurations WDK Native 802.11 , IHV extensions
- IHV configuration extensions WDK Native 802.11
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IHV Configuration Extensions


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

The independent hardware vendor (IHV) uses the [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393) object identifier (OID) for method requests to its miniport driver for setting or querying configuration of proprietary NIC extensions. This OID can be used in all Native 802.11 operation modes supported by the miniport driver.

**Note**  Miniport drivers that provide NIC-specific extensions should use [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393) rather than vendor-defined OIDs.

 

The [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393) OID is an NDIS method OID. When the driver's [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function is called, the *OidRequest* parameter contains the address of an [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure with its members set to the following values:

-   The **RequestType** member set to **NdisRequestMethod**.

-   The **Data.MethodInformation.Oid** member set to OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION.

-   The **Data.MethodInformation.InformationBuffer** member set to the address of a caller-allocated buffer that contains a [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393) structure followed by data in a format defined by the IHV.

An IHV Extensions DLL, developed by the IHV for the support of proprietary connectivity and security extensions, can issue method requests of [OID\_DOT11\_NIC\_SPECIFIC\_EXTENSION](https://msdn.microsoft.com/library/windows/hardware/ff569393) to the miniport driver through calls to the [**Dot11ExtNicSpecificExtension,**](https://msdn.microsoft.com/library/windows/hardware/ff547526) function, which is part of the IHV Extensibility application programming interface (API). For more information about this API, see [Native 802.11 IHV Extensibility Functions](https://msdn.microsoft.com/library/windows/hardware/ff560609).

 

 





