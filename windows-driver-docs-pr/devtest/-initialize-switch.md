---
title: /Initialize Switch
description: The /Initialize switch initializes the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device to its original manufacturer's state.
ms.assetid: 4e04a099-8ad6-4eb6-9ac7-d466b7d828d4
keywords:
- /Initialize Switch Driver Development Tools
topic_type:
- apiref
api_name:
- /Initialize
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# /Initialize Switch


The **/Initialize** switch of the Enhanced Storage Certificate Management tool initializes the authentication silo certificate (ASC) store in an IEEE 1667-compliant USB storage device to its original manufacturer's state.

**Note**  In this topic, the specified IEEE 1667-compliant USB storage device is referred to as the *target device*.



```
    EhStorCertMgrCmd /Initialize  -Volume:
    VolumeName 
    [-Quiet]
```

## <span id="Subparameters"></span><span id="subparameters"></span><span id="SUBPARAMETERS"></span>Subparameters


<span id="_______-Volume_______"></span><span id="_______-volume_______"></span><span id="_______-VOLUME_______"></span> **-Volume:**   
The volume name of the target device. For more information about the format of this parameter, see [Overview of the Enhanced Storage Certificate Management Tool](overview-of-the-enhanced-storage-certificate-management-tool.md).

**Note**  To produce a list of the volume names of the IEEE 1667-compliant USB storage devices that are currently connected to a computer, type **EhStorCertMgrCmd /List** at the command prompt and then press Enter.



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









