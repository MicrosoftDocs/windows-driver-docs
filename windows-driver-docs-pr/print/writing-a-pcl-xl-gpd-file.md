---
title: Writing a PCL XL GPD File
author: windows-driver-content
description: Writing a PCL XL GPD File
MS-HAID:
- 'nt5gpd\_d4d0e598-7ab0-4874-9d8d-ada3cb35e7c5.xml'
- 'print.writing\_a\_pcl\_xl\_gpd\_file'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 35abc33a-a046-452b-b650-5c4f626bf6cb
keywords: ["PCL XL vector graphics WDK Unidrv , writing GPD files", "GPD files WDK Unidrv , PCL XL", "command ordering WDK PCL XL", "writing PCL XL GPD files"]
---

# Writing a PCL XL GPD File


## <a href="" id="ddk-writing-a-pcl-xl-gpd-file-gg"></a>


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

```
*Include: stdnames.gpd
*Include: ttfsub.gpd
*Include: pclxl.gpd
*Include: p6disp.gpd
*Include: p6font.gpd
*Include: pjl.gpd
```

### Enabling PCL XL Support in the GPD File

To enable PCL XL vector support, you only need to set the \*Personality attribute. This is done in the following way:

```
*Personality: = PERSONALITY_PCLXL
```

The PERSONALITY\_PCLXL constant is defined in stdnames.gpd.

A sample GPD file, p6sample.gpd, is included in the WDK to help developers create new PCL XL minidrivers.

### PCL XL Command Ordering

The order of the commands is more critical in PCL XL than in PCL-5. A small error in the PCL stream is not likely to affect the job, but PCL XL commands are valid only at certain points in the stream, so any error in PCL XL (PCL-6) causes an XL error page to be emitted. For example, you cannot send a BeginPage operator before you have sent a BeginSession operator.

A PCL XL stream has a form similar to the following. (The indentation shown is used only to emphasize the point that these operators come in pairs.)

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Writing%20a%20PCL%20XL%20GPD%20File%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


