---
title: Customized PDEV Structures
description: Customized PDEV Structures
keywords:
- rendering plug-ins WDK print , PDEV structures
- PDEV WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Customized PDEV Structures





The rendering plug-ins implement three methods to support private PDEV structures. Unidrv rendering plug-ins must implement the following methods:

[**IPrintOemUni::EnablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-enablepdev)

[**IPrintOemUni::DisablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-disablepdev)

[**IPrintOemUni::ResetPDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuni-resetpdev)

Pscript5 rendering plug-ins must implement the following methods:

[**IPrintOemPS::EnablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-enablepdev)

[**IPrintOemPS::DisablePDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-disablepdev)

[**IPrintOemPS::ResetPDEV**](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemps-resetpdev)

PDEV structure is a generic term. It refers to a private, locally defined structure for use by the module that defines it. Typically, it is used for storing physical device characteristics. Each printer driver, and each rendering plug-in, defines its own PDEV structure. There is no globally defined structure of type "PDEV".

 

