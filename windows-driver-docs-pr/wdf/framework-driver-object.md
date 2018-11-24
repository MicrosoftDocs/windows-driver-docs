---
title: Framework Driver Object
description: Framework Driver Object
ms.assetid: 6e9e568c-7e4f-48bd-b351-4be0e12cc15b
keywords:
- UMDF objects WDK , driver objects
- framework objects WDK UMDF , driver objects
- driver objects WDK UMDF
- IWDFDriver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Driver Object


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

The framework driver object is exposed to drivers by the [IWDFDriver](https://msdn.microsoft.com/library/windows/hardware/ff558893) interface. It is the framework representation of the driver image loaded in the driver host process. The framework creates a new driver object for each driver loaded in the driver host process. The **IWDFDriver** interface is passed to the driver by the [**IDriverEntry::OnInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff554900) method, which is the main entry point for the user-mode driver.

 

 





