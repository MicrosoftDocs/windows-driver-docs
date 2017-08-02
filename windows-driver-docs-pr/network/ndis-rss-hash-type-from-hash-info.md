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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_RSS_HASH_TYPE_FROM_HASH_INFO%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


