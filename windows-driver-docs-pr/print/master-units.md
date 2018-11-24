---
title: Master Units
description: Master Units
ms.assetid: 6c3abf16-1206-4b90-a7e9-c8a581191502
keywords:
- GPD files WDK Unidrv , master units
- master units WDK GPD files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Master Units





Most printers support commands with a variety of horizontal and vertical resolutions. For example, the Immediate Line Feed command for a particular printer might provide a resolution of 1/288th of an inch, while the same printer might support a vertical graphics resolution of 1/96th of an inch. Likewise, this printer might also provide horizontal resolutions of 1/80th, 1/160th, and 1/320th of an inch.

Unidrv provides a single coordinate system to handle these various resolutions. The units in this coordinate system are called master units. A printer's master units are expressed as an (*x*, *y*) pair of values, where *x* is the master unit for the horizontal direction and *y* is the master unit for the vertical direction.

To determine a plane's master units, calculate the least common multiple (LCM) of the denominators for the actual resolutions. Using the example printer, you would do the following:

-   Calculate the LCM of 80, 160, and 320, which is 320. Thus, the horizontal master unit is 1/320th of an inch.

-   Calculate the LCM of 288 and 96, which is 576. Thus, the vertical master unit is 1/576th of an inch.

**Important**   Both of the master unit values and the vertical and horizontal resolutions should be a multiple of the number of pins in the print head (that is, the **PinsPerPhysPass** value). If this condition is not met, it is possible that extra blank lines will be produced for certain paper sizes.

 

To specify a printer's master units, use the \***MasterUnits** attribute. The attribute's format is as follows:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>*<strong>MasterUnits</strong>: PAIR ( <em>X_Denominator</em> , <em>Y_Denominator</em> )</p></td>
</tr>
</tbody>
</table>

 

where *X\_Denominator* is the LCM of the denominators for the horizontal resolutions, and *Y\_Denominator* is the LCM of the denominators for the vertical resolutions. The following GPD entry specifies the master units for the example:

```cpp
*MasterUnits: PAIR(320, 576)
```

Generally, position and size values used in GPD file entries must be specified in master units. For example, to specify that the maximum custom page size for our example printer is 9 inches by 12 inches, the following entry would be used, where 9x320=2880 and 12x576=6912:

```cpp
*MaxSize: PAIR(2880, 6912)
```

When calculating values for master units, use only the device resolutions that you want Unidrv to support. For example, if a printer supports horizontal resolutions of 1/80th, 1/96th, 1/160th, and 1/320th of an inch, but you do not intend to specify the 1/96th of an inch resolution within your GPD file, do not include it in your LCM calculation.

If your printer supports [cursor commands](cursor-commands.md) for moving the cursor position, then the values specified for the \***XMoveUnit** and \***YMoveUnit**[cursor attributes](cursor-attributes.md) must be included in master unit calculations. Suppose, for example, that a GPD file contains the following entries:

```cpp
*XMoveUnit: 60
*YMoveUnit: 60
```

When calculating this printer's master units, 1/60th of an inch must be included in the horizontal and vertical master unit calculations.

 

 




