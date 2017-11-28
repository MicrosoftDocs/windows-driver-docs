---
title: Stream Class SRB Reference
description: Stream Class SRB Reference
ms.assetid: fdd2de58-8825-429a-937a-0bd27a180f2a
---

# Stream Class SRB Reference


## <span id="ddk_stream_class_srb_reference_ks"></span><span id="DDK_STREAM_CLASS_SRB_REFERENCE_KS"></span>


The class driver uses the [**HW\_STREAM\_REQUEST\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff559702) structure to pass SRB requests to the minidriver. In this reference section, pSRB refers to a pointer to a HW\_STREAM\_REQUEST\_BLOCK object. The stream class driver passes this pointer when it calls minidriver-provided callbacks.

SRB requests are either device/instance-specific or stream-specific. Depending on the SRB command, additional parameters may be passed in the HW\_STREAM\_REQUEST\_BLOCK.

See [Device-Specific Command Codes](device-specific-command-codes.md) and [Stream-Specific Command Codes](stream-specific-command-codes.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Stream%20Class%20SRB%20Reference%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




