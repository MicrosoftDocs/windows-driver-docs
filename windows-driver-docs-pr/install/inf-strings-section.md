---
title: INF Strings Section
description: An INF file must have at least one Strings section to define every strkey token specified elsewhere in that INF.
ms.assetid: 7352aa82-a7cd-4d15-9a9e-e03985f6006e
keywords:
- INF Strings Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF Strings Section
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF Strings Section


An INF file must have at least one **Strings** section to define every %*strkey*% token specified elsewhere in that INF.

```cpp
[Strings] | 
[Strings.LanguageID] ...
 
strkey1 = ["]some string["]
strkey2 = "    string-with-leading-or-trailing-whitespace     "  | 
          "very-long-multiline-string" | 
          "string-with-semicolon" | 
          "string-ending-in-backslash" |
          ""double-quoted-string-value""
 ...
```

## Entries


<a href="" id="strkey1--strkey2-----"></a>*strkey1*, *strkey2*, ...  
Each string key in an INF file must specify a unique name that consists of letters, digits, and/or other explicitly visible characters. A % character within such a *strkey* token must be expressed as **%%**.

<a href="" id="some-string----some-string-"></a>*some string* | **"**<em>some string</em>**"**  
Specifies a string, optionally delimited by using double quotation marks characters ("), that contains letters, digits, punctuation, and possibly even certain implicitly visible characters, in particular, internal space and/or tab characters. However, an unquoted string cannot contain an internal double quotation marks ("), semicolon (;), linefeed, return, or any invisible control characters, and it cannot have a backslash (\) as its final character.

<a href="" id="------string-with-leading-or-trailing-whitespace-----------"></a>**"***     string-with-leading-or-trailing-whitespace*     **"** |   

<a href="" id="-very-long-multiline-string----"></a>**"**<em>very-long-multiline-string</em>**"** |   

<a href="" id="-string-with-semicolon----"></a>**"**<em>string-with-semicolon</em>**"** |   

<a href="" id="-string-ending-in-backslash---"></a>**"**<em>string-ending-in-backslash</em>**"** |  

<a href="" id="--double-quoted-string-value--"></a>**"***"double-quoted-string-value"***"**  
The value specified for a %*strkey*% token *must* be enclosed in double quotation marks (") if it meets any of the following criteria:

-   If a specified string has leading or trailing white space that must be retained as part of its value, that string must be enclosed in double quotation marks characters to prevent its leading and/or trailing whitespaces from being discarded by the INF parser.
-   If a long string might contain any internal linefeed or return characters because of line wrapping in the text editor, it should also be enclosed in double quotation marks to prevent truncation of the string at the initial internal linefeed or return character.
-   If such a string contains a semicolon, it must be enclosed in double quotation marks to prevent the string from being truncated at the semicolon. (As already mentioned in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md), the semicolon character begins each comment in INF files.)
-   If such a string ends in a backslash, it must be enclosed in double quotation marks to prevent the string from being concatenated with the next entry. (As already mentioned in General Syntax Rules for INF Files, the backslash character (\) is used as the line continuator in INF files.)
-   Like an unquoted string specification, such a "quoted string" cannot contain internal double quotation marks characters. However, it can be specified as an explicitly double-quoted string value by using one or more additional pairs of double quotation marks characters (for example, ""some string"").

    The INF parser not only discards the outermost pair of enclosing double quotation marks for any "quoted string" in this section, but also condenses each subsequent sequential pair of double quotation marks into a single double quotation marks character.

    For example, """some string""" also becomes "some string" when it is parsed.

