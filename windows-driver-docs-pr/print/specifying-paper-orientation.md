---
title: Specifying Paper Orientation
description: Specifying Paper Orientation
ms.assetid: 2d62e1ff-965b-4fd7-922c-319ec1bc39a5
keywords:
- Unidrv, paper orientation
- paper orientation WDK Unidrv
- PORTRAIT orientation WDK Unidrv
- LANDSCAPE_CC90 orientation WDK Unidrv
- LANDSCAPE_CC270 orientation WDK Unidrv
- landscape mode WDK Unidrv
- portrait mode WDK Unidrv
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Paper Orientation





There are three [standard options](standard-options.md) associated with the Orientation [standard feature](standard-features.md): PORTRAIT, LANDSCAPE\_CC90, and LANDSCAPE\_CC270. Unless otherwise specified, the default orientation is PORTRAIT. The use of this option is straightforward, and is not discussed further in this topic. The balance of this topic is concerned with the two landscape options.

### <a href="" id="landscape-cc90-and-landscape-cc270"></a>LANDSCAPE\_CC90 and LANDSCAPE\_CC270

The LANDSCAPE\_CC90 and LANDSCAPE\_CC270 options of the Orientation feature indicate the amount of rotation to be applied to text and graphics in portrait mode, to convert them to landscape mode. The LANDSCAPE\_CC90 option rotates text and graphics 90 degrees counterclockwise. The LANDSCAPE\_CC270 option rotates text and graphics 270 degrees counterclockwise, which is equivalent to a rotation by 90 degrees clockwise. For both options, Unidrv handles the tasks of rotating the text and graphics the indicated amount, and moving them as appropriate for the new orientation.

Many printers support both portrait mode and landscape mode, while the remaining printers, typically those with fewer features, support only portrait mode. Each mode has its own coordinate system: in portrait mode, the origin is at the upper left corner (x increases to the right and y increases downward); in landscape mode, the origin is at the lower left corner (x increases upward and y increases to the right).

Printers that do not support landscape mode can still be made to print documents in this orientation. For this type of printer, you must specify the LANDSCAPE\_CC270 option in the printer's GPD file. (If you specify the LANDSCAPE\_CC90 option for these printers, text and graphics will appear garbled when printed.) Under this option, Unidrv presents the transformed text and graphics to the printer with coordinates relative to the printer's upper-left-corner origin.

For a printer that supports landscape mode as well as portrait mode, you should specify the LANDSCAPE\_CC90 option in the GPD file. Under this option, Unidrv must be directed to issue a landscape command string to the printer, causing it to switch from the portrait mode coordinate system to the landscape mode coordinate system (with the origin at the lower left corner). Unidrv then presents the transformed text and graphics to the printer with coordinates relative to the printer's lower-left-corner origin.

However, a printer that supports landscape mode (for which the LANDSCAPE\_CC90 option ordinarily would be used), can still operate with the LANDSCAPE\_CC270 option. Under this option, Unidrv is directed to treat the printer as if it supported only portrait mode (that is, with only a single coordinate system, with the origin at the upper left corner). Consequently, Unidrv must not be directed to issue a command to change coordinate systems. Unidrv presents the transformed text and graphics to the printer with coordinates relative to this upper-left-corner origin. Because Unidrv assumes this location of the origin, such a printer must not be issued a landscape mode command string, even when the user has selected the Landscape orientation on the printer's property page. In the following GPD file example, notice that the \*Option: LANDSCAPE\_CC270 section contains a command to place the printer into portrait mode (ORIENT\_PORTRAIT\_CMD), and not one to place it into landscape mode.

```cpp
*Feature: Orientation
{
  *rcNameID: =ORIENTATION_DISPLAY
  *DefaultOption: PORTRAIT
  *Option: PORTRAIT
  {
    *rcNameID: =PORTRAIT_DISPLAY
    *Command: CmdSelect
    {
      *Order: DOC_SETUP.60
      *Cmd: =ORIENT_PORTRAIT_CMD
    }
  }
  *Option: LANDSCAPE_CC270
   {
     *rcNameID: =LANDSCAPE_DISPLAY
     *Command: CmdSelect
     {
       *Order: DOC_SETUP.60
       *Cmd: =ORIENT_PORTRAIT_CMD
     }
  }
}
```

**Note**   For Windows 7, the **MxdcGetPDEVAdjustment** function has new parameters for landscape rotation. For more information, see [**MxdcXDCGetPDEVAdjustment**](https://msdn.microsoft.com/library/windows/hardware/ff557558).

 

 

 




