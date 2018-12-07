---
title: Converting AFM Files to NTF Files
description: Converting AFM Files to NTF Files
ms.assetid: 5c6c8843-c1b8-4cbd-81db-8a54cc377020
keywords:
- minidrivers WDK Pscript , converting AFM files
- NTF files
- .ntf files
- .afm files
- AFM files
- converting AFM files to NTF files
- Adobe Font Metrics WDK Pscript
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Converting AFM Files to NTF Files





For Windows 2000 and later, Adobe Font Metrics ([*AFM*](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-adobe-font-metrics--afm-)) files must be converted to .ntf files. A command-line tool for performing this conversion, named makentf.exe, was provided with the Windows Driver Development Kit (DDK).

To convert one or more .afm files, use the following command syntax:

**makentf** {**-win32**|**-win64**} **** \[**-v**\] **** \[**-o**\] **** <em>NTF\_FileName</em>**.ntf** *AFM\_FileNames*

where *NTF\_FileName* is the name of the .ntf file to be produced, and *AFM\_FileNames* is a set of one or more AFM files to be converted.

The following command-line options are supported:

<a href="" id="-win32"></a>**-win32**  
Create an NTF file for a Win32 driver. If this command-line option is specified, **-win64** cannot be specified.

<a href="" id="-win64"></a>**-win64**  
Create an NTF file for a Win64 driver. If this command-line option is specified, **-win32** cannot be specified.

<a href="" id="-v"></a>**-v**  
Verbose. This option creates a command output stream that contains a textual display of the NTF file structures being generated.

<a href="" id="-o"></a>**-o**  
Omit standard Western glyph sets. By default, Makentf.exe includes the standard Western glyph sets when generating an .ntf file. If you are creating multiple .ntf files, you only need to include the Western glyph sets in one of the files, as long as all the files will be used together. For example, suppose you are creating one .ntf file that contains Roman font metrics and another that contains Japanese font metrics. You might use the following commands:

```cpp
makentf -win32 roman.ntf roman1.afm roman2.afm roman3.afm
makentf -win32 -o jpn.ntf jpn1.afm jpn2.afm jpn3.afm
```

If these files are used together, Western glyph set information will always be obtained from roman.ntf, so duplicating the information in jpn.ntf is not needed and consumes extra space. On the other hand, if jpn.ntf will be used alone, **-o** must not be specified.

A second command syntax is also supported, as follows:

**makentf** *filename*

where *filename* is the name of a file to receive output text. This syntax causes Makentf.exe to create a file containing lists of PostScript glyph names and Unicode values for each code page known to Makentf.exe.

An additional file, PSFamily.dat, is provided with the WDK and must reside in the same directory that contains Makentf.exe. This is a text file that supplies Makentf.exe with the display and family names for each font.

Before a standard .afm file can be converted, you must add a line similar to the following:

```cpp
Comment UniqueID IDnumber
```

where *IDnumber* represents the font's unique identifier, issued by the font vendor.

When it is processing an East Asian font's .afm file, Makentf.txt requires some additional .map and .ps files, which must reside in the same directory as that of **-o** and PSFamily.dat. The additional .map and .ps files, which are provided in the WDK (together with PSFamily.dat), are necessary to create a mapping table from Unicode code to CID for the font. For more information, see [Converting East Asian AFM Files to NTF Files](converting-east-asian-afm-files-to-ntf-files.md).

An .afm file that will be converted to an .ntf file can contain the **FontBBox2** keyword. This keyword's arguments are similar to those for **FontBBox** (see the *Adobe Font Metrics File Format Specification*, from Adobe Systems, Inc.), except that **FontBBox2** arguments describe the bounding box for glyphs used in a specific character set (such as 90ms), while **FontBBox** arguments describe the bounding box for the union of all characters described in the .afm file. If **FontBBox2** is not found, the values specified for **FontBBox** are used for the bounding box.

 

 




