---
title: NDIS_RSS_HASH_FUNC_FROM_HASH_INFO macro
author: windows-driver-content
description: The NDIS_RSS_HASH_FUNC_FROM_HASH_INFO macro gets the hash function from the hash information. Version Information Windows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: 003c5778-47da-434d-ad26-2608d160db7c
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_RSS_HASH_FUNC_FROM_HASH_INFO macro Network Drivers Starting with Windows Vista
---

# NDIS\_RSS\_HASH\_FUNC\_FROM\_HASH\_INFO macro


The NDIS\_RSS\_HASH\_FUNC\_FROM\_HASH\_INFO macro gets the hash function from the hash information.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
ULONG NDIS_RSS_HASH_FUNC_FROM_HASH_INFO(
   ULONG HashInformation
);
```

Parameters
----------

*HashInformation*   
The hash information.

Return value
------------

NDIS\_RSS\_HASH\_FUNC\_FROM\_HASH\_INFO returns the hash function from the specified hash information. For more information about the hash information, see [**NDIS\_RSS\_HASH\_INFO\_FROM\_TYPE\_AND\_FUNC**](ndis-rss-hash-info-from-type-and-func.md).

## <a href="" id="ddk-ndis-rss-hash-func-from-hash-info-nr"></a>


Remarks
-------

A NIC (or its miniport driver) uses the receive side scaling (RSS) hashing function to calculate an RSS hash value.

For more information about the hashing functions, see [RSS Hashing Functions](https://msdn.microsoft.com/library/windows/hardware/ff570725).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_RSS\_HASH\_INFO\_FROM\_TYPE\_AND\_FUNC**](ndis-rss-hash-info-from-type-and-func.md)

 

 




