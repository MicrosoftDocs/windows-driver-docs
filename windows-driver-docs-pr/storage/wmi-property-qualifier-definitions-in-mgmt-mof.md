---
title: WMI Property Qualifier Definitions in Mgmt.mof
description: WMI Property Qualifier Definitions in Mgmt.mof
ms.assetid: 2d8e7e83-6304-459f-b9d8-b40365834bb7
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# WMI Property Qualifier Definitions in Mgmt.mof


## <span id="ddk_wmi_property_qualifier_definitions_in_mgmt_mof_kr"></span><span id="DDK_WMI_PROPERTY_QUALIFIER_DEFINITIONS_IN_MGMT_MOF_KR"></span>


The WMI qualifiers that are defined in *Mgmt.mof* specify some of the data formats that the iSCSI discovery library and other management software can use to report information that is retrieved from iSCSI initiators.

The *Mgmt.mof* file defines the following WMI property qualifiers:

[ISCSI\_CONNECTION\_STATE\_TYPE\_QUALIFIERS](iscsi-connection-state-type-qualifiers.md)

[ISCSI\_CONNECTION\_PROTOCOL\_TYPE\_QUALIFIERS](iscsi-connection-protocol-type-qualifiers.md)

[ISCSI\_SESSION\_TYPE\_QUALIFIERS](iscsi-session-type-qualifiers.md)

[ISCSI\_HEADER\_INTEGRITY\_TYPE\_QUALIFIERS](iscsi-header-integrity-type-qualifiers.md)

[ISCSI\_DATA\_INTEGRITY\_TYPE\_QUALIFIERS](iscsi-data-integrity-type-qualifiers.md)

[ISCSI\_PORTAL\_TYPE\_QUALIFIERS](iscsi-portal-type-qualifiers.md)

[ISCSI\_INITIATOR\_NODE\_FAILURE\_TYPE\_QUALIFIERS](iscsi-initiator-node-failure-type-qualifiers.md)

[ISCSI\_INITIATOR\_FAILURE\_TYPE\_QUALIFIERS](iscsi-initiator-failure-type-qualifiers.md)

If you apply one of the preceding qualifiers to a data field in a WMI class definition, it indicates that you can assign any of the integer values that are indicated in the definition of the qualifier to the corresponding structure member.

Thus, a WMI property qualifier resembles an enumeration because the qualifier represents a set of integer values. But the WMI tool suite does not generate an enumeration declaration in *Iscsimgt.h* that corresponds to the qualifiers in *Mgmt.mof*, neither does it generate a set of symbolic constant definitions that correspond to the qualifier values.

For a general discussion of WMI property qualifiers, see [WMI Property Qualifiers](https://msdn.microsoft.com/library/windows/hardware/ff566365).

 

 





