---
title: Enabling NDIS Debug Tracing By Setting Registry Values
description: Enabling NDIS Debug Tracing By Setting Registry Values
ms.assetid: ae01f546-0636-4e67-bfc7-229c3cc24b27
keywords: ["NDIS debugging, debug tracing, setting registry values"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Enabling NDIS Debug Tracing By Setting Registry Values


You can enable different levels of debug tracing in various NDIS components by editing the registry. Typically, you should add the following entries and values to the **HKLM\\SYSTEM\\CurrentControlSet\\Services\\NDIS\\Parameters** registry key:

```text
"DebugLevel"=dword:00000000
"DebugSystems"=dword:000030F3
"DebugBreakPoint"=dword:00000001 
```

The following values are acceptable for **DebugBreakPoint**, **DebugLevel** and **DebugSystems**:

<span id="DebugBreakPoint"></span><span id="debugbreakpoint"></span><span id="DEBUGBREAKPOINT"></span>**DebugBreakPoint**  
Controls whether an NDIS driver will automatically break into the debugger. If this value is set to 1, NDIS will break into the debugger when a driver enters Ndis.sys's **DriverEntry** function.

<span id="DebugLevel"></span><span id="debuglevel"></span><span id="DEBUGLEVEL"></span>**DebugLevel**  
Selects the level or amount of debug tracing in the NDIS components that you select with the **DebugSystems** value. The following values specify levels that you can select:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Level</th>
<th align="left">Description</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DBG_LEVEL_INFO</p></td>
<td align="left"><p>All available debug information. This is the highest level of trace.</p></td>
<td align="left"><p>0x00000000</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_LEVEL_LOG</p></td>
<td align="left"><p>Log information.</p></td>
<td align="left"><p>0x00000800</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_LEVEL_WARN</p></td>
<td align="left"><p>Warnings.</p></td>
<td align="left"><p>0x00001000</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_LEVEL_ERR</p></td>
<td align="left"><p>Errors.</p></td>
<td align="left"><p>0x00002000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_LEVEL_FATAL</p></td>
<td align="left"><p>Fatal errors, which can cause the operating system to crash. This is the lowest level of trace.</p></td>
<td align="left"><p>0x00003000</p></td>
</tr>
</tbody>
</table>

 

<span id="DebugSystems"></span><span id="debugsystems"></span><span id="DEBUGSYSTEMS"></span>**DebugSystems**  
Enables debug tracing for specified NDIS components. This corresponds to using the [**!ndiskd.dbgsystems**](-ndiskd-dbgsystems.md) extension. The following values specify the NDIS components that you can select:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Component</th>
<th align="left">Description</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DBG_COMP_INIT</p></td>
<td align="left"><p>Handles adapter initialization.</p></td>
<td align="left"><p>0x00000001</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_CONFIG</p></td>
<td align="left"><p>Handles adapter configuration.</p></td>
<td align="left"><p>0x00000002</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_SEND</p></td>
<td align="left"><p>Handles sending data over the network.</p></td>
<td align="left"><p>0x00000004</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_RECV</p></td>
<td align="left"><p>Handles receiving data from the network.</p></td>
<td align="left"><p>0x00000008</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_PROTOCOL</p></td>
<td align="left"><p>Handles protocol operations.</p></td>
<td align="left"><p>0x00000010</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_BIND</p></td>
<td align="left"><p>Handles binding operations.</p></td>
<td align="left"><p>0x00000020</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_BUSINFO</p></td>
<td align="left"><p>Handles bus queries.</p></td>
<td align="left"><p>0x00000040</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_REG</p></td>
<td align="left"><p>Handles registry operations.</p></td>
<td align="left"><p>0x00000080</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_MEMORY</p></td>
<td align="left"><p>Handles memory management.</p></td>
<td align="left"><p>0x00000100</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_FILTER</p></td>
<td align="left"><p>Handles filter operations.</p></td>
<td align="left"><p>0x00000200</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_REQUEST</p></td>
<td align="left"><p>Handles requests.</p></td>
<td align="left"><p>0x00000400</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_WORK_ITEM</p></td>
<td align="left"><p>Handles work-item operations.</p></td>
<td align="left"><p>0x00000800</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_PNP</p></td>
<td align="left"><p>Handles Plug and Play operations.</p></td>
<td align="left"><p>0x00001000</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_PM</p></td>
<td align="left"><p>Handles power management operations.</p></td>
<td align="left"><p>0x00002000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_OPENREF</p></td>
<td align="left"><p>Handles operations that open reference objects.</p></td>
<td align="left"><p>0x00004000</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_LOCKS</p></td>
<td align="left"><p>Handles locking operations.</p></td>
<td align="left"><p>0x00008000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_RESET</p></td>
<td align="left"><p>Handles resetting operations.</p></td>
<td align="left"><p>0x00010000</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_WMI</p></td>
<td align="left"><p>Handles Windows Management Instrumentation operations.</p></td>
<td align="left"><p>0x00020000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_CO</p></td>
<td align="left"><p>Handles Connection-Oriented NDIS.</p></td>
<td align="left"><p>0x00040000</p></td>
</tr>
<tr class="even">
<td align="left"><p>DBG_COMP_REF</p></td>
<td align="left"><p>Handles reference operations.</p></td>
<td align="left"><p>0x00080000</p></td>
</tr>
<tr class="odd">
<td align="left"><p>DBG_COMP_ALL</p></td>
<td align="left"><p>Handles all NDIS components.</p></td>
<td align="left"><p>0xFFFFFFFF</p></td>
</tr>
</tbody>
</table>

 

You can select more than one NDIS component. If more than one component is selected, combine the data values with an OR operator. For example, to select DBG\_COMP\_PNP, DBG\_COMP\_PM, DBG\_COMP\_INIT and DBG\_COMP\_CONFIG, you would combine the corresponding values (0x1000, 0x2000, 0x1, and 0x2) to obtain the value 0x3003, and then set it in the registry thus:

```text
"DebugSystems"=dword:00003003
```

Whenever you change registry values for debug tracing, you must restart your computer for the new settings to take effect.

 

 





