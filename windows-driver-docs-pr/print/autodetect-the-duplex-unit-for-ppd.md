---
title: Autodetect the Duplex Unit for PPD
description: Autodetect the Duplex Unit for PPD
ms.assetid: bbecceb1-ba1d-4d2d-9a7b-e43f49345ca2
keywords:
- autodetecting duplex unit WDK printer autoconfiguration
- PPD files WDK autoconfiguration , autodetecting duplex unit
- in-box autoconfiguration support WDK printer , autodetecting duplex unit
- detecting duplex unit
- duplex unit WDK printer autoconfiguration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Autodetect the Duplex Unit for PPD


The following two examples show one possible mapping between a duplex unit feature as described in a PPD file and its counterpart in the GDL file. This first example is an excerpt from the PPD file.

```PPD
*OpenUI *DuplexUnit: Boolean
*DefaultDuplexUnit: True
*DuplexUnit True/Installed: ""
*DuplexUnit False/Not Installed: ""
*?DuplexUnit: "
  save
    currentpagedevice /Duplex known
    {(True)}{(False)}ifelse = flush
  restore
"
*End
*CloseUI: *DuplexUnit
```

The next example is an excerpt from the GDL file, and shows the DuplexUnit feature definition that corresponds to the duplex unit feature in the preceding example.

```GDL
*Feature: DuplexUnit
{
  *FeatureType: PRINTER_PROPERTY

  *% *BidiQuery and *BidiResponse constructs must have the same names
  *BidiQuery: DuplexUnit
  {
    *QueryString: "\Printer.Configuration.DuplexUnit:Installed"
  }
  *BidiResponse: DuplexUnit
  {
    *ResponseType: BIDI_BOOL
    *ResponseData: ENUM_OPTION (DuplexUnit)
  }

  *Option: False
  {
    *BidiValue: BOOL(FALSE)
  }
  *Option: True
  {
    *BidiValue: BOOL(TRUE)
  }
}
```

 

 




