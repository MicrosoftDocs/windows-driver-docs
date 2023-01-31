---
title: Supporting Device Fonts
description: Supporting Device Fonts
keywords:
- printer graphics DLL WDK , device fonts
- graphics DLL WDK printer , device fonts
- device fonts WDK printer graphics
- fonts WDK printer graphics
ms.date: 01/30/2023
---

# Supporting Device Fonts

[!include[Print Support Apps](../includes/print-support-apps.md)]

If a printer provides device fonts, the printer graphics DLL must define a [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout) function to generate text output commands. The graphics DLL must also define the following functions:

[**DrvQueryAdvanceWidths**](/windows/win32/api/winddi/nf-winddi-drvqueryadvancewidths)

[**DrvQueryFont**](/windows/win32/api/winddi/nf-winddi-drvqueryfont)

[**DrvQueryFontData**](/windows/win32/api/winddi/nf-winddi-drvqueryfontdata)

[**DrvQueryFontTree**](/windows/win32/api/winddi/nf-winddi-drvqueryfonttree)

For more information about supporting device fonts, see [Supporting Graphics DDI Font and Text Functions](../display/supporting-graphics-ddi-font-and-text-functions.md).
