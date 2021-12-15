---
title: Virtual Printers in Printer INF Files
description: Virtual Printers in Printer INF Files
ms.date: 04/20/2017
---

# Virtual Printers in Printer INF Files


A virtual printer is a print destination, such as a fax server or electronic document, that is not a physical printer. Because a virtual printer does not have a hardware ID, it must be represented in your printer INF file by a null hardware ID.

To insert a null hardware ID in an INF file, add a second comma in the models section of the INF between the Install section name and the Compatible ID. The following example shows how to create a null hardware ID for the indicated fax printer.

```cpp
"Objectworld Fax Printer"=OWFAX,,Objectworld_Fax_Printer
```

For more information about virtual printers in INF files, see **DriverCategory** in [Printer INF File Entries](printer-inf-file-entries.md).

 

 




