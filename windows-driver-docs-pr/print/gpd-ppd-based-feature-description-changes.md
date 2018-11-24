---
title: GPD/PPD-Based Feature Description Changes
description: GPD/PPD-Based Feature Description Changes
ms.assetid: 22333d78-f78f-4031-a9f3-50b43ec746b6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPD/PPD-Based Feature Description Changes


The Microsoft XPSDrv Unidrv/PScript5 driver does not contain any hard-coded Unidrv/PScript5 features. You should specify every feature, option, and constraint in GPD or PPD files if the core driver configuration module needs to handle the feature, option, or constraint. You can still implement configuration plug-ins that provide support for non-GPD or non-PPD features, options, or constraints.

The root GPD or PPD file (which is specified in the INF file as the driver's DataFile) is what the core driver configuration module will parse. This root GPD or PPD file can include other GPD or PPD files to enable the modular design of GPD or PPD files. In addition to including the

Msxpsinc.gpd and Msxpsinc.ppd files, you can decide how to construct the GPD and PPD files for your filter pipelines. We a recommend that you pair your filters with GPD or PPD files to maximize the reusability of the filters.

The following code example shows a GPD example to specify the Reverse Order Printing feature that a filter supports in a Unidrv-based XPSDrv filter pipeline:

```cpp
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

```cpp
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



