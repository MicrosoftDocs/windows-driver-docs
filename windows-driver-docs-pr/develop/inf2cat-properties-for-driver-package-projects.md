---
title: Inf2Cat Properties for Driver Package Projects
description: Sets the properties for the Inf2Cat tool. The Inf2Cat tool can be used to create catalog files for any driver package that has an INF file.
ms.date: 04/20/2017
---

# Inf2Cat Properties for Driver Package Projects

Sets the properties for the [**Inf2Cat**](../devtest/inf2cat.md) tool. The **Inf2Cat** tool can be used to create catalog files for any driver package that has an INF file.

## <span id="Setting_Inf2Cat_properties_for_driver_package_projects"></span><span id="setting_inf2cat_properties_for_driver_package_projects"></span><span id="SETTING_INF2CAT_PROPERTIES_FOR_DRIVER_PACKAGE_PROJECTS"></span>Setting Inf2Cat properties for driver package projects


1.  Open the property pages for your driver package. Select and hold (or right-click) the driver package project in Solution Explorer and select **Properties**.
2.  In the property pages for the driver package, select **Configuration Properties** and then select **Inf2Cat**.
3.  Select the **Run Inf2Cat** option. This option runs the [**Inf2Cat**](../devtest/inf2cat.md) tool on any INF files in the project (for example, .inf, .inx, or .inv files).

If the driver package is installed by using an INF file, use the Inf2Cat tool to create the catalog file. Inf2Cat validates that files referenced in the INF file are present in the package. To add files to the package, use the property pages for the package project and driver project. See [Creating a Driver Package](creating-a-driver-package.md) for more information.

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
<td align="left"><p>Runs the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> tool on any INF files in the project (for example, .inf, .inx, or .inv files).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Windows_Version_List"></span><span id="windows_version_list"></span><span id="WINDOWS_VERSION_LIST"></span><strong>Windows Version List</strong></p></td>
<td align="left"><p>Specifies a list of Windows versions supported by the .inf file. Separate each Windows version with a comma. The default setting is $(Inf2CatWindowsVersionList), a macro that builds the driver for the active platform and configuration.</p>
<p>This setting is equivalent to specifying the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> option <strong>/os:</strong><em>WindowsVersionList</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Include_Page_Hashes"></span><span id="include_page_hashes"></span><span id="INCLUDE_PAGE_HASHES"></span><strong>Include Page Hashes</strong></p></td>
<td align="left"><p>Include page hashes with files. Optionally followed by a list of files.</p>
<p>This setting is equivalent to specifying the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> option <strong>/pageHashes[:</strong><em>file1</em><strong>][,</strong><em>file2</em><strong>]...]</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Add_PE_Attribute"></span><span id="add_pe_attribute"></span><span id="ADD_PE_ATTRIBUTE"></span><strong>Add PE Attribute</strong></p></td>
<td align="left"><p>Adds a PE catalog attribute to files. Optionally followed by a list of files.</p>
<p>This setting is equivalent to specifying the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> option <strong>/pe[:</strong><em>file1</em><strong>[,</strong><em>file2</em><strong>]...]</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Add_Drm"></span><span id="add_drm"></span><span id="ADD_DRM"></span><strong>Add Drm</strong></p></td>
<td align="left"><p>Adds a DRM-level catalog attribute to files. Optionally followed by a list of files.</p>
<p>This setting is equivalent to specifying the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> option <strong>/drm[:</strong><em>file1</em><strong>[,</strong><em>file2</em><strong>]...]</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Verbose"></span><span id="verbose"></span><span id="VERBOSE"></span><strong>Verbose</strong></p></td>
<td align="left"><p>Displays detailed information about tool output in the Visual Studio Output window.</p>
<p>This setting is equivalent to specifying the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> option <strong>/verbose</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="No_Catalog"></span><span id="no_catalog"></span><span id="NO_CATALOG"></span><strong>No Catalog</strong></p></td>
<td align="left"><p>Prevents the creation of any catalog files.</p>
<p>This setting is equivalent to specifying the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> option <strong>/nocat</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Use_Local_Time"></span><span id="use_local_time"></span><span id="USE_LOCAL_TIME"></span><strong>Use Local Time</strong></p></td>
<td align="left"><p>Use the local time zone while verifying the <a href="/windows-hardware/drivers/install/inf-driverver-directive" data-raw-source="[&lt;strong&gt;INF DriverVer Directive&lt;/strong&gt;](../install/inf-driverver-directive.md)"><strong>INF DriverVer Directive</strong></a> directive. By default UTC, is used.</p>
<p>This setting is equivalent to specifying the <a href="/windows-hardware/drivers/devtest/inf2cat" data-raw-source="[&lt;strong&gt;Inf2Cat&lt;/strong&gt;](../devtest/inf2cat.md)"><strong>Inf2Cat</strong></a> option <strong>/uselocaltime</strong>.</p></td>
</tr>
</tbody>
</table>

 

For more information about the Inf2Cat tool, see [Using Inf2Cat to Create a Catalog File](../install/using-inf2cat-to-create-a-catalog-file.md).

For information about property pages and projects, see the [WDK and Visual Studio build environment](../devtest/wdk-and-visual-studio-build-environment.md).

## <span id="related_topics"></span>Related topics


* [Creating a Catalog File for a PnP Driver Package](../install/creating-a-catalog-file-for-a-pnp-driver-package.md)
* [**Inf2Cat**](../devtest/inf2cat.md)
* [Creating a Driver Package](creating-a-driver-package.md)
* [Signing a Driver](signing-a-driver.md)
* [Using Inf2Cat to Create a Catalog File](../install/using-inf2cat-to-create-a-catalog-file.md)
* [WDK and Visual Studio build environment](../devtest/wdk-and-visual-studio-build-environment.md)
