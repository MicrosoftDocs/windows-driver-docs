---
title: OID\_DOT11\_CREATE\_MAC
author: windows-driver-content
description: OID\_DOT11\_CREATE\_MAC
ms.assetid: 808f60d4-bd3d-46c9-8bb4-f6d6e9307ff5
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_DOT11_CREATE_MAC Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_CREATE\_MAC


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When a method request of the OID\_DOT11\_CREATE\_MAC object identifier (OID) is made, the miniport driver must create a new 802.11 MAC entity and return a [**DOT11\_MAC\_INFO**](dot11-mac-info.md) structure. For more information about the method request type, see [**NDIS\_OID\_REQUEST**](ndis-oid-request.md).

**Note**  Support for this OID is mandatory.

 

The data type for this OID is the [**DOT11\_MAC\_INFO**](dot11-mac-info.md) structure.

If the miniport driver has already created the maximum number of MAC entities that it can support, it should fail this OID method request and return the status indication NDIS\_STATUS\_OPEN\_LIST\_FULL.

Before the miniport driver completes its response to this OID request, it should call the [**NdisMAllocatePort**](ndismallocateport.md) function to allocate a corresponding NDIS port for each 802.11 MAC entity that the driver creates.

Starting in Windows 8, if the input buffer size is &gt; 0, the input for this OID is formatted as a [**DOT11\_MAC\_PARAMETERS**](dot11-mac-parameters.md) structure.

Remarks
-------

If the MAC is to function as a Wi-Fi Direct device port, **uOpmodeMask** in [**DOT11\_MAC\_PARAMETERS**](dot11-mac-parameters.md) will contain the **DOT11\_OPERATION\_MODE\_WFD\_DEVICE** flag. In this case, the miniport driver must return the same device address in [**DOT11\_MAC\_INFO**](dot11-mac-info.md) as the one specified in the **DeviceAddress** member of [**DOT11\_WFD\_ATTRIBUTES**](dot11-wfd-attributes.md) sent with the [**NdisMSetMiniportAttributes**](ndismsetminiportattributes.md) function.

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
<td><p>Available starting with Windows 7.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_MAC\_INFO**](dot11-mac-info.md)

[**DOT11\_MAC\_PARAMETERS**](dot11-mac-parameters.md)

[**NDIS\_OID\_REQUEST**](ndis-oid-request.md)

[**NdisMAllocatePort**](ndismallocateport.md)

[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_DOT11_CREATE_MAC%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


