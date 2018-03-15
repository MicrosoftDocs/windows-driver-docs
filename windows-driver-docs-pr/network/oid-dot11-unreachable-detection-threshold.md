---
title: OID_DOT11_UNREACHABLE_DETECTION_THRESHOLD
author: windows-driver-content
description: OID_DOT11_UNREACHABLE_DETECTION_THRESHOLD
ms.assetid: f73461f4-088d-4281-a7dd-5cf823f94293
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_DOT11_UNREACHABLE_DETECTION_THRESHOLD Network Drivers Starting with Windows Vista
---

# OID\_DOT11\_UNREACHABLE\_DETECTION\_THRESHOLD


**Important**  The [Native 802.11 Wireless LAN](https://msdn.microsoft.com/library/windows/hardware/ff560690) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](https://msdn.microsoft.com/library/windows/hardware/dn897672).

 

When set, the OID\_DOT11\_UNREACHABLE\_DETECTION\_THRESHOLD object identifier (OID) requests that the miniport driver set the Extensible Station (ExtSTA) **msDot11UnreachableDetectionThreshold** management information base (MIB) object to the specified value.

When queried, this OID requests that the miniport driver return the value of the **msDot11UnreachableDetectionThreshold** MIB object.

The **msDot11UnreachableDetectionThreshold** MIB object specifies the maximum amount of time before the 802.11 station determines that it has lost connectivity to either an access point (AP) (for infrastructure BSS networks) or peer station (for independent BSS networks).

The data type for OID\_DOT11\_UNREACHABLE\_DETECTION\_THRESHOLD is a ULONG value in units of milliseconds.

The independent hardware vendor (IHV) can define any criteria to determine an AP or peer station as unreachable. For example, the 802.11 station might consider an AP it has associated with as unreachable if the station has not received 802.11 Beacon or Probe Response frames from the AP during the past **msDot11UnreachableDetectionThreshold** milliseconds.

After the 802.11 station has determined that the AP or peer station is unreachable, the miniport driver must perform a disassociation operation. For more information about this operation, see [Disassociation Operations](https://msdn.microsoft.com/library/windows/hardware/ff546439).

The default for the **msDot11UnreachableDetectionThreshold** MIB object is 2,000 milliseconds (2 seconds). The miniport driver must set this MIB object to its default if any of the following occurs:

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

 

 




