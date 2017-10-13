---
title: OID_GEN_HD_SPLIT_PARAMETERS
author: windows-driver-content
description: As a set, NDIS and overlying drivers or user-mode applications use the OID\_GEN\_HD\_SPLIT\_PARAMETERS OID to set the current header-data split settings of a miniport adapter.
ms.assetid: 1b33c601-4302-4f63-8265-b75889b42d42
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_HD_SPLIT_PARAMETERS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_HD\_SPLIT\_PARAMETERS


As a set, NDIS and overlying drivers or user-mode applications use the OID\_GEN\_HD\_SPLIT\_PARAMETERS OID to set the current header-data split settings of a miniport adapter. NDIS 6.1 and later miniport drivers that provide header-data split services must support this OID. Otherwise, this OID is optional.

Remarks
-------

The **InformationBuffer** member of [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [**NDIS\_HD\_SPLIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565701) structure.

NDIS might set the OID\_GEN\_HD\_SPLIT\_PARAMETERS OID when an NDIS 5.*x* protocol driver binds to an NDIS 6.1 miniport. NDIS processes this OID before passing it to the miniport driver and updates the miniport adapter's **\*HeaderDataSplit** standardized keyword, if required. If header-data split is disabled, NDIS does not send this OID to the miniport adapter.

NDIS will send this OID to the miniport driver only if header-data split was enabled with the NDIS\_HD\_SPLIT\_ENABLE\_HEADER\_DATA\_SPLIT flag in the [**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694) structure during miniport initialization.

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
<td><p>Supported in NDIS 6.1 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_HD\_SPLIT\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565694)

[**NDIS\_HD\_SPLIT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff565701)

[**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_HD_SPLIT_PARAMETERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


