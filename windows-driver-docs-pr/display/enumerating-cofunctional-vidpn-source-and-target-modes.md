---
title: Enumerating Cofunctional VidPN Source and Target Modes
description: Enumerating Cofunctional VidPN Source and Target Modes
ms.assetid: f1aa6277-7af6-4ba0-8ff1-d562f7029540
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

2.  The VidPN manager calls [**DxgkDdiIsSupportedVidPn**](https://msdn.microsoft.com/library/windows/hardware/ff559684) to determine whether the VidPN can be extended to form a functional VidPN that is supported on the display adapter. That is, it asks whether modes can be pinned on the remaining sources and targets without changing the existing pinned modes.

3.  The VidPN manager calls [**DxgkDdiEnumVidPnCofuncModality**](https://msdn.microsoft.com/library/windows/hardware/ff559649) to obtain the modes that are available on the sources and targets that do not yet have pinned modes.

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

-   [VidPN interface](https://msdn.microsoft.com/library/windows/hardware/ff570556).

    Begin by calling the [**pfnGetTopology**](https://msdn.microsoft.com/library/windows/hardware/ff562854) function to get a pointer to a [VidPN Topology interface](https://msdn.microsoft.com/library/windows/hardware/ff570560) that represents the constraining VidPN's topology.

-   [VidPN Topology interface](https://msdn.microsoft.com/library/windows/hardware/ff570560)

    Call the [**pfnAcquireFirstPathInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562092) and [**pfnAcquireNextPathInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562093) functions to get information about each path in the constraining VidPN's topology. Information about a particular path (source ID, target ID, scaling transformation, rotation transformation, target color basis, etc.) is contained in a [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](https://msdn.microsoft.com/library/windows/hardware/ff546647) structure.

-   [VidPN interface](https://msdn.microsoft.com/library/windows/hardware/ff570556)

    For each path, pass the path's source ID to the [**pfnAcquireSourceModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff562110) function to get the path's source.

-   [VidPN Source Mode Set interface](https://msdn.microsoft.com/library/windows/hardware/ff570558)

    Call the [**pfnAcquirePinnedModeInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562076) function to determine which mode (if any) is pinned in the source's mode set. If the source's mode set has a pinned mode, there is probably no need to examine the remaining modes in the set. If the mode set does not have a pinned mode, examine the remaining modes in the set by calling [**pfnAcquireFirstModeInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562074) and [**pfnAcquireNextModeInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562075).

    Use a similar procedure to examine the target mode sets and to determine which target mode sets have pinned modes.

### <span id="adjusting_mode_sets"></span><span id="ADJUSTING_MODE_SETS"></span>Adjusting mode sets

As you inspect the mode sets associated with sources and targets in the constraining VidPN's topology, take note of which mode sets have pinned modes. If a mode set does not have a pinned mode, determine whether it needs to be adjusted. A mode set must be adjusted if it contains modes that are not cofunctional with the constraints or if it lacks available modes that are cofunctional with the constraints.

For video present targets that have connected monitors, you must also consider the set of modes supported by the monitor. Even if a video present target on the display adapter supports a particular mode (given the constraints), you should only list that mode in the target's mode set if the connected monitor also supports the mode. To determine the modes supported by connected monitor, perform the following steps:

-   [DXGK\_MONITOR Interface](https://msdn.microsoft.com/library/windows/hardware/ff561949)

    Call [**pfnAcquireMonitorSourceModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff561953). If a mode set needs no adjustment, you can leave it alone. If a mode set needs to be adjusted, then you must create a new mode set and replace the existing mode set with the new one.

-   [VidPN interface](https://msdn.microsoft.com/library/windows/hardware/ff570556)

    To create and populate a new source mode set, call [**pfnCreateNewSourceModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff562845).

-   [VidPN Source Mode Set interface](https://msdn.microsoft.com/library/windows/hardware/ff570558)

    Then call [**pfnCreateNewModeInfo**](https://msdn.microsoft.com/library/windows/hardware/ff562078) and [**pfnAddMode**](https://msdn.microsoft.com/library/windows/hardware/ff562077).

-   [VidPN interface](https://msdn.microsoft.com/library/windows/hardware/ff570556)

    Finally call [**pfnAssignSourceModeSet**](https://msdn.microsoft.com/library/windows/hardware/ff562840) to replace the existing source mode set with the new one.

### <span id="adjusting_scaling_support_flags"></span><span id="ADJUSTING_SCALING_SUPPORT_FLAGS"></span>Adjusting scaling support flags

For each path in the constraining VidPN's topology, determine whether the path has a pinned scaling transformation. To make that determination, inspect *vpnPath*.**ContentTransformation.Scaling**, where *vpnPath* is the [**D3DKMDT\_VIDPN\_PRESENT\_PATH**](https://msdn.microsoft.com/library/windows/hardware/ff546647) structure that represents the path. If *vpnPath*.**ContentTransformation.Scaling** is set to **D3DKMDT\_VPPS\_IDENTITY**, **D3DKMDT\_VPPS\_CENTERED**, or **D3DKMDT\_VPPS\_STRETCHED**, then the scaling transformation for the path is pinned. Otherwise, the scaling transformation is not pinned.

If the path does not have a pinned scaling transformation, determine whether the path's scaling support flags need to be adjusted. The support flags must be adjusted if they show support for a type of scaling that is not cofunctional with the constraints or if they fail to show support for a type of scaling that is cofunctional with the constraints. To alter the scaling support flags, set the members of the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_SCALING\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546712) structure that holds the flags.

### <span id="adjusting_rotation_support_flags"></span><span id="ADJUSTING_ROTATION_SUPPORT_FLAGS"></span>Adjusting rotation support flags

Adjusting a path's rotation support flags is similar to adjusting a path's scaling support flags. Suppose *vpnPath* is a D3DKMDT\_VIDPN\_PRESENT\_PATH structure. If *vpnPath*.**ContentTransformation.Rotation** is set to **D3DKMDT\_VPPR\_IDENTITY**, **D3DKMDT\_VPPR\_ROTATE90**, **D3DKMDT\_VPPR\_ROTATE180**, or **D3DKMDT\_VPPR\_ROTATE270**, then the rotation transformation for the path is pinned. Otherwise, the rotation transformation is not pinned. The rotation support flags are in *vpnPath*.**ContentTransformation.RotationSupport**.

### <span id="reporting_multisampling_methods"></span><span id="REPORTING_MULTISAMPLING_METHODS"></span>Reporting multisampling methods

If the display adapter has one or more video output codecs that are capable of antialiasing by multisampling, then you must report the multisampling methods that are available (given the constraints), for each source that has a pinned mode. To report the available multisampling methods, perform the following steps:

-   Create an array of [D3DDDI\_MULTISAMPLINGMETHOD](https://msdn.microsoft.com/library/windows/hardware/ff544594) structures
-   Pass the array to the [**pfnAssignMultisamplingMethodSet**](https://msdn.microsoft.com/library/windows/hardware/ff562115) function of the VidPN interface.

The [D3DDDI\_MULTISAMPLINGMETHOD](https://msdn.microsoft.com/library/windows/hardware/ff544594) structure has two members, which you must set, that characterize a multisampling method. The **NumSamples** member indicates the number of subpixels that are sampled. The **NumQualityLevels** member indicates the number of quality levels at which the method can operate. You can specify any number of quality levels as long as each increase in level noticably improves the quality of the presented image.

### <span id="enumeration_pivots"></span><span id="ENUMERATION_PIVOTS"></span>Enumeration Pivots

As described previously, *DxgkDdiEnumVidPnCofuncModality* must create mode sets that are cofunctional with the VidPN passed in its *hConstrainingVidPn* parameter. In some cases, *DxgkDdiEnumVidPnCofuncModality* must augment its behavior according to additional information (an enumeration pivot) passed in the *EnumPivotType* and *EnumPivot* parameters.

The enumeration pivot can be one of the following:

-   The mode set of a particular video present source

-   The mode set of a particular video present target

-   The scaling transformation of a particular VidPN present path

-   The rotation transformation of a particular VidPN present path

If the enumeration pivot is a mode set, then *DxgkDdkEnumVidPnCofuncModality* must leave that mode set unchanged. If the enumeration pivot is the scaling (rotation) transformation of a path, then *DxgkDdiEnumVidPnCofuncModality* must not change the scaling (rotation) support flags for that path.

 

 





