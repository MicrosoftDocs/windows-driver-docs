---
title: Vendor-Extended Properties
description: Vendor-Extended Properties
ms.assetid: bcc89272-c14d-4d46-a2ca-7da0fb188111
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Vendor-Extended Properties





A **PropCode** entry in the **DeviceData** INF file section (see the example in [Vendor-Extended Features](vendor-extended-features.md)) lists all the vendor-extended property codes, separated by commas. For each property code, an entry of the form **PropCode***XXXX* must be present, where XXXX is the code value in uppercase hexadecimal. The entry should list the WIA property code and text description (which does not need to be localized) enclosed in quotes.

The WIA property codes should be between 0x9802 and 0x11802, which is the range defined for vendor-defined WIA device properties. The properties can be accessed through the **IWiaPropertyStorage::GetPropertyStream** and **IWiaPropertyStorage::SetPropertyStream** methods, which are described in the Microsoft Windows SDK documentation.

 

 




