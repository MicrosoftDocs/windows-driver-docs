---
title: WindowsInfo XML Document
description: WindowsInfo XML Document
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WindowsInfo XML Document


This document contains data that specifies the display actions that the operating system performs for the specified device in the device metadata package. These actions include the following:

-   Whether the [device icon](device-icon-file.md) is displayed when the device is in a disconnected state, such as when the user removes the device. This action is specified by the [**ShowDeviceInDisconnectedState**](/previous-versions/windows/hardware/metadata/ff552242(v=vs.85)) XML element within the WindowsInfo XML document.

-   Whether a Device Stage user interface appears when the device transitions from a disconnected state to a connected state, such as when the user plugs in the device. This action is specified by the [**LaunchDeviceStageOnDeviceConnect**](/previous-versions/windows/hardware/metadata/ff548633(v=vs.85)) XML element within the WindowsInfo XML document.

-   Whether a Device Stage user interface is started when the user double-clicks the [device icon](device-icon-file.md) that appears in either the Devices and Printers user interface or in Windows Explorer. This action is specified by the [**LaunchDeviceStageFromExplorer**](/previous-versions/windows/hardware/metadata/ff548629(v=vs.85)) XML element within the WindowsInfo XML document.

Each device metadata package must contain only one WindowsInfo XML document. The name of the document must be *WindowsInfo.xml*.

The data in the WindowsInfo XML document is formatted based on the [WindowsInfo XML Schema](/previous-versions/windows/hardware/metadata/ff553992(v=vs.85)).

 

