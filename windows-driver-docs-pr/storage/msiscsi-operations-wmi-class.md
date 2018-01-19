---
title: MSiSCSI\_Operations WMI Class
description: MSiSCSI\_Operations WMI Class
ms.assetid: 993118db-cddf-438a-8fdd-566353a6246b
---

# MSiSCSI\_Operations WMI Class


## <span id="ddk_msiscsi_operations_wmi_class_kr"></span><span id="DDK_MSISCSI_OPERATIONS_WMI_CLASS_KR"></span>


The MSiSCSI\_Operations WMI class provides the WMI methods that the iSCSI initiator service uses to communicate with HBA initiators.

Because this class is associated with a particular instance of a storage miniport driver, the miniport driver must register the class using the name of the particular physical device object (PDO) that the miniport driver manages.

This WMI class has no data blocks; therefore, when the WMI tool suite compiles this class definition, it does not produce any structure declarations that correspond to the class. Compilation does produce structure declarations that are associated with the class methods, and these are described in the reference pages for the class methods.

The managed object format (MOF) syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[AddConnectionToSession](addconnectiontosession.md)

[AddRADIUSServer](addradiusserver.md)

[DeleteInitiatorNodeName](deleteinitiatornodename.md)

[LoginToTarget](logintotarget.md)

[LogoutFromTarget](logoutfromtarget.md)

[RemoveConnectionFromSession](removeconnectionfromsession.md)

[RemovePersistentLogin](removepersistentlogin.md)

[RemoveRADIUSServer](removeradiusserver.md)

[**ScsiInquiry**](scsiinquiry.md)

[**ScsiReadCapacity**](scsireadcapacity.md)

[**ScsiReportLuns**](scsireportluns.md)

[SendTargets](sendtargets.md)

[SetCHAPSharedSecret](setchapsharedsecret.md)

[SetInitiatorNodeName](setinitiatornodename.md)

[SetRADIUSSharedSecret](setradiussharedsecret.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MSiSCSI_Operations%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