To summarize, any string must be enclosed in a pair of double quotation mark characters (") if any of the following is true:

-   The string contains leading or trailing white space.
-   The string is so long that it line wraps.
-   The string contains a semicolon or a final backslash character.
-   The string itself is a quoted string.

The system INF parser discards the outermost enclosing pair of double quotation marks characters delimiting such a string, along with any leading or trailing white space characters outside the double quotation marks string delimiters.

Remarks
-------

Because the system INF parser strips the outermost pair of enclosing double quotation marks from any **"**<em>quoted string</em>**"** defining a %*strkey*% token, many of the system INF files define all %*strkey*% tokens as **"**<em>quoted string</em><strong>"</strong>s to avoid the unintended loss of leading and trailing whitespaces during INF parsing. The use of **"**<em>quoted string</em><strong>"</strong>s also ensures that especially long string values that wrap across lines cannot be truncated, and that strings with ending backslashes cannot be concatenated to the next line in the INF file.

To create a single international INF file, an INF can have a set of locale-specific **Strings.**<em>LanguageID</em> sections, as shown in the formal syntax statement. The *LanguageID* extension is a hexadecimal value that is defined as follows:

-   The lower 10 bits contain the primary language ID and the next 6 bits contain the sublanguage ID, as specified by the MAKELANGID macro defined in *Winnt.h*.
-   The language and sublanguage IDs must match the system-defined values of the Win32 LANG_*XXX* and SUBLANG_*XXX* constants defined in *Winnt.h.*

For example, a *LanguageID* value of 0x0407 represents a primary language ID of LANG_GERMAN (07) with a sublanguage ID of SUBLANG_GERMAN (01).

An INF file can contain only one **Strings** section, along with one **Strings.**<em>LanguageID</em> section for each *LanguageID* value.

Windows selects a single **Strings** section that is used to translate all %*strkey*% tokens for the installation. Depending on the current locale of a particular computer, Windows selects a **Strings** section in the following way:

1.  Windows first looks for the *.LanguageID* values in the INF that match the current locale assigned to the computer. If an exact match is found, Windows uses that **Strings.LanguageID** INF section to translate all %*strkey*% tokens that are defined within the INF.
2.  Otherwise, Windows looks next for a match to the LANG_*XXX* value with the value of SUBLANG_NEUTRAL as the SUBLANG_*XXX*. If such a match is found, Windows uses that INF section to translate all %*strkey*% tokens that are defined within the INF.
3.  Otherwise, Windows looks next for a match to the LANG_*XXX* value and any valid SUBLANG_*XXX* for the same LANG_*XXX* family. If such a partial match is found, use that Strings.LanguageID INF section to translate all %*strkey*% tokens that are defined within the INF.
4.  Otherwise, Windows uses the undecorated Strings section to all translate %*strkey*% tokens that are defined within the INF.

By convention, and for convenience in creating a set of INF files for the international market, **Strings** sections are the last within all system INF files. Using %*strkey*% tokens for all user-visible string values within an INF, and placing them in per-locale **Strings** sections, simplifies the translation of such strings. For more information about locale-specific INF files, see [Creating International INF Files](creating-international-inf-files.md).

Although **Strings** sections are the last sections in every INF file, any specified %*strkey*% token defined in a **Strings** section can be used repeatedly elsewhere in the INF, in particular, wherever the translated value of that token is required. The [SetupAPI](setupapi.md) functions expand each %*strkey*% token to the specified string and then use that expanded value for further INF processing.

The use of %*strkey*% tokens within INF files is not restricted to user-visible string values. These tokens can be used in any manner convenient to the INF writer, as long as each token is defined within a **Strings** section. For example, when you write an INF file that requires the specification of several GUIDs, it might be convenient to create a %*strkey*% token for each GUID, by using a meaningful name as a substitute for each such GUID value.

Specifying a set of **%**<em>strkey</em>**% = "{**<em>GUID</em>**}"** values in the INF file's **Strings** section requires you to type each explicit GUID values only once. This can help provide more readable internal INF documentation than by using explicit GUID values throughout the INF file.

All %*strkey*% tokens must be defined within the INF file in which they are referenced. Therefore, for any INF file that has **Include** and **Needs** entries, an included INF must have its own **Strings** section to define all %*strkey*% tokens referenced in that INF.

In an INF **Strings** section, the maximum length, in characters, of a substitution string, including a terminating NULL character, is 4096 (Windows Vista and later versions of Windows) and 512 (Windows Server 2003, Windows XP, and Windows 2000). After string substitution, the maximum length, in characters, of an INF file string is 4096, including a terminating NULL character.

Examples
--------

The following example shows a fragment of a **Strings** section from a system-supplied locale-specific *dvd.inf* for installations in English-speaking countries/regions.

```cpp
[Strings]
Msft="Microsoft"
MfgToshiba="Toshiba"
Tosh404.DeviceDesc="Toshiba DVD decoder card"
; ... 
```

The following example shows string concatenation.

```cpp
[OEM Windows System Component Verification]
OID = 1.3.6.1.4.1.311.10.3.7    ; WHQL OEM OID 
Notice = "%A% %B% %C% %D% %E%" 
[Strings]
A = "This certificate is used to sign untested drivers that have not passed the Windows Hardware Quality Labs (WHQL) testing process."
B = "This certificate and drivers signed with this certificate are intended for use in test environments only, and are not intended for use in any other context."
C = "Vendors who distribute this certificate or drivers signed with this certificate outside a test environment may be in violation of their driver signing agreement."
D = "Vendors who have their drivers signed with this certificate do so at their own risk." 
E = "In particular, Microsoft assumes no liability for any damages that may result from the distribution of this certificate or drivers signed with this certificate outside the test environment described in a vendor&#39;s driver signing agreement."
```

## See also


[***DDInstall***](inf-ddinstall-section.md)

[***DDInstall*.CoInstallers**](inf-ddinstall-coinstallers-section.md)

[***DDInstall*.HW**](inf-ddinstall-hw-section.md)

[***DDInstall*.Interfaces**](inf-ddinstall-interfaces-section.md)

[***DDInstall*.Services**](inf-ddinstall-services-section.md)

[**Manufacturer**](inf-manufacturer-section.md)

[**InterfaceInstall32**](inf-interfaceinstall32-section.md)

[***Models***](inf-models-section.md)

[**SourceDisksNames**](inf-sourcedisksnames-section.md)

[**Version**](inf-version-section.md)

 

 






