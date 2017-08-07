---
title: OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST
author: windows-driver-content
description: When queried, the OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST object identifier (OID) requests that the miniport driver return the list of other devices within range of the Wi-Fi Direct (WFD) device.
ms.assetid: 08264B77-BA5F-4352-A113-2FB5116F20B0
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_WFD_ENUM_DEVICE_LIST Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When queried, the OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST object identifier (OID) requests that the miniport driver return the list of other devices within range of the Wi-Fi Direct (WFD) device. The device list is created from the cache of devices the WFD device detected during the most recent device discovery operation. Device discovery is initiated with an [OID\_DOT11\_WFD\_DISCOVER\_REQUEST](oid-dot11-wfd-discover-request.md) OID.

The data type for OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST is the [**DOT11\_BYTE\_ARRAY**](dot11-byte-array.md) structure.

The device list is returned in the **InformationBuffer** member of the [*MiniportOidRequest*](miniportoidrequest.md) function's *OidRequest* parameter. Each entry in the list is in the form of a [**DOT11\_WFD\_DEVICE\_ENTRY**](-dot11-wfd-device-entry.md) structure. The entries are placed in the **ucBuffer** of the [**DOT11\_BYTE\_ARRAY**](dot11-byte-array.md) structure.

When this OID is queried, the miniport driver must do the following:

-   Verify that the **InformationBuffer** member of its [*MiniportOidRequest*](miniportoidrequest.md) function's *OidRequest* parameter is large enough to return the device list. For more information about this procedure, see [**DOT11\_BYTE\_ARRAY**](dot11-byte-array.md).

<!-- -->

-   The [**DOT11\_WFD\_DEVICE\_ENTRY**](-dot11-wfd-device-entry.md) structure has a variable length. However, the miniport driver must not add padding for alignment between **DOT11\_WFD\_DEVICE\_ENTRY** structures returned in the **InformationBuffer** member of the *OidRequest* parameter.

<!-- -->

-   Use the following macro for calculating the values of the **uNumOfBytes** and **uTotalNumOfBytes** members of the [**DOT11\_BYTE\_ARRAY**](dot11-byte-array.md) structure: `DOT11_WFD_DEVICE_ENTRY_GET_DEVICE_SIZE()`.

The miniport driver may include any legacy networks discovered during a device discovery. If legacy networks are included, the information collected about the access point (AP) (infrastructure BSS networks) or peer station (independent BSS networks) should be included in the [**DOT11\_WFD\_DEVICE\_ENTRY**](-dot11-wfd-device-entry.md) fields.

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


[**DOT11\_BYTE\_ARRAY**](dot11-byte-array.md)

[**DOT11\_WFD\_DEVICE\_ENTRY**](-dot11-wfd-device-entry.md)

[OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](oid-dot11-wfd-enum-device-list.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_WFD_ENUM_DEVICE_LIST%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


