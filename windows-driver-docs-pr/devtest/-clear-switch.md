---
title: /Clear Switch
description: The /Clear switch of the Enhanced Storage Certificate Management tool removes most of the certificates from the authentication silo certificate (ASC) store on a specified IEEE 1667-compliant USB storage device.Note  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the target device.�
ms.assetid: b8002d0c-450a-4c4c-bee6-83e382984b34
keywords: ["/Clear Switch Driver Development Tools"]
topic_type:
- apiref
api_name:
- /Clear
api_type:
- NA
---

# /Clear Switch


The **/Clear** switch of the Enhanced Storage Certificate Management tool removes most of the certificates from the authentication silo certificate (ASC) store on a specified IEEE 1667-compliant USB storage device.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the *target device*.

 

``` syntax
    EhStorCertMgrCmd /Clear  -Volume:
    VolumeName
   
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume______"></span><span id="_______-volume______"></span><span id="_______-VOLUME______"></span> **-Volume**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/Clear** switch clears all certificates from the target device except for following certificates:

-   The provisioning certificate (PCp). To remove the PCp certificate, you must use the [**/Initialize switch**](-initialize-switch.md).

-   The ASC-manufacturer certificate (ASCm).

    **Note**   The Enhanced Storage Certificate Management tool cannot add, remove, or replace the ASC-manufacturer (ASCm) certificate from the ASC store in the target device.

     

In order to clear a certificate from the target device, the device must have been provisioned with a PCp certificate, and the private key of that certificate must reside in the host in order to pass administrative authentication with the device.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows how to clear certificates from a target device:

```
EhStorCertMgrCmd /Clear -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}"
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20/Clear%20Switch%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




