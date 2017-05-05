---
title: Pseudo-Vector Graphics Support
author: windows-driver-content
description: Pseudo-Vector Graphics Support
ms.assetid: 8eeba51b-00fa-4bf3-a78c-ac1d1adc9696
keywords:
- vector graphics WDK Unidrv , pseudovector graphics
- pseudovector graphics WDK Unidrv
- nonvector graphics devices WDK Unidrv
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pseudo-Vector Graphics Support


## <a href="" id="ddk-pseudo-vector-graphics-support-gg"></a>


Devices that do not support true vector graphics can take advantage of the support that Unidrv provides for pseudovector graphics. When you use this feature, Unidrv downloads solid black rectangles and horizontal and vertical lines directly to a nonvector graphics device, reducing the overhead of rendering these figures on a raster surface. This also reduces the size of the output data, which can improve printer throughput for devices that do not handle raster data efficiently.

To benefit from this feature, a minidriver for a nonvector graphics device needs only to support the CmdRectBlackFill command. This functionality is disabled when the **Print Optimization** feature in the **Advanced** tab of the printer property pages is turned off.

The pseudovector graphics feature intercepts calls to [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180), [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316), and [**DrvLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff556245), to determine whether a solid black rectangle or a vertical or horizontal line is to be drawn. When Unidrv recognizes the figure to be drawn as a valid rectangle (one that is solid black, has no complex clipping, and does not use a ROP using the current destination bits), it is stored in a rectangle array instead of being drawn on the surface.

The most difficult aspect of the pseudovector graphics feature is avoiding z-order problems caused by objects that must be drawn on top of previously-drawn objects. The objects on top might need to erase or overwrite part of a black rectangle. If the black rectangle has already been downloaded to the device, an object drawn later on the system surface may not be drawn correctly.

The solution to this problem is to temporarily store a valid rectangle, rather than drawing it immediately on the surface. When a new object is to be drawn on the surface, Unidrv checks it to see whether the object overlaps with any black rectangle. If so, the overlapped portion of the black rectangle is drawn on the surface first, before the new object is drawn, thereby maintaining the correct z-ordering. Drawing the rectangle first also takes into account the possibility that the new object to be drawn might have a ROP associated with it, including one that interacts with the destination.

In addition, it is possible that the new object to be drawn contains complex clipping so that the resulting figure is no longer a rectangle. When the band or page rendering is complete, any remaining black rectangles can be directly downloaded to the device without causing any z-order problems. Unidrv maintains a list of up to 256 rectangles per band, concatenating BitBlt rectangles where possible.

### Pseudovector Graphics Issues

The pseudovector graphics feature may alter the z-ordering in certain situations, particularly when text is downloaded directly to the device and subsequent objects with complex clipping must interact with that text.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Pseudo-Vector%20Graphics%20Support%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


