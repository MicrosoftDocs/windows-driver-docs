---
ms.assetid: 388C0D27-F3B9-4EF0-A03C-B58F38F2EFD6
title: Message Compiler Properties for Driver Projects
description: Sets the properties for the Message Compiler (MC.exe) tool.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Message Compiler Properties for Driver Projects

Sets the properties for the [**Message Compiler (MC.exe)**](https://msdn.microsoft.com/Library/Windows/Hardware/Aa385638) tool. The compiler generates the message resource files that you can add to your project.

For example, if you are using the [Event Tracing for Windows (ETW)](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545699) kernel-mode API to add event tracing to a kernel-mode driver, you could use the message compiler to create a header file that contains definitions for the event provider, event attributes, channels, and events. You must include this header file in your source code. The message compiler creates a resource compiler script (\*.rc) that you add to your project file.

## <span id="Setting_Message_Compiler_properties_for_driver_projects"></span><span id="setting_message_compiler_properties_for_driver_projects"></span><span id="SETTING_MESSAGE_COMPILER_PROPERTIES_FOR_DRIVER_PROJECTS"></span>Setting Message Compiler properties for driver projects


1.  Open the property pages for your driver project. Right-click the driver project in **Solution Explorer** and select **Properties**.
2.  In the property pages for the driver project, click **Configuration Properties** and then click **Message Compiler**.
3.  Set the properties for the project.

This property page is available if you add a message text file (.mc) or a manifest (.man) to your solution.

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
<td align="left"><p>Specifies additional options to pass to the <a href="https://msdn.microsoft.com/Library/Windows/Hardware/Aa385638" data-raw-source="[&lt;strong&gt;Message Compiler (MC.exe)&lt;/strong&gt;](https://msdn.microsoft.com/Library/Windows/Hardware/Aa385638)"><strong>Message Compiler (MC.exe)</strong></a> tool.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Ansi_Input_File"></span><span id="ansi_input_file"></span><span id="ANSI_INPUT_FILE"></span><strong>Ansi Input File</strong></p></td>
<td align="left"><p>Specifies that the input file contains ANSI content (this is the default). (<strong>-a</strong>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Ansi_Message_In_Bin_File"></span><span id="ansi_message_in_bin_file"></span><span id="ANSI_MESSAGE_IN_BIN_FILE"></span><strong>Ansi Message In Bin File</strong></p></td>
<td align="left"><p>Specifies that the messages in the output .bin file should be ANSI. (<strong>-A</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Baseline_Path"></span><span id="baseline_path"></span><span id="BASELINE_PATH"></span><strong>Baseline Path</strong></p></td>
<td align="left"><p>The path must point to the folder that contains the .BIN files that the baseline operation created. (<strong>-t</strong> <em>directory</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Baseline_Resource_Path"></span><span id="baseline_resource_path"></span><span id="BASELINE_RESOURCE_PATH"></span><strong>Baseline Resource Path</strong></p></td>
<td align="left"><p>The folder which contains the baseline manifest files. (<strong>-s</strong> <em>directory</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Debug_Output_Path"></span><span id="debug_output_path"></span><span id="DEBUG_OUTPUT_PATH"></span><strong>Debug Output Path</strong></p></td>
<td align="left"><p>The path in which to place the .dbg C include file. (<strong>-x</strong> <em>path</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Enable_Callout_Macro"></span><span id="enable_callout_macro"></span><span id="ENABLE_CALLOUT_MACRO"></span><strong>Enable Callout Macro</strong></p></td>
<td align="left"><p>Adds a callout macro to invoke user code at logging. Not available for C#, and ignored. (<strong>-co</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Enable_Debug_Output_Path"></span><span id="enable_debug_output_path"></span><span id="ENABLE_DEBUG_OUTPUT_PATH"></span><strong>Enable Debug Output Path</strong></p></td>
<td align="left"><p>Enables the compiler to place the .dbg C include file specified by the <strong>Debug Output Path</strong> property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="File_extension_for_the_generated_header"></span><span id="file_extension_for_the_generated_header"></span><span id="FILE_EXTENSION_FOR_THE_GENERATED_HEADER"></span><strong>File extension for the generated header</strong></p></td>
<td align="left"><p>Specifies the extension of the generated header file. (<strong>-e</strong> <em>extension</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generate_Baseline_Resource"></span><span id="generate_baseline_resource"></span><span id="GENERATE_BASELINE_RESOURCE"></span><strong>Generate Baseline Resource</strong></p></td>
<td align="left"><p>Creates a baseline of your instrumentation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generate_C___managed__logging_class"></span><span id="generate_c___managed__logging_class"></span><span id="GENERATE_C___MANAGED__LOGGING_CLASS"></span><strong>Generate C# (managed) logging class</strong></p></td>
<td align="left"><p>Generates a C# (managed) logging class that includes methods that you would call to log events in your manifest. (<strong>-cs</strong> <em>namespace</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generate_header_file_for_containing_counter_names_and_GUIDs"></span><span id="generate_header_file_for_containing_counter_names_and_guids"></span><span id="GENERATE_HEADER_FILE_FOR_CONTAINING_COUNTER_NAMES_AND_GUIDS"></span><strong>Generate header file for containing counter names and GUIDs</strong></p></td>
<td align="left"><p>Use this option to specify the folder into which you want the compiler to place the generated header file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generate_Kernel_Mode_Logging_Macros"></span><span id="generate_kernel_mode_logging_macros"></span><span id="GENERATE_KERNEL_MODE_LOGGING_MACROS"></span><strong>Generate Kernel Mode Logging Macros</strong></p></td>
<td align="left"><p>Generates kernel-mode logging macros. (<strong>-km</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generate_MOF_File"></span><span id="generate_mof_file"></span><span id="GENERATE_MOF_FILE"></span><strong>Generate MOF File</strong></p></td>
<td align="left"><p>Generate down-level support for all functions and macros generated. MOF file will be generated from the manifest. MOF file will be placed in the location specified by the <strong>-h</strong> option (<strong>-mof</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generate_OLE2_Header"></span><span id="generate_ole2_header"></span><span id="GENERATE_OLE2_HEADER"></span><strong>Generate OLE2 Header</strong></p></td>
<td align="left"><p>Generates an OLE2 header file. (<strong>-o</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generate_static_C___managed__logging_class"></span><span id="generate_static_c___managed__logging_class"></span><span id="GENERATE_STATIC_C___MANAGED__LOGGING_CLASS"></span><strong>Generate static C# (managed) logging class</strong></p></td>
<td align="left"><p>Generates a static C# (managed) logging class that includes methods that you would call to log events in your manifest. (<strong>-css</strong> <em>namespace</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generate_User_Mode_Logging_Macros"></span><span id="generate_user_mode_logging_macros"></span><span id="GENERATE_USER_MODE_LOGGING_MACROS"></span><strong>Generate User Mode Logging Macros</strong></p></td>
<td align="left"><p>Generate user-mode logging macros. (<strong>-um</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Generated_Files_Base_Name"></span><span id="generated_files_base_name"></span><span id="GENERATED_FILES_BASE_NAME"></span><strong>Generated Files Base Name</strong></p></td>
<td align="left"><p>Specifies the base name of all generated files. (<strong>-z</strong> <em>basename</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Generated_RC_and_Binary_Message_Files_Path"></span><span id="generated_rc_and_binary_message_files_path"></span><span id="GENERATED_RC_AND_BINARY_MESSAGE_FILES_PATH"></span><strong>Generated RC and Binary Message Files Path</strong></p></td>
<td align="left"><p>Specifies the path to the generated the RC and binary message files.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Header_File_Path"></span><span id="header_file_path"></span><span id="HEADER_FILE_PATH"></span><strong>Header File Path</strong></p></td>
<td align="left"><p>Specifies the path the generated header file. (<strong>-h</strong> <em>path</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Maximum_Message_Length"></span><span id="maximum_message_length"></span><span id="MAXIMUM_MESSAGE_LENGTH"></span><strong>Maximum Message Length</strong></p></td>
<td align="left"><p>Use this argument to have the compiler generate a warning if any message exceeds length characters. (<strong>-m</strong> <em>length</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Prefix_Macro_Name"></span><span id="prefix_macro_name"></span><span id="PREFIX_MACRO_NAME"></span><strong>Prefix Macro Name</strong></p></td>
<td align="left"><p>Use this argument to override the default prefix that the compiler uses for the logging macro names and method names. (<strong>-p</strong> <em>prefix</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="RC_File_Path"></span><span id="rc_file_path"></span><span id="RC_FILE_PATH"></span><strong>RC File Path</strong></p></td>
<td align="left"><p>The folder into which you want the compiler to place the generated resource compiler script (.rc file) and the generated .bin files. (<strong>-r</strong> <em>path</em>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Remove_Characters_From_Symbolic_Name"></span><span id="remove_characters_from_symbolic_name"></span><span id="REMOVE_CHARACTERS_FROM_SYMBOLIC_NAME"></span><strong>Remove Characters From Symbolic Name</strong></p></td>
<td align="left"><p>Use this argument to remove characters from the beginning of the symbolic name that you specified for the event. (<strong>-P</strong> <em>prefix</em>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Set_Customer_Bit"></span><span id="set_customer_bit"></span><span id="SET_CUSTOMER_BIT"></span><strong>Set Customer Bit</strong></p></td>
<td align="left"><p>Sets the Customer bit in the entire message Ids. (<strong>-c</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Terminate_Message_With_Null"></span><span id="terminate_message_with_null"></span><span id="TERMINATE_MESSAGE_WITH_NULL"></span><strong>Terminate Message With Null</strong></p></td>
<td align="left"><p>Terminates all strings with nulls in the message tables. (<strong>-n</strong>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Unicode_Input_File"></span><span id="unicode_input_file"></span><span id="UNICODE_INPUT_FILE"></span><strong>Unicode Input File</strong></p></td>
<td align="left"><p>Specifies that the input file contains Unicode content. (<strong>-u</strong>)</p>
<p>The default is ANSI.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Unicode_Message_In_Bin_File"></span><span id="unicode_message_in_bin_file"></span><span id="UNICODE_MESSAGE_IN_BIN_FILE"></span><strong>Unicode Message In Bin File</strong></p></td>
<td align="left"><p>Specifies that the messages in the output .bin file are Unicode. (<strong>-U</strong>)</p>
<p>This is the default.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Use_Base_Name_Of_Input"></span><span id="use_base_name_of_input"></span><span id="USE_BASE_NAME_OF_INPUT"></span><strong>Use Base Name Of Input</strong></p></td>
<td align="left"><p>Use this argument to have the compiler use the base name of the input file for the name of the output .bin files. (<strong>-b</strong>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Use_Decimal_Values"></span><span id="use_decimal_values"></span><span id="USE_DECIMAL_VALUES"></span><strong>Use Decimal Values</strong></p></td>
<td align="left"><p>Use this argument to use decimal values for the Severity and Facility constants in the header file instead of hexadecimal values. (<strong>-d</strong>)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Validate_Against_Baseline_Resource"></span><span id="validate_against_baseline_resource"></span><span id="VALIDATE_AGAINST_BASELINE_RESOURCE"></span><strong>Validate Against Baseline Resource</strong></p></td>
<td align="left"><p>Use this argument when you create a new version of your manifest and want to check it for application compatibility against the baseline that you created using the <strong>-s</strong> option.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="Verbose"></span><span id="verbose"></span><span id="VERBOSE"></span><strong>Verbose</strong></p></td>
<td align="left"><p>Use this option to generate verbose output. (<strong>-v</strong>)</p></td>
</tr>
</tbody>
</table>

 

## <span id="related_topics"></span>Related topics


* [Message Compiler (MC.exe)](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454227)
* [WDK and Visual Studio build environment](https://msdn.microsoft.com/Library/Windows/Hardware/Hh454286)
Message compiler task
* [Event Tracing for Windows (ETW)](https://msdn.microsoft.com/Library/Windows/Hardware/Ff545699)
 

 






