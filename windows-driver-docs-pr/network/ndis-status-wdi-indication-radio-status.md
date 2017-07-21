---
title: NDIS_STATUS_WDI_INDICATION_RADIO_STATUS
author: windows-driver-content
description: Miniport drivers use NDIS_STATUS_WDI_INDICATION_RADIO_STATUS to indicate changes in the adapter's radio state.
ms.assetid: c2f90a52-ce55-4819-a66a-cfcc591cb3e9
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_STATUS_WDI_INDICATION_RADIO_STATUS Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_RADIO\_STATUS


Miniport drivers use NDIS\_STATUS\_WDI\_INDICATION\_RADIO\_STATUS to indicate changes in the adapter's radio state. This unsolicited indication is sent when a software radio change is triggered by the host, and when a hardware radio state change is detected by the adapter.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                  | Multiple TLV instances allowed | Optional | Description                                              |
|-----------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------|
| [**WDI\_TLV\_RADIO\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn898043) |                                |          | The current state of the radio in hardware and software. |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

## See also


[WDI\_TASK\_SET\_RADIO\_STATE](oid-wdi-task-set-radio-state.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WDI_INDICATION_RADIO_STATUS%20%20RELEASE:%20%286/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


