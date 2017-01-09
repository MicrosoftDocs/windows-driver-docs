---
title: File a New Bug
description: File a New Bug
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f05df7f1-ab0c-46a8-ac75-16b68359c761
---

# File a New Bug


If you're using the Windows® bug management service to manage the bugs in your product, you can enter a new bug on the **Bug management** page on the Dashboard.

## <span id="Creating_and_filing_a_new_bug"></span><span id="creating_and_filing_a_new_bug"></span><span id="CREATING_AND_FILING_A_NEW_BUG"></span>Creating and filing a new bug


You can create a new bug online, and then submit it to be filed with Microsoft.

**To create and file a new bug**

1.  Sign in to the Dashboard by using your Microsoft account.

2.  On the left side of the window, click **Bug management**.

3.  On the **Bug management** page, in the **File a new bug** tile, click **File new bug**.

4.  On the **File new bug** page, enter details about the bug, making sure that you enter information in every field that has an asterisk. See the following table for more details about the required fields.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Field name</th>
    <th>Description of content</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Title</p></td>
    <td><p>Enter a title for your bug that is as descriptive as possible.</p></td>
    </tr>
    <tr class="even">
    <td><p>Issue type</p></td>
    <td><p>Select a category for the bug, such as Code Bug.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Assigned to</p></td>
    <td><p>Select <strong>Active</strong> or <strong>Microsoft</strong> to assign a bug to Microsoft. The default option is <strong>Active</strong>.</p></td>
    </tr>
    <tr class="even">
    <td><p>Partner Priority</p></td>
    <td><p>Select an option for how quickly the bug must be fixed. For example:</p>
    <p>0 - The issue is currently blocking any further development in this area without a workaround. It must be fixed immediately.</p>
    <p>1 - This issue is blocking in some areas and must be fixed as soon as possible.</p>
    <p>2 - Should fix soon before product release.</p>
    <p>3 - This issue should be fixed if there is time before the release.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Partner Severity</p></td>
    <td><p>Select a ranking for the severity of the bug. For example</p>
    <ul>
    <li><p>1- The issue causes a system crash or a loss of data.</p></li>
    <li><p>2- The issue causes major functionality or other problems, and in some cases, may cause a product failure.</p></li>
    <li><p>3- These are issues with impaired functionality.</p></li>
    <li><p>4- There are minor functionality issues that affect the fit-and-finish of the product.</p></li>
    </ul>
    <p>There is wording that may be unclear, or there are typographical errors that do not affect the use of the product.</p></td>
    </tr>
    <tr class="even">
    <td><p>Repro steps</p></td>
    <td><p>Describe the actions you had taken when the issue occurred.</p>
    <div class="alert">
    <strong>Note</strong>  
    <p>For the quickest response, make sure to include the following details:</p>
    <ul>
    <li><p>Expected results: Describe what you expected to happen after you completed the actions you performed.</p></li>
    <li><p>Actual results: Describe what actually happened. This is the main issue of the bug.</p></li>
    <li><p>The application or applications where the compatibility issue occurs.</p></li>
    <li><p>The application language or languages involved.</p></li>
    <li><p>If the application is downloadable, the URL where it is available.</p>
    <p>If the application is not downloadable, provide Microsoft with permission to share the application, or allow us to use it for reproduction and test purposes only.</p></li>
    </ul>
    </div>
    <div>
     
    </div></td>
    </tr>
    <tr class="odd">
    <td><p>Product family</p></td>
    <td><p>Describe the product family where the issue occurred. For example:</p>
    <ul>
    <li><p>Select Windows if it is a Client Operating System bug</p></li>
    <li><p>Select Windows Server/System Center if it a Server related bug</p></li>
    <li><p>Select Windows Legacy Servicing if it is a Servicing bug</p></li>
    </ul></td>
    </tr>
    <tr class="even">
    <td><p>Partner type</p></td>
    <td><p>Select the entry that best describes the space in which you want to file your bug.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Partner feature</p></td>
    <td><p>Select an appropriate feature area.</p></td>
    </tr>
    <tr class="even">
    <td><p>Partner description</p></td>
    <td><p>Enter a detailed description of the issue.</p></td>
    </tr>
    </tbody>
    </table>

     

5.  Click **Browse** below the Attachments label to attach a file to the bug. (Optional)

    Please include all files as appropriate so that Microsoft can analyze the issue quickly. For Windows deployment/setup issues, please attach the following files in zip format to speed up the diagnosis:

    ``` syntax
    %windir%\Panther\*.*
    %windir%\inf\setupap.dev.log
    %windir%\winsxs\popexec.log
    %windir%\inf\setupapi.dev.log
    %windir%\logs\cbs\cbs.log
    %windir%\windowsupdate.log
    %windir%\winsxs\pending*.xml
    %windir%\*.dmp (if BSOD issue)
    ```

    For Display/GPU-related issues please include:

    ``` syntax
    dxdiag log [start - dxdiag.exe - save all info]
    dispdiag log [run dispdiag.exe from command-prompt and send the .DAT file]
    ```

6.  When all information is complete, click **Save** at the top of the form.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20File%20a%20New%20Bug%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




