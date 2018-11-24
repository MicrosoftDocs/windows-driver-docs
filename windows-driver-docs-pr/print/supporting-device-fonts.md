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





If a printer provides device fonts, the printer graphics DLL must define a [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277) function to generate text output commands. The graphics DLL must also define the following functions:

[**DrvQueryAdvanceWidths**](https://msdn.microsoft.com/library/windows/hardware/ff556259)
[**DrvQueryFont**](https://msdn.microsoft.com/library/windows/hardware/ff556262)
[**DrvQueryFontData**](https://msdn.microsoft.com/library/windows/hardware/ff556264)
[**DrvQueryFontTree**](https://msdn.microsoft.com/library/windows/hardware/ff556266)
For more information about supporting device fonts, see [Supporting Graphics DDI Font and Text Functions](https://msdn.microsoft.com/library/windows/hardware/ff569868).

 

 




