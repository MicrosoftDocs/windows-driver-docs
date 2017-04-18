---
title: USB Video Class Properties
author: windows-driver-content
description: .
ms.assetid: 6295926b-4ec5-42f5-98ca-a375d36f917b
keywords: ["USB Video Class drivers WDK AVStream , properties", "Video Class drivers WDK USB , properties", "UVC drivers WDK AVStream , properties", "property sets WDK USB Video Class"]
---

# USB Video Class Properties


Clients of the USB Video Class can use the following video capture property sets:

[PROPSETID\_VIDCAP\_CAMERACONTROL](https://msdn.microsoft.com/library/windows/hardware/ff567802)
[PROPSETID\_VIDCAP\_VIDEOPROCAMP](https://msdn.microsoft.com/library/windows/hardware/ff568122)
Clients of the USB Video Class can make requests on filters or individual nodes. The functionality of the node-based properties is identical to that of the pre-USB Video Class filter-based properties.

To specify a node-based property, set the KSPROPERTY\_TYPE\_TOPOLOGY flag in the Flags member of the [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure contained in the property descriptor structure—for example, [**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420).

Because clients can address multiple nodes on a single filter, the USB Video Class enables IHVs to support cameras that have multiple independently controlled lenses.

Additionally, a new property set has been defined:

[PROPSETID\_VIDCAP\_SELECTOR](https://msdn.microsoft.com/library/windows/hardware/ff567810)
The property items contained in PROPSETID\_VIDCAP\_SELECTOR are node-based.

Call [**KsSynchronousDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff567142) or **DeviceIoControl** to make property requests from a user-mode component. **DeviceIoControl** is documented in the Microsoft Windows SDK documentation.

Each of the property items contained in the four property sets above has a corresponding method in a DirectShow COM interface. For more information about the methods, see the DirectShow documentation in the Windows SDK.

USB Video Class devices can support some or all of the property sets listed above.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20USB%20Video%20Class%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


