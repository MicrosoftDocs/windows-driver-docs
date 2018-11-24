---
title: Location
description: Location
ms.assetid: f04ce4de-233d-4763-be4d-e913623f4f1a
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Location


Schema Path:\\Printer.Finishing.HolePunch.Location

Node Type:Property

Description:This property contains all the value entries that pertain to the location at which holes are punched in output pages.

The Location property contains two child values: **CurrentValue** and **Supported**.

### <span id="currentvalue"></span><span id="CURRENTVALUE"></span> CurrentValue

Schema Path:\\Printer.Finishing.HolePunch.Location:CurrentValue

Node Type:Value

Data Type:BIDI\_INT

Description:The current (default) location at which holes are punched.

The following values are allowed:

Top

Bottom

Left

Right

### <span id="supported"></span><span id="SUPPORTED"></span> Supported

Schema Path:\\Printer.Finishing.HolePunch.Location:Supported

Node Type:Value

Data Type:BIDI\_STRING

Description:A comma-separated list of all the values supported for hole punch locations.

 

 




