---
title: MPIO WMI Classes
description: MPIO WMI Classes
ms.assetid: c1719f9e-7b45-4de5-b847-6041b89e2677
---

# MPIO WMI Classes


The MPIO WMI classes that are defined in *Mpiowmi.mof*, *Mpiopdow.mof,* and *Mpiolbpo.mof* allow applications to understand the topology of the storage network. They also expose some classes to control certain DSM timers that affect different areas of functionality, as described in the following examples:

-   The amount of time to retain a LUN's device object even after it has lost all its paths.

-   The number of times a failed I/O should be retried before it is sent back to the application.

-   Whether regular path verification needs to be performed by MPIO.

The following topics describe the classes that make up the MPIO WMI interface:

[MPIO\_PATH\_HEALTH\_CLASS WMI Class](mpio-path-health-class-wmi-class.md)

[MPIO\_PATH\_HEALTH\_INFO WMI Class](mpio-path-health-info-wmi-class.md)

[MPIO\_DISK\_HEALTH\_CLASS WMI Class](mpio-disk-health-class-wmi-class.md)

[MPIO\_DISK\_HEALTH\_INFO WMI Class](mpio-disk-health-info-wmi-class.md)

[SCSI\_ADDR WMI Class](scsi-addr-wmi-class.md)

[MPIO\_DRIVE\_INFO WMI Class](mpio-drive-info-wmi-class.md)

[MPIO\_DISK\_INFO WMI Class](mpio-disk-info-wmi-class.md)

[DSM\_VERSION WMI Class](dsm-version-wmi-class.md)

[DSM\_COUNTERS WMI Class](dsm-counters-wmi-class.md)

[DSM\_PARAMETERS WMI Class](dsm-parameters-wmi-class.md)

[MPIO\_REGISTERED\_DSM WMI Class](mpio-registered-dsm-wmi-class.md)

[MPIO\_ADAPTER\_INFORMATION WMI Class](mpio-adapter-information-wmi-class.md)

[MPIO\_PATH\_INFORMATION WMI Class](mpio-path-information-wmi-class.md)

[MPIO\_CONTROLLER\_INFO WMI Class](mpio-controller-info-wmi-class.md)

[MPIO\_CONTROLLER\_CONFIGURATION WMI Class](mpio-controller-configuration-wmi-class.md)

[MPIO\_TIMERS\_COUNTERS WMI Class](mpio-timers-counters-wmi-class.md)

[MPIO\_WMI\_METHODS WMI Class](mpio-wmi-methods-wmi-class.md)

[MPIO\_EventEntry WMI Class](mpio-evententry-wmi-class.md)

[PDOSCSI\_ADDR WMI Class](pdoscsi-addr-wmi-class.md)

[PDO\_INFORMATION WMI Class](pdo-information-wmi-class.md)

[MPIO\_GET\_DESCRIPTOR WMI Class](mpio-get-descriptor-wmi-class.md)

[MPIO\_DEVINSTANCE\_HEALTH\_CLASS WMI Class](mpio-devinstance-health-class-wmi-class.md)

[MPIO\_DEVINSTANCE\_HEALTH\_INFO WMI Class](mpio-devinstance-health-info-wmi-class.md)

[MPIO\_DSM\_Path\_V2 WMI Class](mpio-dsm-path-v2-wmi-class.md)

[DSM\_Load\_Balance\_Policy\_V2 WMI Class](dsm-load-balance-policy-v2-wmi-class.md)

[DSM\_QueryLBPolicy\_V2 WMI Class](dsm-querylbpolicy-v2-wmi-class.md)

[DSM\_QuerySupportedLBPolicies\_V2 WMI Class](dsm-querysupportedlbpolicies-v2-wmi-class.md)

[MPIO\_DSM\_Path WMI Class](mpio-dsm-path-wmi-class.md)

[DSM\_Load\_Balance\_Policy WMI Class](dsm-load-balance-policy-wmi-class.md)

[DSM\_QueryLBPolicy WMI Class](dsm-querylbpolicy-wmi-class.md)

[DSM\_QuerySupportedLBPolicies WMI Class](dsm-querysupportedlbpolicies-wmi-class.md)

[DSM\_LB\_Operations WMI Class](dsm-lb-operations-wmi-class.md)

[DSM\_QueryUniqueId WMI Class](dsm-queryuniqueid-wmi-class.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MPIO%20WMI%20Classes%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




