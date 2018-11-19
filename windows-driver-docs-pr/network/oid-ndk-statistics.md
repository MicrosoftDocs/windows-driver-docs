---
title: OID_NDK_STATISTICS
description: As a query, NDIS and overlying drivers or user-mode applications use the OID_NDK_STATISTICS OID to get the NDK statistics of a miniport adapter.
ms.assetid: 30F16DEC-AEE6-49D4-8599-95374ACBD446
ms.date: 08/08/2017
keywords: 
 -OID_NDK_STATISTICS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_NDK\_STATISTICS


As a query, NDIS and overlying drivers or user-mode applications use the OID\_NDK\_STATISTICS OID to get the NDK statistics of a miniport adapter.

NDIS 6.30 and later miniport drivers that provide NDK services must support this OID. Otherwise, this OID is optional.

**Note**  NDIS supports this OID with the direct OID request interface. For more information about the direct OID request interface, see [NDIS 6.1 Direct OID Request Interface](https://msdn.microsoft.com/library/windows/hardware/ff564736).

 

Remarks
-------

NDIS issues this OID with the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure pointing to an [**NDIS\_NDK\_STATISTICS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451567) structure.

The NDK-capable miniport driver must provide the **CounterSet** member, which is a [**NDIS\_NDK\_PERFORMANCE\_COUNTERS**](https://msdn.microsoft.com/library/windows/hardware/hh451565) structure.

The counters are published to tools such as [perfmon](http://technet.microsoft.com/library/cc731067.aspx) (see the [NetworkDirect Activity](http://technet.microsoft.com/library/hh997022.aspx) performance counter) and made available programmatically with the Performance Data Helper (PDH) and Performance Library (PERFLIB) programming interfaces. For more information about these interfaces, see [Performance Counters](https://msdn.microsoft.com/library/windows/desktop/aa373083).

These counters are also available by calling the [Get-NetAdapterStatistics](http://technet.microsoft.com/library/jj130889) PowerShell cmdlet with the **RdmaStatistics** attribute. For more information about the **RdmaStatistics** attribute, see [**MSFT\_NetAdapterStatisticsSettingData**](https://msdn.microsoft.com/library/hh872390).

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
<td><p>None supported</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2012</p></td>
</tr>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[Kernel Mode Performance Monitoring](https://msdn.microsoft.com/library/windows/hardware/ff548159)

[**NDIS\_NDK\_PERFORMANCE\_COUNTERS**](https://msdn.microsoft.com/library/windows/hardware/hh451565)

[**NDIS\_NDK\_STATISTICS\_INFO**](https://msdn.microsoft.com/library/windows/hardware/hh451567)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 




