---
title: VidPN Objects and Interfaces
description: VidPN Objects and Interfaces
ms.assetid: 5dedac8c-9a99-4b3a-81be-39819135cd97
keywords:
- video present networks WDK display , objects
- VidPN WDK display , objects
- objects WDK video present network
- interfaces WDK video present network
- video present networks WDK display , interfaces
- VidPN WDK display , interfaces
- sub-objects WDK video present network
ms.date: 10/30/2018
ms.localizationpriority: medium
---

# VidPN Objects and Interfaces


The video present network (VidPN) manager uses a VidPN object to maintain information about associations between video present sources, video present targets, and display modes. For more information, see the [Introduction to Video Present Networks](introduction-to-video-present-networks.md) topic.

## VidPN object

A VidPN object contains the following sub-objects.

-   Topology

-   Source mode set

-   Target mode set

-   Monitor source mode set

-   Monitor frequency range set

-   Monitor descriptor set

-   Path

-   Source

-   Target

-   Source mode

-   Target mode

-   Monitor source mode

The following diagram illustrates a VidPN object and its sub-objects.

![diagram illustrating a vidpn object and its sub-objects](images/vidpnobject.png)

The preceding diagram illustrates whether a particular association is one-to-one, one-to-many, many-to-one, or many-to-many. For example, the diagram shows that a source can belong to more than one path, but a target can belong to only one path.

The blue objects in the diagram are accessed through handles and interfaces, and the gray objects are accessed through structure pointers. An interface in this context is a structure that contains function pointers. For example, the [**DXGK\_VIDPNTOPOLOGY\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntopology_interface) structure contains pointers to functions (implemented by the VidPN manager) that the display miniport driver calls to inspect and alter a topology object. When the display miniport driver calls any one of those functions, it must supply a handle to a topology object. The following table lists the handle, interface, and pointer data types used to access a VidPN object and its sub-objects.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Object</th>
<th align="left">Access method and data type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>VidPN (VidPN Interface)</p></td>
<td align="left"><p>Accessed through handle and interface.</p>
<p>D3DKMDT_HVIDPN</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpn_interface" data-raw-source="[&lt;strong&gt;DXGK_VIDPN_INTERFACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpn_interface)"><strong>DXGK_VIDPN_INTERFACE</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Topology (VidPN Topology Interface)</p></td>
<td align="left"><p>Accessed through handle and interface.</p>
<p>D3DKMDT_HVIDPNTOPOLOGY</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntopology_interface" data-raw-source="[&lt;strong&gt;DXGK_VIDPNTOPOLOGY_INTERFACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntopology_interface)"><strong>DXGK_VIDPNTOPOLOGY_INTERFACE</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Source mode set (VidPN Source Mode Set Interface)</p></td>
<td align="left"><p>Accessed through handle and interface.</p>
<p>D3DKMDT_HVIDPNSOURCEMODESET</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpnsourcemodeset_interface" data-raw-source="[&lt;strong&gt;DXGK_VIDPNSOURCEMODESET_INTERFACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpnsourcemodeset_interface)"><strong>DXGK_VIDPNSOURCEMODESET_INTERFACE</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Target mode set (VidPN Target Mode Set Interface)</p></td>
<td align="left"><p>Accessed through handle and interface.</p>
<p>D3DKMDT_HVIDPNTARGETMODESET</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntargetmodeset_interface" data-raw-source="[&lt;strong&gt;DXGK_VIDPNTARGETMODESET_INTERFACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntargetmodeset_interface)"><strong>DXGK_VIDPNTARGETMODESET_INTERFACE</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Monitor source mode set</p></td>
<td align="left"><p>Accessed through handle and interface.</p>
<p>D3DKMDT_HMONITORSOURCEMODESET</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitorsourcemodeset_interface" data-raw-source="[&lt;strong&gt;DXGK_MONITORSOURCEMODESET_INTERFACE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitorsourcemodeset_interface)"><strong>DXGK_MONITORSOURCEMODESET_INTERFACE</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Path</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path" data-raw-source="[&lt;strong&gt;D3DKMDT_VIDPN_PRESENT_PATH&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path)"><strong>D3DKMDT_VIDPN_PRESENT_PATH</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Source</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_present_source" data-raw-source="[&lt;strong&gt;D3DKMDT_VIDEO_PRESENT_SOURCE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_present_source)"><strong>D3DKMDT_VIDEO_PRESENT_SOURCE</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Target</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_present_target" data-raw-source="[&lt;strong&gt;D3DKMDT_VIDEO_PRESENT_TARGET&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_present_target)"><strong>D3DKMDT_VIDEO_PRESENT_TARGET</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Source mode</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_source_mode" data-raw-source="[&lt;strong&gt;D3DKMDT_VIDPN_SOURCE_MODE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_source_mode)"><strong>D3DKMDT_VIDPN_SOURCE_MODE</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Target mode</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_target_mode" data-raw-source="[&lt;strong&gt;D3DKMDT_VIDPN_TARGET_MODE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_target_mode)"><strong>D3DKMDT_VIDPN_TARGET_MODE</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Monitor source mode</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p><a href="/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_monitor_source_mode" data-raw-source="[&lt;strong&gt;D3DKMDT_MONITOR_SOURCE_MODE&lt;/strong&gt;](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_monitor_source_mode)"><strong>D3DKMDT_MONITOR_SOURCE_MODE</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p>Monitor frequency range set</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p>[<strong>DXGK_MONITORFREQUENCYRANGESET_INTERFACE </strong>](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitorfrequencyrangeset_interface)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Monitor descriptor set</p></td>
<td align="left"><p>Accessed through structure pointer.</p>
<p>[<strong>DXGK_MONITORDESCRIPTORSET_INTERFACE</strong>](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitordescriptorset_interface)</p></td>
</tr>
</tbody>
</table>

