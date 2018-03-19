---
title: NDIS_RSS_HASH_INFO_FROM_TYPE_AND_FUNC macro
author: windows-driver-content
description: The NDIS_RSS_HASH_INFO_FROM_TYPE_AND_FUNC macro combines a hash type and hash function into hash information and sets the HashInformation member in the NDIS_RECEIVE_SCALE_PARAMETERS structure.
ms.assetid: c29e3963-d8d0-459d-89ca-1d1a4cf4921f
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_RSS_HASH_INFO_FROM_TYPE_AND_FUNC macro Network Drivers Starting with Windows Vista
---

# NDIS\_RSS\_HASH\_INFO\_FROM\_TYPE\_AND\_FUNC macro


The NDIS\_RSS\_HASH\_INFO\_FROM\_TYPE\_AND\_FUNC macro combines a hash type and hash function into hash information and sets the **HashInformation** member in the NDIS\_RECEIVE\_SCALE\_PARAMETERS structure.

**Version Information**

<a href="" id="windows-vista"></a>Windows Vista  
Supported.

<a href="" id="ndis-6-0-drivers"></a>NDIS 6.0 drivers  
Supported.

Syntax
------

```ManagedCPlusPlus
ULONG NDIS_RSS_HASH_INFO_FROM_TYPE_AND_FUNC(
   ULONG HashType,
   ULONG HashFunction
);
```

Parameters
----------

*HashType*   
The hash type.

The hash type is an OR value of valid combinations of the following flags:

NDIS\_HASH\_IPV4

NDIS\_HASH\_TCP\_IPV4

NDIS\_HASH\_IPV6

NDIS\_HASH\_TCP\_IPV6

NDIS\_HASH\_IPV6\_EX

NDIS\_HASH\_TCP\_IPV6\_EX

For more information about hash types and the valid combinations of these flags, see [RSS Hashing Types](https://msdn.microsoft.com/library/windows/hardware/ff570726).

*HashFunction*
The hash function that is used. For more information, see [RSS Hashing Functions](https://msdn.microsoft.com/library/windows/hardware/ff570725).

The hash function can be one of the following values:

**NdisHashFunctionToeplitz**

**NdisHashFunctionReserved1**

**NdisHashFunctionReserved2**

**NdisHashFunctionReserved3**

Return value
------------

NDIS\_RSS\_HASH\_INFO\_FROM\_TYPE\_AND\_FUNC returns the hash information that results from combining the specified hash type and hash function.

## <a href="" id="ddk-ndis-rss-hash-info-from-type-and-func-nr"></a>


Remarks
-------

Use the [**NDIS\_RSS\_HASH\_TYPE\_FROM\_HASH\_INFO**](ndis-rss-hash-type-from-hash-info.md) and [**NDIS\_RSS\_HASH\_FUNC\_FROM\_HASH\_INFO**](ndis-rss-hash-func-from-hash-info.md) macros to get the hash type and hash function from the hash information.

A NIC (or its miniport driver) uses the receive side scaling (RSS) hash type to identify the portion of received network data that is used to calculate an RSS hash value.

For more information about the hash type, see [RSS Hashing Types](https://msdn.microsoft.com/library/windows/hardware/ff570726).

A NIC (or its miniport driver) uses the RSS hashing function to calculate an RSS hash value.

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


[**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff567228)

[**NDIS\_RSS\_HASH\_FUNC\_FROM\_HASH\_INFO**](ndis-rss-hash-func-from-hash-info.md)

[**NDIS\_RSS\_HASH\_TYPE\_FROM\_HASH\_INFO**](ndis-rss-hash-type-from-hash-info.md)

 

 




