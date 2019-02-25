---
title: Example 14 Starting a Trace Session with Multiple Providers
description: Example 14 Starting a Trace Session with Multiple Providers
ms.assetid: fda63107-608c-4278-abf8-1447c8f8302a
keywords:
- Tracelog WDK , providers
- providers WDK software tracing
- tracing WDK , providers
- multiple providers WDK software tracing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 14: Starting a Trace Session with Multiple Providers


## <span id="ddk_starting_a_session_with_multiple_providers_tools"></span><span id="DDK_STARTING_A_SESSION_WITH_MULTIPLE_PROVIDERS_TOOLS"></span>


The following command starts a trace session with two trace providers:

```
tracelog -start MyTraces -guid 2guids.guid -f mytraces.etl
```

The command looks like a standard **tracelog -start** command, but the file specified by the **-guid** parameter, 2guids.guid, contains two provider GUIDs (one on each line), as in the following example:

```
1540ff4c-3fd7-4bba-9938-1d1bf31573a7
dab01d4d-2d48-477d-b1c3-daad0ce6f06b
```

When you submit this command, Tracelog starts a single trace session with two providers and enables both providers.

The providers share the trace buffers and the event trace log (.etl) file. The trace messages from each provider are interspersed in the trace log. Any flags and levels specified in the command are applied to all providers in the trace session.

To verify that both trace providers have been enabled, use a **tracelog -enumguid** command, as shown in the following command.

```
tracelog -enumguid
```

In response, Tracelog displays the list of providers registered with ETW and shows that two of them are enabled. The enabled providers are shown in bold text.

```
c:\Tracelog>tracelog -enumguid
##     Guid                       Enabled  LoggerId Level Flags
------------------------------------------------------------
1046d4b1-fce5-48bc-8def-fd33196af19a     FALSE  0    0    0
4a8aaa94-cfc4-46a7-8e4e-17bc45608f0a     FALSE  0    0    0
196e57d9-49c0-4b3b-ac3a-a8a93ada1938     FALSE  0    0    0
1540ff4c-3fd7-4bba-9938-1d1bf31573a7      TRUE  2    0    0
f12b1984-4c42-11d3-ab7b-00c04f68fcdc     FALSE  0    0    0
1fbecc45-c060-4e7c-8a0e-0dbd6116181b     FALSE  0    0    0
94a984ef-f525-4bf1-be3c-ef374056a592     FALSE  0    0    0
3121cf5d-c5e6-4f37-be86-57083590c333     FALSE  0    0    0
fc4b0d39-e8be-4a83-a32f-c0c7c4f61ee4     FALSE  0    0    0
fc570986-5967-4641-a6f9-05291bce66c5     FALSE  0    0    0
39a7b5e0-be85-47fc-b9f5-593a659abac1     FALSE  0    0    0
dab01d4d-2d48-477d-b1c3-daad0ce6f06b      TRUE  2    0    0k
bca7bd7f-b0bf-4051-99f4-03cfe79664c1     FALSE  0    0    0
d58c126f-b309-11d1-969e-0000f875a5bc     FALSE  0    0    0
d58c126e-b309-11d1-969e-0000f875a5bc     FALSE  0    0    0
58db8e03-0537-45cb-b29b-597f6cbebbfe     FALSE  0    0    0
27246e9d-b4df-4f20-b969-736fa49ff6ff     FALSE  0    0    0
```

To specify different flags and levels for each trace provider in the session, use a separate **tracelog -enable** command for each provider, as shown in the following command.

```
tracelog -enable MyTraces -guid #1540ff4c-3fd7-4bba-9938-1d1bf31573a7 -flag 2 -level 1
tracelog -enable MyTraces -guid #dab01d4d-2d48-477d-b1c3-daad0ce6f06b -flag 3 -level ffff
```

 

 





