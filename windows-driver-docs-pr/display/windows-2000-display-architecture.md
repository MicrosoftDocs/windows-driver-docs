---
title: Windows 2000 Display Architecture
description: Windows 2000 Display Architecture
ms.assetid: c18e1464-13b7-4e55-b3e1-77aaf9270f60
keywords:
- VGA WDK Windows 2000 display
- display driver model WDK Windows 2000 , architecture
- Windows 2000 display driver model WDK , architecture
- architecture WDK Windows 2000 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Windows 2000 Display Architecture


## <span id="ddk_display_architecture_gg"></span><span id="DDK_DISPLAY_ARCHITECTURE_GG"></span>


The following figure shows the components required to display on Windows 2000 and later.

![diagram illustrating the windows 2000 and later display subsystem](images/dpy1.png)

The shaded elements in the preceding figure represent services that are supplied with Windows 2000 and later. The unshaded elements indicate that a third-party display driver and video miniport driver are required in order for a graphics adapter to display in the Windows 2000 and later systems.

For every type of graphics card that can be used with an NT-based operating system, there must be both a display driver and a corresponding video miniport driver. The miniport driver is written specifically for one graphics adapter (or family of adapters). The display driver can be written for any number of adapters that share a common drawing interface; for example, the VGA display driver can be used with either the VGA or ET4000 miniport driver. This is because the display driver draws, while the miniport driver performs operations such as mode sets and provides information about the hardware to the driver. It is also possible for more than one display driver to work with a particular miniport driver; for example, the 16- and 256-color SVGA display drivers can use the same miniport driver.

The following sections describe the key responsibilities of display and video miniport drivers. The breakdown in responsibilities is not hard and fast; the balance between modularity and performance is the key. For example, the hardware pointer code for the VGA driver resides in the miniport driver. This promotes modularity, so the same display driver can handle both the Video Seven VRAM, which has a hardware pointer, and the ET4000, which does not.

[Windows 2000 Display Driver Responsibilities](windows-2000-display-driver-responsibilities.md)

[Windows 2000 Video Miniport Driver Responsibilities](windows-2000-video-miniport-driver-responsibilities.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Windows%202000%20Display%20Architecture%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




