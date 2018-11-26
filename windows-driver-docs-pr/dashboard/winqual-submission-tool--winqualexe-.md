---
title: Winqual Submission Tool (winqual.exe)
description: Winqual Submission Tool (winqual.exe)
ms.assetid: f7a34ee3-0532-465b-acb0-1ff80e2d4cb8
ms.topic: article
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Winqual Submission Tool (winqual.exe)


The Winqual Submission Tool (Winqual.exe) helps you to create a submission package for Microsoft Windows Hardware Certification. The tool collects information about the type of submission prepared, and gathers all the logs, drivers, and symbols required for submission.

In addition, the use of Winqual.exe is applicable only to WLK.

## Installing the Winqual submission tool


1.  Sign in to the dashboard with your Microsoft account.

2.  On the left navigation menu, click on **Drivers**. in the **Get the essentials** section, click **Winqual Submission Tool (WST)**.

3.  In the **File Download - Security Warning** dialog box, click **Run**.

4.  In the **Internet Explorer - Security Warning** dialog box, click **Run**.

5.  On the **Welcome** screen, click **Next**.

6.  On the **License Agreement** screen, select **I agree** and click **Next**.

7.  On the **Select Installation Folder** screen, click **Next**.

8.  On the **Confirm Installation** screen, click **Next**.

9.  Click **Close** to exit the installation process.

## <span id="How_to_use_WST"></span><span id="how_to_use_wst"></span><span id="HOW_TO_USE_WST"></span>How to use WST


To use the Windows Submission Tool (WST):

1.  When you open the tool, a **Welcome** screen appears. You can choose to not show this dialog box next time you open the tool by selecting **Don't show this message again**. To re-enable this dialog box, click **Tools**, click **Options**, and then select the **Show Welcome screen on startup** check box.

2.  The main screen appears, where test results and drivers can be added for creating the submission package.

3.  If a new version of WST is available, you'll receive a prompt to install the new version.

4.  If the version check fails, you'll receive a warning message, which can be disabled by selecting the **Don't show this message again** check box.

    **Note**  
    To re-enable this dialog box, click **Tools**, click **Options**, and then select the **Warn if update check fails** check box.

     

5.  Add the test results to the submission package, and choose to save the list for later use. An **.xml** file (which you'll use later for creating the submission) is created with all the submission information.

6.  You can save the file with a different file name by using the **Save As** menu item or toolbar button.

7.  Saved files are added to the **Recent Files** menu.

You can also perform the following additional actions in the WST:

-   You can start a new submission by clicking the **New** menu item or toolbar button.

-   A file saved earlier can be opened using the **Open** menu item or toolbar button. A file in **Recent Files** can also be opened by clicking the menu item.

-   Entries from the list can be removed individually by clicking the **Remove** button, or all at once by clicking **Remove All**.

-   An optional Read-me file (**.docx**, **.doc**, or **.txt**) file can be placed in the submission package.

## <span id="How_to_create_a_systems_submission_package"></span><span id="how_to_create_a_systems_submission_package"></span><span id="HOW_TO_CREATE_A_SYSTEMS_SUBMISSION_PACKAGE"></span>How to create a systems submission package


1.  On the main screen, click the **Add** button.

2.  Browse to the **.cpk** file (WLK test results) and click **Load**.

3.  After the test results are added, close the **Add DTM Results** dialog box to add the information to the main screen.

4.  The entries created can be edited by clicking the **Edit** button. This opens the **Edit DTM Results** dialog box with all of the information pre-populated.

5.  After all the entries have been added, you can create the submission package by clicking the **Create Submission** button.

6.  The tool can find errors while packaging. The packaging stops if an error is encountered. The entry with the error(s) will be highlighted in red. To view the errors again, click the **View Errors** button on the main window. Before the package can be created, all errors must be fixed. You can fix errors by editing the entry and updating the driver or the test result.

7.  After all of the errors are fixed, you can create a submission package. The submission package is created with the same name as the .xml file at the same location.

## <span id="How_to_create_a_device_submission_package"></span><span id="how_to_create_a_device_submission_package"></span><span id="HOW_TO_CREATE_A_DEVICE_SUBMISSION_PACKAGE"></span>How to create a device submission package


1.  On the main screen click the **Add** button.

2.  Browse to the **.cpk** file (WLK test results) and click **Load**.

3.  If the device is not inbox, you'll be asked to add a driver, locales, and (optional) symbols.

4.  After the test results are added, close the **Add DTM Results** dialog box to add the information to the main screen.

5.  The entries created can be edited by clicking the **Edit** button. This opens the **Edit DTM Results** dialog box with all of the information prepopulated.

6.  After all the entries have been added, you can create the submission package by clicking the **Create Package** button.

7.  The tool can find errors while packaging. The packaging stops if an error is encountered. The entry with the error(s) will be highlighted in red. To view the errors again, click the **View Errors** button on the main window. Before the package can be created, all errors must be fixed. You can fix errors by editing the entry and updating the driver or the test result.

8.  After all the errors are fixed, you can create a submission package. The submission package is created with the same name as the **.xml** file at the same location.

 

 





