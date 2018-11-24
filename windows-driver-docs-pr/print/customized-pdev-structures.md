---
title: Customized PDEV Structures
description: Customized PDEV Structures
ms.assetid: e5c51b9a-5f73-4411-88d8-931981a8450c
keywords:
- rendering plug-ins WDK print , PDEV structures
- PDEV WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized PDEV Structures





The rendering plug-ins implement three methods to support private PDEV structures. Unidrv rendering plug-ins must implement the following methods:

[**IPrintOemUni::EnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff554249)

[**IPrintOemUni::DisablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff554238)

[**IPrintOemUni::ResetPDEV**](https://msdn.microsoft.com/library/windows/hardware/ff554270)

Pscript5 rendering plug-ins must implement the following methods:

[**IPrintOemPS::EnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff553215)

[**IPrintOemPS::DisablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff553209)

[**IPrintOemPS::ResetPDEV**](https://msdn.microsoft.com/library/windows/hardware/ff553233)

PDEV structure is a generic term. It refers to a private, locally defined structure for use by the module that defines it. Typically, it is used for storing physical device characteristics. Each printer driver, and each rendering plug-in, defines its own PDEV structure. There is no globally defined structure of type "PDEV".

 

 




