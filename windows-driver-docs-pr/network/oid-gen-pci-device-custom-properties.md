---
title: OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES
author: windows-driver-content
description: As a query, overlying drivers use the OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES OID to get the PCI custom properties of a device.
ms.assetid: fe94884b-f5e3-4c60-8f52-e61d0df81a2a
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES Network Drivers Starting with Windows Vista
---

# OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES


As a query, overlying drivers use the OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES OID to get the PCI custom properties of a device.

Remarks
-------

NDIS handles OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES and miniport drivers do not receive an OID query.

This query is optional for other NDIS drivers.

NDIS returns an [**NDIS\_PCI\_DEVICE\_CUSTOM\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff566745) structure that contains the PCI custom properties.

For non-PCI miniport adapters, NDIS fails OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES with the NDIS\_STATUS\_INVALID\_DEVICE\_REQUEST status code.

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
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PCI\_DEVICE\_CUSTOM\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff566745)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


