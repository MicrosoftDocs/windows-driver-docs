---
title: GPD/PPD-Based Feature Description Changes
author: windows-driver-content
description: GPD/PPD-Based Feature Description Changes
ms.assetid: 22333d78-f78f-4031-a9f3-50b43ec746b6
---

# GPD/PPD-Based Feature Description Changes


The Microsoft XPSDrv Unidrv/PScript5 driver does not contain any hard-coded Unidrv/PScript5 features. You should specify every feature, option, and constraint in GPD or PPD files if the core driver configuration module needs to handle the feature, option, or constraint. You can still implement configuration plug-ins that provide support for non-GPD or non-PPD features, options, or constraints.

The root GPD or PPD file (which is specified in the INF file as the driver's DataFile) is what the core driver configuration module will parse. This root GPD or PPD file can include other GPD or PPD files to enable the modular design of GPD or PPD files. In addition to including the

Msxpsinc.gpd and Msxpsinc.ppd files, you can decide how to construct the GPD and PPD files for your filter pipelines. We a recommend that you pair your filters with GPD or PPD files to maximize the reusability of the filters.

The following code example shows a GPD example to specify the Reverse Order Printing feature that a filter supports in a Unidrv-based XPSDrv filter pipeline:

```
*Feature: ReverseOrderPrinting
 {
 *PrintSchemaKeywordMap: "JobPageOrder"

 *Option: FrontToBack
 {
 *PrintSchemaKeywordMap: "Standard"
 }

 *Option: BackToFront
 {
 *PrintSchemaKeywordMap: "Reverse"
 }
}
```

In the preceding example, the "ReverseOrderPrinting" custom GPD feature is defined with two custom options: "FrontToBack" and "BackToFront". The example uses the **PrintSchemaKeywordMap** keyword to map the GPD custom feature or option to public Print Schema keywords.

The following code example shows a PPD example to specify the Page Orientation feature that a filter supports in a PScript5-based XPSDrv filter pipeline.

```
*OpenUI *PageOrientation: PickOne
*DefaultPageOrientation: Portrait
*PageOrientation Portrait: ""
*PageOrientation Landscape: ""
*PageOrientation RotatedLandscape: ""
*CloseUI: *PageOrientation

*MSPrintSchemaKeywordMap: PageOrientation  *PageOrientation
*MSPrintSchemaKeywordMap: PageOrientation Portrait *PageOrientation Portrait
*MSPrintSchemaKeywordMap: PageOrientation Landscape *PageOrientation Landscape
*MSPrintSchemaKeywordMap: PageOrientation ReverseLandscape *PageOrientation RotatedLandscape
```

In the preceding example, a custom PPD feature with three custom options is defined to specify the filter's ability to support the three Print Schema standard PageOrientation options.

By using the **PrintSchemaKeywordMap** or **MSPrintSchemaKeywordMap** keyword, these GPD or PPD custom features or options will be properly exposed in XML PrintCapabilities or PrintTickets by using the mapped public Print Schema keywords.

In a core driver's DEVMODE structure, settings for these custom GPD or PPD features are stored in the option array.

**Note**   For Windows 7, the **MxdcGetPDEVAdjustment** function has new parameters for landscape rotation. For more information, see [**MxdcXDCGetPDEVAdjustment**](https://msdn.microsoft.com/library/windows/hardware/ff557558).

 

## Related topics
[**MxdcXDCGetPDEVAdjustment**](https://msdn.microsoft.com/library/windows/hardware/ff557558)  
[V4 Printer Driver Localization](v4-driver-localization.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GPD/PPD-Based%20Feature%20Description%20Changes%20%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


