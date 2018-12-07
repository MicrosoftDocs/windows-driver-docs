---
title: Understanding Volume Enumerations with Duplicate Volume Names
description: Understanding Volume Enumerations with Duplicate Volume Names
ms.assetid: c05982dc-4124-4f9a-93b8-0e56ac296d1b
keywords:
- volumes WDK file system , duplicate names
- volumes WDK file system , enumerating
- filter manager WDK file system minifilter , volumes
- duplicate volume names WDK file system
- enumerating volumes WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




