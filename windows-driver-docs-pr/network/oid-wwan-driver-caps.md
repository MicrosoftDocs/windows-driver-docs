---
title: OID\_WWAN\_DRIVER\_CAPS
author: windows-driver-content
description: OID\_WWAN\_DRIVER\_CAPS returns the version of the MB driver model supported by the miniport driver.
ms.assetid: 2310a341-6899-44ad-8dfb-a13fd0c42dcb
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - OID_WWAN_DRIVER_CAPS Network Drivers Starting with Windows Vista
---

# OID\_WWAN\_DRIVER\_CAPS


OID\_WWAN\_DRIVER\_CAPS returns the version of the MB driver model supported by the miniport driver.

Set requests are not supported.

Miniport drivers process OID\_WWAN\_DRIVER\_CAPS synchronously and should immediately return with the response buffer containing an [**NDIS\_WWAN\_DRIVER\_CAPS**](ndis-wwan-driver-caps.md) structure that describes the version of the MB driver model implemented by the miniport driver when completing query requests.

Remarks
-------

For more information about using this OID, see [MB Miniport Driver Initialization](https://msdn.microsoft.com/library/windows/hardware/ff557186).

Miniport drivers should not access the provider network, or the Subscriber Identity Module (SIM card), when processing query operations.

The current version of the MB driver model version is defined by the WWAN\_MAJOR\_VERSION and WWAN\_MINOR\_VERSION \#define tokens. If the miniport driver returns a version of the MB driver model that the MB Service does not support, the MB Service will ignore the device.

When the MB Service is initialized or restarted, the miniport driver may already have been loaded. In this case, the MB Service queries the version of the MB driver model implement by miniport driver before it proceeds to issue any other OIDs. This occurs at the beginning of any session.

Miniport drivers should return NDIS\_STATUS\_NOT\_SUPPORTED in the case of any initialization error. If a miniport driver returns NDIS\_STATUS\_NOT\_SUPPORTED, the MB Service will ignore the device and will not proceed with any other OIDs.

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
<td><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[MB Miniport Driver Initialization](https://msdn.microsoft.com/library/windows/hardware/ff557186)

[**NDIS\_WWAN\_DRIVER\_CAPS**](ndis-wwan-driver-caps.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DRIVER_CAPS%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


