---
ms.assetid: 4444E8A5-9624-4CA2-84D8-C83A67A2C871
title: MOF Compiler Properties for Driver Projects
description: The Managed Object Format (MOF) compiler (mofcomp.exe) parses MOF files and adds classes and class instances defined in the files to the WMI repository.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MOF Compiler Properties for Driver Projects

The Managed Object Format (MOF) compiler (mofcomp.exe) parses MOF files and adds the classes and class instances defined in the files to the WMI repository. Use the Mofcomp property page to compile MOF files with your driver. For more information about Mofcomp.exe and WMI, see [**mofcomp**](https://msdn.microsoft.com/Library/Windows/Hardware/Aa392389), [Compiling MOF Files](https://msdn.microsoft.com/Library/Windows/Hardware/Aa389240), and [Compiling a Driver's MOF File](https://msdn.microsoft.com/Library/Windows/Hardware/Ff542012).

## <span id="Setting_Managed_Object_Format__MOF__Compiler_properties_for_driver_projects"></span><span id="setting_managed_object_format__mof__compiler_properties_for_driver_projects"></span><span id="SETTING_MANAGED_OBJECT_FORMAT__MOF__COMPILER_PROPERTIES_FOR_DRIVER_PROJECTS"></span>Setting Managed Object Format (MOF) Compiler properties for driver projects


1.  Open the property pages for your driver project. Right-click the driver project in **Solution Explorer** and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties** and then click **Mof Compiler**.
3.  Set the properties for the project.

This property page is available if you add a Managed Object Format (MOF) file (.mof) to your solution.

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
<td align="left"><p><span id="Additional_Options"></span><span id="additional_options"></span><span id="ADDITIONAL_OPTIONS"></span><strong>Additional Options</strong></p></td>
<td align="left"><p>Specifies additional options to pass to the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Aa392389" data-raw-source="[&lt;strong&gt;mofcomp&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Aa392389)"><strong>mofcomp</strong></a> tool.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Amendement"></span><span id="amendement"></span><span id="AMENDEMENT"></span><strong>Amendement</strong></p></td>
<td align="left"><p>Splits the MOF file into language-neutral and -specific versions. (<strong>-AMENDMENT:</strong><em>Locale</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Authority"></span><span id="authority"></span><span id="AUTHORITY"></span><strong>Authority</strong></p></td>
<td align="left"><p>Specifies Authority as the authority (domain name) to use when logging on to WMI. (<strong>-A:</strong><em>Authority</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Auto_Recover"></span><span id="auto_recover"></span><span id="AUTO_RECOVER"></span><strong>Auto Recover</strong></p></td>
<td align="left"><p>Adds the named MOF file to the list of files compiled during repository recovery. (<strong>-autorecover</strong>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Create_Binary_Mof_File"></span><span id="create_binary_mof_file"></span><span id="CREATE_BINARY_MOF_FILE"></span><strong>Create Binary Mof File</strong></p></td>
<td align="left"><p>Requests that the compiler create a binary version of the MOF file with the name filename without making any modifications to the WMI repository. (<strong>-B:</strong><em>Filename</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Language_Neutral_Output"></span><span id="language_neutral_output"></span><span id="LANGUAGE_NEUTRAL_OUTPUT"></span><strong>Language Neutral Output</strong></p></td>
<td align="left"><p>Name of the language neutral output. (<strong>-MOF:</strong><em>Path</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Language_Specific_Output"></span><span id="language_specific_output"></span><span id="LANGUAGE_SPECIFIC_OUTPUT"></span><strong>Language Specific Output</strong></p></td>
<td align="left"><p>Name of the language specific output. (<strong>-MFL:</strong><em>Path</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Mof_Class"></span><span id="mof_class"></span><span id="MOF_CLASS"></span><strong>Mof Class</strong></p></td>
<td align="left"><p>Creates or updates MOF classes.</p>
<p><strong>Create Only (-class:createonly)</strong> Requests that the compiler not make any changes to existing classes. When this switch is used, the compile operation terminates if a class specified in the MOF file already exists.</p>
<p><strong>Force Update (class:forceupdate)</strong> Forces updates of classes when conflicting child classes exist.</p>
<p><strong>Safe Update (-class:safeupdate)</strong> Allows updates of classes even if there are child classes, as long as the change does not cause conflicts with child classes.</p>
<p><strong>Update Only (-class:updateonly)</strong> Requests that the compiler not create any new classes.</p>
<p></p>
<p>See <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Aa392389" data-raw-source="[&lt;strong&gt;mofcomp&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Aa392389)"><strong>mofcomp</strong></a> for more information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="NamespacePath"></span><span id="namespacepath"></span><span id="NAMESPACEPATH"></span><strong>NamespacePath</strong></p></td>
<td align="left"><p>Requests that the compiler load the MOF file into the namespace specified as <em>namespacepath</em>. (<strong>-N:</strong><em>namespacepath</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Resource_Locale"></span><span id="resource_locale"></span><span id="RESOURCE_LOCALE"></span><strong>Resource Locale</strong></p></td>
<td align="left"><p>Extracts the localized MOF descriptions from the binary MOF when used with -ER switch. (<strong>-L:</strong><em>ResourceLocale</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Resource_Name"></span><span id="resource_name"></span><span id="RESOURCE_NAME"></span><strong>Resource Name</strong></p></td>
<td align="left"><p>Extracts binary MOF from a named resource. (<strong>-ER:</strong><em>ResourceName</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Syntax_Check"></span><span id="syntax_check"></span><span id="SYNTAX_CHECK"></span><strong>Syntax Check</strong></p></td>
<td align="left"><p>Requests that the compiler perform a syntax check only and print appropriate error messages. No other option can be used with the <strong>Syntax Check</strong> option.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="WMI_Syntax_Check"></span><span id="wmi_syntax_check"></span><span id="WMI_SYNTAX_CHECK"></span><strong>WMI Syntax Check</strong></p></td>
<td align="left"><p>Requests that the compiler perform a WMI syntax check <strong>-WMI</strong> . If you select this option, you must also select the <strong>Create Binary Mof File</strong> option (<strong>-B:</strong><em>Filename</em>)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


* [Compiling MOF Files](https://msdn.microsoft.com/Library/Windows/Hardware/Aa389240)
* [Compiling a Driver's MOF File](https://msdn.microsoft.com/Library/Windows/Hardware/Ff542012)
* [**mofcomp**](https://msdn.microsoft.com/Library/Windows/Hardware/Aa392389)
 

 






