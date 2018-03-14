---
title: OID_DOT11_MEDIA_STREAMING_ENABLED
author: windows-driver-content
description: OID_DOT11_MEDIA_STREAMING_ENABLED
ms.assetid: c286775c-996e-419d-9d65-84aa3c732dbd
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_MEDIA_STREAMING_ENABLED Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_MEDIA\_STREAMING\_ENABLED


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_MEDIA\_STREAMING\_ENABLED object identifier (OID) requests that the miniport driver set the Extensible Station (ExtSTA) **msDot11MediaStreamingEnabled** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **msDot11MediaStreamingEnabled** MIB object.

The **msDot11MediaStreamingEnabled** MIB object defines the current setting of media streaming on the 802.11 station. For more information about media streaming, see [Native 802.11 Media Streaming](https://msdn.microsoft.com/library/windows/hardware/ff560643).

The data type for OID\_DOT11\_MEDIA\_STREAMING\_ENABLED is a BOOLEAN value. A value of **TRUE** indicates that the 802.11 station has enabled media streaming.

The default for the **msDot11MediaStreamingEnabled** MIB object is **FALSE**. The miniport driver must set this MIB object to its default if any of the following occurs:

-   The miniport driver's [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function is called.

-   A method request of [OID\_DOT11\_RESET\_REQUEST](oid-dot11-reset-request.md) is made to reset the media access control (MAC) layer of the 802.11 station and the **bSetDefaultMIB** member of the DOT11\_RESET\_REQUEST structure is **TRUE**.

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
<td><p>Available in Windows Vista and later versions of the Windows operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Windot11.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Native 802.11 Wireless LAN OIDs](https://msdn.microsoft.com/library/windows/hardware/ff560691)

 

 




