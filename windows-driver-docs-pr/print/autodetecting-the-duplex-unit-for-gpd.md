---
title: Autodetecting the Duplex Unit for GPD
description: Autodetecting the Duplex Unit for GPD
ms.assetid: a5c91b00-ca7c-4c22-a16c-a976011d8b89
keywords:
- autodetecting duplex unit WDK printer autoconfiguration
- GPD files WDK GDL extensions , autodetecting duplex unit
- in-box autoconfiguration support WDK printer , autodetecting duplex unit
- detecting duplex unit
- duplex unit WDK printer autoconfiguration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autodetecting the Duplex Unit for GPD


Suppose that your GPD file has a Duplex feature that is defined like the following example, such that the duplex unit is installable:

```GPD
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

```GDL
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








