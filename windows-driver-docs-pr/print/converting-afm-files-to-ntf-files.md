---
title: Converting AFM Files to NTF Files
author: windows-driver-content
description: Converting AFM Files to NTF Files
ms.assetid: 5c6c8843-c1b8-4cbd-81db-8a54cc377020
keywords: ["minidrivers WDK Pscript , converting AFM files", "NTF files", ".ntf files", ".afm files", "AFM files", "converting AFM files to NTF files", "Adobe Font Metrics WDK Pscript"]
---

# Converting AFM Files to NTF Files


## <a href="" id="ddk-converting-afm-files-to-ntf-files-gg"></a>


For Windows 2000 and later, Adobe Font Metrics ([*AFM*](https://msdn.microsoft.com/library/windows/hardware/ff556270#wdkgloss-adobe-font-metrics--afm-)) files must be converted to .ntf files. A command-line tool for performing this conversion, named makentf.exe, was provided with the Windows Driver Development Kit (DDK).

To convert one or more .afm files, use the following command syntax:

**makentf** {**-win32**|**-win64**} **** \[**-v**\] **** \[**-o**\] **** *NTF\_FileName***.ntf** *AFM\_FileNames*

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

```
makentf -win32 roman.ntf roman1.afm roman2.afm roman3.afm
makentf -win32 -o jpn.ntf jpn1.afm jpn2.afm jpn3.afm
```

If these files are used together, Western glyph set information will always be obtained from roman.ntf, so duplicating the information in jpn.ntf is not needed and consumes extra space. On the other hand, if jpn.ntf will be used alone, **-o** must not be specified.

A second command syntax is also supported, as follows:

**makentf** *filename*

where *filename* is the name of a file to receive output text. This syntax causes Makentf.exe to create a file containing lists of PostScript glyph names and Unicode values for each code page known to Makentf.exe.

An additional file, PSFamily.dat, is provided with the WDK and must reside in the same directory that contains Makentf.exe. This is a text file that supplies Makentf.exe with the display and family names for each font.

Before a standard .afm file can be converted, you must add a line similar to the following:

```
Comment UniqueID IDnumber
```

where *IDnumber* represents the font's unique identifier, issued by the font vendor.

When it is processing an East Asian font's .afm file, Makentf.txt requires some additional .map and .ps files, which must reside in the same directory as that of **-o** and PSFamily.dat. The additional .map and .ps files, which are provided in the WDK (together with PSFamily.dat), are necessary to create a mapping table from Unicode code to CID for the font. For more information, see [Converting East Asian AFM Files to NTF Files](converting-east-asian-afm-files-to-ntf-files.md).

An .afm file that will be converted to an .ntf file can contain the **FontBBox2** keyword. This keyword's arguments are similar to those for **FontBBox** (see the *Adobe Font Metrics File Format Specification*, from Adobe Systems, Inc.), except that **FontBBox2** arguments describe the bounding box for glyphs used in a specific character set (such as 90ms), while **FontBBox** arguments describe the bounding box for the union of all characters described in the .afm file. If **FontBBox2** is not found, the values specified for **FontBBox** are used for the bounding box.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Converting%20AFM%20Files%20to%20NTF%20Files%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


