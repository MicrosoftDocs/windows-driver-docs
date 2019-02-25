---
title: WMI Class Qualifier Definitions in Hbaapi.mof
description: WMI Class Qualifier Definitions in Hbaapi.mof
ms.assetid: 9db543f1-f6ad-4735-8ba0-21476aa229ba
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# WMI Class Qualifier Definitions in Hbaapi.mof


## <span id="ddk_wmi_class_qualifier_definitions_in_hbaapi_mof_kr"></span><span id="DDK_WMI_CLASS_QUALIFIER_DEFINITIONS_IN_HBAAPI_MOF_KR"></span>


The WMI class qualifiers defined by the *Hbaapi.mof* file are as follows:

[EVENT\_TYPES\_QUALIFIERS](event-types-qualifiers.md)

[HBA\_BIND\_TYPE](hba-bind-type.md)

[HBA\_STATUS](hba-status.md)

When one of the qualifiers that are described in this section is applied to a data field in a WMI class definition it indicates that the field can be assigned any of the set of predetermined integer values that are indicated in the definition of the qualifier in *Hbaapi.mof*. Thus each WMI class qualifier described here resembles an enumerator in that it represents a set of integer values, but the WMI tool suite does not generate an enumerator declaration in *Hbapiwmi.h* that corresponds to the qualifiers in *Hbaapi.mof*, nor does it generate a set of symbolic constant definitions that correspond to the qualifier values.

However, by including *Hbaapi.h* your driver or application can use a set of symbolic constants that were defined with a view to providing an easy-to-remember name for each value associated with the WMI class qualifiers that are defined in *Hbaapi.mof*.

For a general discussion of WMI class qualifiers, see [WMI Class Qualifiers](https://msdn.microsoft.com/library/windows/hardware/ff566348).

 

 





