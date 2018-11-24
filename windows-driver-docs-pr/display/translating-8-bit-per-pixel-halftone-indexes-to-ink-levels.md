---
title: Translating 8-Bit-Per-Pixel Halftone Indexes to Ink Levels
description: Translating 8-Bit-Per-Pixel Halftone Indexes to Ink Levels
ms.assetid: 5859b379-4e03-4cd8-836d-9a0b068b47c0
keywords:
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
- 8-bit-per-pixel CMY mask modes WDK GDI
- GenerateInkLevels
- INKLEVELS
- translating 8-bit-per-pixel halftone indexes WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Translating 8-Bit-Per-Pixel Halftone Indexes to Ink Levels


## <span id="ddk_translating_8_bit_per_pixel_halftone_indexes_to_ink_levels_gg"></span><span id="DDK_TRANSLATING_8_BIT_PER_PIXEL_HALFTONE_INDEXES_TO_INK_LEVELS_GG"></span>


The **GenerateInkLevels** function shown here provides an example of how to translate 8-bit-per-pixel halftone indexes to ink levels. These indexes are contained in CMY mode and CMY\_INVERTED mode palettes that GDI's [**HT\_Get8BPPMaskPalette**](https://msdn.microsoft.com/library/windows/hardware/ff567320) function returns in its *pPaletteEntry* parameter. **GenerateInkLevels** generates a 256-element array of INKLEVELS structures.

This function can be used to generate either a Windows 2000 CMY mode or a post-Windows 2000 CMY\_INVERTED mode translation table. This function can also be used to generate a Windows 2000 CMY mode CMY332 reverse-mapping index table. (CMY332 uses three bits each for cyan and magenta, and two bits for yellow.) When *CMYMask* value is in the range 3 to 255, the function's caller can use this table to map post-Windows 2000 CMY\_INVERTED indexes to Windows 2000 CMY indexes for currently existing drivers.

### <span id="inklevels_structure"></span><span id="INKLEVELS_STRUCTURE"></span>INKLEVELS Structure

```cpp
typedef struct _INKLEVELS {
   BYTE  Cyan;          // Cyan level from 0 to max
   BYTE  Magenta;       // Magenta level from 0 to max
   BYTE  Yellow;        // Yellow level from 0 to max
   BYTE  CMY332Idx;     // Original windows 2000 CMY332 Index
} INKLEVELS, *PINKLEVELS;
```

### <span id="example_generateinklevels_function"></span><span id="EXAMPLE_GENERATEINKLEVELS_FUNCTION"></span>Example GenerateInkLevels Function

The **GenerateInkLevels** function computes an 8-bit-per-pixel translation table of INKLEVELS structures, based on the values in the *CMYMask* and *CMYInverted parameters*. This function generates an INKLEVELS translation table for a valid *CMYMask* value in the range 0 to 255.

When this function is called, the *pInkLevels* parameter must point to a valid memory location of 256 INKLEVELS entries. If the function returns **TRUE**, then *pInkLevels* can be used to translate 8-bit-per-pixel indexes to ink levels, or to map to the older CMY332 indexes. If the function is called with *CMYMask* set to an invalid value (a value from 3 to 255 in which any of the cyan, magenta, or yellow levels is zero), the function returns **FALSE**.

