---
title: Converting East Asian AFM Files to NTF Files
author: windows-driver-content
description: Converting East Asian AFM Files to NTF Files
ms.assetid: 0932068a-9101-4cdc-8c80-b2d3a4b507ba
keywords:
- minidrivers WDK Pscript , converting AFM files
- NTF files
- .ntf files
- .afm files
- AFM files
- converting AFM files to NTF files WDK Pscript
- Adobe Font Metrics WDK Pscript
- East Asian fonts WDK print
- Asian fonts WDK print
- Chinese Simplified font support WDK print
- Chinese Traditional font support WDK print
- Japanese font support WDK
- Korean font support WDK print
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Converting East Asian AFM Files to NTF Files


## <a href="" id="ddk-converting-east-asian-afm-files-to-ntf-files-gg"></a>


To process an East Asian font's .afm file, Makentf.exe (discussed in [Converting AFM Files to NTF Files](converting-afm-files-to-ntf-files.md)) requires .map and .ps files to create a mapping table from Unicode to CID (character ID) for the font.

The East Asian .afm file has the CID description and metrics for each glyph contained in the font. The .map file lists the Unicode codes and corresponding character codes for the font's character set. The .ps file contains a list of Unicode codes and the corresponding CIDs for the font's character set.

Starting with an East Asian .afm file, Makentf.exe determines the character set. Based on the character set, Makentf.exe finds the appropriate .map and .ps files. From the .map file, Makentf.exe lists the Unicode codes that can be used in the font. From the Unicode code list and the .ps file, Makentf.exe then creates a Unicode-to-CID mapping table for the font. Currently, the .afm file is used to verify that each CID (glyph) is actually contained in the font. If the CID is found in the .afm file, a mapping entry from the Unicode code to the CID is created in the mapping table. If the CID is not found, the mapping entry is not created.

The .map and .ps files needed to create an .ntf file for Chinese Simplified, Chinese Traditional, Japanese, and Korean are shown in the following lists. Place these files and your .afm files in the same directory.

### Chinese Simplified

-   ucs2gbk.map

-   unigbh.ps

-   unigbv.ps

### Chinese Traditional

-   ucs2bg5.map

-   unicnsh.ps

-   unicnsv.ps

### Japanese

-   ucs283h.map

-   ucs283v.map

-   ucs2msj.map

-   uni83h.ps

-   uni83v.ps

-   unijish.ps

-   unijisv.ps

### Korean

-   ucs2jhb.map

-   ucs2uhc.map

-   uniksh.ps

-   uniksv.ps

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Converting%20East%20Asian%20AFM%20Files%20to%20NTF%20Files%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


