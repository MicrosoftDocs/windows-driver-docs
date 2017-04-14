---
title: Marking Sources as Removable
description: Marking Sources as Removable
ms.assetid: 7fe48a4b-25d2-4e2c-9c26-a425928947ce
---

# Marking Sources as Removable


To prevent a display application from making a video present source the primary view, you should mark the source as removable. To indicate which sources are removable, you can specify a DWORD Plug and Play (PnP) value in the registry named **RemovableSources**.

**Note**   You cannot mark source 0 in the DWORD bit-field value as removable.

 

The n<sup>th</sup> bit in the bit-field value specifies whether source n-1 is removable. For example, to mark source 1 as removable, you can add the following line to a display miniport driver's INF file:

```
HKR,, RemovableSources, %REG_DWORD%, 2
...
```

For more information about installing display drivers, see [Installation Requirements for Display Miniport and User-Mode Display Drivers](installing-display-miniport-and-user-mode-display-drivers.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Marking%20Sources%20as%20Removable%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




