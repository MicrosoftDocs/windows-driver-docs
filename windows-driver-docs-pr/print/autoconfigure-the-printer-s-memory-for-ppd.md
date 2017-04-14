---
title: Autoconfigure the Printer's Memory for PPD
author: windows-driver-content
description: Autoconfigure the Printer's Memory for PPD
ms.assetid: 75df1026-896f-4840-a69d-975f813ca636
keywords: ["memory WDK printer autoconfig", "PPD files WDK autoconfiguration , memory", "in-box autoconfiguration support WDK printer , memory", "autoconfiguring printer memory WDK", "printer memory configurations WDK autoconfiguration"]
---

# Autoconfigure the Printer's Memory for PPD


Add entries to the GDL for memory options specified in the PPD. The first sample is an example excerpt from a PPD file that concerns installable memory options:

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autoconfigure%20the%20Printer's%20Memory%20for%20PPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


