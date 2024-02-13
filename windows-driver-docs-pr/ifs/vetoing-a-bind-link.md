---
title: Vetoing a Bind Link
description: Minifilters can veto a bind link on the system boot partition starting in Windows 11, version 24H2.
ms.date: 02/12/2024
---

# Vetoing a bind link

[!NOTE]
> Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Starting in Windows 11, version 24H2, [bind links](/windows/win32/bindlink/) can be used to bind a file system namespace to a local "virtual path" through the Bind Filter (*bindflt.sys*).

Minifilters can choose to veto a bind link that changes directories they care about. For example, an antivirus filter can veto the bind link of a folder that stores its definition files.

Minifilters can veto a bind link only on the system's boot partition (DO_SYSTEM_BOOT_PARTITION). It's not possible to veto a bind link on any other partitions.

In response to a [**CreateBindLink**](/windows/win32/api/bindlink/nf-bindlink-createbindlink) request, *BindFlt* sends [**IRP_MJ_QUERY_OPEN**](flt-parameters-for-irp-mj-query-open.md) with the following parameters:

* [**FileInformationClass**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_file_information_class) is set to **FileStatBasicInformation**.
* **FileInformation** points to a [**FILE_STAT_BASIC_INFORMATION**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-file_stat_basic_information) structure.
* **Irp** has a **GUID_ECP_TYPE_VETO_BINDING** ECP with a [**VETO_BINDING_ECP_CONTEXT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-veto_binding_ecp_context) structure as the ECP context.

Since *BindFlt* is sending the IRP, a filter must sit below *BindFlt* in order to veto a bind link. Such a minifilter can watch for this IRP and veto the bind link by setting the **ShouldVetoBinding** member of the [**VETO_BINDING_ECP_CONTEXT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-veto_binding_ecp_context) structure to **TRUE**. In this event, *BindFlt* vetoes the bind link and returns an error to the caller.
