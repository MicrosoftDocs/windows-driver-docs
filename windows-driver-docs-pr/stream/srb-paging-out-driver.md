---
title: SRB\_PAGING\_OUT\_DRIVER
description: SRB\_PAGING\_OUT\_DRIVER
MS-HAID:
- 'strclass-srbs\_327570df-0516-476e-95b2-23df0f9a1adb.xml'
- 'stream.srb\_paging\_out\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9bcb9f07-6fea-427b-9ae8-afdc6aec540f
keywords: ["SRB_PAGING_OUT_DRIVER Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_PAGING_OUT_DRIVER
api_type:
- NA
---

# SRB\_PAGING\_OUT\_DRIVER


## <span id="ddk_srb_paging_out_driver_ks"></span><span id="DDK_SRB_PAGING_OUT_DRIVER_KS"></span>


The class driver sends this request to signal that it is about to page out the minidriver.

### <span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The minidriver should set one of the following as the status in the SRB:

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS  
Indicates successful completion of the command.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The class driver only attempts to page out the minidriver if it has no open streams or devices. Though it is unlikely that a minidriver would have pending callbacks in this state, the minidriver should cancel any outstanding callbacks upon receipt of this SRB. The minidriver should disable adapter interrupts and then return STATUS\_SUCCESS.

The class driver pages out the minidriver only if the minidriver turns on this feature. The minidriver enables this feature by setting the registry variable PageOutWhenUnopened to 1 in the device's INF file. See the sample streaming minidriver's INFs for more information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_PAGING_OUT_DRIVER%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