```cpp
BOOL
GenerateInkLevels(
    PINKLEVELS  pInkLevels,  // Pointer to 256 INKLEVELS table
    BYTE        CMYMask,     // CMYMask mode
    BOOL        CMYInverted  // TRUE for CMY_INVERTED mode
    )

{
    PINKLEVELS  pILDup;
    PINKLEVELS  pILEnd;
    INKLEVELS   InkLevels;
    INT         Count;
    INT         IdxInc;
    INT         cC;  // Number of Cyan levels
    INT         cM;  // Number of Magenta levels
    INT         cY;  // Number of Yellow levels
    INT         xC;  // Max. number Cyan levels
    INT         xM;  // Max. number Magenta levels
    INT         xY;  // Max. number Yellow levels
    INT         iC;
    INT         iM;
    INT         iY;
    INT         mC;
    INT         mM;

    switch (CMYMask) {

    case 0:

        cC =
        cM =
        xC =
        xM = 0;
        cY =
        xY = 255;
        break;

    case 1:
    case 2:

        cC =
        cM =
        cY =
        xC =
        xM =
        xY = 3 + (INT)CMYMask;
        break;

    default:

        cC = (INT)((CMYMask >> 5) & 0x07);
        cM = (INT)((CMYMask >> 2) & 0x07);
        cY = (INT)( CMYMask       & 0x03);
        xC = 7;
        xM = 7;
        xY = 3;
        break;
    }   // end switch statement

    Count = (cC + 1) * (cM + 1) * (cY + 1);

    if ((Count < 1) || (Count > 256)) {
        return(FALSE);
    }

    InkLevels.Cyan      =
    InkLevels.Magenta   =
    InkLevels.Yellow    =
    InkLevels.CMY332Idx = 0;
    mC                  = (xM + 1) * (xY + 1);
    mM                  = xY + 1;
    pILDup              = NULL;
    if (CMYInverted) {

        //
        // Move the pInkLevels to the first entry following 
        // the centered embedded entries.
        // Skipped entries are set to white (zero). Because this 
        // is a CMY_INVERTED mode, entries start from back of the
        // table and move toward the beginning of the table.
        //

        pILEnd      = pInkLevels - 1;
        IdxInc      = ((256 - Count - (Count & 0x01)) / 2);
        pInkLevels += 255;

        while (IdxInc--) {

            *pInkLevels-- = InkLevels;
        }

        if (Count & 0x01) {

            //
            // If we have an odd number of entries, we need to
            // duplicate the center one for the XOR ROP to
            // operate correctly. pILDup will always be index
            // 127, and the duplicates are at indexes 127 and 128.
            //
            pILDup = pInkLevels - (Count / 2) - 1;
        }

        //
        // We are running from the end of table to the beginning,
        // because in CMY_INVERTED mode, index 0 is black and
        // index 255 is white. Since we generate only Count 
        // white, black, and colored indexes, and place them at
        // the center, we will change xC, xM, xY max. indexes 
        // to the same as cC, cM and cY
        // so we only compute cC*cM*cY entries.
        //

        IdxInc = -1;
        xC     = cC;
        xM     = cM;
        xY     = cY;

    } else {
        IdxInc = 1;
        pILEnd = pInkLevels + 256;
    }

    //
    // In the following composition of ink levels, the index
    // always runs from 0 ink level (white) to maximum ink 
    // levels (black).  With CMY_INVERTED mode, we compose ink
    // levels from index 255 to index 0 rather than from index 
    // 0 to 255.
    //

    if (CMYMask) {

        INT Idx332C;
        INT Idx332M;

        for (iC = 0, Idx332C = -mC; iC <= xC; iC++) {

            if (iC <= cC) {

                InkLevels.Cyan  = (BYTE)iC;
                Idx332C        += mC;
            }

            for (iM = 0, Idx332M = -mM; iM <= xM; iM++) {

                if (iM <= cM) {

                    InkLevels.Magenta  = (BYTE)iM;
                    Idx332M           += mM;
                }

                for (iY = 0; iY <= xY; iY++) {

                    if (iY <= cY) {

                        InkLevels.Yellow = (BYTE)iY;
                    }

                    InkLevels.CMY332Idx = (BYTE)(Idx332C + 
                                          Idx332M) +
                                          InkLevels.Yellow;
                    *pInkLevels         = InkLevels;

                    if ((pInkLevels += IdxInc) == pILDup) {

                        *pInkLevels  = InkLevels;
                        pInkLevels  += IdxInc;
                    }
                }
            }
        }

        //
        // Now, if we need to pad black at the other end of the
        // translation table, then do it here. Notice that
        // InkLevels are at cC, cM and cY here and CMY332Idx
        // is at black.
        //

        while (pInkLevels != pILEnd) {

            *pInkLevels  = InkLevels;
            pInkLevels  += IdxInc;
        }

    } else {

        //
        // Gray Scale case
        //

        for (iC = 0; iC < 256; iC++, pInkLevels += IdxInc) {

            pInkLevels->Cyan      =
            pInkLevels->Magenta   =
            pInkLevels->Yellow    =
            pInkLevels->CMY332Idx = (BYTE)iC;
        }
    }

    return(TRUE);
}
```

 

 





