---
title: SRB\_GET\_DATA\_INTERSECTION
description: SRB\_GET\_DATA\_INTERSECTION
ms.assetid: 67100c7f-dbca-4f75-b884-52e25a666190
keywords: ["SRB_GET_DATA_INTERSECTION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_GET_DATA_INTERSECTION
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# SRB\_GET\_DATA\_INTERSECTION


## <span id="ddk_srb_get_data_intersection_ks"></span><span id="DDK_SRB_GET_DATA_INTERSECTION_KS"></span>


The class driver sends this request to query the minidriver for the best-matching data format in a data range.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates that a match was found.

### Comments

*pSrb*-&gt;**CommandData**.**IntersectInfo** specifies both the data range to search for a match and the buffer to return the format. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. (The **IntersectInfo** member is of type pointer to a [**STREAM\_DATA\_INTERSECT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568299) structure.)

The class driver uses this request to satisfy [**KSPROPERTY\_PIN\_DATAINTERSECTION**](ksproperty-pin-dataintersection.md) property requests. The class drivers feeds one [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) at a time to the minidriver until the minidriver returns the request with a *pSrb*-&gt;**Status** value of STATUS\_SUCCESS. The minidriver checks for a match in DataRange.Specifier values.

Generally, the resulting data format is immediately used to open a stream in that format. For more information about data formats and data ranges, see [Data Range Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

 

 





