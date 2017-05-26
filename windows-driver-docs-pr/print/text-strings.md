---
title: Text Strings
author: windows-driver-content
description: Text Strings
ms.assetid: 773c977b-aac4-4c7c-8bab-aa2c69b2a89a
keywords:
- GPD file entries WDK Unidrv , text strings
- text strings WDK GPD files
- strings WDK GPD files
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Text Strings


## <a href="" id="ddk-text-strings-gg"></a>


Text strings are strings of literal characters, delimited by quotation marks. Strings used by [Unidrv minidrivers](unidrv-minidrivers.md) can be placed in either of two locations:

-   They can be placed in a resource file. Strings that require localization, such as user interface text, should be placed in a resource file, as described in [Using Resource DLLs in a Minidriver](using-resource-dlls-in-a-minidriver.md).

-   They can be included in GPD files. Strings representing the escape sequences that make up printer commands are typically included within GPD files, because these strings do not need to be localized.

Strings must obey the following rules:

-   Strings must be delimited by quotation marks ("...").

-   Hexadecimal byte values can be placed in a string by delimiting hexadecimal digits by angle brackets (&lt;...&gt;), such as &lt;03&gt; or &lt;1B&gt;. Within a set of angle brackets, each pair of digits is interpreted as another hexadecimal byte value. Therefore &lt;03&gt;&lt;1B&gt;, &lt;03 1B&gt;, and &lt;031B&gt; are all equivalent.

-   The percent sign (%) is used as an escape character. To include a quotation mark or left angle bracket (", &lt;) in a string, precede it with a percent sign. To specify a string that ends with a percent sign, you must specify the hexadecimal value for %, as in "&lt;25&gt;".

    Additionally, to include a percent sign in a text string representing a [printer command](printer-commands.md), you must precede it with another percent sign. To specify a printer command that ends with a percent sign, you must specify two hexadecimal % values, as in

    "command-string&lt;25 25&gt;"

An example string is the command that selects letter-sized paper for the Canon BJC-600 printer. This command, which is the byte sequence 1B 28 67 03 00 6E 01 72, can be specified as:

"&lt;1B&gt;(g&lt;03 00&gt;n&lt;01&gt;r"

Each ASCII character included in the string is converted to its one-byte hexadecimal equivalent.

-   Strings that are included in GPD files must obey the following additional rule:

    To extend a string beyond a single line, precede each line after the first with a [line continuation](line-continuation.md) character (+), and delimit the text on each line with quotation marks.

-   A string value can consist of multiple text strings. For example, the following two GPD entries are equivalent:
    ```
    *Name: "abc""def" *% Comment
    +      "gh"    "ijk"

    *Name: "abcdefghijk"
    ```

For additional rules pertaining to strings defined in resource files, refer to the STRINGTABLE statement description in the Microsoft Windows SDK documentation.

For more information about specifying printer command escape sequences, see [Command String Format](command-string-format.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Text%20Strings%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


