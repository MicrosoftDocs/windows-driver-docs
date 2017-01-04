---
title: Winqual Submission Tool (winqual.exe)
description: Winqual Submission Tool (winqual.exe)
MS-HAID:
- 'p\_dashboard.winqual\_submission\_tool\_\_winqualexe\_'
- 'hw\_dashboard.winqual\_submission\_tool\_\_winqualexe\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f7a34ee3-0532-465b-acb0-1ff80e2d4cb8
---

# Winqual Submission Tool (winqual.exe)


The Winqual Submission Tool (Winqual.exe) helps you to create a submission package for Microsoft Windows Hardware Certification. The tool collects information about the type of submission prepared, and gathers all the logs, drivers, and symbols required for submission.

In addition, the use of Winqual.exe is applicable only to WLK.

## <span id="How_to_Install_Winqual_Submission_Tool"></span><span id="how_to_install_winqual_submission_tool"></span><span id="HOW_TO_INSTALL_WINQUAL_SUBMISSION_TOOL"></span>How to Install Winqual Submission Tool


1.  Sign in to the dashboard with your Microsoft account.

2.  Click **Hardware logo**, click **Downloads**, and then click **Winqual Submission Tool (WST)**.

3.  In the **File Download - Security Warning** dialog box, click **Run**.

4.  In the **Internet Explorer - Security Warning** dialog box, click **Run**.

5.  On the **Welcome** screen, click **Next**.

6.  On the **License Agreement** screen, select **I agree** and click **Next**.

7.  On the **Select Installation Folder** screen, click **Next**.

8.  On the **Confirm Installation** screen, click **Next**.

9.  Click **Close** to exit the installation process.

## <span id="How_to_use_WST"></span><span id="how_to_use_wst"></span><span id="HOW_TO_USE_WST"></span>How to use WST


To use the WST, follow these steps:

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Winqual%20Submission%20Tool%20%28winqual.exe%29%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