## VidPN Manager

The VidPN manager, which is one of the components of the DirectX graphics kernel subsystem, cooperates with the display miniport driver to build and maintain VidPNs. The following steps describe how the display miniport driver obtains a handle and an interface to a VidPN object.

1.  During initialization, the DirectX graphics kernel subsystem calls the display miniport driver's [*DxgkDdiStartDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device) function. That call provides the display miniport driver with a [**DXGKRNL\_INTERFACE**](/windows-hardware/drivers/ddi/index) structure, which contains pointers to functions implemented by the DirectX graphics kernel subsystem. One of those functions is [*DxgkCbQueryVidPnInterface*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_queryvidpninterface).

2.  At some point, the VidPN manager needs help from the display miniport driver, so it provides the display miniport driver with a handle to a VidPN object by calling one of the following functions:
    -   [*DxgkDdiIsSupportedVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_issupportedvidpn)
    -   [*DxgkDdiRecommendFunctionalVidPn*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_recommendfunctionalvidpn)
    -   [*DxgkDdiEnumVidPnCofuncModality*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality)

3.  The display miniport driver passes the handle obtained in Step 2 to [*DxgkCbQueryVidPnInterface*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkcb_queryvidpninterface), which returns a pointer to a [**DXGK\_VIDPN\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpn_interface) structure.

After the display miniport driver has a handle and an interface to a VidPN object, it can get handles and interfaces (as needed) to the primary sub-objects: topology, source mode set, target mode set, and monitor source mode set. For example, the display miniport driver can call [*pfnGetTopology*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_gettopology) (one of the functions in the VidPN interface) to get a handle to a VidPN topology object and a pointer to a [**DXGK\_VIDPNTOPOLOGY\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntopology_interface) structure.

The following functions (in the VidPN interface) provide handles and interfaces to the primary sub-objects of a VidPN object.

-   [*pfnGetTopology*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_gettopology)
-   [*pfnAcquireSourceModeSet*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_acquiresourcemodeset)
-   [*pfnAcquireTargetModeSet*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_acquiretargetmodeset)

