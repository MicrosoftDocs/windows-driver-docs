---
title: Debugging Device Metadata Packages by Using Problem Reports
description: Debugging device metadata packages by using problem reports
ms.date: 06/19/2025
ms.topic: how-to
---

# Debugging device metadata packages by using problem reports

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](windows-hardware/drivers/install/driver-package-container-metadata)**.

Starting with Windows 7, the operating system sends problem reports about device metadata package errors (error code 0x50000xx) to the Windows error report (WER) server. These reports provide useful debug information to help diagnose problems with your device metadata package.

For more information about the device metadata package errors, see [Device Metadata Error Codes](device-metadata-error-codes.md).

You can use either Action Center or Event Viewer to view the problem reports that the operating system has sent or will soon send to the Windows error report server.

## Viewing problem reports by using Action Center

Follow these steps to view device metadata package error reports by using Action Center:

1. On the **Start** menu, type "view all problem reports" and press ENTER.
1. Select a problem report that you want to review.

    The report contains detailed information for the error.

## Viewing error reports by using Event Viewer

You can view problem reports in Event Viewer. Follow these steps to view device metadata package problem reports by using Event Viewer:

1. On the **Start** menu, right-click **Computer**, and then click **Manage**.
1. Expand the **System Tools** node.
1. Expand and then click the **Event Viewer** node.
1. Expand the **Windows Logs** node.
1. Right-click **Application**, and then click **Filter Current Log**.
1. Type "1001" in the **Event ID** text box, and then click **OK**.

    The **Event ID** text box is the unlabeled text box in the middle of the dialog box that has the default contents of "&lt;All Event Ids&gt;".

## Interpreting a problem report

Every device metadata retrieval client problem report contains the following information:

- An application-specific error code. For more information about these error codes, see [Device Metadata Error Codes](device-metadata-error-codes.md).
- A Win32 error code.
- The source of the device metadata package, which is either the [device metadata store](device-metadata-store.md) or the [device metadata cache](device-metadata-cache.md).
- The name of the device metadata package.
