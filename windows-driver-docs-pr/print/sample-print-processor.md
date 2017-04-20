---
title: Sample Print Processor
author: windows-driver-content
description: Sample Print Processor
ms.assetid: 42ab44f2-dba4-4b52-870a-2cb42fc2d0a9
keywords:
- print processors WDK , samples
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sample Print Processor


## <a href="" id="ddk-sample-print-processor-gg"></a>


Source code for Genprint.dll, a sample print processor that accepts [EMF data](emf-data-type.md), [RAW data](raw-data-type.md), and [TEXT data](text-data-type.md) as input, is included in the Windows Driver Kit (WDK). The code is located in the \\Src\\Print\\Genprint subdirectory in the WDK.

**Note**   When you compile this print processor, set the Unicode flag with \#define UNICODE.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Sample%20Print%20Processor%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


