---
title: NDIS_RSS_HASH_TYPE_FROM_HASH_INFO macro
author: windows-driver-content
description: The NDIS_RSS_HASH_TYPE_FROM_HASH_INFO macro gets the hash type from the hash information. Version Information Windows VistaSupported. NDIS 6.0 driversSupported.
ms.assetid: 927fd4bf-60fa-4779-a6ec-73e577b43a95
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_RSS_HASH_TYPE_FROM_HASH_INFO macro Network Drivers Starting with Windows Vista
---

# NDIS\_RSS\_HASH\_TYPE\_FROM\_HASH\_INFO macro


The NDIS\_RSS\_HASH\_TYPE\_FROM\_HASH\_INFO macro gets the hash type from the hash information.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
ULONG NDIS_RSS_HASH_TYPE_FROM_HASH_INFO(
   ULONG HashInformation
);
```

Parameters
----------

*HashInformation*   
The hash information. For more information about the hash information, see [**NDIS\_RSS\_HASH\_INFO\_FROM\_TYPE\_AND\_FUNC**](ndis-rss-hash-info-from-type-and-func.md).

Return value
------------

NDIS\_RSS\_HASH\_TYPE\_FROM\_HASH\_INFO returns the hash type from the specified hash information. For more information about the hash type, see [RSS Hashing Types](https://msdn.microsoft.com/library/windows/hardware/ff570726).

## <a href="" id="ddk-ndis-rss-hash-type-from-hash-info-nr"></a>


Remarks
-------

A NIC (or its miniport driver) uses the receive side scaling (RSS) hash type to identify the portion of received network data that is used to calculate an RSS hash value.

For more information about the hash type, see [RSS Hashing Types](https://msdn.microsoft.com/library/windows/hardware/ff570726).

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

 

 




