---
title: Handling End of Stream in AVStream Codecs
author: windows-driver-content
description: Handling End of Stream in AVStream Codecs
ms.assetid: ee57137b-999a-449f-9f9d-50bc19e07ba8
keywords: ["handling end of stream WDK AVStream", "end of stream WDK AVStream", "hardware codec support WDK AVStream , end of stream", "AVStream hardware codec support WDK , handling end of stream"]
---

# Handling End of Stream in AVStream Codecs


When a HW MFT receives a sample with an end of stream (EOS) flag set, it sets KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM in the **OptionsFlag** member of the [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure that corresponds to that sample.

After the minidriver receives a [**KSSTREAM\_POINTER**](https://msdn.microsoft.com/library/windows/hardware/ff567139) with the KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM flag set in **StreamHeader.OptionsFlag**, the input pin will not receive any new input stream pointers until the minidriver sets KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM on an output stream pointer.

Before the minidriver sets KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM on an output stream pointer, it should generate as many output frames as possible with currently available inputs.

The minidriver should then clear any cached information related to previously processed stream pointers, in addition to the data associated with these stream pointers. Then the minidriver should set KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM on the output pin.

The minidriver should treat new input stream pointers that arrive subsequently as part of a new stream. An exception is if the EOS occurs as a result of a discontinuity in the media stream. If this is the case,the newly arriving stream pointer would have KSSTREAM\_HEADER\_OPTIONSF\_DATADISCONTINUITY or KSSTREAM\_HEADER\_OPTIONSF\_TIMEDISCONTINUITY, or both, flags set in KSSTREAM\_HEADER.**OptionsFlags**. If stream pointers with one of these flags set arrive at the input pin, the minidriver must set the same flags on the corresponding output pin's stream pointer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Handling%20End%20of%20Stream%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


