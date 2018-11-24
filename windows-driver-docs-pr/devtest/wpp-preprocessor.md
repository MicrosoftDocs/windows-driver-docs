---
title: WPP Preprocessor
description: WPP Preprocessor
ms.assetid: 92bcb2c4-f6de-4704-8f5c-9a2e5901616a
keywords:
- Windows software trace preprocessor WDK , options
- WPP software tracing WDK , options
- WPP preprocessor WDK
- Windows software trace preprocessor WDK , invoking preprocessor
- WPP software tracing WDK , invoking preprocessor
- Windows software trace preprocessor WDK , build process
- WPP software tracing WDK , build process
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WPP Preprocessor


This section describes the *Windows Software Trace Preprocessor*, commonly known as the WPP preprocessor.

## <span id="invoking_the_wpp_preprocessor"></span><span id="INVOKING_THE_WPP_PREPROCESSOR"></span> Invoking the WPP Preprocessor


You can invoke the WPP preprocessor using Visual Studio and the MSBuild environment.

**To invoke the WPP preprocessor**

1.  Right-click the driver project in Solutions Explorer and click **Properties.**
2.  In the project property page, click **Configuration Properties** and click **WPP Tracing**
3.  Under **General**, set the **Run WPP** option to **Yes**.
4.  Under **Command Line**, you can add options below to customize tracing behavior.

    For example, under **WPP Tracing**, you can specify a single **Scan Configuration Data** file.

    If you need to provide more than one configuration file, for instance to specify custom data types, reference your file in **Command Line** using the **-scan** option, for example:

    ```
    -scan:"$(KMDF_INC_PATH)\$(KMDF_VER_PATH)\WdfTraceEnums.h"
    ```

For more information about the build process, see [TraceWPP task](tracewpp-task.md) and [WDK and Visual Studio build environment](wdk-and-visual-studio-build-environment.md).

You can also run the preprocessor separate from the build environment by using the TraceWPP tool (TraceWPP.exe). This tool is located in the bin/x86 subdirectory of the WDK.

## <span id="WPP_Tracing_General_Options"></span><span id="wpp_tracing_general_options"></span><span id="WPP_TRACING_GENERAL_OPTIONS"></span>WPP Tracing General Options


The following tables describe the options for the WPP preprocessor. You can configure these options in Visual Studio using the WPP Tracing property page for your project, or as parameters to the TraceWPP tool.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WPP Tracing Option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run WPP</p></td>
<td align="left"><p>If true, invokes WPP.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Enable Minimal Rebuild</p></td>
<td align="left"><p>If true, a tracked incremental build is performed; if false, a rebuild is performed.</p></td>
</tr>
</tbody>
</table>

 

## <span id="run_wpp_options"></span><span id="RUN_WPP_OPTIONS"></span>


## <span id="Function_and_Macro_Options"></span><span id="function_and_macro_options"></span><span id="FUNCTION_AND_MACRO_OPTIONS"></span>Function and Macro Options


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WPP Tracing Option</th>
<th align="left">TraceWPP command option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Preprocessor Definitions</p></td>
<td align="left"><p><strong>-D</strong><em>Macro</em></p></td>
<td align="left"><p>Adds <strong>#define</strong> <em>Macro</em> to the beginning of the generated file where <em>Macro</em> is the name of a macro.</p>
<p>This option has the same effect as the <strong>/D</strong> (define a macro) compiler option. It is included to ensure that defines are valid at the start of the TMH files.</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p><strong>-D</strong><em>Macro</em><strong>=</strong><em>Expansion</em></p></td>
<td align="left"><p>Adds <strong>#define</strong> <em>Macro Expansion</em> to the beginning of the generated file where <em>Macro</em> is the name of a macro and <em>Expansion</em> is the expanded value.</p>
<p>This option has the same effect as the <strong>/D</strong> (define a macro) compiler option. It is included to ensure that defines are valid at the start of the TMH files.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Trace Kernel-Mode Components</p></td>
<td align="left"><p><strong>-km</strong></p></td>
<td align="left"><p>Defines the WPP_KERNEL_MODE macro, which traces kernel-mode components. By default, only user-mode components are traced.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Enable Dll Macro</p></td>
<td align="left"><p><strong>-dll</strong></p></td>
<td align="left"><p>Defines the WPP_DLL macro, which causes the WPP data structures to be initialized whenever WPP_INIT_TRACING is called. Otherwise, the structures are initialized only once.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Specify Control GUID</p></td>
<td align="left"><p><strong>-ctl:</strong> <em>GUID</em></p></td>
<td align="left">Defines a <a href="https://msdn.microsoft.com/library/windows/hardware/ff556186" data-raw-source="[WPP_CONTROL_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff556186)">WPP_CONTROL_GUIDS</a> macro with the specified <a href="control-guid.md" data-raw-source="[control GUID](control-guid.md)">control GUID</a> and WPP_DEFINE_BIT entries named Error, Unusual, and Noise.
<p>This is an alternative to adding the macro to the source file.</p>
<p><em>GUID</em> represents the control GUID.</p></td>
</tr>
</tbody>
</table>

 

