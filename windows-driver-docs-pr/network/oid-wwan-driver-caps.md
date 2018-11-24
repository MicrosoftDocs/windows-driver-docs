---
title: OID_WWAN_DRIVER_CAPS
description: OID_WWAN_DRIVER_CAPS returns the version of the MB driver model supported by the miniport driver.
ms.assetid: 2310a341-6899-44ad-8dfb-a13fd0c42dcb
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_DRIVER_CAPS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_DRIVER\_CAPS


OID\_WWAN\_DRIVER\_CAPS returns the version of the MB driver model supported by the miniport driver.

Set requests are not supported.

Miniport drivers process OID\_WWAN\_DRIVER\_CAPS synchronously and should immediately return with the response buffer containing an [**NDIS\_WWAN\_DRIVER\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567908) structure that describes the version of the MB driver model implemented by the miniport driver when completing query requests.

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

[**NDIS\_WWAN\_DRIVER\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567908)

 

 




