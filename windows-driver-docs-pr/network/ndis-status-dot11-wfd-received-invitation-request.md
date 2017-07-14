---
title: NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_INVITATION\_REQUEST
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: F279D2A3-3381-4579-AFAE-B4F37D9DF814
description: 
keywords: ["NDIS_STATUS_DOT11_WFD_RECEIVED_INVITATION_REQUEST Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_DOT11_WFD_RECEIVED_INVITATION_REQUEST
api_location:
- ndis.h
api_type:
- HeaderDef
---

# NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_INVITATION\_REQUEST


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

The status of the reception of an invitation request from a peer Wi-Fi Direct (WFD) device is reported with an NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_INVITATION\_REQUEST indication.

The data type for this indication is the [**DOT11\_RECEIVED\_INVITATION\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406528) structure.

The miniport driver calls [**NdisMIndicateStatusEx**](https://msdn.microsoft.com/library/windows/hardware/ff563600) to make an NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_INVITATION\_REQUEST indication, and must pass a pointer to an [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure through the *StatusIndication* parameter. When making this indication, the miniport driver must set the following members of the **NDIS\_STATUS\_INDICATION** structure:

-   **StatusCode** must be set to NDIS\_STATUS\_DOT11\_WFD\_RECEIVED\_INVITATION\_REQUEST.

-   **StatusBuffer** must be set to the address of a [**DOT11\_RECEIVED\_INVITATION\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406528) structure.

-   **StatusBufferSize** must be set to the total of both the size of [**DOT11\_RECEIVED\_INVITATION\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406528) and the size of the list of returned Information Elements (IEs).

After receiving the status indication, the system will determine the appropriate response for the invitation discovery request. The system may then send [OID\_DOT11\_WFD\_SEND\_INVITATION\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451807) OID to the driver for creation and transmission of the invitation response.

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


[**DOT11\_RECEIVED\_INVITATION\_REQUEST\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh406528)

[OID\_DOT11\_WFD\_SEND\_INVITATION\_RESPONSE](https://msdn.microsoft.com/library/windows/hardware/hh451807)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_DOT11_WFD_RECEIVED_INVITATION_REQUEST%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





