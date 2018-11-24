---
title: Direct3D rendering performance improvements
description: Windows Display Driver Model (WDDM) 1.3 and later drivers can support Microsoft Direct3D rendering performance improvements that let Direct3D 9 hardware make better use of hardware command buffers and counters and make efficient copies of system memory to subresources. These capabilities, which mirror some of the capabilities available for Direct3D Version 10 hardware, are new starting with Windows 8.1.
ms.assetid: F9AAE489-EC45-4EE6-875E-E084BB3054EE
ms.date: 10/20/2018
ms.localizationpriority: medium
---

# Direct3D rendering performance improvements


Windows Display Driver Model (WDDM) 1.3 and later drivers can support Microsoft Direct3D rendering performance improvements that let Direct3D 9 hardware make better use of hardware command buffers and counters and make efficient copies of system memory to subresources. These capabilities, which mirror some of the capabilities available for Direct3D Version 10 hardware, are new starting with Windows 8.1.

New Direct3D 11.1 resource trim and map default performance improvements are also available. The map default scenario is outlined in the Behavior changes section below.

## <span id="Rendering_performance_reference"></span><span id="rendering_performance_reference"></span><span id="RENDERING_PERFORMANCE_REFERENCE"></span>Rendering performance reference


This reference section describes the user-mode device driver interfaces (DDIs).

### Direct3D rendering performance functions implemented by the user-mode driver

This section contains functions that a Windows Display Driver Model (WDDM) 1.3 and later user-mode display driver implements in order to support Microsoft Direct3D rendering performance improvements.


|||
|:--|:--|
|[PFND3DDDI_FLUSH1](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_flush1)| [PFND3DDDI_CHECKCOUNTERINFO](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_checkcounterinfo)|
|[PFND3DDDI_CHECKCOUNTER](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_checkcounter) |[PFND3DDDI_UPDATESUBRESOURCEUP](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dumddi/nc-d3dumddi-pfnd3dddi_updatesubresourceup)|

### Direct3D rendering performance structures and enumerations

These user-mode structures and enumerations support rendering performance improvements and are new or updated for Windows 8.1. All apply to Direct3D Level 9 drivers except for [**D3D11\_1\_DDI\_FLUSH\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh451049).

