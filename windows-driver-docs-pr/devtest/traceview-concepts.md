---
title: TraceView Concepts
description: TraceView Concepts
ms.assetid: 4fab2b23-8f7b-407b-b944-41ac8caf1a75
keywords: ["TraceView WDK , terminology", "trace sessions WDK , groups", "grouping trace sessions", "workspaces WDK TraceView , about workspaces", "trace sessions WDK , workspaces", "trace providers WDK", "providers WDK software tracing", "trace sessions WDK , providers", "TMF files WDK , search paths", "search paths WDK software tracing", "TMF files WDK , options"]
---

# TraceView Concepts


## <span id="ddk_traceview_concepts_tools"></span><span id="DDK_TRACEVIEW_CONCEPTS_TOOLS"></span>


This topic explains the concepts that are used in TraceView.

For information about concepts that are common to the tracing tools in the WDK, see [Tracing Tool Concepts](tracing-tool-concepts.md).

### <span id="Trace_Session_Group"></span><span id="trace_session_group"></span><span id="TRACE_SESSION_GROUP"></span>Trace Session Group

TraceView lets you combine [trace log](trace-log.md) displays or real-time trace sessions into a *trace session group* and manage them as though they were a single session. When trace logs or sessions are in the same trace session group, their messages are combined in one [trace message list](trace-message-lists.md).

By default, each trace session is a member of a trace session group that consists of only that trace session.

For information about creating trace session groups, see [Grouping Trace Sessions](grouping-trace-sessions.md).

### <span id="Workspace"></span><span id="workspace"></span><span id="WORKSPACE"></span>Workspace

In TraceView, a *workspace* is a set of trace session properties and trace log display properties that you can save and reuse. With workspaces, you can display a frequently used log or start a carefully configured trace session in one quick step.

A workspace includes:

-   All properties of the trace session, including buffers, flags and the level, and the location of the trace log

-   The location of the [program database (PDB) symbol file](pdb-symbol-files.md), [trace message format (TMF) file](trace-message-format-file.md), or TMF search path

-   The path and file names of the TraceView listing file and summary file

-   Filters

When you open the workspace for a real-time trace session, TraceView starts a new trace session with the saved properties and configuration settings. When you open the workspace for a trace log display, the log appears exactly as you had configured it.

For more information, see [Using TraceView Workspaces](using-traceview-workspaces.md).

### <span id="Specifying_Trace_Providers"></span><span id="specifying_trace_providers"></span><span id="SPECIFYING_TRACE_PROVIDERS"></span>Specifying Trace Providers

To create a trace session, you must identify the trace providers and locate the formatting instructions for the binary trace messages that the providers generate. You can do this any one of the following ways:

-   Locate the [PDB symbol file](pdb-symbol-files.md) for the source code that includes the provider or providers. TraceView can extract from the PDB file all of the information that it needs to identify the providers and format their trace messages.

-   Locate a [control GUID (.ctl) file](control-guid-file.md) for the provider and specify the [TMF file](trace-message-format-file.md) or the path to a directory where TMF files are stored.

-   Type or paste the [control GUID](control-guid.md) of the provider and specify the TMF file or the path to a directory where TMF files are stored.

-   Select a [registered provider](registered-provider.md) from the list that TraceView assembles and specify the TMF file or the path to a directory where TMF files are stored.

-   Select an [NT Kernel Logger Trace Session](nt-kernel-logger-trace-session.md), select one or more operating system events to trace, and then locate the *System.tmf* file a file included in the WDK that contains instructions for formatting trace messages that Windows components generate.

### <span id="Set_TMF_Search_Path_and_Select_TMF_Files_Options"></span><span id="set_tmf_search_path_and_select_tmf_files_options"></span><span id="SET_TMF_SEARCH_PATH_AND_SELECT_TMF_FILES_OPTIONS"></span>Set TMF Search Path and Select TMF Files Options

Unless you have the [PDB symbol file](pdb-symbol-files.md) for the provider, you must specify a directory in which TraceView can find the TMF files or must locate the [TMF files](trace-message-format-file.md) for the provider's trace messages.

TraceView supports both methods:

-   Use the **Set TMF Search Path** option when you are not sure which TMF files to use for the trace provider. TraceView searches all of the TMF files in the specified directory and matches the message GUID of the message that is generated to the name of the TMF file. The TMF files must be located in the specified directory. TraceView does not search recursively.

-   Use the **Select TMF files** option when you know which TMF file to use for the trace provider, or when the TMF files you need are in different directories. You must also use this option if the name of the TMF file is not a [message GUID](message-guid.md), because TraceView cannot find it in a directory.

If TraceView cannot find a TMF file for the trace provider, it does not add the trace provider to the provider list in the **Create New Log Session** dialog box and it does not display a message that explains why the provider was not added. If you cannot locate a PDB file or a TMF file for the provider, you cannot use TraceView to create a trace session with the provider.

If the TMF files that are specified or those that TraceView finds in the specified directory do not match the trace messages that are generated by the trace provider, TraceView cannot format the messages. Instead, it displays the trace message GUID and the following error message:

```
No Format Information found.
```

To create TMF files from a PDB symbol file, in a Command Prompt window, type **traceview -parsepdb**. For more information about this command, see [**TraceView -parsepdb**](traceview--parsepdb.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20TraceView%20Concepts%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




