---
title: Command String Format
author: windows-driver-content
description: Command String Format
MS-HAID:
- 'nt5gpd\_3e75feec-3134-4f59-b814-17d42e347ec1.xml'
- 'print.command\_string\_format'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3b33b261-08c7-4441-94f5-6c9de53ae349
keywords: ["printer commands WDK Unidrv , strings", "command strings WDK Unidrv", "strings WDK Unidrv"]
---

# Command String Format


## <a href="" id="ddk-command-string-format-gg"></a>


Command strings are used to specify the escape sequences that Unidrv must send to printer hardware. Command strings can be made up of the following elements:

-   Quoted text strings, which have the following format:

    "*TextString*"

-   Command arguments, which have the following format:

    %*ArgumentType*{*StandardVariableExpression*}

Unidrv supports a maximum of 14 quoted text strings and command arguments in a command string.

As an example, a printer's command to set a rectangle's gray fill percentage might be specified as follows:

```
*Command: CmdRectGrayFill: "<1B>*c" %d{GrayPercentage} "g2P"
```

To send a percent sign (**%**) to a printer, include two percent sign characters (**%%**) in the command string. If the percent sign is at the end of the command string, you must use the hexadecimal equivalent, as in:

**"***string* **&lt;25 25&gt;"**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Command%20String%20Format%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


