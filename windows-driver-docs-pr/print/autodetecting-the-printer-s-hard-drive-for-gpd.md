---
title: Autodetecting the Printer's Hard Drive for GPD
description: Autodetecting the Printer's Hard Drive for GPD
ms.assetid: c3bc415e-fa4d-42d0-9686-3105a588a7ea
keywords:
- autodetecting printer hard drive WDK printer autoconfiguration
- GPD files WDK GDL extensions , autodetecting hard drive
- in-box autoconfiguration support WDK printer , autodetecting hard drive
- detecting printer hard drive
- hard drive autodetection WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autodetecting the Printer's Hard Drive for GPD


Add entries to the GDL file for any hard drive-related features in your GPD file. For example, if you have a Collate feature that depends on whether a hard drive is installed, you can use autoconfiguration to automatically determine whether the printer is able to collate. Consider the following code example from a GPD file.

```GPD
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

```GDL
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








