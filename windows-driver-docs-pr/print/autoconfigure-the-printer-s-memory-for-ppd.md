---
title: Autoconfigure the Printer's Memory for PPD
description: Autoconfigure the Printer's Memory for PPD
ms.assetid: 75df1026-896f-4840-a69d-975f813ca636
keywords:
- memory WDK printer autoconfig
- PPD files WDK autoconfiguration , memory
- in-box autoconfiguration support WDK printer , memory
- autoconfiguring printer memory WDK
- printer memory configurations WDK autoconfiguration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autoconfigure the Printer's Memory for PPD


Add entries to the GDL for memory options specified in the PPD. The first sample is an example excerpt from a PPD file that concerns installable memory options:

```PPD
*% === Installable Options ===========
*OpenGroup: InstallableOptions/Options Installed
 
*OpenUI *InstalledMemory/Memory Configuration: PickOne
*DefaultInstalledMemory: 24Meg
*InstalledMemory 24Meg/Standard 24 MB RAM: ""
*InstalledMemory 56Meg/56 MB Total RAM: ""
*InstalledMemory 72Meg/72 MB Total RAM: ""
*CloseUI: *InstalledMemory
 
*CloseGroup: InstallableOptions
```

To enable autoconfiguration for the "InstalledMemory" PPD feature, add the following code example to the GDL file.

```GDL
*% This feature definition merges with the definition in the PPD file
*% because both have the same name
*Feature: InstalledMemory
{
  *FeatureType: PRINTER_PROPERTY

  *% *BidiQuery and *BidiResponse constructs must have the same names
  *BidiQuery: InstalledMemory
  {
    *QueryString: "\Printer.Configuration.Memory:Size"
  }
  *BidiResponse: InstalledMemory
  {
    *ResponseType: BIDI_INT
    *ResponseData: ENUM_OPTION (InstalledMemory)
  }
 
  *Option: 24Meg
  { 
    *BidiValue: INT(24576)
  } 
  *Option: 56Meg
  {
    *BidiValue: INT(57344)
  }
  *Option: 72Meg
  {
    *BidiValue: INT(73728)
  }
}
```

 

 




