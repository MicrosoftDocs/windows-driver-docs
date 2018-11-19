---
title: Converting East Asian AFM Files to NTF Files
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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Converting East Asian AFM Files to NTF Files





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

 

 




