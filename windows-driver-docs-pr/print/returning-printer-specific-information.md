---
title: Returning Printer-Specific Information
description: Returning Printer-Specific Information
ms.assetid: 7a47b395-4b01-437f-bed7-967b31b5841e
keywords:
- printer graphics DLL WDK , return printer-specific information
- graphics DLL WDK printer , return printer-specific information
- returning printer-specific information WDK printer graphics
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Returning Printer-Specific Information





GDI sometimes requests a printer graphics DLL to return printer-specific information in between print jobs, by calling such **DrvQuery**-prefixed graphics DDI functions as [**DrvQueryAdvanceWidths**](https://msdn.microsoft.com/library/windows/hardware/ff556259) (if defined by the graphics DLL).

An example of when this might occur is the case of a word processing application that is maintaining a WYSIWYG screen display of a printable page. To correctly display the line breaks in text, the word processor must base line-fitting calculations on character widths and other font metrics from the selected printer's implementation of a font.

 

 




