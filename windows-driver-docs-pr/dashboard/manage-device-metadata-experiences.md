---
title: Manage Device Metadata Experiences
description: Manage Device Metadata Experiences
MS-HAID:
- 'p\_dashboard.manage\_device\_metadata\_experiences'
- 'hw\_dashboard.manage\_device\_metadata\_experiences'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: aede9597-4b67-4c1a-8ae4-924d39c88b53
---

# Manage Device Metadata Experiences


After you've created and submitted your device metadata experiences, you can review or edit them through the dashboard.

## <span id="Managing_your_device_metadata_experiences"></span><span id="managing_your_device_metadata_experiences"></span><span id="MANAGING_YOUR_DEVICE_METADATA_EXPERIENCES"></span>Managing your device metadata experiences


On the **Manage experiences** page, you can add, remove, or promote (from preview to release) a device metadata package in a selected experience. You can also add packages for the same hardware IDs or model IDs into the same experience if the IDs are for different locales.

**To filter your device metadata experiences**

1.  Sign in to the **Dashboard** from either the Hardware Dev Center or the Windows Dev Center by using a Microsoft account.

2.  On the left side of the window, click **Device metadata**, and then click **Manage experiences**.

3.  All the experiences that you or your company created appear. Click the column headings to change the order of the list.

4.  Use the filter at the top of the list to display only the experiences that you want to see. Enter one or more of the following parameters:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Parameter</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Experience name</p></td>
    <td><p>From the list, select the name of the experience that you want to review or update.</p></td>
    </tr>
    <tr class="even">
    <td><p>Hardware ID(s)</p></td>
    <td><p>Enter the hardware ID(s) that you want to review, inserting a semicolon after each entry. This displays the experiences that contain the selected hardware ID(s).</p></td>
    </tr>
    <tr class="odd">
    <td><p>Device category</p></td>
    <td><p>From the list, select the device category that you want to review.</p></td>
    </tr>
    <tr class="even">
    <td><p>Model ID(s)</p></td>
    <td><p>Enter the model ID(s) that you want to review, inserting a semicolon after each entry. This displays the experiences that contain the selected model ID(s).</p></td>
    </tr>
    </tbody>
    </table>

     

**To open and view your device metadata experience**

1.  Click an experience to view the details.

2.  Under **Experience information**, review the information, which includes:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Element</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Experience type</p></td>
    <td><p>The type of packages in an experience, including metadata for:</p>
    <ul>
    <li><p>Devices and printers</p></li>
    <li><p>Device stage</p></li>
    </ul></td>
    </tr>
    <tr class="even">
    <td><p>Device category</p></td>
    <td><p>The device category of the packages in the experience.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Model ID(s)</p></td>
    <td><p>The model IDs defined in the packages in the experience.</p></td>
    </tr>
    <tr class="even">
    <td><p>Hardware ID(s)</p></td>
    <td><p>The hardware IDs defined in the packages in the experience.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Logo submission ID(s)</p></td>
    <td><p>The submission IDs bound to the experience.</p></td>
    </tr>
    </tbody>
    </table>

     

3.  Under **Metadata packages**, expand an individual package to view more details. You can also download a package that is live or ready to be published.

    **Note**  
    If a metadata package has an error, it will be displayed here.

     

4.  You can sort the list by clicking one of the following column headers:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Column header</th>
    <th>Description</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>Name</p></td>
    <td><p>The packages in the experience are listed according to their friendly name, if they have one, or by their file name.</p></td>
    </tr>
    <tr class="even">
    <td><p>Submission date</p></td>
    <td><p>This shows the date when you submitted each individual package.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Preview</p></td>
    <td><p>This check box is selected if the package is in preview and hasn't been released.</p></td>
    </tr>
    <tr class="even">
    <td><p>Locale</p></td>
    <td><p>This lists the country/region for which the package has been designed.</p></td>
    </tr>
    <tr class="odd">
    <td><p>Default</p></td>
    <td><p><strong>Yes</strong> indicates the package that you have designated as the default package.</p></td>
    </tr>
    <tr class="even">
    <td><p>Status</p></td>
    <td><p>This value indicates the current state of the selected package, and can be one of the following:</p>
    <ul>
    <li><p>Pending: The package has been uploaded and is being validated.</p></li>
    <li><p>To Be Published: The package has been validated and is waiting to be sent to the metadata servers. You can download a validated copy of your package, and it will be live and available to your users within 24 hours.</p></li>
    <li><p>Live: The package is now available for your users to download.</p></li>
    <li><p>Error: One or more errors were discovered during validation. Expand the section for more details.</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

     

**To modify your device metadata experience**

1.  To release a preview package, select the package, and then click **Release**.

    **Note**  
    It can take up to 48 hours for a released file to be available for users to download.

     

2.  To remove a package from the experience, select the package, and then click **Delete**.

    **Note**  
    You can only remove a package that is in the **Live** or **Error** state.

     

3.  To update an existing package, select the package, click **Delete**, and then create and upload a new package.

    For more information about creating a new package, see the [Device Metadata Authoring Wizard](http://go.microsoft.com/fwlink/p/?LinkID=265479), available in the [Windows Driver Kit](http://go.microsoft.com/fwlink/p/?LinkID=265477).

4.  To add a new package, under **Add more metadata**, browse for the file or files that you want to add, create a friendly name if you want, and then click **Submit**.

    **Note**  
    You can add a total of 50 packages to an experience.

     

## <span id="related_topics"></span>Related topics


[Create a Device Metadata Experience](https://msdn.microsoft.com/library/windows/hardware/br230794.aspx)

[Submit a Bulk Metadata Package](https://msdn.microsoft.com/library/windows/hardware/hh801895.aspx)

[Creating a Preview Package](https://msdn.microsoft.com/library/windows/hardware/br230780.aspx)

[Errors and Solutions When Submitting Device Metadata Experiences](https://msdn.microsoft.com/library/windows/hardware/br230786.aspx)

[Device Metadata Business Rules](https://msdn.microsoft.com/library/windows/hardware/br230767.aspx)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20Manage%20Device%20Metadata%20Experiences%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





