---
title: TEXT Data Type
description: TEXT Data Type
ms.assetid: 4d84b639-70e3-48e5-bfcc-61849e835710
keywords:
- print processors WDK , data types
- data types WDK print processor
- TEXT data type WDK print processor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TEXT Data Type





TEXT data consists solely of ANSI text. The print processor calls GDI to draw characters using the print device's default font, and sends the resulting RAW-formatted output to the spooler (by calling **WritePrinter**, described in the Microsoft Windows SDK documentation). The process is equivalent to opening the input file with Notepad and then printing the file. (This format is used for printers that do not print text characters.)

For more information about the TEXT data type, see the *Windows 2000 Professional Resource Kit* or the *Windows 2000 Server Resource Kit*. (These resources may not be available in some languages and countries.)

 

 




