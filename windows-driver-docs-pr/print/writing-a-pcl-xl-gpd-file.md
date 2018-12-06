---
title: Writing a PCL XL GPD File
description: Writing a PCL XL GPD File
ms.assetid: 35abc33a-a046-452b-b650-5c4f626bf6cb
keywords:
- PCL XL vector graphics WDK Unidrv , writing GPD files
- GPD files WDK Unidrv , PCL XL
- command ordering WDK PCL XL
- writing PCL XL GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing a PCL XL GPD File





This section provides general information about writing a PCL XL GPD file, such as which files your GPD file should include, how to enable PCL XL in your GPD file, and how to order PCL XL commands in a PCL XL stream.

The Windows Driver Kit (WDK) contains a sample PCL XL GPD file (p6sample.gpd) in the \\src\\print\\mini\\mdw\\vector\\pcl6 directory. (This resource may not be available in some languages and countries.)

### Files to Include

To write a GPD-based minidriver, use the preprocessor directive \*Include to specify the following GPD files:

pclxl.gpd -- contains macros for the PCL XL operators so that you can write GPD code that is easier to read and understand. For example, you can write =**BeginPage** instead of &lt;43&gt;.

p6disp.gpd -- contains macros for resource strings contained in pcl5eres.dll and pclxl.dll.

p6font.gpd -- contains macros for fonts contained in pclxl.dll.

pjl.gpd -- contains macros for PJL commands.

In addition to the preceding files, include the standard GPD files, stdnames.gpd and ttfsub.gpd.

The following example shows how these files would be included in a GPD file.

```cpp
*Include: stdnames.gpd
*Include: ttfsub.gpd
*Include: pclxl.gpd
*Include: p6disp.gpd
*Include: p6font.gpd
*Include: pjl.gpd
```

### Enabling PCL XL Support in the GPD File

To enable PCL XL vector support, you only need to set the \*Personality attribute. This is done in the following way:

```cpp
*Personality: = PERSONALITY_PCLXL
```

The PERSONALITY\_PCLXL constant is defined in stdnames.gpd.

A sample GPD file, p6sample.gpd, is included in the WDK to help developers create new PCL XL minidrivers.

### PCL XL Command Ordering

The order of the commands is more critical in PCL XL than in PCL-5. A small error in the PCL stream is not likely to affect the job, but PCL XL commands are valid only at certain points in the stream, so any error in PCL XL (PCL-6) causes an XL error page to be emitted. For example, you cannot send a BeginPage operator before you have sent a BeginSession operator.

A PCL XL stream has a form similar to the following. (The indentation shown is used only to emphasize the point that these operators come in pairs.)

```cpp
PJL commands
BeginSession
  OpenDataSource
    BeginPage
      <page data>
    EndPage
  CloseDataSource
EndSession
PJL commands
```

The PCL XL stream is preceded by and followed by PJL commands. The PCL XL stream itself begins with a BeginSession operator, and ends with an EndSession operator. Within that pair of operators, there is another pair of operators: OpenDataSource and CloseDataSource. Within that operator pair come one or more BeginPage/EndPage operator pairs, one pair for each page sent to the printer. The page data, which describes how an individual page is rendered, is bracketed by a BeginPage/EndPage operator pair.

For detailed information about all PCL XL operators, refer to the *PCL XL Feature Reference Protocol Class 2.0* documentation.

### Additional Information about PCL XL GPD Files

In PCL XL GPD files, the \*FontFormat attribute name, which specifies the way that fonts are downloaded, is restricted to two values: HPPCL\_OUTLINE and HPPCL\_RES. The first value indicates that Unidrv is to download TrueType outline data. The second value indicates that Unidrv is to download bitmap soft font data.

An IHV can lessen printer memory usage by limiting the number of fonts to be downloaded, or by limiting the number of characters to be downloaded in a given font. The \*MinFontID and \*MaxFontID attribute names are used to inform Unidrv to download soft fonts whose IDs lie within the range specified by these values. Similarly, the \*MinGlyphID and \*MaxGlyphID attribute names are used to limit the number of glyphs in a given font to download to those within a specific range.

Unidrv operates under the assumption that each GPD file contains its own dither matrix. It is also recommended that each device have its own dither matrix. The dither matrix is specified in a \*Feature: Dither [customized feature](customized-features.md).

 

 




