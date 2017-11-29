---
title: SRB\_GET\_DATA\_FORMAT
description: SRB\_GET\_DATA\_FORMAT
ms.assetid: 6346d719-395d-4847-af80-6c65e15af250
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# SRB\_GET\_DATA\_FORMAT


## <span id="ddk_srb_get_data_format_ks"></span><span id="DDK_SRB_GET_DATA_FORMAT_KS"></span>


The class driver issues this request to query the data format for the stream. The minidriver should set *pSrb*-&gt;**CommandData** to the current data format for the stream.

For more information about data formats, see the [Stream Class Minidriver Design Guide](https://msdn.microsoft.com/library/windows/hardware/ff568277).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_GET_DATA_FORMAT%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




