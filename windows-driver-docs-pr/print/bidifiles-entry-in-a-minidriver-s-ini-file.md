---
title: BidiFiles Entry in a Minidriver's INI File
author: windows-driver-content
description: BidiFiles Entry in a Minidriver's INI File
MS-HAID:
- 'autocfg\_f0b0b793-2613-499c-8a39-74fe8ccf5173.xml'
- 'print.bidifiles\_entry\_in\_a\_minidriver\_s\_ini\_file'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 953a29d2-f778-410e-bc8a-a09e294f2473
keywords: ["BidiFiles section", "INF files WDK print , bidi extension file information", "bidi extension files WDK printer autoconfig", "in-box autoconfiguration support WDK printer , bidi extension files"]
---

# BidiFiles Entry in a Minidriver's INI File


A printer minidriver communicates information about the bidi extension file to the port monitor by means of a minidriver-specific INI file. The port monitor uses this information during port initialization.

The following sample shows the `BidiFiles` section of the INI file. The `BidiSPMFile` entry would be used for a standard TCP/IP port monitor, and the `BidiWSDFile` entry would be used for a Web Services for Devices (WSD) port monitor.

```
# OEM Mapping & Extension GDL files 
# 
[BidiFiles]
BidiSPMFile = BidiSPM_AcmeXXX.XML
BidiWSDFile  = BidiWSD_AcmeXXX.XML
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20BidiFiles%20Entry%20in%20a%20Minidriver's%20INI%20File%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


