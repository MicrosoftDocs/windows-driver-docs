---
title: WindowsInfo XML Document
description: WindowsInfo XML Document
ms.assetid: 8004d165-46c5-4bf4-849d-ba83205b9f54
---

# WindowsInfo XML Document


This document contains data that specifies the display actions that the operating system performs for the specified device in the device metadata package. These actions include the following:

-   Whether the [device icon](device-icon-file.md) is displayed when the device is in a disconnected state, such as when the user removes the device. This action is specified by the [**ShowDeviceInDisconnectedState**](https://msdn.microsoft.com/library/windows/hardware/ff552242) XML element within the WindowsInfo XML document.

-   Whether a Device Stage user interface appears when the device transitions from a disconnected state to a connected state, such as when the user plugs in the device. This action is specified by the [**LaunchDeviceStageOnDeviceConnect**](https://msdn.microsoft.com/library/windows/hardware/ff548633) XML element within the WindowsInfo XML document.

-   Whether a Device Stage user interface is started when the user double-clicks the [device icon](device-icon-file.md) that appears in either the Devices and Printers user interface or in Windows Explorer. This action is specified by the [**LaunchDeviceStageFromExplorer**](https://msdn.microsoft.com/library/windows/hardware/ff548629) XML element within the WindowsInfo XML document.

Each device metadata package must contain only one WindowsInfo XML document. The name of the document must be *WindowsInfo.xml*.

The data in the WindowsInfo XML document is formatted based on the [WindowsInfo XML Schema](https://msdn.microsoft.com/library/windows/hardware/ff553992).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20WindowsInfo%20XML%20Document%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




