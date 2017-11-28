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
---

# SRB\_GET\_DATA\_INTERSECTION


## <span id="ddk_srb_get_data_intersection_ks"></span><span id="DDK_SRB_GET_DATA_INTERSECTION_KS"></span>


The class driver sends this request to query the minidriver for the best-matching data format in a data range.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates that a match was found.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

*pSrb*-&gt;**CommandData**.**IntersectInfo** specifies both the data range to search for a match and the buffer to return the format. The *pSrb* pointer points to a [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure. (The **IntersectInfo** member is of type pointer to a [**STREAM\_DATA\_INTERSECT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff568299) structure.)

The class driver uses this request to satisfy [**KSPROPERTY\_PIN\_DATAINTERSECTION**](ksproperty-pin-dataintersection.md) property requests. The class drivers feeds one [**KSDATARANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561658) at a time to the minidriver until the minidriver returns the request with a *pSrb*-&gt;**Status** value of STATUS\_SUCCESS. The minidriver checks for a match in DataRange.Specifier values.

Generally, the resulting data format is immediately used to open a stream in that format. For more information about data formats and data ranges, see [Data Range Intersections in AVStream](https://msdn.microsoft.com/library/windows/hardware/ff558680).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_GET_DATA_INTERSECTION%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




