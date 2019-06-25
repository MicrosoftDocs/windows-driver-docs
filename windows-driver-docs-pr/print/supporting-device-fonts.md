---
title: Supporting Device Fonts
description: Supporting Device Fonts
ms.assetid: 9ca3269d-3f87-4d8a-a897-7305ac172227
keywords:
- printer graphics DLL WDK , device fonts
- graphics DLL WDK printer , device fonts
- device fonts WDK printer graphics
- fonts WDK printer graphics
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Device Fonts





If a printer provides device fonts, the printer graphics DLL must define a [**DrvTextOut**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvtextout) function to generate text output commands. The graphics DLL must also define the following functions:

[**DrvQueryAdvanceWidths**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvqueryadvancewidths)
[**DrvQueryFont**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvqueryfont)
[**DrvQueryFontData**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvqueryfontdata)
[**DrvQueryFontTree**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvqueryfonttree)
For more information about supporting device fonts, see [Supporting Graphics DDI Font and Text Functions](https://docs.microsoft.com/windows-hardware/drivers/display/supporting-graphics-ddi-font-and-text-functions).

 

 




