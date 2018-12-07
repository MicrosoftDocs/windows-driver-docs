---
title: Orientation
description: Orientation
ms.assetid: a3bd9d67-200f-4739-ad0e-ff7fd2eb20a3
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Orientation


Schema Path:\\Printer.Layout.Orientation

Node Type:Property

Description:The property associated with page orientation. The value entries that are children of this property are the current page orientation and a list of page orientations supported by the device.

The Orientation property contains two child values: **CurrentValue** and **Supported**.

### <span id="currentvalue"></span><span id="CURRENTVALUE"></span> CurrentValue

Schema Path:\\Printer.Layout.Orientation:CurrentValue

Node Type:Value

Data Type:BIDI\_STRING

Description:The current (default) orientation in which pages will be printed.

Must be one of the following values.

Portrait

Landscape

ReversePortrait

ReverseLandscape

### <span id="supported"></span><span id="SUPPORTED"></span> Supported

Schema Path:\\Printer.Layout.Orientation:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all values supported for Orientation.

 

 




