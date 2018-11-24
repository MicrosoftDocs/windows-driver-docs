---
title: /Clear Switch
description: The /Clear switch of the Enhanced Storage Certificate Management tool removes most of the certificates from the authentication silo certificate (ASC) store on a specified IEEE 1667-compliant USB storage device.Note  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the target device.
ms.assetid: b8002d0c-450a-4c4c-bee6-83e382984b34
keywords:
- /Clear Switch Driver Development Tools
topic_type:
- apiref
api_name:
- /Clear
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# /Clear Switch


The **/Clear** switch of the Enhanced Storage Certificate Management tool removes most of the certificates from the authentication silo certificate (ASC) store on a specified IEEE 1667-compliant USB storage device.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the *target device*.



```
    EhStorCertMgrCmd /Clear  -Volume:
    VolumeName
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume______"></span><span id="_______-volume______"></span><span id="_______-VOLUME______"></span> **-Volume**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.



### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **/Clear** switch clears all certificates from the target device except for following certificates:

-   The provisioning certificate (PCp). To remove the PCp certificate, you must use the [**/Initialize switch**](-initialize-switch.md).

-   The ASC-manufacturer certificate (ASCm).

    **Note**   The Enhanced Storage Certificate Management tool cannot add, remove, or replace the ASC-manufacturer (ASCm) certificate from the ASC store in the target device.



In order to clear a certificate from the target device, the device must have been provisioned with a PCp certificate, and the private key of that certificate must reside in the host in order to pass administrative authentication with the device.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following example shows how to clear certificates from a target device:

```
EhStorCertMgrCmd /Clear -Volume:"\\?\usbstor#ieee1667control&ven_&prod_&rev_#123456789&0&control#{4f40006f-b933-4550-b532-2b58cee614d3}"
```





