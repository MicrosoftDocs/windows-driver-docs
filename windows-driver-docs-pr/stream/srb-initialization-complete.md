---
title: SRB\_INITIALIZATION\_COMPLETE
description: SRB\_INITIALIZATION\_COMPLETE
ms.assetid: 72412ab0-226d-4bf6-af6b-98d62653e061
keywords: ["SRB_INITIALIZATION_COMPLETE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- SRB_INITIALIZATION_COMPLETE
api_type:
- NA
---

# SRB\_INITIALIZATION\_COMPLETE


## <span id="ddk_srb_initialization_complete_ks"></span><span id="DDK_SRB_INITIALIZATION_COMPLETE_KS"></span>


The class driver sends this request to signal the minidriver that it has completed its initialization.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

Once the minidriver completes this request, the class driver can begin to send [**SRB\_OPEN\_STREAM**](srb-open-stream.md) requests.

When this SRB is received by the minidriver, the minidriver should create any necessary Registry entries. For example, a DirectShow filter might register a TV tuner or Crossbar for use with the FilterGraph using the [**StreamClassRegisterFilterWithNoKSPins**](https://msdn.microsoft.com/library/windows/hardware/ff568261) routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20SRB_INITIALIZATION_COMPLETE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




