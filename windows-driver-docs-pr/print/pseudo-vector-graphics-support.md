---
title: Pseudo-Vector Graphics Support
description: Pseudo-Vector Graphics Support
ms.assetid: 8eeba51b-00fa-4bf3-a78c-ac1d1adc9696
keywords:
- vector graphics WDK Unidrv , pseudovector graphics
- pseudovector graphics WDK Unidrv
- nonvector graphics devices WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pseudo-Vector Graphics Support





Devices that do not support true vector graphics can take advantage of the support that Unidrv provides for pseudovector graphics. When you use this feature, Unidrv downloads solid black rectangles and horizontal and vertical lines directly to a nonvector graphics device, reducing the overhead of rendering these figures on a raster surface. This also reduces the size of the output data, which can improve printer throughput for devices that do not handle raster data efficiently.

To benefit from this feature, a minidriver for a nonvector graphics device needs only to support the CmdRectBlackFill command. This functionality is disabled when the **Print Optimization** feature in the **Advanced** tab of the printer property pages is turned off.

The pseudovector graphics feature intercepts calls to [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180), [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316), and [**DrvLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff556245), to determine whether a solid black rectangle or a vertical or horizontal line is to be drawn. When Unidrv recognizes the figure to be drawn as a valid rectangle (one that is solid black, has no complex clipping, and does not use a ROP using the current destination bits), it is stored in a rectangle array instead of being drawn on the surface.

The most difficult aspect of the pseudovector graphics feature is avoiding z-order problems caused by objects that must be drawn on top of previously-drawn objects. The objects on top might need to erase or overwrite part of a black rectangle. If the black rectangle has already been downloaded to the device, an object drawn later on the system surface may not be drawn correctly.

The solution to this problem is to temporarily store a valid rectangle, rather than drawing it immediately on the surface. When a new object is to be drawn on the surface, Unidrv checks it to see whether the object overlaps with any black rectangle. If so, the overlapped portion of the black rectangle is drawn on the surface first, before the new object is drawn, thereby maintaining the correct z-ordering. Drawing the rectangle first also takes into account the possibility that the new object to be drawn might have a ROP associated with it, including one that interacts with the destination.

In addition, it is possible that the new object to be drawn contains complex clipping so that the resulting figure is no longer a rectangle. When the band or page rendering is complete, any remaining black rectangles can be directly downloaded to the device without causing any z-order problems. Unidrv maintains a list of up to 256 rectangles per band, concatenating BitBlt rectangles where possible.

### Pseudovector Graphics Issues

The pseudovector graphics feature may alter the z-ordering in certain situations, particularly when text is downloaded directly to the device and subsequent objects with complex clipping must interact with that text.

 

 




