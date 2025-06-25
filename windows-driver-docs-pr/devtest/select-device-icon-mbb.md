---
title: Select Service Icon in the Mobile Broadband Metadata Authoring Wizard
description: Select service icon in the Mobile Broadband Metadata Authoring Wizard
keywords:
- Select service icon in the Mobile Broadband Metadata Authoring Wizard
ms.date: 06/25/2025
ms.topic: how-to
---

# Select service icon in the Mobile Broadband Metadata Authoring Wizard

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](../install/driver-package-container-metadata.md)**.

You must specify the icon to appear for your service in Windows Connection Manager. The icon appears next to your network entry when the mobile broadband adapter is registered to the home network provider. The icon isn't shown if the mobile broadband adapter is roaming.

Icons must have a transparent backgrounds and smooth edges. They must also meet the following format and size requirements:

- 256 x 256: 32-bit + Alpha
- 48 x 48: 32-bit + Alpha
- 48 x 48: 8-bit 256 color
- 48 x 48: 4-bit 16 color
- 32 x 32: 32-bit + Alpha
- 32 x 32: 8-bit 256 color
- 32 x 32: 4-bit 16 color
- 24 x 24: 32-bit + Alpha
- 24 x 24: 8-bit 256 color
- 24 x 24: 4-bit 16 color
- 16 x 16: 32-bit + Alpha
- 16 x 16: 8-bit 256 color
- 16 x 16: 4-bit 16 color

## To specify an icon for a service

1. Click the **Icon** tab.
1. Specify an icon for Windows Connection Manager.
    - Drop the icon file from your computer onto the black **Drop Service Icon Here** area. Or, click **Browse** and select the icon file. If you're running the device metadata authoring tool as an administrator, you must use the **Browse** button to select the icon file.
    - If you don't have an icon of your own, click **Next**. Windows assigns a generic icon based on the primary category that you specify in the **Categories** tab.
