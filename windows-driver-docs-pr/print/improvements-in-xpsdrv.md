---
title: Improvements in XPSDrv
author: windows-driver-content
description: This topic provides information about updates that have been made to the XPSDrv rendering architecture.
ms.assetid: 5D76ECA2-C5F6-47E4-BC05-B5137AD4196B
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Improvements in XPSDrv


This topic provides information about updates that have been made to the XPSDrv rendering architecture.

**XPS Format**

The XPS Print API and/or the print filter pipeline will convert seamlessly between [Microsoft Xml Paper Specification 1.0](http://msdn.microsoft.com/windows/hardware/gg463375) (MS XPS), and [OpenXPS](http://www.ecma-international.org/publications/standards/Ecma-388.md) (ECMA-388). Unless otherwise specified, v4 print drivers default to consuming MS XPS. Using the manifest directive XpsFormat, drivers may choose to support one or both of the available XPS formats. For more information about OpenXPS support, see [OpenXPS Support in Windows](http://msdn.microsoft.com/library/windows/hardware/br259130).

**XPS Rasterization Service Improvements**

The XPS Rasterization Service has been improved in Windows 8 to make use of the Graphics Processing Unit (GPU) to provide faster XPS rasterization. These performance improvements are available on Windows 8 systems with GPUs that use the Windows Display Driver Model (WDDM) 1.2. XPS rendering filters do not require any modification to take advantage of this improvement, and it will be available for both v3 and v4 print drivers.

The XPS Rasterization Service can also provide rasterization in several pixel formats, including the following new, high precision formats. As a result, print drivers that use the XPS Rasterization Service can now target color precision at 8-bits, 16-bits and 32-bits per channel. For more information on pixel formats, see [Native Pixel Formats Overview](http://msdn.microsoft.com/library/windows/hardware/ee719797.aspx). These new pixel formats are supported by the [**XPSRaterizationFactory1::CreateRasterizer1**](https://msdn.microsoft.com/library/windows/hardware/hh802468) method. The following table shows the XPS Rasterization Service Pixel Formats.

| Value                                | Channel Count | Bits per channel | Bits per pixel | Storage type |
|--------------------------------------|---------------|------------------|----------------|--------------|
| GUID\_WICPixelFormat32bppPBGRA       | 4             | 8                | 32             | UINT         |
| GUID\_WICPixelFormat64bppPRGBAHalf   | 4             | 16               | 64             | Float        |
| GUID\_WICPixelFormat128bppPRGBAFloat | 4             | 32               | 128            | Float        |

 

**IPrintCoreHelperUni2**

The [IPrintCoreHelperUni2](https://msdn.microsoft.com/library/windows/hardware/hh406580) interface was introduced in Windows 8 to support the retrieval of command strings from GPD files. The interface is identical to [IPrintCoreHelperUni](https://msdn.microsoft.com/library/windows/hardware/ff552940), except for the additional **GetNamedCommand** method.

## Related topics
[IPrintCoreHelperUni](https://msdn.microsoft.com/library/windows/hardware/ff552940)  
[IPrintCoreHelperUni2](https://msdn.microsoft.com/library/windows/hardware/hh406580)  
[Microsoft Xml Paper Specification 1.0](http://msdn.microsoft.com/windows/hardware/gg463375)  
[Native Pixel Formats Overview](http://msdn.microsoft.com/library/windows/hardware/ee719797.aspx)  
[OpenXPS](http://www.ecma-international.org/publications/standards/Ecma-388.md)  
[OpenXPS Support in Windows](http://msdn.microsoft.com/library/windows/hardware/br259130)  
[V4 Printer Driver Rendering Architecture](v4-driver-rendering-architecture.md)  
[**XPSRaterizationFactory1::CreateRasterizer1**](https://msdn.microsoft.com/library/windows/hardware/hh802468)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Improvements%20in%20XPSDrv%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


