---
title: MSiSCSI\_Operations WMI Class
description: MSiSCSI\_Operations WMI Class
ms.assetid: 993118db-cddf-438a-8fdd-566353a6246b
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 





