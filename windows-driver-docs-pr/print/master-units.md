---
title: Master Units
author: windows-driver-content
description: Master Units
ms.assetid: 6c3abf16-1206-4b90-a7e9-c8a581191502
keywords:
- GPD files WDK Unidrv , master units
- master units WDK GPD files
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Master Units


## <a href="" id="ddk-master-units-gg"></a>


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

```
*MasterUnits: PAIR(320, 576)
```

Generally, position and size values used in GPD file entries must be specified in master units. For example, to specify that the maximum custom page size for our example printer is 9 inches by 12 inches, the following entry would be used, where 9x320=2880 and 12x576=6912:

```
*MaxSize: PAIR(2880, 6912)
```

When calculating values for master units, use only the device resolutions that you want Unidrv to support. For example, if a printer supports horizontal resolutions of 1/80th, 1/96th, 1/160th, and 1/320th of an inch, but you do not intend to specify the 1/96th of an inch resolution within your GPD file, do not include it in your LCM calculation.

If your printer supports [cursor commands](cursor-commands.md) for moving the cursor position, then the values specified for the \***XMoveUnit** and \***YMoveUnit**[cursor attributes](cursor-attributes.md) must be included in master unit calculations. Suppose, for example, that a GPD file contains the following entries:

```
*XMoveUnit: 60
*YMoveUnit: 60
```

When calculating this printer's master units, 1/60th of an inch must be included in the horizontal and vertical master unit calculations.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Master%20Units%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


