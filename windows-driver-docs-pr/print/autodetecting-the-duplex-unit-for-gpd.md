---
title: Autodetecting the Duplex Unit for GPD
author: windows-driver-content
description: Autodetecting the Duplex Unit for GPD
MS-HAID:
- 'autocfg\_cf609580-e1ff-4efc-87e7-dae548406cf3.xml'
- 'print.autodetecting\_the\_duplex\_unit\_for\_gpd'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a5c91b00-ca7c-4c22-a16c-a976011d8b89
keywords: ["autodetecting duplex unit WDK printer autoconfiguration", "GPD files WDK GDL extensions , autodetecting duplex unit", "in-box autoconfiguration support WDK printer , autodetecting duplex unit", "detecting duplex unit", "duplex unit WDK printer autoconfiguration"]
---

# Autodetecting the Duplex Unit for GPD


Suppose that your GPD file has a Duplex feature that is defined like the following example, such that the duplex unit is installable:

```
*Feature: Duplex
{
   *rcNameID: =TWO_SIDED_PRINTING_DISPLAY
  *DefaultOption: NONE
  *Option: NONE
  {
    *rcNameID: =NONE_DISPLAY
    *Command: CmdSelect
    {
      *Order: DOC_SETUP.9
      *Cmd: "<1B>&l0S"
    }
  }
  *Option: VERTICAL
  {
    *rcNameID: =FLIP_ON_LONG_EDGE_DISPLAY
    *Command: CmdSelect
    {
      *Order: DOC_SETUP.10
      *Cmd: "<1B>&l1S"
    }
  }
  *Option: HORIZONTAL
  {
    *rcNameID: =FLIP_ON_SHORT_EDGE_DISPLAY
    *Command: CmdSelect
    {
      *Order: DOC_SETUP.10
      *Cmd: "<1B>&l2S"
    }
  }
}
 
*%
*% Installable Option
*%
*Feature: DuplexUnit
{
  *rcNameID: 429 *% Duplex Unit
  *HelpIndex: 12004
  *FeatureType: PRINTER_PROPERTY
  *DefaultOption: FALSE
  *Option: NotInstalled
  {
    *rcNameID: 444
    *DisabledFeatures: LIST(Duplex.VERTICAL, Duplex.HORIZONTAL)
  }
  *Option: Installed
  {
    *rcNameID: 443
  }
}
 
```

The following GDL code example provides the ability to autodetect the existence of a duplex unit (which is described in the preceding GPD code example) and set the appropriate option. In this example, the spooler sends the query that is shown in the \***BidiQuery** construct. When the printer receives the query, it responds with one of the two possible \***Option** construct values.

```
*Feature: DuplexUnit
{
  *% Note that the *BidiQuery and *BidiResponse constructs must have the same names
  *BidiQuery: DuplexUnit
  {
    *QueryString: "\Printer.Configuration.DuplexUnit:Installed"
  }
 
  *BidiResponse: DuplexUnit
  {
    *ResponseType: BIDI_BOOL
    *ResponseData: ENUM_OPTION(DuplexUnit)
  }
 
  *Option: NotInstalled
  {
    *BidiValue: BOOL(FALSE)
  }
 
  *Option: Installed
  {
    *BidiValue: BOOL(TRUE)
  }
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autodetecting%20the%20Duplex%20Unit%20for%20GPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


