---
title: MS\_SMHBA\_BINDINGENTRY WMI Class
description: MS\_SMHBA\_BINDINGENTRY WMI Class
ms.assetid: b7b2315f-21db-41a4-8390-3c413cb39f5b
---

# MS\_SMHBA\_BINDINGENTRY WMI Class


An HBA miniport driver that supports the Storage Management API uses the MS\_SMHBA\_BINDINGENTRY class to expose binding information between data that the operating system uses to identify a SCSI device and the SSP protocol identifier for the device.

The MS\_SMHBA\_BINDINGENTRY class is defined as follows in Hbaapi.mof:

```
class MS_SMHBA_BINDINGENTRY
{
    [SMHBA_BIND_TYPE_QUALIFIERS, WmiDataId(1)]
    uint32 type;

    [HBAType("MS_SMHBA_PORTLUN"), WmiDataId(2)]
    MS_SMHBA_PORTLUN  PortLun;

    [HBAType("HBA_LUID"), WmiDataId(3)]
    uint8  LUID[256];

    [HBA_STATUS_QUALIFIERS, WmiDataId(4)]
    HBA_STATUS Status;

    [HBAType("HBA_SCSIID"), WmiDataId(5)]
    HBAScsiID ScsiId;
};
```

When this class definition is compiled by the WMI tool suite, it produces the following data structure:

MS\_SMHBA\_BINDINGENTRY found in hbapiwmi.h.

There are no methods associated with this WMI class.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20MS_SMHBA_BINDINGENTRY%20WMI%20Class%20%20RELEASE:%20%281/11/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




