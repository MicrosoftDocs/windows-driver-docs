---
title: File System Filter Driver Classes and Class GUIDs
description: File System Filter Driver Classes and Class GUIDs
ms.assetid: dd247b06-4529-4818-9239-b89c25f5c1df
keywords:
- GUIDs WDK file system
- class GUIDs WDK file system
- classes WDK file system
- filter drivers WDK file system , classes
- file system filter drivers WDK , classes
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Filter Driver Classes and Class GUIDs


## <span id="ddk_file_system_filter_driver_classes_and_class_guids_if"></span><span id="DDK_FILE_SYSTEM_FILTER_DRIVER_CLASSES_AND_CLASS_GUIDS_IF"></span>


Microsoft Windows XP and later operating systems provide setup classes for file system filter drivers. These classes provide a subset of the functionality that system-supplied device setup classes provide for hardware devices. (For more information about setup classes for hardware devices, see [Device Setup Classes](https://msdn.microsoft.com/library/windows/hardware/ff541509).)

Each setup class is associated with a class GUID. The system-defined class GUIDs are defined in devguid.h.

This topic lists the setup classes for file system filter drivers. In the definition for each class, the **Class** and **ClassGuid** entries contain the values that you should specify in the [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502) of a filter's INF file. Your filter driver should use the class and GUID that match the load order group that is specified in your driver's INF file.

Supplying the appropriate class GUID value in the INF file for a device, rather than, or in addition to, the **Class** = *class-name* entry, significantly improves the performance of searching system INF files.

The following list includes system-defined classes and class GUIDs for file system filter drivers. The entries in this list correspond to the load order groups that were created for file system filter drivers in Windows XP and later operating systems.

**Note**   Three load order groups do not appear in the list, because they are not considered setup classes and thus do not have class GUIDs assigned to them: Filter, FSFilter Top, and FSFilter Bottom.

 

<span id="FSFilter_Activity_Monitor"></span><span id="fsfilter_activity_monitor"></span><span id="FSFILTER_ACTIVITY_MONITOR"></span>FSFilter Activity Monitor<br/>
Class = ActivityMonitor<br/>
ClassGuid = {b86dff51-a31e-4bac-b3cf-e8cfe75c9fc2}

<span id="FSFilter_Undelete"></span><span id="fsfilter_undelete"></span><span id="FSFILTER_UNDELETE"></span>FSFilter Undelete<br/>
Class = Undelete<br/>
ClassGuid = {fe8f1572-c67a-48c0-bbac-0b5c6d66cafb}

<span id="FSFilter_Anti-Virus"></span><span id="fsfilter_anti-virus"></span><span id="FSFILTER_ANTI-VIRUS"></span>FSFilter Anti-Virus<br/>
Class = AntiVirus<br/>
ClassGuid = {b1d1a169-c54f-4379-81db-bee7d88d7454}

<span id="FSFilter_Replication"></span><span id="fsfilter_replication"></span><span id="FSFILTER_REPLICATION"></span>FSFilter Replication<br/>
Class = Replication<br/>
ClassGuid = {48d3ebc4-4cf8-48ff-b869-9c68ad42eb9f}

<span id="FSFilter_Continuous_Backup"></span><span id="fsfilter_continuous_backup"></span><span id="FSFILTER_CONTINUOUS_BACKUP"></span>FSFilter Continuous Backup<br/>
Class = ContinuousBackup<br/>
ClassGuid = {71aa14f8-6fad-4622-ad77-92bb9d7e6947}

<span id="FSFilter_Content_Screener"></span><span id="fsfilter_content_screener"></span><span id="FSFILTER_CONTENT_SCREENER"></span>FSFilter Content Screener<br/>
Class = ContentScreener<br/>
ClassGuid = {3e3f0674-c83c-4558-bb26-9820e1eba5c5}

<span id="FSFilter_Quota_Management"></span><span id="fsfilter_quota_management"></span><span id="FSFILTER_QUOTA_MANAGEMENT"></span>FSFilter Quota Management<br/>
Class = QuotaManagement<br/>
ClassGuid = {8503c911-a6c7-4919-8f79-5028f5866b0c}

<span id="FSFilter_Cluster_File_System"></span><span id="fsfilter_cluster_file_system"></span><span id="FSFILTER_CLUSTER_FILE_SYSTEM"></span>FSFilter Cluster File System<br/>
Class = CFSMetaDataServer<br/>
ClassGuid = {cdcf0939-b75b-4630-bf76-80f7ba655884}

<span id="FSFilter_HSM"></span><span id="fsfilter_hsm"></span><span id="FSFILTER_HSM"></span>FSFilter HSM<br/>
Class = HSM<br/>
ClassGuid = {d546500a-2aeb-45f6-9482-f4b1799c3177}

<span id="FSFilter_Compression"></span><span id="fsfilter_compression"></span><span id="FSFILTER_COMPRESSION"></span>FSFilter Compression<br/>
Class = Compression<br/>
ClassGuid = {f3586baf-b5aa-49b5-8d6c-0569284c639f}

<span id="FSFilter_Encryption"></span><span id="fsfilter_encryption"></span><span id="FSFILTER_ENCRYPTION"></span>FSFilter Encryption<br/>
Class = Encryption<br/>
ClassGuid = {a0a701c0-a511-42ff-aa6c-06dc0395576f}

<span id="FSFilter_Physical_Quota_Management"></span><span id="fsfilter_physical_quota_management"></span><span id="FSFILTER_PHYSICAL_QUOTA_MANAGEMENT"></span>FSFilter Physical Quota Management<br/>
Class = PhysicalQuotaManagement<br/>
ClassGuid = {6a0a8e78-bba6-4fc4-a709-1e33cd09d67e}

<span id="FSFilter_Open_File"></span><span id="fsfilter_open_file"></span><span id="FSFILTER_OPEN_FILE"></span>FSFilter Open File<br/>
Class = OpenFileBackup<br/>
ClassGuid = {f8ecafa6-66d1-41a5-899b-66585d7216b7}

<span id="FSFilter_Security_Enhancer"></span><span id="fsfilter_security_enhancer"></span><span id="FSFILTER_SECURITY_ENHANCER"></span>FSFilter Security Enhancer<br/>
Class = SecurityEnhancer<br/>
ClassGuid = {d02bc3da-0c8e-4945-9bd5-f1883c226c8c}

<span id="FSFilter_Copy_Protection"></span><span id="fsfilter_copy_protection"></span><span id="FSFILTER_COPY_PROTECTION"></span>FSFilter Copy Protection<br/>
Class = CopyProtection<br/>
ClassGuid = {89786ff1-9c12-402f-9c9e-17753c7f4375}

<span id="FSFilter_System"></span><span id="fsfilter_system"></span><span id="FSFILTER_SYSTEM"></span>FSFilter System<br/>
Class = FSFilterSystem<br/>
ClassGuid = {5d1b9aaa-01e2-46af-849f-272b3f324c46}

<span id="FSFilter_Infrastructure"></span><span id="fsfilter_infrastructure"></span><span id="FSFILTER_INFRASTRUCTURE"></span>FSFilter Infrastructure<br/>
Class = Infrastructure<br/>
ClassGuid = {e55fa6f9-128c-4d04-abab-630c74b1453a}
 

 




