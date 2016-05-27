---
title: Understanding Volume Enumerations with Duplicate Volume Names
author: windows-driver-content
description: Understanding Volume Enumerations with Duplicate Volume Names
ms.assetid: c05982dc-4124-4f9a-93b8-0e56ac296d1b
keywords: ["volumes WDK file system , duplicate names", "volumes WDK file system , enumerating", "filter manager WDK file system minifilter , volumes", "duplicate volume names WDK file system", "enumerating volumes WDK file system"]
---

# Understanding Volume Enumerations with Duplicate Volume Names


When enumerating volumes, it is possible for duplicate volume names to appear in a resulting volume information list.

To help understand why this can occur, consider the following scenario: the volume enumeration routine [**FltEnumerateVolumeInformation**](https://msdn.microsoft.com/library/windows/hardware/ff542091) is used to enumerate all system volumes. This results in a buffer filled with volume information structures - one for each volume known to filter manager. In this buffer, each volume information structure can be of type [**FILTER\_VOLUME\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff541631) or [**FILTER\_VOLUME\_STANDARD\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff541647), but not both.

Given this list of volume information structures, it is possible for multiple list elements to contain the same volume name. That is, the **FilterVolumeName** members of two or more list elements could be identical. This is possible because all filter manager enumeration routines, such as [**FltEnumerateVolumes**](https://msdn.microsoft.com/library/windows/hardware/ff542092), enumerate volumes including those that have been dismounted but have not been torn-down (due to the fact that open files still exist on the volume). Thus, when a volume becomes dismounted, its name can appear more than once in a volume information list - once for its current mounted state and once for its prior dismounted but non-torn-down state, in the simplest case.

If duplicate volume names appear in a volume information list, each group of identical names is explained by the above description. However, it is possible to confirm the above scenario by using the following procedures:

-   If the list is populated with structures of type FILTER\_VOLUME\_STANDARD\_INFORMATION, identify a group of structures whose **FilterVolumeName** members are equal. If one or more of the structures in this group has the FLTFL\_VSI\_DETACHED\_VOLUME flag set in its **Flags** member, the volume associated with the group was in a dismounted but non-torn-down state. This confirms why duplicate volume names exist. Repeat this procedure for all such remaining groups, if applicable.

-   If the list is populated with structures of type FILTER\_VOLUME\_BASIC\_INFORMATION, convert this list to its equivalent FILTER\_VOLUME\_STANDARD\_INFORMATION structure form and proceed as in the previous bullet point.

**Note**   The FILTER\_VOLUME\_STANDARD\_INFORMATION structure is only available starting with Windows Vista.

 

Routines and structures affected by this topic include the following:

[**FILTER\_VOLUME\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff541631)

[**FILTER\_VOLUME\_STANDARD\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff541647)

[**FilterVolumeFindFirst**](https://msdn.microsoft.com/library/windows/hardware/ff541525)

[**FilterVolumeFindNext**](https://msdn.microsoft.com/library/windows/hardware/ff541530)

[**FltEnumerateVolumeInformation**](https://msdn.microsoft.com/library/windows/hardware/ff542091)

[**FltEnumerateVolumes**](https://msdn.microsoft.com/library/windows/hardware/ff542092)

[**FltGetVolumeInformation**](https://msdn.microsoft.com/library/windows/hardware/ff543238)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Understanding%20Volume%20Enumerations%20with%20Duplicate%20Volume%20Names%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


