---
title: Improvements in XPSDrv
description: This topic provides information about updates that have been made to the XPSDrv rendering architecture.
ms.assetid: 5D76ECA2-C5F6-47E4-BC05-B5137AD4196B
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Improvements in XPSDrv


This topic provides information about updates that have been made to the XPSDrv rendering architecture.

**XPS Format**

The XPS Print API and/or the print filter pipeline will convert seamlessly between [Microsoft Xml Paper Specification 1.0](https://msdn.microsoft.com/windows/hardware/gg463375) (MS XPS), and [OpenXPS](http://www.ecma-international.org/publications/standards/Ecma-388.htm) (ECMA-388). Unless otherwise specified, v4 print drivers default to consuming MS XPS. Using the manifest directive XpsFormat, drivers may choose to support one or both of the available XPS formats. For more information about OpenXPS support, see [OpenXPS Support in Windows](https://msdn.microsoft.com/library/windows/hardware/br259130).

**XPS Rasterization Service Improvements**

The XPS Rasterization Service has been improved in Windows 8 to make use of the Graphics Processing Unit (GPU) to provide faster XPS rasterization. These performance improvements are available on Windows 8 systems with GPUs that use the Windows Display Driver Model (WDDM) 1.2. XPS rendering filters do not require any modification to take advantage of this improvement, and it will be available for both v3 and v4 print drivers.

The XPS Rasterization Service can also provide rasterization in several pixel formats, including the following new, high precision formats. As a result, print drivers that use the XPS Rasterization Service can now target color precision at 8-bits, 16-bits and 32-bits per channel. For more information on pixel formats, see [Native Pixel Formats Overview](https://msdn.microsoft.com/library/windows/hardware/ee719797.aspx). These new pixel formats are supported by the [**XPSRaterizationFactory1::CreateRasterizer1**](https://msdn.microsoft.com/library/windows/hardware/hh802468) method. The following table shows the XPS Rasterization Service Pixel Formats.

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
[Microsoft Xml Paper Specification 1.0](https://msdn.microsoft.com/windows/hardware/gg463375)  
[Native Pixel Formats Overview](https://msdn.microsoft.com/library/windows/hardware/ee719797.aspx)  
[OpenXPS](http://www.ecma-international.org/publications/standards/Ecma-388.htm)  
[OpenXPS Support in Windows](https://msdn.microsoft.com/library/windows/hardware/br259130)  
[V4 Printer Driver Rendering Architecture](v4-driver-rendering-architecture.md)  
[**XPSRaterizationFactory1::CreateRasterizer1**](https://msdn.microsoft.com/library/windows/hardware/hh802468)  



