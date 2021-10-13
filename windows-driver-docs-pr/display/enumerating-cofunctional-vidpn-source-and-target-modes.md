---
title: Enumerating Cofunctional VidPN Source and Target Modes
description: Enumerating Cofunctional VidPN Source and Target Modes
keywords:
- video present networks WDK display , enumerate target and source modes
- VidPN WDK display , enumerate target and source modes
- constraining VidPN WDK
- enumerating target and source modes WDK video present networks
- source modes WDK video present network
- target modes WDK video present network
- pinned scaling transformations WDK video present networks
- pinned rotation transformations WDK video present networks
- multisampling methods WDK video present networks
- mode sets WDK video present networks
- inspecting constraining VidPN WDK
- scaling support flags WDK video present networks
- rotation support flags WDK video present networks
- enumeration pivot WDK video present networks
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating Cofunctional VidPN Source and Target Modes


This topic describes how the video present network (VidPN) manager and the display miniport driver collaborate to enumerate modes that are available on video present sources and targets. Before reading this material, you should be familiar with the material in the following topics:

-   [Introduction to Video Present Networks](introduction-to-video-present-networks.md)

-   [VidPN Objects and Interfaces](vidpn-objects-and-interfaces.md)

From time to time, the VidPN manager asks the display miniport driver to enumerate the modes that are available on a display adapter's video present sources and targets. Typically, the request has the following pattern:

1.  The VidPN manager creates or obtains a VidPN that has modes pinned on some, but not all, of its sources and targets.

2.  The VidPN manager calls [**DxgkDdiIsSupportedVidPn**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_issupportedvidpn) to determine whether the VidPN can be extended to form a functional VidPN that is supported on the display adapter. That is, it asks whether modes can be pinned on the remaining sources and targets without changing the existing pinned modes.

3.  The VidPN manager calls [**DxgkDdiEnumVidPnCofuncModality**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_enumvidpncofuncmodality) to obtain the modes that are available on the sources and targets that do not yet have pinned modes.

One of the arguments passed to *DxgkDdiEnumVidPnCofuncModality* is a handle to a VidPN object called the constraining VidPN.

*DxgkDdiEnumVidPnCofuncModality* must do the following:

-   Inspect the constraining VidPN.

-   For each source and target that does not have a pinned mode, adjust the mode set so that it is the largest possible mode set that is cofunctional with the constraints.

-   For each path that does not have a pinned scaling transformation, adjust the scaling support flags so that they are cofunctional with the constraints.

-   For each path that does not have a pinned rotation transformation, adjust the rotation support flags so that they are cofunctional with the constraints.

-   For each source that has a pinned mode, report the multisampling methods that are available for that source.

The following paragraphs give details on how to perform each of the tasks in the previous bulleted list.

### <span id="inspecting_the_constraining_vidpn"></span><span id="INSPECTING_THE_CONSTRAINING_VIDPN"></span>Inspecting the constraining VidPN

The following properties of the constraining VidPN are the constraints that must be honored by *DxgkDdiEnumVidPnCofuncModality*.

-   Topology (the set of associations between sources and targets)

-   Pinned modes

-   Scaling, scaling support, rotation, and rotation support of each path

-   Target color basis of each path

-   Target color coefficient dynamic ranges of each path

-   Content type (graphics or video) of each path

-   Gamma ramp of each path

To extract the constraints from the constraining VidPN, perform the following steps:

-   Begin by calling the [**pfnGetTopology**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_gettopology) function to get a pointer to a [VidPN Topology interface](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpntopology_interface) that represents the constraining VidPN's topology.

-   Call the [**pfnAcquireFirstPathInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpntopology_acquirefirstpathinfo) and [**pfnAcquireNextPathInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpntopology_acquirenextpathinfo) functions to get information about each path in the constraining VidPN's topology. Information about a particular path (source ID, target ID, scaling transformation, rotation transformation, target color basis, etc.) is contained in a [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path) structure.

-   For each path, pass the path's source ID to the [**pfnAcquireSourceModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_acquiresourcemodeset) function to get the path's source.

-   Call the [**pfnAcquirePinnedModeInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_acquirepinnedmodeinfo) function to determine which mode (if any) is pinned in the source's mode set. If the source's mode set has a pinned mode, there is probably no need to examine the remaining modes in the set. If the mode set does not have a pinned mode, examine the remaining modes in the set by calling [**pfnAcquireFirstModeInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_acquirefirstmodeinfo) and [**pfnAcquireNextModeInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_acquirenextmodeinfo).

    Use a similar procedure to examine the target mode sets and to determine which target mode sets have pinned modes.

### <span id="adjusting_mode_sets"></span><span id="ADJUSTING_MODE_SETS"></span>Adjusting mode sets

As you inspect the mode sets associated with sources and targets in the constraining VidPN's topology, take note of which mode sets have pinned modes. If a mode set does not have a pinned mode, determine whether it needs to be adjusted. A mode set must be adjusted if it contains modes that are not cofunctional with the constraints or if it lacks available modes that are cofunctional with the constraints.