-   [**D3DDDI\_FLUSH\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/dn449154) (new)
-   [**D3DDDIARG\_COPYFLAGS**](https://msdn.microsoft.com/library/windows/hardware/dn449151) (new)
-   [**D3DDDIARG\_COUNTER\_INFO**](https://msdn.microsoft.com/library/windows/hardware/dn449152) (new)
-   [**D3DDDIARG\_UPDATESUBRESOURCEUP**](https://msdn.microsoft.com/library/windows/hardware/dn449153) (new)
-   [**D3DDDICAPS\_SIMPLE\_INSTANCING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/dn465882) (new)
-   [*CreateResource2*](https://msdn.microsoft.com/library/windows/hardware/hh406287) (WDDM 1.3 and later Direct3D Level 9 drivers must return the **E\_INVALIDARG** error code if the **CaptureBuffer** flag value is set)
-   [**D3D11\_1\_DDI\_FLUSH\_FLAGS**](https://msdn.microsoft.com/library/windows/hardware/hh451049) (**D3DWDDM1\_3DDI\_TRIM\_MEMORY** constant added)
-   [**D3DDDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff544519) (**pfnFlush1**, **pfnCheckCounterInfo**, **pfnCheckCounter**, **pfnUpdateSubresourceUP** members added)
-   [**D3DDDI\_POOL**](https://msdn.microsoft.com/library/windows/hardware/ff544634) (**D3DDDIPOOL\_STAGINGMEM** constant added)
-   [**D3DDDICAPS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff544132) (**D3DDDICAPS\_GET\_SIMPLE\_INSTANCING\_SUPPORT** constant added)
-   [*GetCaps*](https://msdn.microsoft.com/library/windows/hardware/ff566762) (new info in Remarks)

## <span id="ddi_implementation_requirements_starting_with_wddm_1.3"></span><span id="DDI_IMPLEMENTATION_REQUIREMENTS_STARTING_WITH_WDDM_1.3"></span>DDI implementation requirements starting with WDDM 1.3


Starting with WDDM 1.3, the following functions are required or optional for user-mode drivers to implement.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function group</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="_9_functions_that_are_optional_prior_to__1.3._Now_required_"></span><span id="_9_functions_that_are_optional_prior_to__1.3._now_required_"></span><span id="_9_FUNCTIONS_THAT_ARE_OPTIONAL_PRIOR_TO__1.3._NOW_REQUIRED_"></span>Direct3D 9 functions that are optional prior to WDDM 1.3. Now required:</p></td>
<td align="left"><ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406236" data-raw-source="[&lt;em&gt;BufBlt1&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406236)"><em>BufBlt1</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406287" data-raw-source="[&lt;em&gt;CreateResource2&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406287)"><em>CreateResource2</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439866" data-raw-source="[&lt;em&gt;TexBlt1&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439866)"><em>TexBlt1</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439911" data-raw-source="[&lt;em&gt;VolBlt1&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439911)"><em>VolBlt1</em></a></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><span id="_9_functions_that_are_available_starting_with__1.3._A_driver_must_either_implement_all_of_these_functions_or_none_of_them_"></span><span id="_9_functions_that_are_available_starting_with__1.3._a_driver_must_either_implement_all_of_these_functions_or_none_of_them_"></span><span id="_9_FUNCTIONS_THAT_ARE_AVAILABLE_STARTING_WITH__1.3._A_DRIVER_MUST_EITHER_IMPLEMENT_ALL_OF_THESE_FUNCTIONS_OR_NONE_OF_THEM_"></span>Direct3D 9 functions that are available starting with WDDM 1.3. A driver must either implement all of these functions or none of them:</p></td>
<td align="left"><ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn449227" data-raw-source="[&lt;em&gt;pfnCheckCounter&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn449227)"><em>pfnCheckCounter</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn449228" data-raw-source="[&lt;em&gt;pfnCheckCounterInfo&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn449228)"><em>pfnCheckCounterInfo</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn449229" data-raw-source="[&lt;em&gt;pfnFlush1&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn449229)"><em>pfnFlush1</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn458010" data-raw-source="[&lt;em&gt;pfnPresent1(D3D)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn458010)"><em>pfnPresent1(D3D)</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn469267" data-raw-source="[&lt;em&gt;pfnPresent1(DXGI)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn469267)"><em>pfnPresent1(DXGI)</em></a></li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn449230" data-raw-source="[&lt;em&gt;pfnUpdateSubresourceUP&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn449230)"><em>pfnUpdateSubresourceUP</em></a></li>
<li>pfnSetMarker</li>
<li>pfnSetMarkerMode</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="When_the__1.3_and_later_optional_functions_immediately_above_are_implemented__these_functions_have_associated_behavior_changes_"></span><span id="when_the__1.3_and_later_optional_functions_immediately_above_are_implemented__these_functions_have_associated_behavior_changes_"></span><span id="WHEN_THE__1.3_AND_LATER_OPTIONAL_FUNCTIONS_IMMEDIATELY_ABOVE_ARE_IMPLEMENTED__THESE_FUNCTIONS_HAVE_ASSOCIATED_BEHAVIOR_CHANGES_"></span>When the WDDM 1.3 and later optional functions immediately above are implemented, these functions have associated behavior changes:</p></td>
<td align="left"><ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff538252" data-raw-source="[&lt;em&gt;BltDXGI&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff538252)"><em>BltDXGI</em></a> —native staging</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406235" data-raw-source="[&lt;em&gt;Blt1DXGI&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406235)"><em>Blt1DXGI</em></a> —native staging</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh406287" data-raw-source="[&lt;em&gt;CreateResource2&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh406287)"><em>CreateResource2</em></a> —native staging, large capture textures</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff566762" data-raw-source="[&lt;em&gt;GetCaps&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566762)"><em>GetCaps</em></a> —time stamps, simple instancing</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff568213" data-raw-source="[&lt;em&gt;Lock&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff568213)"><em>Lock</em></a> —native staging</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439866" data-raw-source="[&lt;em&gt;TexBlt1&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439866)"><em>TexBlt1</em></a> —native staging</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff570104" data-raw-source="[&lt;em&gt;Unlock&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff570104)"><em>Unlock</em></a> —native staging</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/hh439911" data-raw-source="[&lt;em&gt;VolBlt1&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/hh439911)"><em>VolBlt1</em></a> —native staging</li>
</ul>
<p>These scenarios apply when <a href="https://msdn.microsoft.com/library/windows/hardware/ff566762" data-raw-source="[&lt;em&gt;GetCaps&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566762)"><em>GetCaps</em></a> is called:</p>
<ul>
<li>If <strong>D3DDDICAPS_GETD3DQUERYDATA</strong> is set, the driver can optionally report support for time stamps, meaning that the Direct3D runtime won&#39;t mask support.</li>
<li>If <strong>D3DDDICAPS_GET_SIMPLE_INSTANCING_SUPPORT</strong> is set, the driver can report optional hardware support for instancing.</li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p><span id="These__11_functions_have_associated_behavior_changes_"></span><span id="these__11_functions_have_associated_behavior_changes_"></span><span id="THESE__11_FUNCTIONS_HAVE_ASSOCIATED_BEHAVIOR_CHANGES_"></span>These Direct3D 11 functions have associated behavior changes:</p></td>
<td align="left"><ul>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff540694" data-raw-source="[&lt;em&gt;CreateResource(D3D11)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540694)"><em>CreateResource(D3D11)</em></a> — buffer map default (see Behavior changes section below)</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/dn449229" data-raw-source="[&lt;em&gt;pfnFlush1&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/dn449229)"><em>pfnFlush1</em></a> — resource trim</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff569492" data-raw-source="[&lt;em&gt;ResourceMap&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569492)"><em>ResourceMap</em></a> — buffer map default (see Behavior changes section below)</li>
<li><a href="https://msdn.microsoft.com/library/windows/hardware/ff569495" data-raw-source="[&lt;em&gt;ResourceUnmap&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569495)"><em>ResourceUnmap</em></a> — buffer map default (see Behavior changes section below)</li>
</ul></td>
</tr>
</tbody>
</table>

 

## <span id="_behavior_"></span><span id="_BEHAVIOR_"></span>Behavior changes for calls to resource create, map, and unmap functions


For these functions that are implemented by WDDM 1.3 and later drivers, the Direct3D runtime supplies a restricted set of input values for the map default scenario. These restricted values apply only to drivers that support feature level 11.1 and later.

[***CreateResource(D3D11)***](https://msdn.microsoft.com/library/windows/hardware/ff540694) **function**—

These input [**D3D11DDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542062) structure members are restricted:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="ResourceDimension_and_Usage"></span><span id="resourcedimension_and_usage"></span><span id="RESOURCEDIMENSION_AND_USAGE"></span><strong>ResourceDimension</strong> and <strong>Usage</strong></p></td>
<td align="left"><p>These behavior changes only apply when the Direct3D runtime supplies type <strong>D3D10DDIRESOURCE_BUFFER</strong> for <strong>ResourceDimension</strong> and type <strong>D3D10_DDI_USAGE_DEFAULT</strong> for <strong>Usage</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="BindFlags"></span><span id="bindflags"></span><span id="BINDFLAGS"></span><strong>BindFlags</strong></p></td>
<td align="left"><p>The Direct3D runtime sets only the <strong>D3D10_DDI_BIND_SHADER_RESOURCE</strong> and <strong>D3D11_DDI_BIND_UNORDERED_ACCESS</strong> values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MapFlags"></span><span id="mapflags"></span><span id="MAPFLAGS"></span><strong>MapFlags</strong></p></td>
<td align="left"><p>If all the other member requirements listed here are met, the runtime can set <strong>D3D10_DDI_MAP_READ</strong>, <strong>D3D10_DDI_MAP_WRITE</strong>, and <strong>D3D10_DDI_MAP_READWRITE</strong> values. The driver must support these values. Values of <strong>D3D10_DDI_MAP_WRITE_DISCARD</strong> and <strong>D3D10_DDI_MAP_WRITE_NOOVERWRITE</strong> are invalid.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="MiscFlags"></span><span id="miscflags"></span><span id="MISCFLAGS"></span><strong>MiscFlags</strong></p></td>
<td align="left"><p>The runtime sets only the <strong>D3D11_DDI_RESOURCE_MISC_BUFFER_ALLOW_RAW_VIEWS</strong> and <strong>D3D11_DDI_RESOURCE_MISC_BUFFER_STRUCTURED</strong> values.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Format"></span><span id="format"></span><span id="FORMAT"></span><strong>Format</strong></p></td>
<td align="left"><p>The runtime sets only the <strong>DXGI_FORMAT_UNKNOWN</strong> value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="SampleDesc"></span><span id="sampledesc"></span><span id="SAMPLEDESC"></span><strong>SampleDesc</strong></p></td>
<td align="left"><p>The runtime sets the <a href="https://msdn.microsoft.com/library/windows/desktop/bb173072" data-raw-source="[&lt;strong&gt;DXGI_SAMPLE_DESC&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/bb173072)"><strong>DXGI_SAMPLE_DESC</strong></a>.<strong>Count</strong> member to 1, and the <strong>Quality</strong> member to zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="MipLevels"></span><span id="miplevels"></span><span id="MIPLEVELS"></span><strong>MipLevels</strong></p></td>
<td align="left"><p>The runtime sets the value to 1.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="ArraySize"></span><span id="arraysize"></span><span id="ARRAYSIZE"></span><strong>ArraySize</strong></p></td>
<td align="left"><p>The runtime sets the value to 1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="pPrimaryDesc"></span><span id="pprimarydesc"></span><span id="PPRIMARYDESC"></span><strong>pPrimaryDesc</strong></p></td>
<td align="left"><p>The runtime sets the value to <strong>NULL</strong>.</p></td>
</tr>
</tbody>
</table>

 

[***ResourceMap***](https://msdn.microsoft.com/library/windows/hardware/ff569492) **function**—

These input parameters to [*ResourceMap*](https://msdn.microsoft.com/library/windows/hardware/ff569492) are restricted:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="hResource"></span><span id="hresource"></span><span id="HRESOURCE"></span><em>hResource</em></p></td>
<td align="left"><p>The Direct3D runtime sets only a <strong>D3D10DDIRESOURCE_BUFFER</strong> resource when a non-zero value for <em>MapFlags</em> is set in the creation call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff540694" data-raw-source="[&lt;em&gt;CreateResource(D3D11)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540694)"><em>CreateResource(D3D11)</em></a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span></span><em></em></p></td>
<td align="left"><p>The runtime sets only the <strong>DXGI_FORMAT_UNKNOWN</strong> value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Subresource"></span><span id="subresource"></span><span id="SUBRESOURCE"></span><em>Subresource</em></p></td>
<td align="left"><p>The runtime only sets the value to 0.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="DDIMap"></span><span id="ddimap"></span><span id="DDIMAP"></span><em>DDIMap</em></p></td>
<td align="left"><p>If all the other member requirements listed here are met, the runtime can set <strong>D3D10_DDI_MAP_READ</strong>, <strong>D3D10_DDI_MAP_WRITE</strong>, or <strong>D3D10_DDI_MAP_READWRITE</strong> values, matching the <em>MapFlags</em> value set in the creation call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff540694" data-raw-source="[&lt;em&gt;CreateResource(D3D11)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540694)"><em>CreateResource(D3D11)</em></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span><em>Flags</em></p></td>
<td align="left"><p>Although the input value from the runtime isn&#39;t restricted, the driver must be able to support the <strong>D3D10_DDI_MAP_FLAG_DONOTWAIT</strong> value.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="pMappedSubResource"></span><span id="pmappedsubresource"></span><span id="PMAPPEDSUBRESOURCE"></span>pMappedSubResource</p></td>
<td align="left"><p>Although the input value from the runtime isn&#39;t restricted, the driver must assign a valid CPU-cacheable pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541839" data-raw-source="[&lt;strong&gt;D3D10DDI_MAPPED_SUBRESOURCE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff541839)"><strong>D3D10DDI_MAPPED_SUBRESOURCE</strong></a>.<strong>pData</strong> member and must set the <strong>RowPitch</strong> and <strong>DepthPitch</strong> to match the size of the buffer and the data provided in <strong>pData</strong>.</p></td>
</tr>
</tbody>
</table>

 

[***ResourceUnmap***](https://msdn.microsoft.com/library/windows/hardware/ff569495) **function**—

These input parameters to [*ResourceUnmap*](https://msdn.microsoft.com/library/windows/hardware/ff569495) are restricted:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><span id="hDevice"></span><span id="hdevice"></span><span id="HDEVICE"></span><em>hDevice</em></p></td>
<td align="left"><p>Although the input value from the Direct3D runtime isn&#39;t restricted, the value which match the <em>hDevice</em> value from the original <a href="https://msdn.microsoft.com/library/windows/hardware/ff569492" data-raw-source="[&lt;em&gt;ResourceMap&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff569492)"><em>ResourceMap</em></a> call.</p></td>
</tr>
<tr class="even">
<td align="left"><p><span id="hResource"></span><span id="hresource"></span><span id="HRESOURCE"></span><em>hResource</em></p></td>
<td align="left"><p>The runtime sets only a <strong>D3D10DDIRESOURCE_BUFFER</strong> resource when a non-zero value for <em>MapFlags</em> is set in the creation call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff540694" data-raw-source="[&lt;em&gt;CreateResource(D3D11)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540694)"><em>CreateResource(D3D11)</em></a>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><span id="Subresource"></span><span id="subresource"></span><span id="SUBRESOURCE"></span><em>Subresource</em></p></td>
<td align="left"><p>The runtime only sets the value to 0.</p></td>
</tr>
</tbody>
</table>

 

 

 





