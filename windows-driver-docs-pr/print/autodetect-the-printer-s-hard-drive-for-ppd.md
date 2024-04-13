---
title: Autodetect the Printer's Hard Drive for PPD
description: Autodetect the Printer's Hard Drive for PPD
keywords:
- autodetecting printer hard drive WDK printer autoconfiguration
- PPD files WDK autoconfiguration , autodetecting hard drive
- in-box autoconfiguration support WDK printer , autodetecting hard drive
- detecting printer hard drive
- hard drive autodetection WDK printer
ms.date: 04/20/2017
---

# Autodetect the Printer's Hard Drive for PPD


Add entries to the GDL file for any hard drive-related features in your PPD file. You can do this by creating a corresponding feature construct in the GDL file using the same technique shown in the previous example. The following GDL construct automatically detects whether a hard disk is installed.

```GDL
*% The GDL parser merges this feature definition with the 
*% corresponding feature construct in the GPD file
*Feature: PrinterHardDisk
{
  *FeatureType: PRINTER_PROPERTY

  *BidiQuery: PrinterHardDisk
  {
     *QueryString: "\Printer.Configuration.HardDisk:Installed"
  }
  *BidiResponse: PrinterHardDisk
  {
     *ResponseType: BIDI_BOOL
     *ResponseData: ENUM_OPTION (PrinterHardDisk)
  }
  *Option: FALSE
  {
     *BidiValue: BOOL(FALSE)
  }
  *Option: TRUE
  {
     *BidiValue: BOOL(TRUE)
  }
}
```

 

 




