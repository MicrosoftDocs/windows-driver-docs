---
title: Debugging Device Metadata Packages by Using Problem Reports
description: Debugging Device Metadata Packages by Using Problem Reports
ms.assetid: 303d1b08-1f1c-48ca-89a9-9087516fcd48
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging Device Metadata Packages by Using Problem Reports


Starting with Windows 7, the operating system sends problem reports about device metadata package errors (error code 0x50000xx) to the Windows Error Report (WER) server. These reports provide useful debug information to help diagnose problems with your device metadata package.

For more information about the device metadata package errors, see [Device Metadata Error Codes](device-metadata-error-codes.md).

You can use either Action Center or Event Viewer to view the problem reports that the operating system has sent or will soon send to the Windows Error Report Server.

### <a href="" id="viewing-error-reports-through-problem-reports-and-solution"></a>Viewing problem reports by using Action Center

Follow these steps to view device metadata package error reports by using Action Center:

1.  On the **Start** menu, type "view all problem reports" and press ENTER.

2.  Select a problem report that you want to review.

    The report contains detailed information for the error.

### <a href="" id="viewing-error-reports-through-event-viewer"></a>Viewing error reports by using Event Viewer

You can view problem reports in Event Viewer. Follow these steps to view device metadata package problem reports by using Event Viewer:

1.  On the **Start** menu, right-click **Computer**, and then click **Manage**.

2.  Expand the **System Tools** node.

3.  Expand and then click the **Event Viewer** node.

4.  Expand the **Windows Logs** node.

5.  Right-click **Application**, and then click **Filter Current Log**.

6.  Type "1001" in the **Event ID** text box, and then click **OK**.

    The **Event ID** text box is the unlabeled text box in the middle of the dialog box that has the default contents of "&lt;All Event Ids&gt;".

### <a href="" id="interpreting-the-problem-report"></a>Interpreting a problem report

Every Device Metadata Retrieval Client problem report contains the following information:

-   An application-specific error code. For more information about these error codes, see [Device Metadata Error Codes](device-metadata-error-codes.md).

-   A Win32 error code.

-   The source of the device metadata package, which is either the [device metadata store](device-metadata-store.md) or the [device metadata cache](device-metadata-cache.md).

-   The name of the device metadata package.

 

 





