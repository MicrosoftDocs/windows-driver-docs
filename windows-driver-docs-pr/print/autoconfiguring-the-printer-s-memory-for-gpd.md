---
title: Autoconfiguring the Printer's Memory for GPD
author: windows-driver-content
description: Autoconfiguring the Printer's Memory for GPD
ms.assetid: 5e8339a5-d515-4821-853e-bc6607b2d9c1
keywords:
- memory WDK printer autoconfig
- GPD files WDK GDL extensions , memory
- in-box autoconfiguration support WDK printer , memory
- autoconfiguring printer memory WDK
- printer memory configurations WDK autoconfiguration
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Autoconfiguring the Printer's Memory for GPD


The following code example shows how to add entries to the GDL file for any memory options in your GPD file. The GPD code example that is shown after the following example is a typical definition of the Memory feature.

```
*Feature: Memory
{
  *rcNameID: =PRINTER_MEMORY_DISPLAY
  *DefaultOption: 4096KB
 
  *MemConfigKB: PAIR(4096, 3150)
  *MemConfigKB: PAIR(8192, 6750)
}
 
```

You can enable memory autoconfiguration by adding the following feature to the GDL file.

```
*% This feature definition merges with the definition in the GPD file
*Feature: Memory
{
  *% *BidiQuery and *BidiResponse constructs must have the same names
  *BidiQuery: Memory
  {
  *QueryString: "\Printer.Configuration.Memory:Size"
  }
  *BidiResponse: Memory
   {
    *ResponseType: BIDI_INT
    *ResponseData: ENUM_OPTION (Memory)
  }
 
  *Option: 4096KB
  {
    *% Names for the memory options already defined in GPD
    *BidiValue: INT(4096)
  }
 
  *Option: 8192KB
  {
    *BidiValue: INT(8192)
  }
}
 
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfiguring%20the%20Printer's%20Memory%20for%20GPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


