---
title: WMI Class Qualifier Definitions in Hbaapi.mof
description: WMI Class Qualifier Definitions in Hbaapi.mof
ms.assetid: 9db543f1-f6ad-4735-8ba0-21476aa229ba
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20WMI%20Class%20Qualifier%20Definitions%20in%20Hbaapi.mof%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




