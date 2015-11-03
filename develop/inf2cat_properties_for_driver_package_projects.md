Inf2Cat Properties for Driver Package Projects
========================================================================================================================

Sets the properties for the [**Inf2Cat**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089) tool. The **Inf2Cat** tool can be used to create catalog files for any driver package that has an INF file.

<span id="Setting_Inf2Cat_properties_for_driver_package_projects"></span><span id="setting_inf2cat_properties_for_driver_package_projects"></span><span id="SETTING_INF2CAT_PROPERTIES_FOR_DRIVER_PACKAGE_PROJECTS"></span>Setting Inf2Cat properties for driver package projects
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1.  Open the property pages for your driver package. Right-click the driver package project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver package, click **Configuration Properties** and then click **Inf2Cat**.
3.  Select the **Run Inf2Cat** option. This option runs the [**Inf2Cat**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089) tool on any INF files in the project (for example, .inf, .inx, or .inv files).

If the driver package is installed by using an INF file, use the Inf2Cat tool to create the catalog file. Inf2Cat validates that files referenced in the INF file are present in the package. To add files to the package, use the property pages for the package project and driver project. See [Creating a Driver Package](creating_a_driver_package.md) for more information.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="Run_Inf2Cat"></span><span id="run_inf2cat"></span><span id="RUN_INF2CAT"></span><strong>Run Inf2Cat</strong></p></td>
<td align="left"><p>Runs the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> tool on any INF files in the project (for example, .inf, .inx, or .inv files).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Windows_Version_List"></span><span id="windows_version_list"></span><span id="WINDOWS_VERSION_LIST"></span><strong>Windows Version List</strong></p></td>
<td align="left"><p>Specifies a list of Windows versions supported by the .inf file. Separate each Windows version with a comma. The default setting is $(Inf2CatWindowsVersionList), a macro that builds the driver for the active platform and configuration.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> option <strong>/os:</strong><em>WindowsVersionList</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Include_Page_Hashes"></span><span id="include_page_hashes"></span><span id="INCLUDE_PAGE_HASHES"></span><strong>Include Page Hashes</strong></p></td>
<td align="left"><p>Include page hashes with files. Optionally followed by a list of files.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> option <strong>/pageHashes[:</strong><em>file1</em><strong>][,</strong><em>file2</em><strong>]...]</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Add_PE_Attribute"></span><span id="add_pe_attribute"></span><span id="ADD_PE_ATTRIBUTE"></span><strong>Add PE Attribute</strong></p></td>
<td align="left"><p>Adds a PE catalog attribute to files. Optionally followed by a list of files.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> option <strong>/pe[:</strong><em>file1</em><strong>[,</strong><em>file2</em><strong>]...]</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Add_Drm"></span><span id="add_drm"></span><span id="ADD_DRM"></span><strong>Add Drm</strong></p></td>
<td align="left"><p>Adds a DRM-level catalog attribute to files. Optionally followed by a list of files.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> option <strong>/drm[:</strong><em>file1</em><strong>[,</strong><em>file2</em><strong>]...]</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Verbose"></span><span id="verbose"></span><span id="VERBOSE"></span><strong>Verbose</strong></p></td>
<td align="left"><p>Displays detailed information about tool output in the Visual Studio Output window.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> option <strong>/verbose</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="No_Catalog"></span><span id="no_catalog"></span><span id="NO_CATALOG"></span><strong>No Catalog</strong></p></td>
<td align="left"><p>Prevents the creation of any catalog files.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> option <strong>/nocat</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Use_Local_Time"></span><span id="use_local_time"></span><span id="USE_LOCAL_TIME"></span><strong>Use Local Time</strong></p></td>
<td align="left"><p>Use the local time zone while verifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547394"><strong>INF DriverVer Directive</strong></a> directive. By default UTC, is used.</p>
<p>This setting is equivalent to specifying the <a href="https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089"><strong>Inf2Cat</strong></a> option <strong>/uselocaltime</strong>.</p></td>
</tr>
</tbody>
</table>

 

For more information about the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff553618).

For information about property pages and projects, see the [WDK and Visual Studio build environment](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454286).

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Creating a Catalog File for a PnP Driver Package](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff540161)
* [**Inf2Cat**](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff547089)
* [Creating a Driver Package](creating_a_driver_package.md)
* [Signing a Driver](signing_a_driver.md)
* [Using Inf2Cat to Create a Catalog File](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff553618)
* [WDK and Visual Studio build environment](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh454286)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20Inf2Cat%20Properties%20for%20Driver%20Package%20Projects%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


