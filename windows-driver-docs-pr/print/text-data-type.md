---
title: TEXT Data Type
author: windows-driver-content
description: TEXT Data Type
ms.assetid: 4d84b639-70e3-48e5-bfcc-61849e835710
keywords: ["print processors WDK , data types", "data types WDK print processor", "TEXT data type WDK print processor"]
---

# TEXT Data Type


## <a href="" id="ddk-text-data-type-gg"></a>


TEXT data consists solely of ANSI text. The print processor calls GDI to draw characters using the print device's default font, and sends the resulting RAW-formatted output to the spooler (by calling **WritePrinter**, described in the Microsoft Windows SDK documentation). The process is equivalent to opening the input file with Notepad and then printing the file. (This format is used for printers that do not print text characters.)

For more information about the TEXT data type, see the *Windows 2000 Professional Resource Kit* or the *Windows 2000 Server Resource Kit*. (These resources may not be available in some languages and countries.)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20TEXT%20Data%20Type%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


