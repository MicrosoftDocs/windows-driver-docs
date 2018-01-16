---
title: WMI Property Qualifier Definitions in Mgmt.mof
description: WMI Property Qualifier Definitions in Mgmt.mof
ms.assetid: 2d8e7e83-6304-459f-b9d8-b40365834bb7
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20WMI%20Property%20Qualifier%20Definitions%20in%20Mgmt.mof%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




