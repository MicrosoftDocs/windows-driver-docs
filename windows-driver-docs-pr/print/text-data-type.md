---
title: TEXT data type
description: Provides information about the TEXT data type.
keywords:
- print processors WDK, data types
- data types WDK print processor
- TEXT data type WDK print processor
ms.date: 09/16/2022
---

# TEXT data type

TEXT data consists solely of ANSI text. The print processor calls GDI to draw characters using the print device's default font, and sends the resulting RAW-formatted output to the spooler by calling [**WritePrinter**](/windows/win32/printdocs/writeprinter). The process is equivalent to opening the input file with Notepad and then printing the file. This format is used for printers that do not print text characters.
