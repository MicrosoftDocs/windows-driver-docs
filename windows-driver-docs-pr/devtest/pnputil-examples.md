---
title: PnPUtil Examples
description: PnPUtil Examples
ms.assetid: 4805edb9-e4f8-441d-a7f4-0c962ddeae4e
ms.date: 01/31/2018
ms.localizationpriority: medium
---

# PnPUtil Examples

This topic provides examples on how to use the PnPUtil tool.

```
  pnputil /add-driver x:\driver.inf       <- Add driver package
  pnputil /add-driver c:\oem\*.inf        <- Add multiple driver packages
  pnputil /add-driver device.inf /install <- Add and install driver package
  pnputil /enum-drivers                   <- Enumerate OEM driver packages
  pnputil /delete-driver oem0.inf         <- Delete driver package
  pnputil /delete-driver oem1.inf /force  <- Force delete driver package
  pnputil /export-driver oem6.inf .       <- Export driver package
  pnputil /export-driver * c:\backup      <- Export all driver packages
```

 

 





