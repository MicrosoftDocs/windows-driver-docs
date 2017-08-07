---
title: NDIS\_STATUS\_DOT11\_ROAMING\_START
author: windows-driver-content
description: NDIS\_STATUS\_DOT11\_ROAMING\_START
ms.assetid: ff8f5d8f-b094-4f9b-bf5d-e92c2d5650f2
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords:
 - NDIS_STATUS_DOT11_ROAMING_START Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_DOT11\_ROAMING\_START


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

A miniport driver makes an NDIS\_STATUS\_DOT11\_ROAMING\_START indication before the 802.11 station begins a roaming operation.

The miniport driver indicates the completion of the roaming operation through the [NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION](ndis-status-dot11-roaming-completion.md) indication. Every NDIS\_STATUS\_DOT11\_ROAMING\_START indication made by the driver must have a corresponding NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION indication.

For more information about the roaming operation, see [Roaming Operations](https://msdn.microsoft.com/library/windows/hardware/ff570717).

The data type for this indication is the [**DOT11\_ROAMING\_START\_PARAMETERS**](dot11-roaming-start-parameters.md) structure:

The miniport driver can make the NDIS\_STATUS\_DOT11\_ROAMING\_START indication only after it has completed a connection operation with a BSS network. For more information about connection operations, see [Connection Operations](https://msdn.microsoft.com/library/windows/hardware/ff545185).

Before it initiates a roaming operation, the miniport driver must allocate all of the resources that it will need to make the corresponding [NDIS\_STATUS\_DOT11\_ROAMING\_COMPLETION](ndis-status-dot11-roaming-completion.md) indication.

The miniport driver calls [**NdisMIndicateStatusEx**](ndismindicatestatusex.md) to make an NDIS\_STATUS\_DOT11\_ROAMING\_START indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](ndis-status-indication.md) structure through the *StatusIndication* parameter. When making this indication, the driver must set the following members of the NDIS\_STATUS\_INDICATION structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_ROAMING\_START.

-   **StatusBuffer** must be set to the address of a DOT11\_ROAMING\_START\_PARAMETERS structure.

-   **StatusBufferSize** must be set to sizeof(DOT11\_ROAMING\_START\_PARAMETERS).

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
<td><p>Available in Windows Vista and later versions of the Windows operating systemss.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_ROAMING_START%20%20RELEASE:%20%288/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


