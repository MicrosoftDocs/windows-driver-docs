---
title: dg (Display Selector)
description: The dg command shows the segment descriptor for the specified selector.
ms.assetid: bf680931-f4f9-4b72-bb25-42d095514d2a
keywords: ["dg (Display Selector) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- dg (Display Selector)
api_type:
- NA
ms.localizationpriority: medium
---

# dg (Display Selector)


The **dg** command shows the segment descriptor for the specified selector.

```dbgcmd
dg FirstSelector [LastSelector]
```

## <span id="ddk_cmd_display_selector_dbg"></span><span id="DDK_CMD_DISPLAY_SELECTOR_DBG"></span>Parameters


<span id="_______FirstSelector______"></span><span id="_______firstselector______"></span><span id="_______FIRSTSELECTOR______"></span> *FirstSelector*   
Specifies the hexadecimal selector value of the first selector to be displayed.

<span id="_______LastSelector______"></span><span id="_______lastselector______"></span><span id="_______LASTSELECTOR______"></span> *LastSelector*   
Specifies the hexadecimal selector value of the last selector to be displayed. If this is omitted, only one selector will be displayed.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>x86, Itanium</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

No more than 256 selectors can be displayed by this command.

Common selector values are:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Id</th>
<th align="left">decimal</th>
<th align="left">hex</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>KGDT_NULL</p></td>
<td align="left"><p>0</p></td>
<td align="left"><p>0x00</p></td>
</tr>
<tr class="even">
<td align="left"><p>KGDT_R0_CODE</p></td>
<td align="left"><p>8</p></td>
<td align="left"><p>0x08</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KGDT_R0_DATA</p></td>
<td align="left"><p>16</p></td>
<td align="left"><p>0x10</p></td>
</tr>
<tr class="even">
<td align="left"><p>KGDT_R3_CODE</p></td>
<td align="left"><p>24</p></td>
<td align="left"><p>0x18</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KGDT_R3_DATA</p></td>
<td align="left"><p>32</p></td>
<td align="left"><p>0x20</p></td>
</tr>
<tr class="even">
<td align="left"><p>KGDT_TSS</p></td>
<td align="left"><p>40</p></td>
<td align="left"><p>0x28</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KGDT_R0_PCR</p></td>
<td align="left"><p>48</p></td>
<td align="left"><p>0x30</p></td>
</tr>
<tr class="even">
<td align="left"><p>KGDT_R3_TEB</p></td>
<td align="left"><p>56</p></td>
<td align="left"><p>0x38</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KGDT_VDM_TILE</p></td>
<td align="left"><p>64</p></td>
<td align="left"><p>0x40</p></td>
</tr>
<tr class="even">
<td align="left"><p>KGDT_LDT</p></td>
<td align="left"><p>72</p></td>
<td align="left"><p>0x48</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KGDT_DF_TSS</p></td>
<td align="left"><p>80</p></td>
<td align="left"><p>0x50</p></td>
</tr>
<tr class="even">
<td align="left"><p>KGDT_NMI_TSS</p></td>
<td align="left"><p>88</p></td>
<td align="left"><p>0x58</p></td>
</tr>
</tbody>
</table>

 

 

 





