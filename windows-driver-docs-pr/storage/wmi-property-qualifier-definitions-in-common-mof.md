---
title: WMI Property Qualifier Definitions in Common.mof
description: WMI Property Qualifier Definitions in Common.mof
ms.assetid: 24a95c4b-f4f4-4042-9a06-069685ac0260
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# WMI Property Qualifier Definitions in Common.mof


## <span id="ddk_wmi_property_qualifier_definitions_in_common_mof_kr"></span><span id="DDK_WMI_PROPERTY_QUALIFIER_DEFINITIONS_IN_COMMON_MOF_KR"></span>


The *Common.mof* file defines the following WMI property qualifiers:

[ISCSI\_AUTH\_TYPES\_QUALIFIERS](iscsi-auth-types-qualifiers.md)

[ISCSI\_STATUS\_QUALIFIERS](iscsi-status-qualifiers.md)

[SECURITY\_FLAG\_QUALIFIERS](security-flag-qualifiers.md)

If you apply one of the preceding qualifiers to a data field in a WMI class definition, it indicates that you can assign any of the integer values that are indicated in the definition of the qualifier to the corresponding structure member.

Thus, a WMI property qualifier resembles an enumeration because the qualifier represents a set of integer values. But the WMI tool suite does not generate an enumeration declaration in *Iscsidef.h* that corresponds to the qualifiers in *Common.mof*, neither does it generate a set of symbolic constant definitions that correspond to the qualifier values.

For a general discussion of WMI property qualifiers, see [WMI Property Qualifiers](https://msdn.microsoft.com/library/windows/hardware/ff566365).

 

 





