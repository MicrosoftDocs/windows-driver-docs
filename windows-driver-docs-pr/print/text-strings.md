---
title: Text Strings
description: Text Strings
ms.assetid: 773c977b-aac4-4c7c-8bab-aa2c69b2a89a
keywords:
- GPD file entries WDK Unidrv , text strings
- text strings WDK GPD files
- strings WDK GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Text Strings





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
    ```cpp
    *Name: "abc""def" *% Comment
    +      "gh"    "ijk"

    *Name: "abcdefghijk"
    ```

For additional rules pertaining to strings defined in resource files, refer to the STRINGTABLE statement description in the Microsoft Windows SDK documentation.

For more information about specifying printer command escape sequences, see [Command String Format](command-string-format.md).

 

 




