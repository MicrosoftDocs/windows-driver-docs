---
title: OID_DOT11_WFD_ENUM_DEVICE_LIST
author: windows-driver-content
description: When queried, the OID_DOT11_WFD_ENUM_DEVICE_LIST object identifier (OID) requests that the miniport driver return the list of other devices within range of the Wi-Fi Direct (WFD) device.
ms.assetid: 08264B77-BA5F-4352-A113-2FB5116F20B0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_WFD_ENUM_DEVICE_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST object identifier (OID) requests that the miniport driver return the list of other devices within range of the Wi-Fi Direct (WFD) device. The device list is created from the cache of devices the WFD device detected during the most recent device discovery operation. Device discovery is initiated with an [OID\_DOT11\_WFD\_DISCOVER\_REQUEST](oid-dot11-wfd-discover-request.md) OID.

The data type for OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST is the [**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670) structure.

The device list is returned in the **InformationBuffer** member of the [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter. Each entry in the list is in the form of a [**DOT11\_WFD\_DEVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh464146) structure. The entries are placed in the **ucBuffer** of the [**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670) structure.

When this OID is queried, the miniport driver must do the following:

-   Verify that the **InformationBuffer** member of its [*MiniportOidRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559416) function's *OidRequest* parameter is large enough to return the device list. For more information about this procedure, see [**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670).

<!-- -->

-   The [**DOT11\_WFD\_DEVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh464146) structure has a variable length. However, the miniport driver must not add padding for alignment between **DOT11\_WFD\_DEVICE\_ENTRY** structures returned in the **InformationBuffer** member of the *OidRequest* parameter.

<!-- -->

-   Use the following macro for calculating the values of the **uNumOfBytes** and **uTotalNumOfBytes** members of the [**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670) structure: `DOT11_WFD_DEVICE_ENTRY_GET_DEVICE_SIZE()`.

The miniport driver may include any legacy networks discovered during a device discovery. If legacy networks are included, the information collected about the access point (AP) (infrastructure BSS networks) or peer station (independent BSS networks) should be included in the [**DOT11\_WFD\_DEVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh464146) fields.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported starting with Windows 8.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Windot11.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_BYTE\_ARRAY**](https://msdn.microsoft.com/library/windows/hardware/ff547670)

[**DOT11\_WFD\_DEVICE\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/hh464146)

[OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](oid-dot11-wfd-enum-device-list.md)

 

 




