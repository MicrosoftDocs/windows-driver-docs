---
title: Tracelog Enumguid Display
description: Tracelog Enumguid Display
ms.assetid: 9bb93238-98f7-4422-8434-b4dc105ec008
keywords:
- Tracelog WDK , providers
- providers WDK software tracing
- tracing WDK , providers
- -enumguid command
- enumguid command
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tracelog Enumguid Display


When you submit a **tracelog -enumguid** command, Tracelog displays a list of the trace providers that are running and have [registered](registered-provider.md) with Event Tracing for Windows (ETW). The display is very useful, but it is often misinterpreted.

### <span id="which_providers_appear_in_the_display_"></span><span id="WHICH_PROVIDERS_APPEAR_IN_THE_DISPLAY_"></span>Which Providers Appear in the Display?

The Tracelog enumguid display lists some of the providers that you can enable for a trace session, but it is not a complete list. It includes only the trace providers that are running and have registered with ETW.

The display does not include the following providers:

Trace providers that are available on the system, but are not registered, usually because they are not running.

Trace providers that are enabled for a trace session but are not currently running. (These are often called *pre-enabled* or *pre-registered* providers.) This includes providers that do not run continuously, such as DLLs that are loaded and unloaded as needed.

Providers built into Windows, including providers for system sessions and providers for the [Global Logger trace session](global-logger-trace-session.md) and [NT Kernel Logger trace session](nt-kernel-logger-trace-session.md).

### <span id="the_logman_query_providers_display"></span><span id="THE_LOGMAN_QUERY_PROVIDERS_DISPLAY"></span>The Logman Query Providers Display

The Tracelog enumguid display is quite different from the query providers display in Logman (**logman query providers**), although the displays are often confused.

Logman (logman.exe) is a trace controller for trace events and performance counters. It is included in Windows XP and later versions of Windows.

The Logman provider query (**logman query providers**) displays a list of providers that have registered Managed Object Format (MOF) files with WMI. The Logman display does not include providers that are instrumented for software tracing, unless they have also registered with WMI.

Developers who want to help users find their providers occasionally register their MOF files just to make the provider appear in the Logman display. Unfortunately, neither the Logman query provider display nor the Tracelog enumguid display are complete lists of all trace providers on the system. For more information about Logman, see "Logman" in Help and Support Center.

### <span id="elements_of_the_enumguid_display"></span><span id="ELEMENTS_OF_THE_ENUMGUID_DISPLAY"></span>Elements of the Enumguid Display

The table in the Tracelog enumguid display includes the following columns.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Column heading</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Guid</strong></p></td>
<td align="left"><p>The <a href="control-guid.md" data-raw-source="[control GUID](control-guid.md)">control GUID</a> of the trace provider</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Enabled</strong></p></td>
<td align="left"><p>Shows whether the provider is currently enabled (<strong>TRUE</strong>) or is registered but not enabled (<strong>FALSE</strong>).</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>LoggerId</strong></p></td>
<td align="left"><p>Identifies the trace session.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Level</strong></p></td>
<td align="left"><p>The level currently set for the provider. Valid only when the provider is enabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Flags</strong></p></td>
<td align="left"><p>The flags currently set for the provider. Valid only when the provider is enabled.</p></td>
</tr>
</tbody>
</table>

 

If a provider is registered but not enabled, then it appears in the enumguid display but its entry in the **Enabled** column is **FALSE**.

If a provider is enabled but is not currently running and is, therefore, not registered, then it does not appear in the enumguid display.

### <span id="sample_enumguid_display"></span><span id="SAMPLE_ENUMGUID_DISPLAY"></span>Sample Enumguid Display

The following enumguid display was copied from a computer running Windows Server 2003. The display lists the providers that are registered and running. One provider, the Tracedrv sample driver, is enabled for tracing. [TraceDrv](http://go.microsoft.com/fwlink/p/?LinkId=617726), a sample driver that was designed for software tracing, is available in the [Windows driver samples](http://go.microsoft.com/fwlink/p/?LinkId=616507) repository on GitHub.

```
c:\Tracelog>tracelog -enumguid
##     Guid                     Enabled  LoggerId Level Flags
------------------------------------------------------------
1046d4b1-fce5-48bc-8def-fd33196af19a     FALSE  0    0    0
196e57d9-49c0-4b3b-ac3a-a8a93ada1938     FALSE  0    0    0
4a8aaa94-cfc4-46a7-8e4e-17bc45608f0a     FALSE  0    0    0
1540ff4c-3fd7-4bba-9938-1d1bf31573a7     FALSE  0    0    0
1fbecc45-c060-4e7c-8a0e-0dbd6116181b     FALSE  0    0    0
f12b1984-4c42-11d3-ab7b-00c04f68fcdc     FALSE  0    0    0
94a984ef-f525-4bf1-be3c-ef374056a592     FALSE  0    0    0
3121cf5d-c5e6-4f37-be86-57083590c333     FALSE  0    0    0
f498b9f5-9e67-446a-b9b8-1442ffaef434     FALSE  0    0    0
e1f65b93-f32a-4ed6-aa72-b039e28f1574     FALSE  0    0    0
dd5ef90a-6398-47a4-ad34-4dcecdef795f     FALSE  0    0    0
e80aa9fe-913d-4ede-af58-73e332dcac8d     FALSE  0    0    0
1b1d4ff4-f27b-4c99-8bd7-da8f1a74051a     FALSE  0    0    0
f33959b4-dbec-11d2-895b-00c04f79ab69     FALSE  0    0    0
cc85922f-db41-11d2-9244-006008269001     FALSE  0    0    0
c92cf544-91b3-4dc0-8e11-c580339a0bf8     FALSE  0    0    0
bba3add2-c229-4cdb-ae2b-57eb6966b0c4     FALSE  0    0    0
8fc7e81a-f733-42e0-9708-cfdae07ed969     FALSE  0    0    0
cddc01e2-fdce-479a-b8ee-3c87053fb55e     FALSE  0    0    0
fc4b0d39-e8be-4a83-a32f-c0c7c4f61ee4     FALSE  0    0    0
fc570986-5967-4641-a6f9-05291bce66c5     FALSE  0    0    0
39a7b5e0-be85-47fc-b9f5-593a659abac1     FALSE  0    0    0
dab01d4d-2d48-477d-b1c3-daad0ce6f06b     FALSE  0    0    0
bca7bd7f-b0bf-4051-99f4-03cfe79664c1     FALSE  0    0    0
d58c126f-b309-11d1-969e-0000f875a5bc      TRUE  2    0    0
d58c126e-b309-11d1-969e-0000f875a5bc     FALSE  0    0    0
58db8e03-0537-45cb-b29b-597f6cbebbfe     FALSE  0    0    0
58db8e03-0537-45cb-b29b-597f6cbebbfd     FALSE  0    0    0
688a5248-f348-4576-86cf-3521c7094614     FALSE  0    0    0
27246e9d-b4df-4f20-b969-736fa49ff6ff    FALSE  0    0    0
```

 

 





