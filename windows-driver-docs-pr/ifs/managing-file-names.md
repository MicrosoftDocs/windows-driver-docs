---
title: Managing File Names
description: Managing File Names
keywords:
- filter manager WDK file system minifilter , file names
- file names WDK file system minifilter
- names WDK file systems
ms.date: 04/20/2017
---

# Managing File Names


The filter manager eliminates much of the work required for legacy filter drivers to retrieve and manage file names. When a name is requested, the filter manager provides the name in a reference-counted structure in the appropriate format for the current operation: normalized name, opened name, or short name.

A minifilter driver can call [**FltGetDestinationFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetdestinationfilenameinformation) to construct a full destination path name for a file or directory that is being renamed or for which an NTFS hard link is being created. This name can be returned in either normalized or opened-file format.

The filter manager also provides the [**FltGetTunneledName**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgettunneledname) routine for retrieving normalized file name information that is invalidated due to file name tunneling.

To improve performance, the filter manager places names in a cache (where possible) that is shared among all minifilter drivers in the system. A minifilter driver can query either the cache or the file system, or both.

Minifilter drivers that modify the namespace can take advantage of the filter manager's support for name providers by registering callback routines to intercept name query operations, such as requests by upper minifilter drivers to generate or normalize a name.

### <span id="Filter_Manager_Routines_for_Name_Management"></span><span id="filter_manager_routines_for_name_management"></span><span id="FILTER_MANAGER_ROUTINES_FOR_NAME_MANAGEMENT"></span>Filter Manager Routines for Name Management

The filter manager provides the following support routines for name management:

[**FltGetDestinationFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetdestinationfilenameinformation)

[**FltGetFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilenameinformation)

[**FltGetFileNameInformationUnsafe**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgetfilenameinformationunsafe)

[**FltGetTunneledName**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltgettunneledname)

[**FltParseFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltparsefilenameinformation)

[**FltReleaseFileNameInformation**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleasefilenameinformation)

### <span id="Minifilter_Driver_Callback_Routines_for_Name_Management"></span><span id="minifilter_driver_callback_routines_for_name_management"></span><span id="MINIFILTER_DRIVER_CALLBACK_ROUTINES_FOR_NAME_MANAGEMENT"></span>Minifilter Driver Callback Routines for Name Management

The following callback routines are stored in the [**FLT\_REGISTRATION**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration) structure that is passed as a parameter to [**FltRegisterFilter**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltregisterfilter), for minifilter drivers that modify the namespace:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Callback Routine Name</th>
<th align="left">Callback Routine Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><em>GenerateFileNameCallback</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_generate_file_name" data-raw-source="[&lt;strong&gt;PFLT_GENERATE_FILE_NAME&lt;/strong&gt;](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_generate_file_name)"><strong>PFLT_GENERATE_FILE_NAME</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><em>NormalizeContextCleanupCallback</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_normalize_context_cleanup" data-raw-source="[&lt;strong&gt;PFLT_NORMALIZE_CONTEXT_CLEANUP&lt;/strong&gt;](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_normalize_context_cleanup)"><strong>PFLT_NORMALIZE_CONTEXT_CLEANUP</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><em>NormalizeNameComponentCallback</em></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_normalize_name_component" data-raw-source="[&lt;strong&gt;PFLT_NORMALIZE_NAME_COMPONENT&lt;/strong&gt;](/windows-hardware/drivers/ddi/fltkernel/nc-fltkernel-pflt_normalize_name_component)"><strong>PFLT_NORMALIZE_NAME_COMPONENT</strong></a></p></td>
</tr>
</tbody>
</table>

 

