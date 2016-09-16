---
title: Pscript-Specific Customized Rendering
author: windows-driver-content
description: Pscript-Specific Customized Rendering
MS-HAID:
- 'custdrvr\_9172473f-75c8-4c99-bcf0-2d5915bebf63.xml'
- 'print.pscript\_specific\_customized\_rendering'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e984f0f0-1435-4cfd-9a99-297f6a9521f5
keywords: ["rendering plug-ins WDK print , Pscript5", "Pscript WDK print , customized rendering"]
---

# Pscript-Specific Customized Rendering


## <a href="" id="ddk-pscript-specific-customized-rendering-gg"></a>


Pscript5 allows device-specific customized code to inject Postscript commands into the data stream that the Pscript5 driver sends to the printer device. If you want to provide this type of customized code, you must provide a rendering plug-in that implements the [**IPrintOemPS::Command**](https://msdn.microsoft.com/library/windows/hardware/ff553199) method.

Pscript5 calls the **IPrintOemPS::Command** method at a variety of points within the print job's data stream. One of the function's arguments specifies an index value that represents the current point in the data stream. Each time the function is called, it can check the index value and either provide additional stream data or not.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Pscript-Specific%20Customized%20Rendering%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


