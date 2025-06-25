---
title: Review and Save Package in the Device Metadata Authoring Wizard
description: Review and save package in the Device Metadata Authoring Wizard
keywords:
- Review and save package in the Device Metadata Authoring Wizard
ms.date: 06/25/2025
ms.topic: how-to
---

# Review and save package in the Device Metadata Authoring Wizard

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](../install/driver-package-container-metadata.md)**.

After completing all of the tabs in the wizard, review and save your package.

## To review a package

1. Click the **Finish** tab.
1. Review all of the information that's listed under **Summary information**.
1. Make a note of the Experience ID. If you're creating a UWP device app, you need to include this ID in the in StoreManifest.xml, a file that must be included in the final UWP app submitted to the Microsoft Store.
1. If applicable, review any errors in red and fix them in the appropriate tabs.

## To save a package

1. Click the **Finish** tab.
1. Under **Save As**, confirm the package name next to **Windows 8 Package**.
1. Next to **Folder location**, confirm the location on your computer where you want to save package, or click **Change** to select a different location.
1. If you want to install and test the metadata package on your PC, select **Copy packages to your system's local metadata store**.
1. Click **Finish**.
