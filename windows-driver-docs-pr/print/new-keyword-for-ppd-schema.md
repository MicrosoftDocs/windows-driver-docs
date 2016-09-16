---
title: ew Keyword for PPD Schema
author: windows-driver-content
description: ew Keyword for PPD Schema
MS-HAID:
- 'autocfg\_174fa1b7-2827-44b0-8d4f-db08539209bd.xml'
- 'print.new\_keyword\_for\_ppd\_schema'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 05caa402-4949-4c0f-913c-1c87e65c30d7
keywords: ["root-level keywords WDK printer autoconfiguration", "PPD files WDK autoconfiguration , keywords", "keywords WDK printer autoconfiguration", "in-box autoconfiguration support WDK printer , keywords"]
---

# ew Keyword for PPD Schema


For Windows Vista and later versions of Windows, a new root-level keyword should be added to the PPD file which points to the GDL file in the PPD, \***MSBidiQueryFile**, which would identify a GDL file that contains the bidi mapping information required for AutoConfig. If the keyword is missing, AutoConfig does not need to invoke the GDL parser or hit the file system again to search for a GDL file.

Developers writing PScript-based drivers must use a separate GDL file that the driver's main PPD file references directly using the \***MSBidiQueryFile** Keyword.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20ew%20Keyword%20for%20PPD%20Schema%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


