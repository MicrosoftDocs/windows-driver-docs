---
title: /Initialize Switch
description: The /Initialize switch of the Enhanced Storage Certificate Management tool initializes the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device to its original manufacturer's state.Note  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the target device.�
ms.assetid: 4e04a099-8ad6-4eb6-9ac7-d466b7d828d4
keywords: ["/Initialize Switch Driver Development Tools"]
topic_type:
- apiref
api_name:
- /Initialize
api_type:
- NA
---

# /Initialize Switch


The **/Initialize** switch of the Enhanced Storage Certificate Management tool initializes the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device to its original manufacturer's state.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the *target device*.

 

``` syntax
    EhStorCertMgrCmd /Initialize  -Volume:
    VolumeName 
    [-Quiet]
   
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume_______"></span><span id="_______-volume_______"></span><span id="_______-VOLUME_______"></span> **-Volume:**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.

 

<span id="_______-Quiet______"></span><span id="_______-quiet______"></span><span id="_______-QUIET______"></span> **-Quiet**   
Suppresses verbose output when the USB storage device is initialized.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/Initialize** switch removes all the certificates from the ASC store except for the ASC-manufacturer (ASCm) certificate. Unlike the [**/Clear Switch**](-clear-switch.md), the **/Initialize** switch removes the Provisioning (PCp) certificates from the ASC store.

If the target device was provisioned with a provisioning certificate (PCp), the private key of that certificate must reside in the host in order to pass administrative authentication with the device.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows how to initialize a target device:

```
EhStorCertMgrCmd /Initialize -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}"
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20/Initialize%20Switch%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




