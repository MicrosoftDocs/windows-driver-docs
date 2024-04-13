---
title: WMI Property Qualifier Definitions in Config.mof
description: WMI Property Qualifier Definitions in Config.mof
ms.date: 10/17/2018
---

# WMI Property Qualifier Definitions in Config.mof


## <span id="ddk_wmi_property_qualifier_definitions_in_config_mof_kr"></span><span id="DDK_WMI_PROPERTY_QUALIFIER_DEFINITIONS_IN_CONFIG_MOF_KR"></span>


The WMI qualifiers that are defined in *Config.mof* specify some of the data formats that the iSCSI software uses to indicate the configuration of the network.

The *Config.mof* file defines the following WMI property qualifier:

[ENCRYPTION\_TYPES\_QUALIFIERS](encryption-types-qualifiers.md)

If you apply one of the preceding qualifiers to a data field in a WMI class definition, it indicates that you can assign any of the integer values that are indicated in the definition of the qualifier to the corresponding structure member.

For a general discussion of WMI property qualifiers, see [WMI Property Qualifiers](../kernel/wmi-property-qualifiers.md).

 

