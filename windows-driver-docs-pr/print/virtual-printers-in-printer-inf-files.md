---
title: Virtual Printers in Printer INF Files
description: Virtual Printers in Printer INF Files
ms.assetid: a7308b0f-61b8-4b4d-a116-ce940787882b
---

# Virtual Printers in Printer INF Files


A virtual printer is a print destination, such as a fax server or electronic document, that is not a physical printer. Because a virtual printer does not have a hardware ID, it must be represented in your printer INF file by a null hardware ID.

To insert a null hardware ID in an INF file, add a second comma in the models section of the INF between the Install section name and the Compatible ID. The following example shows how to create a null hardware ID for the indicated fax printer.

```
"Objectworld Fax Printer"=OWFAX,,Objectworld_Fax_Printer
```

For more information about virtual printers in INF files, see **DriverCategory** in [Printer INF File Entries](printer-inf-file-entries.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Virtual%20Printers%20in%20Printer%20INF%20Files%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