For video present targets that have connected monitors, you must also consider the set of modes supported by the monitor. Even if a video present target on the display adapter supports a particular mode (given the constraints), you should only list that mode in the target's mode set if the connected monitor also supports the mode. To determine the modes supported by connected monitor, perform the following steps:

-   [DXGK\_MONITOR Interface](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_monitor_interface)

    Call [**pfnAcquireMonitorSourceModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_monitor_acquiremonitorsourcemodeset). If a mode set needs no adjustment, you can leave it alone. If a mode set needs to be adjusted, then you must create a new mode set and replace the existing mode set with the new one.

-   [DXGK_VIDPN_INTERFACE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpn_interface)

    To create and populate a new source mode set, call [**pfnCreateNewSourceModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_createnewsourcemodeset).

-   [_DXGK_VIDPNSOURCEMODESET_INTERFACE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpnsourcemodeset_interface)

    Then call [**pfnCreateNewModeInfo**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_createnewmodeinfo) and [**pfnAddMode**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpnsourcemodeset_addmode).

-   [DXGK_VIDPN_INTERFACE](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpn_interface)

    Finally call [**pfnAssignSourceModeSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_assignsourcemodeset) to replace the existing source mode set with the new one.

### Adjusting scaling support flags

For each path in the constraining VidPN's topology, determine whether the path has a pinned scaling transformation. To make that determination, inspect *vpnPath*.**ContentTransformation.Scaling**, where *vpnPath* is the [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path) structure that represents the path. If *vpnPath*.**ContentTransformation.Scaling** is set to **D3DKMDT\_VPPS\_IDENTITY**, **D3DKMDT\_VPPS\_CENTERED**, or **D3DKMDT\_VPPS\_STRETCHED**, then the scaling transformation for the path is pinned. Otherwise, the scaling transformation is not pinned.

If the path does not have a pinned scaling transformation, determine whether the path's scaling support flags need to be adjusted. The support flags must be adjusted if they show support for a type of scaling that is not cofunctional with the constraints or if they fail to show support for a type of scaling that is cofunctional with the constraints. To alter the scaling support flags, set the members of the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_vidpn_present_path_scaling_support) structure that holds the flags.

### Adjusting rotation support flags

Adjusting a path's rotation support flags is similar to adjusting a path's scaling support flags. Suppose *vpnPath* is a D3DKMDT\_VIDPN\_PRESENT\_PATH structure. If *vpnPath*.**ContentTransformation.Rotation** is set to **D3DKMDT\_VPPR\_IDENTITY**, **D3DKMDT\_VPPR\_ROTATE90**, **D3DKMDT\_VPPR\_ROTATE180**, or **D3DKMDT\_VPPR\_ROTATE270**, then the rotation transformation for the path is pinned. Otherwise, the rotation transformation is not pinned. The rotation support flags are in *vpnPath*.**ContentTransformation.RotationSupport**.

### <span id="reporting_multisampling_methods"></span><span id="REPORTING_MULTISAMPLING_METHODS"></span>Reporting multisampling methods

If the display adapter has one or more video output codecs that are capable of antialiasing by multisampling, then you must report the multisampling methods that are available (given the constraints), for each source that has a pinned mode. To report the available multisampling methods, perform the following steps:

-   Create an array of [D3DDDI\_MULTISAMPLINGMETHOD](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_multisamplingmethod) structures
-   Pass the array to the [**pfnAssignMultisamplingMethodSet**](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_vidpn_assignmultisamplingmethodset) function of the [VidPN interface](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidpn_interface).

The [D3DDDI\_MULTISAMPLINGMETHOD](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_multisamplingmethod) structure has two members, which you must set, that characterize a multisampling method. The **NumSamples** member indicates the number of subpixels that are sampled. The **NumQualityLevels** member indicates the number of quality levels at which the method can operate. You can specify any number of quality levels as long as each increase in level noticably improves the quality of the presented image.

### <span id="enumeration_pivots"></span><span id="ENUMERATION_PIVOTS"></span>Enumeration Pivots

As described previously, *DxgkDdiEnumVidPnCofuncModality* must create mode sets that are cofunctional with the VidPN passed in its *hConstrainingVidPn* parameter. In some cases, *DxgkDdiEnumVidPnCofuncModality* must augment its behavior according to additional information (an enumeration pivot) passed in the *EnumPivotType* and *EnumPivot* parameters.

The enumeration pivot can be one of the following:

-   The mode set of a particular video present source

-   The mode set of a particular video present target

-   The scaling transformation of a particular VidPN present path

-   The rotation transformation of a particular VidPN present path

If the enumeration pivot is a mode set, then *DxgkDdkEnumVidPnCofuncModality* must leave that mode set unchanged. If the enumeration pivot is the scaling (rotation) transformation of a path, then *DxgkDdiEnumVidPnCofuncModality* must not change the scaling (rotation) support flags for that path.

 

