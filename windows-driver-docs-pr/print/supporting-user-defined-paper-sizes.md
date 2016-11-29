---
title: Supporting User-Defined Paper Sizes
author: windows-driver-content
description: Supporting User-Defined Paper Sizes
MS-HAID:
- 'nt5gpd\_c4027b04-9e7f-4fb9-8990-e7546eb632e8.xml'
- 'print.supporting\_user\_defined\_paper\_sizes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f9c0b759-687e-4d92-80ce-330e30cbc41c
keywords: ["user-defined paper sizes WDK Unidrv", "customized paper sizes WDK Unidrv", "largest paper size WDK Unidrv", "margins WDK paper size"]
---

# Supporting User-Defined Paper Sizes


## <a href="" id="ddk-supporting-user-defined-paper-sizes-gg"></a>


User-defined paper sizes can be specific to a single print server and are typically customized for a specific application. Hence they are often called customized paper sizes. System administrators use the print folder to define customized paper sizes. If a printer can handle customized paper sizes, vendors must use the printer's GPD file to specify the acceptable range of sizes.

Two methods are provided for describing acceptable size ranges for customized paper:

-   You can specify size ranges explicitly.

-   You can specify size ranges relative to the printer's largest paper size.

### Specifying Paper Size Ranges Explicitly

To use this method, your GPD file's PaperSize feature must include an \*Option entry with a CUSTOMSIZE argument. This entry must contain the following option attributes:

\*MinSize
\*MaxSize
\*MaxPrintableWidth
\*MinLeftMargin
\*TopMargin
\*BottomMargin
\*CenterPrintable?
\*CursorOrigin
\*Command
You can use these GPD entries to create customized paper size descriptions only for printers having the following characteristics:

-   The printer supports commands to explicitly select customized paper sizes (typically by moving the cursor origin).

-   The cursor origin remains fixed, relative to the upper left-hand corner of the paper, for all customized paper sizes. (This is typically not true for landscape mode printing, or for printers that are center-fed or right-hand-fed.)

-   The top and bottom margins are independent of paper size.

-   If the paper width is less than the sum of the values specified for \***MinLeftMargin** and \***MaxPrintableWidth**, there is no right-hand margin. That is, the printer can print to the right edge of the paper.

Command parameters (specified in \***Command** entries) can be calculated at print time if [standard variable expressions](standard-variable-expressions.md) are used, typically including the PhysPaperLength and PhysPaperWidth variables. These variables represent the actual paper size requested for the print job, as specified by an application.

### Specifying Paper Size Ranges Relative to the Printer's Largest Paper Size

For printers that do not support the characteristics required for specifying customized paper size ranges explicitly, an alternate method is provided, which specifies paper sizes relative to the printer's largest paper size.

To use this method, your GPD file's PaperSize feature must include an \*Option entry with a CUSTOMSIZE argument. This entry must contain the following option attributes:

\*MinSize
\*MaxSize
\*MaxPrintableWidth
\*CustCursorOriginX
\*CustCursorOriginX
\*CustPrintableOriginX
\*CustPrintableOriginY
\*CustPrintableSizeX
\*CustPrintableSizeY
\*Command
When specifying a size range relative to the printer's largest paper size, use the following alignment rules:

-   For left-feed printers, the top and left margins of all paper sizes must be aligned.

-   For right-feed printers, the top and right margins of all paper sizes must be aligned.

-   For center-feed printers, the top margins and top center points of all paper sizes must be aligned.

The following steps are involved:

1.  Determine the following information for the printer's largest paper size:
    -   The command required to select the largest paper size.
    -   Values that would be used for the largest paper size's \*PageDimensions, \*CursorOrigin, \*PrintableOrigin, and \*PrintableArea GPD entries, as if they were going to be included in the GPD file. However, you will not actually place these entries in the file.

2.  Create formulas that specify or calculate the following information for each customized paper size, relative to the printer's largest paper size.
    -   The origin and size of each paper's printable area.
    -   The cursor origin for each paper.

