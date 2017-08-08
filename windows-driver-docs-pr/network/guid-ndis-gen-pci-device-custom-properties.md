---
title: GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES
author: windows-driver-content
description: WMI clients can use the GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES method GUID to determine the current link state.
ms.assetid: a02b9049-e521-41df-ab4d-41e334ef779e
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES Network Drivers Starting with Windows Vista
---

# GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES


WMI clients can use the GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES method GUID to determine the current link state.

Remarks
-------

NDIS handles this GUID and miniport drivers do not receive an OID query.

When a WMI client issues a GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES WMI method request, NDIS returns the PCI custom properties of a PCI device for the miniport adapter. The WMI method identifier should be NDIS\_WMI\_DEFAULT\_METHOD\_ID, and the WMI input buffer should contain an [**NDIS\_WMI\_METHOD\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567903) structure.

The data buffer that NDIS returns with this GUID contains an [**NDIS\_PCI\_DEVICE\_CUSTOM\_PROPERTIES**](https://msdn.microsoft.com/library/windows/hardware/ff566745) structure.

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

[**NDIS\_WMI\_METHOD\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567903)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


