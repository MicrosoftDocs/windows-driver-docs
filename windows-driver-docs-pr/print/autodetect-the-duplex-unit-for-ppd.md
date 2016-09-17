---
title: Autodetect the Duplex Unit for PPD
author: windows-driver-content
description: Autodetect the Duplex Unit for PPD
MS-HAID:
- 'autocfg\_0208652e-4f28-4806-93f2-7ee91d8fbdd6.xml'
- 'print.autodetect\_the\_duplex\_unit\_for\_ppd'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: bbecceb1-ba1d-4d2d-9a7b-e43f49345ca2
keywords: ["autodetecting duplex unit WDK printer autoconfiguration", "PPD files WDK autoconfiguration , autodetecting duplex unit", "in-box autoconfiguration support WDK printer , autodetecting duplex unit", "detecting duplex unit", "duplex unit WDK printer autoconfiguration"]
---

# Autodetect the Duplex Unit for PPD


The following two examples show one possible mapping between a duplex unit feature as described in a PPD file and its counterpart in the GDL file. This first example is an excerpt from the PPD file.

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Autodetect%20the%20Duplex%20Unit%20for%20PPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


