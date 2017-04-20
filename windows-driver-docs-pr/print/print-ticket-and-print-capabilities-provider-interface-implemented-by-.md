---
title: Print ticket and capabilities - Unidrv/Pscript5
author: windows-driver-content
description: Print ticket and print capabilities provider interface implemented by Unidrv/Pscript5 plug-ins
ms.assetid: 00dcbbde-e4e4-4fcc-b69f-9c91051e0e29
keywords:
- Unidrv WDK print
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Print ticket and print capabilities provider interface implemented by Unidrv/Pscript5 plug-ins


The [Microsoft Universal Printer Driver](microsoft-universal-printer-driver.md) (Unidrv) and [Microsoft PostScript Printer Driver](microsoft-postscript-printer-driver.md) (Pscript5) core printer drivers on Windows Vista provide the means for plug-ins to implement print ticket support. Because Unidrv and Pscript5 both support loading multiple plug-ins for a single driver, each plug-in is able to provide its own provider implementation. The driver vendor is responsible for ensuring that each of the OEM plug-in provider implementations works correctly with the others. Not all of the plug-ins in a printer driver need to support the provider interface. However, the versions of the print ticket schema that are supported by the core driver are a subset of the versions that are supported by the core driver and all of the available plug-in providers. Because calls into the plug-in provider are driven by the application, the plug-in provider must be implemented in a thread-safe manner.

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Ticket%20and%20Print%20Capabilities%20Provider%20Interface%20Implemented%20by%20Unidrv/Pscript5%20Plug-ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