Note that two of the functions in the preceding list have corresponding functions that release VidPN sub-objects.

-   [*pfnReleaseSourceModeSet*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_releasesourcemodeset)

-   [*pfnReleaseTargetModeSet*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_releasetargetmodeset)

After the display miniport driver obtains a handle and an interface to one of a VidPNs primary sub-objects, it can call the interface functions to get descriptors of objects related to the sub-object. For example, given a handle and an interface to a topology object, the display miniport driver could perform the following steps to get descriptors of all the paths in topology.

1.  [VidPN Topology interface](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntopology_interface)

    Call the [*pfnAcquireFirstPathInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpntopology_acquirefirstpathinfo) function of the VidPN topology interface to obtain a pointer to a [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path) structure that describes the first path in the topology.

2.  [VidPN Topology interface](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntopology_interface)

    Call the [*pfnAcquireNextPathInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpntopology_acquirenextpathinfo) function repeatedly to obtain pointers to D3DKMDT\_VIDPN\_PRESENT\_PATH structures that describe the remaining paths in the topology.

Similarly, the display miniport driver can get descriptors of the modes in a mode set by calling the *pfnAcquireFirstModeInfo* and *pfnAcquireNextModeInfo* functions of any of the following mode set interfaces.

-   [**DXGK\_VIDPNSOURCEMODESET\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpnsourcemodeset_interface)

-   [**DXGK\_VIDPNTARGETMODESET\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntargetmodeset_interface)

-   [**DXGK\_MONITORSOURCEMODESET\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitorsourcemodeset_interface)

Note that the [**DXGK\_VIDPNSOURCEMODESET\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpnsourcemodeset_interface) interface has no function for removing a mode from a source mode set. When the display miniport driver needs to update a source mode set, it does not alter an existing mode set by adding and removing modes. Instead, it creates a new mode set that replaces the old mode set. An example of a function that must update mode sets is the display miniport driver's [*DxgkDdiEnumVidPnCofuncModality*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality) function. The steps involved in updating a source mode set are as follows:

1.  Call the [*pfnCreateNewModeInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_createnewmodeinfo) of the [**DXGK\_VIDPNSOURCEMODESET\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpnsourcemodeset_interface) interface to get a pointer to a [**D3DKMDT\_VIDPN\_SOURCE\_MODE**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_source_mode) structure (allocated by the VidPN manager).

    Call [*pfnAddMode*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_addmode) repeatedly to add modes to the source mode set.

2.  Call the [*pfnAssignSourceModeSet*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_assignsourcemodeset) function of the [**DXGK\_VIDPN\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpn_interface) to assign the new mode set to a particular video present source. The new source mode set replaces the source mode set that is currently assigned to that source.

Updating a target mode set is similar to updating a source mode set. The [**DXGK\_VIDPNTARGETMODESET\_INTERFACE**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntargetmodeset_interface) interface has the following functions:

-   [VidPN Target Mode Set interface](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_target_mode)

    A [*pfnCreateNewModeInfo*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpntargetmodeset_createnewmodeinfo) function for creating a new target mode set and a [*pfnAddMode*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpntargetmodeset_addmode) function for adding modes to the set.

There is no interface (set of functions) for obtaining the source and target that belong to a particular path. The display miniport driver can determine which source and target belong to a particular path by inspecting the **VidPnSourceId** and **VidPnTargetId** members of the [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path) structure that represents the path.

## See also

[Determining Whether a VidPN is Supported on a Display Adapter](determining-whether-a-vidpn-is-supported-on-a-display-adapter.md)

[Enumerating Cofunctional VidPN Source and Target Modes](enumerating-cofunctional-vidpn-source-and-target-modes.md)

[Video Present Network Terminology](video-present-network-terminology.md)

[Obtaining Additional Monitor Target Modes](obtaining-additional-monitor-target-modes.md)