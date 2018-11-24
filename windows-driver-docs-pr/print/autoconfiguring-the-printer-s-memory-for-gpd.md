---
title: Autoconfiguring the Printer's Memory for GPD
description: Autoconfiguring the Printer's Memory for GPD
ms.assetid: 5e8339a5-d515-4821-853e-bc6607b2d9c1
keywords:
- memory WDK printer autoconfig
- GPD files WDK GDL extensions , memory
- in-box autoconfiguration support WDK printer , memory
- autoconfiguring printer memory WDK
- printer memory configurations WDK autoconfiguration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfiguring the Printer's Memory for GPD


The following code example shows how to add entries to the GDL file for any memory options in your GPD file. The GPD code example that is shown after the following example is a typical definition of the Memory feature.

```GPD
*Feature: Memory
{
  *rcNameID: =PRINTER_MEMORY_DISPLAY
  *DefaultOption: 4096KB

  *MemConfigKB: PAIR(4096, 3150)
  *MemConfigKB: PAIR(8192, 6750)
}
```

You can enable memory autoconfiguration by adding the following feature to the GDL file.

```GDL
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








