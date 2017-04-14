---
title: Autodetect the Printer's Hard Drive for PPD
author: windows-driver-content
description: Autodetect the Printer's Hard Drive for PPD
ms.assetid: 0f2eba5c-1a05-4aaf-8780-266d2339570e
keywords: ["autodetecting printer hard drive WDK printer autoconfiguration", "PPD files WDK autoconfiguration , autodetecting hard drive", "in-box autoconfiguration support WDK printer , autodetecting hard drive", "detecting printer hard drive", "hard drive autodetection WDK printer"]
---

# Autodetect the Printer's Hard Drive for PPD


Add entries to the GDL file for any hard drive-related features in your PPD file. You can do this by creating a corresponding feature construct in the GDL file using the same technique shown in the previous example. The following GDL construct automatically detects whether a hard disk is installed.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autodetect%20the%20Printer's%20Hard%20Drive%20for%20PPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