## <span id="Search_and_Formatting_Options"></span><span id="search_and_formatting_options"></span><span id="SEARCH_AND_FORMATTING_OPTIONS"></span>Search and Formatting Options


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WPP Tracing Option</th>
<th align="left">TraceWPP command option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Ignore Exclamation Marks</p></td>
<td align="left"><p><strong>-noshrieks</strong></p></td>
<td align="left"><p>Directs WPP to ignore exclamation marks, also known as &quot;shrieks.&quot;</p>
<p>Used in complex formatting, such as %!timestamp!%. By default, exclamation marks are required and WPP tries to interpret them.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Numeric base for numbering of format strings</p></td>
<td align="left"><p><strong>-argbase:</strong> <em>Number</em></p></td>
<td align="left"><p>Establishes a numeric base for numbering of format strings, such as &quot;%1!d!, %2!s!.&quot; The default is 1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Function To Generate Trace Messages</p></td>
<td align="left"><p><strong>-func:</strong> <em>FunctionDescription</em></p></td>
<td align="left"><p>Specifies alternatives to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544918" data-raw-source="[&lt;strong&gt;DoTraceMessage&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544918)"><strong>DoTraceMessage</strong></a> macro. These functions can then be used to generate trace messages.</p>
<p>For example, you can define a function that specifies both the flags and the level for a trace message, such as:</p>
<pre space="preserve"><code>-func (DoMyTraceMessage(LEVEL,FLAGS,MSG,...)</code></pre>
<p>You can use multiple instances of the <strong>-func</strong> option.</p>
<p>This option is an alternative to specifying function descriptions in a local configuration file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Specify String To Search For</p></td>
<td align="left"><p><strong>-lookfor:</strong><em>String</em></p></td>
<td align="left"><p>Directs WPP to search the source files for the specified string to initiate tracing. By default, WPP searches for the string &quot;WPP_INIT_TRACING.&quot;</p>
<p>This is an advanced option for users who are writing their own templates.</p>
<p>For example, in default.tpl:</p>
<pre space="preserve"><code><code>IF FOUND WPP_INIT_TRACING</code>
 <code>INCLUDE um-init.tpl</code>
<code>ENDIF</code></code></pre></td>
</tr>
<tr class="odd">
<td align="left"><p>Specify Module Name</p></td>
<td align="left"><p><strong>-p:</strong> <em>String</em></p></td>
<td align="left"><p>Specifies an alternate friendly name for the <a href="message-guid.md" data-raw-source="[message GUID](message-guid.md)">message GUID</a> of messages from this <a href="trace-provider.md" data-raw-source="[trace provider](trace-provider.md)">trace provider</a>. By default, the friendly name of the message GUID is the name of the directory in which the trace provider was built.</p>
<p>The friendly name of the message GUID appears, by default, in the <a href="trace-message-prefix.md" data-raw-source="[trace message prefix](trace-message-prefix.md)">trace message prefix</a> that is represented by the variable, <strong>%1</strong>. You can use this parameter to add a string to the prefix that helps the user to identify the trace provider, such as the friendly name of the trace provider, the name of the module that includes the trace provider, or the name of a project that is implemented by creating several trace providers. This information helps users to associate related trace providers that are in different files or different paths.</p>
<p>The <strong>-p</strong> parameter requires the version of WPP that is included in the Windows Driver Kit (WDK) for Windows Vista and later versions of the WDK. The <strong>-p</strong> parameter works on Windows 2000 and later versions of Windows.</p>
<p>Examples:</p>
<pre space="preserve"><code>-p:TraceDrv
-p:AudioModule</code></pre></td>
</tr>
</tbody>
</table>

 

## <span id="File_Options"></span><span id="file_options"></span><span id="FILE_OPTIONS"></span>File Options


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">WPP Tracing Option</th>
<th align="left">TraceWPP command option</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Additional Include Directories</p></td>
<td align="left"><p><strong>-I</strong> <em>Path1</em><strong>[;</strong><em>Path2</em><strong>]</strong></p></td>
<td align="left"><p>Specifies one or more directories to add to the include path; separate with semi-colons if more than one. Same as -<strong>cfgdir</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Configuration Directories</p></td>
<td align="left"><p><strong>-cfgdir:</strong> <em>Path1</em><strong>[;</strong><em>Path2</em><strong>]</strong></p></td>
<td align="left"><p>Specifies the location of configuration and template files.</p>
<p><em>Path1</em> and <em>Path2</em> represent the fully qualified path to a directory. You can specify multiple paths. The default is the local directory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>File Extensions</p></td>
<td align="left"><p><strong>-ext:.</strong> <em>ext1</em> <strong>[.</strong><em>ext2</em><strong>]</strong></p></td>
<td align="left"><p>Specifies the file types that WPP recognizes as source files. WPP ignores files with a different file name extension.</p>
<p>By default, WPP recognizes only .c, .c++, .cpp, and .cxx files.</p>
<p>This option allows you to use the default settings for WPP without having to delete or rename resource files that WPP doesn&#39;t use, such as .rc and .mc files.</p>
<p>For example, to add tracing to C++ files and header (.h) files, use the following command:</p>
<p><strong>-ext:.cpp.CPP.h.H</strong></p>
<p>Also, to give the TMH files for the C++ and header files different names, use the <strong>-preserveext</strong> option.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Preserve File Extensions</p></td>
<td align="left"><p><strong>-preserveext:</strong> <em>.ext1</em><strong>[.</strong><em>ext2</em><strong>]</strong></p></td>
<td align="left"><p>Preserves the specified file name extensions when creating TMH files.</p>
<p>By default, TMH files for all file types are named <em>filename</em>.tmh. This caused file name conflicts when you have more than one source file with the same name.</p>
<p>For example, by default, TMH files for C files (.c) and header (.h) files would be named &lt;filename&gt;.tmh. By using <strong>-preserveext:.c .h</strong>, the TMH files are named &lt;filename&gt;.c.tmh and &lt;filename&gt;.h.tmh.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Output Directory</p></td>
<td align="left"><strong>-odir:</strong> <em>path</em></td>
<td align="left"><p>Specifies the directory for the output files that WPP creates.</p>
<p><em>Path</em> is the fully qualified path to the directory. The default is the local directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Specify Template File</p></td>
<td align="left"><p><strong>-gen{ File.tpl }<em>. ext</strong></p></td>
<td align="left"><p>For every source file that WPP processes with the name specified between braces {}, create another file with the specified file name extension.</p>
<p>File.tpl represents the source file. *.ext represents the type of file that is created and its file name extension.</p>
<p>You can specify multiple <strong>-gen</strong> options.</p>
<p>For example, <strong>-gen{um-default.tpl}</em>.tmh</strong> means that for every <strong>um-default.tpl</strong> file that WPP processes, it produces a <strong>um-default.tmh</strong> file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Scan Configuration Data</p></td>
<td align="left"><p><strong>-scan:</strong><em>File</em></p></td>
<td align="left"><p>Searches for configuration data, such as custom data types, in a file that is not a configuration file, as well as in defaultwpp.ini.</p>
<p>Place <strong>begin_wpp config</strong> and <strong>end_wpp</strong> strings around the configuration data to identify it. Use the same format for the configuration data as is used in defaultwpp.ini.</p>
<p>If you added the configuration data to a custom configuration file, use the <strong>-ini</strong> parameter.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Alternate Configuration File</p></td>
<td align="left"><p><strong>-defwpp:</strong><em>path</em></p></td>
<td align="left"><p>Specifies an alternate configuration file. Wpp uses this file instead of the defaultwpp.ini file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Additional Configuration File</p></td>
<td align="left"><p><strong>-ini:</strong><em>Path</em></p></td>
<td align="left"><p>Specifies an additional configuration file. WPP uses the specified file in addition to the default file, defaultwpp.ini.</p>
<p>Use this parameter when you have created a new configuration file to store configuration data for tracing. If you have added the configuration data to another type of file, such as a source or header file, use the <strong>-scan</strong> parameter.</p></td>
</tr>
</tbody>
</table>

 

## <span id="wpp_build_process"></span><span id="WPP_BUILD_PROCESS"></span>WPP Build Process


If WPP is enabled for a driver or user-mode application, building the driver or application invokes the WPP preprocessor before the driver or application files are compiled.

The WPP build process completes the following steps:

1.  The WPP preprocessor processes WPP macros in each source file and creates a [trace message header file](trace-message-header-file.md) for each source file. The source code is not directly modified.

2.  After the WPP preprocessor has created the trace message header files, the C preprocessor processes the built-in WPP macros in the trace message header files in a normal manner.

 

 





