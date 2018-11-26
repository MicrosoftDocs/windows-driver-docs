---
title: Handling End of Stream in AVStream Codecs
description: Handling End of Stream in AVStream Codecs
ms.assetid: ee57137b-999a-449f-9f9d-50bc19e07ba8
keywords:
- handling end of stream WDK AVStream
- end of stream WDK AVStream
- hardware codec support WDK AVStream , end of stream
- AVStream hardware codec support WDK , handling end of stream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling End of Stream in AVStream Codecs


When a HW MFT receives a sample with an end of stream (EOS) flag set, it sets KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM in the **OptionsFlag** member of the [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure that corresponds to that sample.

After the minidriver receives a [**KSSTREAM\_POINTER**](https://msdn.microsoft.com/library/windows/hardware/ff567139) with the KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM flag set in **StreamHeader.OptionsFlag**, the input pin will not receive any new input stream pointers until the minidriver sets KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM on an output stream pointer.

Before the minidriver sets KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM on an output stream pointer, it should generate as many output frames as possible with currently available inputs.

The minidriver should then clear any cached information related to previously processed stream pointers, in addition to the data associated with these stream pointers. Then the minidriver should set KSSTREAM\_HEADER\_OPTIONSF\_ENDOFSTREAM on the output pin.

The minidriver should treat new input stream pointers that arrive subsequently as part of a new stream. An exception is if the EOS occurs as a result of a discontinuity in the media stream. If this is the case,the newly arriving stream pointer would have KSSTREAM\_HEADER\_OPTIONSF\_DATADISCONTINUITY or KSSTREAM\_HEADER\_OPTIONSF\_TIMEDISCONTINUITY, or both, flags set in KSSTREAM\_HEADER.**OptionsFlags**. If stream pointers with one of these flags set arrive at the input pin, the minidriver must set the same flags on the corresponding output pin's stream pointer.

 

 




