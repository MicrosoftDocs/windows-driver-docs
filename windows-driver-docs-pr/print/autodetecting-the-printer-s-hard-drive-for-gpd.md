---
title: Autodetecting the Printer's Hard Drive for GPD
author: windows-driver-content
description: Autodetecting the Printer's Hard Drive for GPD
ms.assetid: c3bc415e-fa4d-42d0-9686-3105a588a7ea
keywords: ["autodetecting printer hard drive WDK printer autoconfiguration", "GPD files WDK GDL extensions , autodetecting hard drive", "in-box autoconfiguration support WDK printer , autodetecting hard drive", "detecting printer hard drive", "hard drive autodetection WDK printer"]
---

# Autodetecting the Printer's Hard Drive for GPD


Add entries to the GDL file for any hard drive-related features in your GPD file. For example, if you have a Collate feature that depends on whether a hard drive is installed, you can use autoconfiguration to automatically determine whether the printer is able to collate. Consider the following code example from a GPD file.

```
*% Printer supports collation only if PrinterHardDisk is installed
*Feature: Collate
{
  *rcNameID: 392 
 
  *DefaultOption: OFF
  *Option: ON
  {
    *rcNameID: =ON_DISPLAY
    *switch: PrinterHardDisk
    {
      *case: FALSE
      {
        *Command: CmdSelect
        {
           *Order: JOB_SETUP.5
           *% Collate requested but no disk =>
           *%   printer collate disabled
           *% Print Processor will take care
           *%   of collated copies
 
           *Cmd: ""
         }
      }
      *case: TRUE
      {
        *Command: CmdSelect
        {
           *Order: JOB_SETUP.5
           *% Collate requested with disk => 
            *%   printer collate enabled
           *% Printer will take care of collated copies
 
           *Cmd: "@PJL SET QTY=" %d{NumOfCopies}"<0A>"
        }
      }
    }
  }
  *Option: OFF
  {
    *rcNameID: =OFF_DISPLAY
    *Command: CmdSelect
    {
      *Order: JOB_SETUP.5
      *Cmd: ""
    }
  }
}
 
*% Feature to explicitly constrain the Collate feature
*Feature: PrinterHardDisk
{
  *rcNameID: 430 *% Printer Hard Disk
  *HelpIndex: 12002
  *FeatureType: PRINTER_PROPERTY
  *DefaultOption: FALSE
  *Option: FALSE
  {
    *rcNameID: 444
    *DisabledFeatures: Collate.ON
  }
  *Option: TRUE
  {
    *rcNameID: 443
  }
}
 
```

To automatically detect whether a hard disk is installed, and enable or disable collating accordingly, simply add the following code example to the GDL file.

```
*%The GDL parser merges this code with the corresponding feature construct in the GPD file
*Feature: PrinterHardDisk
{
  *% *BidiQuery and *BidiResponse constructs must have the same names
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
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autodetecting%20the%20Printer's%20Hard%20Drive%20for%20GPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


