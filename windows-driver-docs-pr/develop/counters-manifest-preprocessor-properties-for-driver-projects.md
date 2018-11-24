---
ms.assetid: 216E5337-0B05-4560-92AF-0D7AB90EAEEB
title: Counters Manifest Preprocessor Properties for Driver Projects
description: Sets the properties for the CTRPP tool that parses and validates your counters manifest.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Counters Manifest Preprocessor Properties for Driver Projects

Sets the properties for the [CTRPP](https://msdn.microsoft.com/library/windows/desktop/aa372128) tool that parses and validates your counters manifest. For information about working with performance counters, see [Performance Counters](https://msdn.microsoft.com/Library/Windows/Desktop/aa373083). For information about using performance counters in a kernel-mode Windows driver, see [Kernel Mode Performance Monitoring](https://msdn.microsoft.com/Library/Windows/Hardware/Ff548159).

## <span id="Setting_the_Counters_Manifest_Preprocessor_properties_for_driver_projects"></span><span id="setting_the_counters_manifest_preprocessor_properties_for_driver_projects"></span><span id="SETTING_THE_COUNTERS_MANIFEST_PREPROCESSOR_PROPERTIES_FOR_DRIVER_PROJECTS"></span>Setting the Counters Manifest Preprocessor properties for driver projects


1.  Open the property pages for your driver project. Right-click the driver project in **Solution Explorer** and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties** and then click **Counters Manifest Preprocessor Properties**.
3.  Set the properties for the project.

If you want to add this property page to your project so that you can run the CTRPP tool during the build process, see the [WDK and Visual Studio build environment](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454286) and the [Ctrpp task](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454206).

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
<td align="left"><p><span id="Add_Prefix"></span><span id="add_prefix"></span><span id="ADD_PREFIX"></span>Add Prefix</p></td>
<td align="left"><p>Specifies the prefix to use for the global variables and functions defined in the generated header file (same as the <strong>-prefix</strong> command option.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Additional_Options"></span><span id="additional_options"></span><span id="ADDITIONAL_OPTIONS"></span>Additional Options</p></td>
<td align="left"><p>Specifies additional options to the <a href="https://msdn.microsoft.com/Library/Windows/Desktop/aa372128" data-raw-source="[&lt;strong&gt;CTRPP&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Desktop/aa372128)"><strong>CTRPP</strong></a> tool.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Backward_Compatibility"></span><span id="backward_compatibility"></span><span id="BACKWARD_COMPATIBILITY"></span>Backward Compatibility</p></td>
<td align="left"><p>Generates code that is binary compatible with versions of Windows prior to Windows 7 (same as the <strong>-backcompat</strong> command option).</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Enable_Legacy"></span><span id="enable_legacy"></span><span id="ENABLE_LEGACY"></span>Enable Legacy</p></td>
<td align="left"><p>Reverts to generating code using Windows Vista code templates. This option causes <a href="https://msdn.microsoft.com/Library/Windows/Desktop/aa372128" data-raw-source="[&lt;strong&gt;CTRPP&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Desktop/aa372128)"><strong>CTRPP</strong></a> to generate four output files: two header files (.h, _r.h), a resource file (.rc), and a source code file (c). (<strong>-legacy</strong>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generate_header_file_for_containing_counter_names_and_GUIDs"></span><span id="generate_header_file_for_containing_counter_names_and_guids"></span><span id="GENERATE_HEADER_FILE_FOR_CONTAINING_COUNTER_NAMES_AND_GUIDS"></span>Generate header file for containing counter names and GUIDs</p></td>
<td align="left"><p>Creates a header file that assigns symbols to the counter set names and GUIDs for each counter set in the manifest.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generate_header_file_for_provider"></span><span id="generate_header_file_for_provider"></span><span id="GENERATE_HEADER_FILE_FOR_PROVIDER"></span>Generate header file for provider</p></td>
<td align="left"><p>Specifies the name of the header file that the tool generates. If you do not specify a path, the file is generated in the current folder.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generate_Memory_Routines"></span><span id="generate_memory_routines"></span><span id="GENERATE_MEMORY_ROUTINES"></span>Generate Memory Routines</p></td>
<td align="left"><p>Generate memory allocation/free routine templates. (<strong>-MemoryRoutines</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generate_Notification_Callback"></span><span id="generate_notification_callback"></span><span id="GENERATE_NOTIFICATION_CALLBACK"></span>Generate Notification Callback</p></td>
<td align="left"><p>Generate customized notification callback template. (<strong>-NotificationCallback</strong> )</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generate_resource_file"></span><span id="generate_resource_file"></span><span id="GENERATE_RESOURCE_FILE"></span>Generate resource file</p></td>
<td align="left"><p>Specifies the name of the resource file that the tool generates. If you do not specify a path, the file is generated in the current folder.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generate_Summary_Global_File"></span><span id="generate_summary_global_file"></span><span id="GENERATE_SUMMARY_GLOBAL_FILE"></span>Generate Summary Global File</p></td>
<td align="left"><p>Generates a binary counter file per provider. (<strong>-summary</strong> <em>path</em>)</p>
<p>Generates a summary global file GenSumResource.BIN.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generated_Counter_Files_Path"></span><span id="generated_counter_files_path"></span><span id="GENERATED_COUNTER_FILES_PATH"></span>Generated Counter Files Path</p></td>
<td align="left"><p>Specifies the path to generate binary counter files. (<strong>-sumPath</strong> <em>path</em>)</p>
<p>If no path is specified, the current directory is used.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Header_File_Name_For_Counter"></span><span id="header_file_name_for_counter"></span><span id="HEADER_FILE_NAME_FOR_COUNTER"></span>Header File Name For Counter</p></td>
<td align="left"><p>Generates a header file for containing counter names and ids. (<strong>-ch</strong> <em>filename</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Header_FileName_For_Provider"></span><span id="header_filename_for_provider"></span><span id="HEADER_FILENAME_FOR_PROVIDER"></span>Header FileName For Provider</p></td>
<td align="left"><p>Generates a header file for the provider. It replaces the default name. (<strong>-o</strong> <em>filename</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Resource_File_Name"></span><span id="resource_file_name"></span><span id="RESOURCE_FILE_NAME"></span>Resource File Name</p></td>
<td align="left"><p>Specifies the name for the resource file. This replaces the default name. (<strong>-rc</strong> <em>filename</em>)</p></td>
</tr>
</tbody>
</table>

 

## <span id="Comment"></span><span id="comment"></span><span id="COMMENT"></span>Comment


The default names of the files that the tool generates are based on the name of the manifest file that you pass to the [**CTRPP**](https://msdn.microsoft.com/Library/Windows/Desktop/aa372128) tool.

## <span id="related_topics"></span>Related topics


* [**CTRPP**](https://msdn.microsoft.com/Library/Windows/Desktop/aa372128)
* [Performance Counters](https://msdn.microsoft.com/Library/Windows/Desktop/aa373083)
* [Kernel Mode Performance Monitoring](https://msdn.microsoft.com/Library/Windows/Hardware/Ff548159)
 

 






