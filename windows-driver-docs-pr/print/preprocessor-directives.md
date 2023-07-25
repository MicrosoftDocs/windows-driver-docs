---
title: Preprocessor directives
description: Preprocessor directives
keywords:
- GPD file entries WDK Unidrv , preprocessor directives
- preprocessor directives WDK GPD files
- parsing GPD file sections
- preprocessor symbols WDK GPD files
ms.date: 07/19/2023
---

# Preprocessor directives

[!include[Print Support Apps](../includes/print-support-apps.md)]

GPD files can contain preprocessor directives, which can be used to control conditional parsing of sections within the GPD file. The following table describes the preprocessor directives that can be used in GPD files.

| PreprocessorDirective | Definition |
|--|--|
| \***Define**: *SymbolName* | Defines a symbol. |
| \***Undefine**: *SymbolName* | Removes a previously defined symbol. |
| \***Ifdef**: *SymbolName* | Indicates the beginning of a block of GPD file entries.<br><br>If the specified symbol is defined, the GPD file entries between this directive and the next \***Ifdef****, \***Elseifdef**, \***Else**, or \***Endif** directive are processed by the GPD parser. |
| \***Elseifdef** : *SymbolName* | If the specified symbol is defined, and the symbol specified by the previous \***Ifdef** or \***Elseifdef** directive is undefined, the GPD file entries between this directive and the next \***Ifdef**, \***Elseifdef**,  \***Else**, or \***Endif** directive are processed by the GPD parser. |
| \***Else**: | If the symbol specified by the previous \***Ifdef** or \***Elseifdef** directive is undefined, the GPD file entries between this directive and the next \***Ifdef** or \***Endif** directive are processed by the GPD parser. |
| \***Endif**: | Indicates the end of a block of GPD file entries. |
| \***Include**: "*FileName*" | Specifies the name of an additional GPD file. For more information, see [Using Multiple GPD Files in a Minidriver](using-multiple-gpd-files-in-a-minidriver.md). |
| \***SetPPPrefix** : *PrefixString* | Changes the prefix string prepended to preprocessor directives. For more information, see the **Changing the Preprocessor Directive Prefix** section. |

Conditional preprocessor directives can be nested. At each nesting level, the sequence for using conditional preprocessor directives is as follows:

\***Ifdef**: *Symbol1* GPD file section

\***Elseifdef**: *Symbol2* GPD file section

\***Elseifdef**: *Symbol3* GPD file section

\***Elseifdef**: *Symbol4* GPD file section

...

\***Else**: GPD file section

\***Endif**:

For each \***Ifdef** directive used, \***Endif** is required. The \***Elseifdef** and \***Else** directives are optional. Each GPD file section can contain GPD file entries and, optionally, a nested sequence of conditional preprocessor directives.

All symbols defined using \***Define** remain defined until explicitly undefined using \***Undefine**.

The \***Include** directive allows you to specify the name of an additional GPD file. For more information, see [Using Multiple GPD Files in a Minidriver](using-multiple-gpd-files-in-a-minidriver.md).

Note that the \*IgnoreBlock GPD entry does not affect preprocessor directives, because the preprocessor executes before the GPD parser.

## Changing the Preprocessor Directive Prefix

The \***SetPPPrefix** directive allows you to change the prefix used with preprocessor directives. That is, you can use this directive to replace the asterisk (\*) character that prepends the preprocessor directives with another character or string.

For example, if your GPD file contains the following directive:

```GPD
*SetPPPrefix: #SpecialPrefix#
```

then the preprocessor stops searching for preprocessor directives that begin with **\*** and instead looks for directives beginning with **\#SpecialPrefix\#**. The following sequence temporarily changes the preprocessor prefix to **\#SpecialPrefix\#**, then restores it to **\***.

```GPD
*SetPPPrefix: #SpecialPrefix#
#SpecialPrefix#Ifdef: WINNT_50
#SpecialPrefix#Include: "ExtraGPD.gpd"
#SpecialPrefix#Endif:
#SpecialPrefix#SetPPPrefix: *
```

The primary purpose of this feature is to allow GPD files written for future operating system versions to be compatible with Windows 2000. For example, suppose GPD files for a future version of the operating system can include GPD file entries that conflict with the asterisk-prefixed preprocessor directives supported by Windows 2000. By changing the prefix, a GPD file written for the future operating system version can also be used with Windows 2000. An example might be constructed as follows:

```GPD
*Ifdef: WINNT_70
    *SetPPPrefix: #SpecialPrefix#
    *% Do special, OS-specific processing of
    *% GPD file entries that might conflict with
    *% asterisk-prefixed preprocessor directives.
    #SpecialPrefix#SetPPPrefix: *
*Endif:
```

Note that this technique only changes the prefix that the preprocessor looks for. Keywords recognized by the parser must always be preceded by an asterisk.

## Predefined Preprocessor Symbols

Microsoft defines the following preprocessor symbols.

| Symbol | Where Defined | Definition |
|--|--|--|
| WINNT_51 | GPD preprocessor for Windows XP | Environment is Windows XP. |
| WINNT_50 | GPD preprocessor for Windows XP and Windows 2000 | Environment is Windows 2000. |
| WINNT_40 | GPD preprocessors for Windows XP, Windows 2000, and Windows NT 4.0 | Environment is Windows NT 4.0. |
| PARSER_VER_1.0 | GPD preprocessors for Windows NT 4.0, Windows 2000, and Windows XP | GPD parser version 1.0 |

The WINNT_40, WINNT_50, and WINNT_51 symbols are useful for creating GPD files that are compatible with Windows NT 4.0, Windows 2000, and Windows XP. If, for example, Windows XP supports a printer capability that is not supported by Windows 2000, then that capability can be specified within a GPD file section that is bounded by \***Ifdef**: WINNT\_51 and \***Endif** directives.
