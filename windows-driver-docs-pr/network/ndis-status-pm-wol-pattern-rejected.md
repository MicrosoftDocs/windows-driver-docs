---
title: NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED
description: The NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indicates to overlying drivers that a power management wake on LAN (WOL) pattern was rejected.
MS-HAID:
- 'miniport\_power\_management\_ref\_5a9d7aab-12fc-44cc-88bc-51f5272e1356.xml'
- 'netvista.ndis\_status\_pm\_wol\_pattern\_rejected'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 49180c69-a3b8-4a6f-b34f-93e063c88f43
keywords: ["NDIS_STATUS_PM_WOL_PATTERN_REJECTED Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NDIS_STATUS_PM_WOL_PATTERN_REJECTED
api_location:
- Ndis.h
api_type:
- HeaderDef
---

# NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED


The NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indicates to overlying drivers that a power management wake on LAN (WOL) pattern was rejected.

Remarks
-------

NDIS or miniport drivers can generate the NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indication when either of them removes a WOL pattern. The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains a ULONG for the WOL pattern identifier of the rejected WOL pattern. NDIS provided the WOL pattern identifier in the **PatternId** member of the [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure.

NDIS generates an NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indication when it must remove a previously added WOL pattern from a network adapter. For example, NDIS might remove the WOL pattern to free resources for a higher priority WOL pattern. The notification event will only be sent to the binding that added the removed pattern.

For wireless network adapters that use infrastructure elements to offload the patterns and roam across the infrastructure, it is possible that a new infrastructure element might not support the same capabilities as the previous one. In this case, the miniport driver can issue a status indication to NDIS, and NDIS will issue NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED with a specific error code.

A WiFi driver might cache wake-up patterns locally. When the driver processes an OID for adding or deleting a wake-up pattern, the driver can choose to only update its local cache. The driver can defer the update of the infrastructure until it receives the [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768) OID.

The infrastructure might not have enough resources to accommodate all of the wake-up patterns. In this case, the infrastructure can accept a partial list of the wake-up patterns. When the miniport driver completes the OID\_PM\_PARAMETERS set request, the driver must make NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indications for each of the WOL patterns that the access point (AP) rejects.

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
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_PM_WOL_PATTERN_REJECTED%20%20RELEASE:%20%287/6/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





