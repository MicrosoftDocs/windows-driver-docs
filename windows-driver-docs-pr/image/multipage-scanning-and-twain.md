---
title: Multipage Scanning and TWAIN
author: windows-driver-content
description: Multipage Scanning and TWAIN
MS-HAID:
- 'WIA\_drv\_scan\_bd8fe910-f764-466e-9db7-715ffdd6bc12.xml'
- 'image.multipage\_scanning\_and\_twain'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 02b5ef48-413d-403b-8c42-caecd9521067
---

# Multipage Scanning and TWAIN


## <a href="" id="ddk-multipage-scanning-and-twain-si"></a>


Starting with Windows XP, the TWAIN compatibility layer supports multipage scanning from scroll-fed devices, provided that all scanned pages are of the same length. The reason for this is that TWAIN obtains information from the calling application about page length only on the first page. TWAIN does not require the calling application to ask for image information between pages. Furthermore, TWAIN applies the information it receives from the application about the first page to all succeeding pages.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Multipage%20Scanning%20and%20TWAIN%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


