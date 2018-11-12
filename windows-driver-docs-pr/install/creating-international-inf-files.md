---
title: Creating International INF Files
description: Creating International INF Files
ms.assetid: 7c07c4de-4a0f-4555-b153-15307c76a2a3
keywords:
- INF files WDK device installations , international
- international INF files WDK
- locale-specific INF files WDK
- locale-specific driver files WDK
- Unicode INF files WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating International INF Files





Creating installations for international markets requires providing locale-specific INF files and, possibly, locale-specific driver files.

An INF file that will be used in an international market should use **%**<em>strkey</em>**%** tokens for all user-viewable text. The strings are defined in an INF **Strings** section, which is typically at the end of the INF file.

### Locale-Specific INF Files

You can create a single INF file that supports several locales, or you can create a separate INF file for each locale, by following these guidelines:

- To create a single international INF file, you should include a set of locale-specific **Strings.**<em>LanguageID</em> sections, as described in the reference page for the [**INF Strings section**](inf-strings-section.md). Use this technique if you intend to supply a single installation medium for all international markets.

  For installations on Windows 2000 and later versions of Windows, this is the recommended method for supporting international markets.

- To create a separate INF file for each locale, start with a main INF file that contains all the necessary sections and entries, except for the **Strings** section. Then create a second set of files, where each file contains just the **Strings** section for a supported locale. Concatenate the main file with each strings file to generate the locale-specific INF files.

  For installations on Windows 2000 and later versions of Windows, use this technique *only* if you intend to supply a separate installation medium for each international market. You cannot provide multiple versions of an INF file, for a particular operating system version, on a single installation medium because Windows cannot determine which INF file to use.

### Locale-Specific Versions of Driver Files

If you have to provide locale-specific versions of driver files for Windows 2000 and later versions of Windows, mark each version of each file with its locale. Be sure to mark files that are not locale-specific as language-neutral. You can do this by adding the following macro definition to your resource file:

```cpp
#define VER_LANGNEUTRAL
```

This definition must appear before the preprocessor directive that includes *common.ver*.

After compiling your files, you can verify that each is marked as language-neutral by doing the following:

1.  Right-click the file in Windows Explorer.

2.  Click **Properties**.

3.  Click the **Version** tab.

The **Language** selection in the **Other version information** pane contains a value that identifies the file as Language Neutral, or as intended for a specific locale.

Put the locale-specific files in separate, locale-specific subdirectories of the distribution medium, such as /*English* and /*German*. In your INF file, do the following:

-   Within the [**INF SourceDisksFiles section**](inf-sourcedisksfiles-section.md), specify locale-specific subdirectories by using a string key token such as **%LocaleSubDir%**.

-   Provide separate [**INF Strings sections**](inf-strings-section.md) for each language, and define the appropriate subdirectory name string in each section.

For example:

```cpp
[SourceDisksNames]
1=%DiskName%,,,%LocaleSubDir%

[SourceDisksFiles]
mysftwre.exe=1

[Strings]              ; No language ID implies English
DiskName="My Excellent Software"
LocaleSubDir="English"
[Strings.0407]         ; 0407 is the language ID for German
DiskName="Meine ausgezeichnete Software"
LocaleSubDir="German"
```

### Creating Unicode INF Files

If an INF file contains characters that fall outside the ASCII range (that is, outside the range of 0-127), the INF file should be in Unicode format. One way to create a Unicode INF file is to use an application such as Notepad to save it in Unicode format. If the INF is not in Unicode format, Windows uses the current locale to translate characters. If the INF file is in Unicode format, Windows uses the full Unicode character set.

Some applications, such as Notepad, allow you to create a Unicode file in either little-endian or big-endian format. Windows supports INF files that use either format.

 

 





