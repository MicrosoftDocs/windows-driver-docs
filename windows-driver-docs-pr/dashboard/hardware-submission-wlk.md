---
title: Create a new WLK hardware submission
description: Create a new WLK hardware submission
ms.topic: article
ms.date: 04/22/2022
---

# Create a WLK hardware submission package

For drivers compatible with Windows Server 2008 (and below) hardware for certification, you'll need to use the Winqual Submission Tool (WST), to create a submission package for Microsoft Windows Hardware Certification. The tool collects information about the type of submission prepared, and gathers all the logs, drivers, and symbols required for submission.

This article describes how to use WST to create your submission package and submit it to the Hardware dashboard.


## Prerequisites

* Make sure your [dashboard account](https://partner.microsoft.com/dashboard) is registered for the Windows Hardware Developer Program. For information on how to register, see [How to register for the Windows Hardware Developer Program](register-for-the-hardware-program.md).

* Download the[Windows Hardware Lab Kit (HLK)](https://docs.microsoft.com/windows-hardware/test/hlk/). Be sure to test your driver or drivers with the appropriate certification kit on each operating system that you want certification for. You'll need the WLK test results (.CPK file) for your driver that you want to submit for certification.

## Install the Winqual submission tool

1. Go to [Partner Center Hardware dashboard](https://partner.microsoft.com/dashboard/hardware/Search) and sign in using your credentials.

1. On the left menu, select **Drivers**.

1. Move through to the bottom of the page. In the **Get the essentials** section, select **Winqual Submission Tool (WST)**.

1. Follow the prompts to install WST.

## Create a systems or driver submission package

To create a systems or driver submission package:

1. In Windows search, enter "WST" to find the Windows Submission tool, and then select **Winqual Submission Tool**.

    :::image type="content" source="./images/winqual-submission-tool--winqualexe-/wst-windows-search.png" alt-text="Screenshot of Windows search result for 'WST'.":::

1. When you open the tool, a **Welcome** screen appears. Select **OK**.

1. If a new version of WST is available, you'll receive a prompt to install the new version. Select **OK**.

    :::image type="content" source="./images/winqual-submission-tool--winqualexe-/wst-update-prompt.png" alt-text="Screenshot of WST prompt to update the WST.":::

    >[!NOTE]
    >If the version check fails, you'll receive a warning message, which can be disabled by selecting the **Don't show this message again** check box.  To re-enable this dialog box, click **Tools**, click **Options**, and then select the **Warn if update check fails** check box.

1. To create a new submission, select **Submissions** on the top menu, and then select **New** .

1. Select **+ Add** to open the **Add DTM Results:** dialog.

    :::image type="content" source="./images/winqual-submission-tool--winqualexe-/wst-add-test-results.png" alt-text="Screenshot of WST showing how to add test results. 'Add' button is selected.":::

1. Select **Load** to add the .CPK file (WLK test results) to the submission package, and then select **OK**.

1. If the device isn't inbox, enter the **Driver Package, Driver Locales, and Symbols (optional)**.

    >[!NOTE]
    > The relative path plus filenames for your driver package must be less than 160 characters. Submissions will fail to process if this is exceeded.

1. (Optional) Select **Edit** to edit any entries.

1. Once you add the test results, an **WQReady.xml** file (which you'll use later for creating the submission) is created with all the submission information. To save the **WQReady.xml** file with a different file name, select **Submissions** on the top menu, and then select **Save As**.

>[!NOTE]
>Saved files are added to **Submissions > Recent Files** .

1. (Optional) Select **Browse...**, to add a README file (**.docx**, **.doc**, or **.txt**) to the submission package.

    :::image type="content" source="./images/winqual-submission-tool--winqualexe-/wst-add-readme.png" alt-text="Screenshot of WST showing how to add README file. 'Browse...' button is selected.":::

1. Select **> Create Package**.  The submission package is created with the same name as the .xml file at the same location.

1. If errors are encountered, entries with the errors will be highlighted in red. To view the errors again, select **View Errors**. Before the package can be created, all errors must be fixed. You can fix errors by editing the entry and updating the driver or the test result.

1. When all errors are fixed, you select **> Create Package**.

## Next Steps

> [!div class="nextstepaction"]
> [Create a new hardware submission in the Partner Center](create-a-new-hardware-submission.md)

> [!div class="nextstepaction"]
> [Managing hardware submissions in the Partner Center](manage-your-hardware-submissions.md)
 

 





