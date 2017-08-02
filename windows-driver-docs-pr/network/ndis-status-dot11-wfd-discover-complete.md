---
title: NDIS_STATUS_DOT11_WFD_DISCOVER_COMPLETE
author: windows-driver-content
description: NDIS_STATUS_DOT11_WFD_DISCOVER_COMPLETE
ms.assetid: 82836F84-BA52-4705-B077-E19D03321E24
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_DOT11_WFD_DISCOVER_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver must make an NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE indication after a Wi-Fi Direct (WFD) device discovery operation completes. A discover operation is initiated by an [OID\_DOT11\_WFD\_DISCOVER\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451795) request.

The data type for this indication is the [**DOT11\_WFD\_DISCOVER\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh464148) structure.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the **NDIS\_STATUS\_INDICATION** structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_WFD\_DISCOVER\_COMPLETE.

-   **StatusBuffer** must be set to the address of a [**DOT11\_WFD\_DISCOVER\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh464148) structure.

-   **StatusBufferSize** must be set to the total of both the size of [**DOT11\_WFD\_DISCOVER\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh464148) and the size of the list of discovered devices.

The discover completion indication must not include more than **DOT11\_WFD\_DISCOVER\_COMPLETE\_MAX\_LIST\_SIZE** entries. If more devices were recently discovered, the miniport should populate the completion structure to the maximum list size and use the **uTotalNumOfEntries** member of [**DOT11\_WFD\_DISCOVER\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh464148) to specify the total number of discovered devices. The system may query for the full list later by issuing [OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](https://msdn.microsoft.com/library/windows/hardware/hh451796).

The miniport must include both WFD devices and legacy networks in the list of reported devices.

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
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**DOT11\_WFD\_DISCOVER\_COMPLETE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh464148)

[OID\_DOT11\_WFD\_DISCOVER\_REQUEST](https://msdn.microsoft.com/library/windows/hardware/hh451795)

[OID\_DOT11\_WFD\_ENUM\_DEVICE\_LIST](https://msdn.microsoft.com/library/windows/hardware/hh451796)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_WFD_DISCOVER_COMPLETE%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


