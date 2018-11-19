---
title: Halftone Algorithms
description: Halftone Algorithms
ms.assetid: 1831f952-4c83-4dfa-87e7-1c755f143227
keywords:
- HP-GL/2 monochrome WDK Unidrv , halftone algorithms
- PCL-5e WDK Unidrv , halftone algorithms
- halftoning WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Halftone Algorithms





Some printer vendors prefer to use different halftone algorithms while printing different kinds of objects, such as text, vector objects, and bitmaps. The three examples that follow show what should be added to the GPD to print each of these types of objects.

The first example shows how to incorporate halftone rendering while printing text.

```cpp
*Ifdef: WINNT_51
*Feature: TEXTHALFTONE
{
  *rcNameID: =TEXTHALFTONE_DISPLAY
  *DefaultOption: DETAIL
  *Option: DETAIL
   {
     *rcNameID: =DETAIL_HT_DISPLAY
     *Command: CmdSetTextHTAlgo { *Cmd : "<1B>*t0J" }
   }
  *Option: SMOOTH
   {
     *rcNameID: =SMOOTH_HT_DISPLAY
     *Name: "Smooth"
     *Command: CmdSetTextHTAlgo { *Cmd : "<1B>*t15J" }
   }
  *Option: BASIC
   {
     *rcNameID: =BASIC_HT_DISPLAY
     *Command: CmdSetTextHTAlgo { *Cmd : "<1B>*t18J" }
   }
}
*Endif:
```

The second example includes commands for halftone rendering while printing vector graphics.

```cpp
*Ifdef:  WINNT_51
*Feature: GRAPHICSHALFTONE
{
  *rcNameID: =GRAPHICSHALFTONE_DISPLAY
  *DefaultOption: SMOOTH
  *Option: DETAIL
   {
     *rcNameID: =DETAIL_HT_DISPLAY
     *Command: CmdSetGraphicsHTAlgo { *Cmd : "<1B>*t15J" }
   }
  *Option: SMOOTH
   {
     *rcNameID: =SMOOTH_HT_DISPLAY
     *Command: CmdSetGraphicsHTAlgo { *Cmd : "<1B>*t18J" }
   }
  *Option: BASIC
   {
     *rcNameID: =BASIC_HT_DISPLAY
     *Command: CmdSetGraphicsHTAlgo { *Cmd : "<1B>*t18J" }
   }
}
*Endif:
```

The third example includes commands for halftone rendering while printing bitmaps.

```cpp
*Ifdef: WINNT_51
*Feature: PHOTOHALFTONE
{
  *rcNameID: =PHOTOHALFTONE_DISPLAY
  *DefaultOption: SMOOTH
  *Option: DETAIL
   {
     *rcNameID: =DETAIL_HT_DISPLAY
     *Command: CmdSetPhotoHTAlgo { *Cmd : "<1B>*t15J" }
   }
  *Option: SMOOTH
   {
     *rcNameID: =SMOOTH_HT_DISPLAY
     *Command: CmdSetPhotoHTAlgo { *Cmd : "<1B>*t7J" }
   }
  *Option: BASIC
   {
     *rcNameID: =BASIC_HT_DISPLAY
     *Command: CmdSetPhotoHTAlgo { *Cmd : "<1B>*t3J" }
   }
}
*Endif:
```

 

 