The formulas for step 2 must be [CUSTOMSIZE parameter expressions](option-attributes-for-the-papersize-feature.md#ddk-customsize-parameter-expressions-gg), which are specified as values for the following GPD entries:

\*CustCursorOriginX
\*CustCursorOriginX
\*CustPrintableOriginX
\*CustPrintableOriginY
\*CustPrintableSizeX
\*CustPrintableSizeY
The CUSTOMSIZE option must also include a \*Command entry which specifies the command that selects the largest printer size. This command is sent for all custom paper sizes, and the formulas specified for the printable area and cursor origin control where the printer prints on the actual paper, whatever its size.

### Sample Calculations

As a simple example, assume your printer supports customized paper sizes that have margins of the same size as the largest paper size's margins. The steps involved are:

Determine values for the largest paper size's \***PageDimensions**, \***CursorOrigin**, \***PrintableOrigin**, and \***PrintableArea** entries. (Do not put these entries in the GPD file.)

Determine the width of each of the largest paper size's margins in terms of these values, as illustrated in the following pseudoexpressions:

LeftMarginWidth=\***PrintableOrigin**.x

RightMarginWidth=\***PageDimensions**.x-\***PrintableArea**.x-LeftMarginWidthTopMarginWidth=\***PrintableOrigin**.y
BottomMarginWidth=\***PageDimensions**.y-\***PrintableArea**.y-**TopMarginWidth**

In these pseudoexpressions, .x and .y represent the horizontal and vertical components of each entry's [pair](pairs.md) value. For landscape printing, use landscape values for \***PrintableArea** and \***PrintableOrigin**.

Now create pseudoexpressions that specify or calculate the printable areas for nonstandard paper sizes.

\*CustPrintableOriginX: %d{LeftMarginWidth}

\*CustPrintableOriginY: %d{TopMarginWidth}

\*CustPrintableSizeX: %d{PhysPaperWidth-LeftMarginWidth-RightMarginWidth}

\*CustPrintableSizeY: %d{PhysPaperLength-TopMarginWidth-BottomMarginWidth}

Notice use of the two standard variables, PhysPaperWidth and PhysPaperLength. At run time, these variables contain the length and width of the actual paper size that has been requested by an application.

Note that these pseudoexpressions are valid whether the paper is left-fed, right-fed, or center-fed.

Insert actual values, determined in step 1, into these expressions to create GPD entries. Examples might be:
```
*CustPrintableOriginX:  %d{300}
*CustPrintableOriginY:  %d{300}
*CustPrintableSizeX:   %d{PhysPaperWidth-600}
*CustPrintableSizeY:  %d{PhysPaperLength-600}
```

Create pseudoexpressions that calculate the cursor origin indexes. In the following pseudoexpressions, \*CursorOrigin.x and \*CursorOrigin.y are place holders for the horizontal and vertical components of the [pair](pairs.md) value for largest paper size's cursor origin.

For left-fed printers:

\*CustCursorOriginX: %d{\*CursorOrigin.x}
\*CustCursorOriginY: %d{\*CursorOrigin.y}
For right-fed printers:

\*CustCursorOriginX: %d{\*CursorOrigin.x+PhysPaperWidth-\*PageDimensions.x}
\*CustCursorOriginY: %d{\*CursorOrigin.y}
For center-fed printers:

\*CustCursorOriginX: %d{\*CursorOrigin.x+(PhysPaperWidth-PageDimensions.x)/2}
\*CustCursorOriginY: %d{\*CursorOrigin.y}
Insert actual values, determined in step 1, into these expressions to create GPD entries. Examples might be (for center-fed paper):
```
*CustCursorOriginX:  %d{((PhysPaperWidth-14040)/2)+300}
*CustCursorOriginY:   %d{180}
```

Specify values for the remaining three GPD entries--\*MinSize, \*MaxSize, and \*MaxPrintableWidth. The value specified for \*MaxPrintableWidth is not actually used for this method, but the parser requires the entry to exist, so its value can be set to 1.

### A Real Example

The following example GPD file segment describes acceptable customized paper sizes for a center-fed printer. For portrait mode, all margins for all custom paper sizes are 300 master units (1/4 inch) in size. For landscape mode, top and bottom margins are 240 master units while left and right margins are 200 master units.

```
*Option: CUSTOMSIZE
{
  *rcNameID: =USER_DEFINED_SIZE_DISPLAY
  *MinSize: PAIR(4200,9000)
  *MaxSize: PAIR(14040, 21240)
  *MaxPrintableWidth: 14040
  *MinLeftMargin: 100
  *CenterPrintable?: FALSE
  *PageProtectMem: 1692
  *InsertBlock: =PaperConstraints
  *switch: Orientation
  {
    *case: PORTRAIT
    {
       *CustCursorOriginX:  %d{((PhysPaperWidth-14040)/2)+300}
       *CustCursorOriginY:   %d{180}
       *CustPrintableOriginX:  %d{300}
       *CustPrintableOriginY:  %d{300}
       *CustPrintableSizeX:   %d{PhysPaperWidth-600}
       *CustPrintableSizeY:  %d{PhysPaperLength-600}
       *Command: CmdSelect
       {
         *Order: DOC_SETUP.13
 *Cmd: "<1B>&l101a8c1e99F<1B>*p0x0Y<1B>*c0t8064x12528Y"
 }
    }
    *case: LANDSCAPE_CC90
    {
      *switch:  Option20
      {
      *% The 8100 rotates the landscape job 180 degrees if a stapler
      *% is attached, so the staple can be placed in the top left
      *% corner of the document. The printer always rotates the
      *% landscape job, even if stapling is not selected.
        *case: 3KStapler
        {
          *CustCursorOriginX:  %d{((PhysPaperWidth-14040)/2)+200}
          *CustCursorOriginY:   %d{PhysPaperLength}
          *CustPrintableOriginX:  %d{200}
          *CustPrintableOriginY:  %d{240}
          *CustPrintableSizeX:   %d{PhysPaperWidth-400}
          *CustPrintableSizeY:  %d{PhysPaperLength-480}
          *Command: CmdSelect
          {
            *Order: DOC_SETUP.13
            *Cmd: "<1B>&l101a8c1e63F<1B>*p0x0Y<1B>*c0t12456x8184Y"
          }
        }
        *case: MBM5S
        {
          *CustCursorOriginX:  %d{((PhysPaperWidth-14040)/2)+200}
          *CustCursorOriginY:   %d{PhysPaperLength}
          *CustPrintableOriginX:  %d{200}
          *CustPrintableOriginY:  %d{240}
          *CustPrintableSizeX:   %d{PhysPaperWidth-400}
          *CustPrintableSizeY:  %d{PhysPaperLength-480}
          *Command: CmdSelect
          {
            *Order: DOC_SETUP.13
            *Cmd: "<1B>&l101a8c1e63F<1B>*p0x0Y<1B>*c0t12456x8184Y"
          }
        }
        *default
        {
          *CustCursorOriginX:  %d{((PhysPaperWidth-14040)/2)+200}
          *CustCursorOriginY:   %d{21000}
          *CustPrintableOriginX:  %d{200}
          *CustPrintableOriginY:  %d{240}
          *CustPrintableSizeX:   %d{PhysPaperWidth-400}
          *CustPrintableSizeY:  %d{PhysPaperLength-480}
          *Command: CmdSelect
          {
            *Order: DOC_SETUP.13
 *Cmd: "<1B>&l101a8c1e63F<1B>*p0x0Y<1B>*c0t12456x8184Y"
 }
        }
      } *% switch Option20
    } *% case LANDSCAPE_CC90
  } *% switch Orientation
}
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Supporting%20User-Defined%20Paper%20Sizes%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


